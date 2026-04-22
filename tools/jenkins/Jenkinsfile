@Library('dyalog-scripts') _

def hashSame = null

// Per-version SVN path configuration.
// Convention: trunk is always the current development version;
// released versions live under branches/{version}/.

def getSvnDocbinUrl(String version) {
    if (version == env.TRUNK_VERSION) {
        return "docbin/trunk/documentation"
    }
    return "docbin/branches/${version}/documentation"
}

def getSvnReadmeUrl(String version) {
    if (version == env.TRUNK_VERSION) {
        return "dyalog/trunk/svn/docs/readmes"
    }
    return "dyalog/branches/${version}/svn/docs/readmes"
}

/**
 * Download release assets for a specific documentation version.
 * Finds the latest non-draft release whose tag starts with "v{version}."
 * and downloads all assets to the target directory.
 */
def getVersionedReleaseAssets(String repo, String targetDir, String version) {
    withCredentials([
        usernamePassword(
            credentialsId: getCredentialsId('github'),
            usernameVariable: 'GITHUB_USER',
            passwordVariable: 'GITHUB_PASS'
        )
    ]) {
        sh """#!/bin/bash
            set -euo pipefail
            echo "\${GITHUB_PASS}" | /usr/bin/gh auth login --with-token

            REPO="Dyalog/${repo}"
            TAG=\$(gh release list -R "\$REPO" --exclude-drafts \\
                --json tagName,createdAt \\
                | jq -r '[.[] | select(.tagName | startswith("v${version}."))]
                         | sort_by(.createdAt) | last | .tagName')

            if [ -z "\$TAG" ] || [ "\$TAG" = "null" ]; then
                echo "ERROR: No release found matching v${version}.*"
                exit 1
            fi

            echo "Downloading assets from release \$TAG for version ${version}"
            rm -rf "\$WORKSPACE/${targetDir}"
            mkdir -p "\$WORKSPACE/${targetDir}"
            gh release download "\$TAG" -R "\$REPO" -D "\$WORKSPACE/${targetDir}"
            gh release view "\$TAG" -R "\$REPO" \\
                --json apiUrl,author,createdAt,id,isDraft,isPrerelease,name,publishedAt,tagName \\
                > "\$WORKSPACE/${targetDir}/buildinfo.json"
            echo "Downloaded:"
            ls "\$WORKSPACE/${targetDir}"
        """
    }
}

pipeline {
    agent none

    options {
        // One job at a time and timestamped log lines
        disableConcurrentBuilds()
        timestamps()
        // Keep last 10 builds but only 5 artifacts (backups)
        buildDiscarder(logRotator(
            numToKeepStr: '10',
            artifactNumToKeepStr: '5'
        ))
    }

    parameters {
        booleanParam(
            name: 'SKIP_BACKUP',
            defaultValue: false,
            description: 'Skip creating backup before deployment'
        )
        booleanParam(
            name: 'DEBUG',
            defaultValue: false,
            description: 'Enable debug output to show environment variables and state'
        )
    }

    environment {
        GITHUB_REPO     = 'https://github.com/dyalog/documentation.git'
        WEB_ROOT        = '/DockerVolumes/websites/docs.dyalog.com/'
        WEB_URL         = 'docs.dyalog.com'
        HASH_SAME       = 'unknown'
        SWARM_NAME      = "docsweb"

        // ============================================================
        // PRODUCTION_VERSIONS: Space-separated list of versions to deploy
        // Add '21.0' when v21 is ready for production release
        // ============================================================
        PRODUCTION_VERSIONS = '20.0'

        // The "development" version currently on trunk in SVN.
        // When v21 is released and v22 development starts, update this to '22.0'.
        TRUNK_VERSION = '21.0'

        GITDOCURL       = 'documentation'

        // Version-agnostic SVN paths
        SVNSHARPPLOTURL = "dyalogtools/Causeway/trunk/release"

        SVNDOCDIR       = 'svn_docs'
        GITDOCDIR       = 'git_docs'
    }

    stages {
        stage('Update svndocs') {
            agent {
                docker
                {
                    image 'dyalogci/ubuntu:22.04-build'
                    args '-v /home/jenkins/.ssh:/build/.ssh'
                }
            }
            options
            {
                skipDefaultCheckout(true)
            }
            stages
            {
                stage('Checkout from svndocs')
                {
                    steps {
                        script
                        {
                            sh '[ "x" != "x$WORKSPACE" ] && rm -rf $WORKSPACE/*'
                            doGitCheckout('JenkinsBuild', 'Jenkins')

                            // Fetch release assets and SVN checkout for each production version
                            def versions = env.PRODUCTION_VERSIONS.split(' ')
                            versions.each { version ->
                                getVersionedReleaseAssets(GITDOCURL, "${GITDOCDIR}/${version}", version)
                                doSvnCheckout(getSvnDocbinUrl(version), "${SVNDOCDIR}/${version}")
                            }
                        }
                    }
                }
                stage('Update and Commit svndocs')
                {
                    steps
                    {
                        withCredentials([
                            usernamePassword(credentialsId: getCredentialsId('svn'),
                            passwordVariable: 'SVN_PASS',
                            usernameVariable: 'SVN_USER')
                        ])
                        {
                            script {
                                def versions = env.PRODUCTION_VERSIONS.split(' ')
                                versions.each { version ->
                                    sh """
                                        SVNDOCDIR="${SVNDOCDIR}/${version}" \
                                        GITDOCDIR="${GITDOCDIR}/${version}" \
                                        ./Jenkins/gitdocs2svn
                                    """
                                }
                            }
                        }
                    }
                }
            }
        } // Update svndocs

        stage('Update online files')
        {
            agent {
                // Change to 'swarm && gosport for live server'
                label 'swarm && gosport'
            }
            stages {

                stage('Initialise') {
                    steps {
                        script {
                            try {
                                env.BUILD_TIMESTAMP = sh(
                                    script: 'date -u +%Y%m%d_%H%M%S',
                                    returnStdout: true
                                ).trim()
                                echo "Build timestamp: ${env.BUILD_TIMESTAMP}"
                            } catch (Exception e) {
                                error "Failed to generate build timestamp: ${e.message}"
                            }
                        }
                    }
                }

                stage('Get files from svn/docbin etc') {
                    steps {
                        script {
                            def versions = env.PRODUCTION_VERSIONS.split(' ')
                            versions.each { version ->
                                dir("${version}/files") {
                                    deleteDir()
                                }
                                dir("${version}") {
                                    doSvnCheckout(getSvnDocbinUrl(version), "files", true, 'svncom')
                                    doSvnCheckout(env.SVNSHARPPLOTURL, "files/sharpplot", true, 'svncom')
                                    doSvnCheckout(getSvnReadmeUrl(version), "files/readmes", true, 'svncom')
                                    sh "\$WORKSPACE/get_svn_docbin ${version}"
                                }
                            }
                        }
                    }
                }

                stage('Check for changes') { // Check if the current deployed hash matches the latest commit
                    steps {
                        script {
                            try {
                                def currentHash = sh(
                                    script: '''#!/bin/bash
                                        set -euo pipefail
                                        cat "${WEB_ROOT}/.git-hash" 2>/dev/null || true
                                    ''',
                                    returnStdout: true
                                ).trim()

                                def latestHash = sh(
                                    script: '''#!/bin/bash
                                        set -euo pipefail
                                        git rev-parse HEAD
                                    ''',
                                    returnStdout: true
                                ).trim()

                                echo "Current deployed hash : ${currentHash ?: 'none'}"
                                echo "Latest gh-pages hash  : ${latestHash}"

                                if (currentHash && currentHash == latestHash) {
                                    hashSame = true
                                    env.HASH_SAME = 'true'
                                    echo 'No changes detected – deployment will be skipped.'
                                } else {
                                    hashSame = false
                                    env.HASH_SAME = 'false'
                                    env.LATEST_HASH = latestHash
                                    echo 'Changes detected or no current deployment – proceeding with deployment.'
                                }
                            } catch (Exception e) {
                                echo "ERROR: Failed to check for changes - ${e.message}"
                                hashSame = null
                                throw e
                            }
                        }
                    }
                }

                stage('Debug Environment') {
                    when {
                        expression { params.DEBUG }
                    }
                    steps {
                        script {
                            echo "DEBUG: After Check for changes stage:"
                            echo "  hashSame (global) = ${hashSame}"
                            echo "  HASH_SAME (env) = ${env.HASH_SAME}"
                            echo "  LATEST_HASH = ${env.LATEST_HASH ?: 'not set'}"
                            echo "  BUILD_TIMESTAMP = ${env.BUILD_TIMESTAMP ?: 'not set'}"
                            echo "  PRODUCTION_VERSIONS = ${env.PRODUCTION_VERSIONS}"
                            echo "  TRUNK_VERSION = ${env.TRUNK_VERSION}"
                            echo "  WEB_ROOT exists = ${sh(script: "test -d '${env.WEB_ROOT}' && echo 'yes' || echo 'no'", returnStdout: true).trim()}"
                        }
                    }
                }

                stage('Backup current site') {
                    when {
                        allOf {
                            expression { hashSame == false }
                            // Check if WEB_ROOT exists and is a directory
                            expression { sh(script: "test -d '${env.WEB_ROOT}' && echo 'exists' || true", returnStdout: true).trim() == 'exists' }
                            expression { !params.SKIP_BACKUP }
                        }
                    }
                    options {
                        timeout(time: 10, unit: 'MINUTES')
                    }
                    steps {
                        script {
                            def currentHash = sh(
                                script: '''
                                if [ -f "${WEB_ROOT}/.git-hash" ]; then
                                    cat "${WEB_ROOT}/.git-hash" 2>/dev/null | cut -c1-8
                                else
                                    echo "unknown"
                                fi
                                ''',
                                returnStdout: true
                            ).trim()

                            def backupName = "docs.backup.${env.BUILD_TIMESTAMP}.${currentHash}.tar.gz"
                            env.BACKUP_FILE = backupName
                        }
                        sh '''#!/bin/bash
                            set -euo pipefail
                            echo "Backing up current site at ${WEB_ROOT} before deployment."

                            echo "Creating compressed backup: ${BACKUP_FILE}"
                            cd "${WEB_ROOT}"

                            # Build list of existing directories to backup
                            BACKUP_TARGETS=""
                            for VERSION in ${PRODUCTION_VERSIONS}; do
                                if [ -d "${VERSION}" ]; then
                                    BACKUP_TARGETS="${BACKUP_TARGETS} ${VERSION}"
                                else
                                    echo "  Note: ${VERSION} does not exist yet, skipping from backup"
                                fi
                            done

                            # Add .git-hash if it exists
                            if [ -f ".git-hash" ]; then
                                BACKUP_TARGETS="${BACKUP_TARGETS} .git-hash"
                            fi

                            # Only create backup if we have something to backup
                            if [ -z "${BACKUP_TARGETS}" ]; then
                                echo "WARNING: Nothing to backup (no existing production versions)"
                                # Create empty marker file so archiveArtifacts doesn't fail
                                touch "${WORKSPACE}/${BACKUP_FILE}.empty"
                            else
                                echo "Backing up:${BACKUP_TARGETS}"
                                tar -czf "${WORKSPACE}/${BACKUP_FILE}" ${BACKUP_TARGETS}
                                BACKUP_SIZE=$(ls -lh "${WORKSPACE}/${BACKUP_FILE}" | awk '{print $5}')
                                echo "Backup created successfully. Size: ${BACKUP_SIZE}"
                            fi

                            cd "${WORKSPACE}"
                        '''
                        archiveArtifacts artifacts: "${env.BACKUP_FILE}",
                                        fingerprint: true,
                                        onlyIfSuccessful: true
                    }
                }

                stage('Deploy site') {
                    when {
                        expression { hashSame == false }
                    }
                    options {
                        lock('docs-deploy')
                    }
                    steps {
                        sh '''#!/bin/bash
                            set -euo pipefail
                            echo "Starting deployment to ${WEB_ROOT}."

                            if [ -z "${WEB_ROOT}" ]; then
                                echo "ERROR: WEB_ROOT NOT SET"
                                exit 1
                            fi

                            # Create WEB_ROOT if it doesn't exist
                            if [ ! -d "${WEB_ROOT}" ]; then
                                mkdir -p "${WEB_ROOT}"
                            fi

                            # Track deployment success
                            DEPLOYED_COUNT=0

                            # Deploy only PRODUCTION_VERSIONS
                            for VERSION in ${PRODUCTION_VERSIONS}; do
                                echo "Processing version: ${VERSION}"

                                # CRITICAL: Verify source exists before touching production
                                if [ ! -d "${WORKSPACE}/${VERSION}" ]; then
                                    echo "  ERROR: Source ${WORKSPACE}/${VERSION} does not exist!"
                                    echo "  This version may not have been published to gh-pages."
                                    echo "  Skipping to avoid wiping production."
                                    continue
                                fi

                                if [ ! -f "${WORKSPACE}/${VERSION}/index.html" ]; then
                                    echo "  ERROR: ${WORKSPACE}/${VERSION}/index.html missing!"
                                    echo "  Source appears incomplete. Skipping to avoid corruption."
                                    continue
                                fi

                                # Source verified - safe to deploy
                                echo "  Source verified, deploying..."

                                # Clear existing version directory (only now that source is verified)
                                if [ -d "${WEB_ROOT}/${VERSION}" ]; then
                                    rm -rf "${WEB_ROOT}/${VERSION:?}"/*
                                fi

                                # Sync this version
                                rsync -rl --delete --exclude-from="${WORKSPACE}/.rsync-exclude" "${WORKSPACE}/${VERSION}" "${WEB_ROOT}"
                                echo "  Deployed ${VERSION} successfully"
                                DEPLOYED_COUNT=$((DEPLOYED_COUNT + 1))
                            done

                            # Only update git hash if at least one version was deployed
                            if [ $DEPLOYED_COUNT -eq 0 ]; then
                                echo "ERROR: No versions were deployed! Not updating .git-hash"
                                exit 1
                            fi

                            # Update git hash
                            echo "Storing new git hash (${LATEST_HASH})."
                            echo "${LATEST_HASH}" | tee "${WEB_ROOT}/.git-hash" >/dev/null

                            echo "Deployment completed successfully. Deployed ${DEPLOYED_COUNT} version(s)."
                        '''
                        script {
                            env.DEPLOYMENT_EXECUTED = 'true'
                        }
                    }
                    post {
                        failure {
                            echo "ERROR: Deployment failed at ${env.WEB_ROOT}"
                        }
                    }
                }

                stage('Verify deployment') {
                    when {
                        expression { hashSame == false }
                    }
                    steps {
                        sh '''#!/bin/bash
                            set -euo pipefail
                            echo "Verifying deployment at ${WEB_ROOT}..."

                            FAILED=0
                            for VERSION in ${PRODUCTION_VERSIONS}; do
                                if ! test -f "${WEB_ROOT}/${VERSION}/index.html"; then
                                    echo "ERROR: ${VERSION}/index.html not found"
                                    FAILED=1
                                else
                                    echo "  ${VERSION}/index.html OK"
                                fi
                            done

                            if [ $FAILED -eq 1 ]; then
                                exit 1
                            fi

                            echo "Deployment verified successfully."
                            echo "Site location: ${WEB_ROOT}"
                            echo "Deployed Git hash: $(cat "${WEB_ROOT}/.git-hash" 2>/dev/null || echo 'unknown')"
                        '''
                    }
                    post {
                        failure {
                            echo "ERROR: Deployment verification failed - site may be in inconsistent state"
                        }
                    }
                }
                stage('Update Containers') { // Deploy the swarm server incase anything has changed
                // Note: Swarm is clever enough that if nothing changes in the config, it won't re-deploy the service.
                    steps {
                        sh '''#!/bin/bash
                            sed -i 's%{{WEB_ROOT}}%${WEB_ROOT}%g' service.yml
                            sed -i 's%{{WEB_URL}}%${WEB_URL}%g' service.yml
                        '''
                        swarmDeploy "${SWARM_NAME}"
                    }

                }
            }

            post {
                success {
                    script {
                        if (env.HASH_SAME == 'true') {
                            echo "No deployment was needed - site is already up to date."
                        } else if (env.DEPLOYMENT_EXECUTED == 'true') {
                            echo "Site successfully deployed. New active commit: ${env.LATEST_HASH}"
                        } else if (env.HASH_SAME == 'false') {
                            echo "WARNING: Changes were detected but deployment did not execute. Check pipeline logs."
                        } else {
                            echo "Pipeline completed successfully."
                        }
                    }
                }
                failure {
                    script {
                        // Report which stage failed
                        echo "FAILURE: Pipeline failed at stage: ${env.STAGE_NAME ?: 'Unknown'}"

                        // Only attempt rollback if a deployment was actually attempted
                        if (hashSame == false) {
                            echo "ERROR: Deployment failed. Attempting automatic rollback to the latest backup..."
                            try {
                                // Copy the most recent successful build's backup
                                copyArtifacts projectName: env.JOB_NAME,
                                            selector: lastSuccessful(),
                                            filter: 'docs.backup.*.tar.gz',
                                            flatten: true,
                                            optional: false

                                sh '''#!/bin/bash
                                    set -euo pipefail
                                    # Find the backup file that was copied
                                    BACKUP_FILE=$(ls docs.backup.*.tar.gz | head -n1)

                                    if [[ -n "${BACKUP_FILE}" ]]; then
                                        echo "Found backup for rollback: ${BACKUP_FILE}"

                                        # Clear contents but preserve mount point
                                        echo "Clearing failed deployment from ${WEB_ROOT}..."
                                        find "${WEB_ROOT}" -mindepth 1 -delete

                                        echo "Extracting ${BACKUP_FILE} to ${WEB_ROOT}..."
                                        tar -xzf "${BACKUP_FILE}" -C "${WEB_ROOT}" --strip-components=1
                                        echo "Extraction complete."

                                        chown -R www-data:www-data "${WEB_ROOT}"
                                        echo "Ownership set for rolled-back site."

                                        echo "Automatic rollback completed successfully from ${BACKUP_FILE}"
                                        if test -f "${WEB_ROOT}/.git-hash"; then
                                            echo "Rolled back to Git hash: $(cat "${WEB_ROOT}/.git-hash")"
                                        fi

                                        # Clean up the copied artifact
                                        rm -f "${BACKUP_FILE}"
                                    else
                                        echo "ERROR: No backup file found after copy"
                                        exit 1
                                    fi
                                '''
                            } catch (Exception e) {
                                echo "CRITICAL: Rollback failed - ${e.message}"
                                echo "The site at ${env.WEB_ROOT} might be in an inconsistent or broken state."
                            }
                        } else {
                            echo "ERROR: Pipeline failed, but no deployment was attempted."
                        }
                    }
                }
            }
        } // Update online files
    } // Stages
} // Pipeline
