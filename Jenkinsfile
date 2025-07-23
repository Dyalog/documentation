@Library('dyalog-scripts') _

def hashSame = null

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
        HASH_SAME       = 'unknown'  // Prevent undefined variable issues
        SWARM_NAME      = "docsweb"
        DOCSVERSION     = '20.0'
        GITDOCURL       = 'documentation'

        SVNDOCURL       = "docbin/trunk/documentation"
        SVNSHARPPLOTURL = "dyalogtools/Causeway/trunk/release"

        SVNDOCDIR = 'svn_docs'
        GITDOCDIR = 'git_docs'
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
                            r=ghGetReleaseAssets(GITDOCURL, GITDOCDIR)
                            doSvnCheckout(SVNDOCURL, SVNDOCDIR)
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
                            sh "./Jenkins/gitdocs2svn"
                        }
                    }
                }
            }
        } // Update svndocs

        stage('Update online files')
        {
            agent {
                // Change to 'swarm && gosport for live server'
                label 'swarm && bramley'
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

                stage('Get files from svn/docbin') {
                    steps {
                        dir("site/${env.DOCSVERSION}/files") { // Remove files directory to ensure we start with a clean sheet
                            deleteDir()
                        }
                        dir("site/${env.DOCSVERSION}") {
                            doSvnCheckout(SVNDOCURL, "files", true, 'svncom')
                            doSvnCheckout(SVNSHARPPLOTURL, "files/sharpplot", true, 'svncom')
                            sh '''$WORKSPACE/get_svn_docbin ${DOCSVERSION}'''
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
                            BACKUP_DIR=$(dirname "${WEB_ROOT}")
                            SITE_BASENAME=$(basename "${WEB_ROOT}")

                            echo "Creating compressed backup: ${BACKUP_FILE}"
                            tar -czf "${BACKUP_FILE}" -C "${BACKUP_DIR}" --exclude='*.tar.gz' "${SITE_BASENAME}"
                            
                            BACKUP_SIZE=$(ls -lh "${BACKUP_FILE}" | awk '{print $5}')
                            echo "Backup created successfully. Size: ${BACKUP_SIZE}"
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

                            # Since WEB_ROOT is a volume mount (on Docker), we need to sync directly into it.
                            # This is safer on non-Docker, too, rather than wiping the directory itself.
                            echo "Clearing existing content in ${WEB_ROOT}..."
                            # Safety check!
                            if [ "x" = "x${WEB_ROOT}" ]; then
                                echo "WEB_ROOT NOT SET"
                                exit 1
                            fi 

                            ## Force docs/20.0 so we don't overwrite older versions
                            if [ -d "${WEB_ROOT}" ]; then
                                rm -rf "${WEB_ROOT}"/20.0/*
                                rm -rf "${WEB_ROOT}"/.[^.]*  2>/dev/null || true
                            else
                                mkdir -p "${WEB_ROOT}/20.0"
                            fi
                            
                            echo "Syncing content from ${WORKSPACE} to ${WEB_ROOT}/"
                            rsync -rl --delete --exclude-from="${WORKSPACE}/.rsync-exclude" "${WORKSPACE}/20.0" "${WEB_ROOT}"
                            
                            echo "Storing new git hash (${LATEST_HASH})."
                            echo "${LATEST_HASH}" | tee "${WEB_ROOT}/.git-hash" >/dev/null
                            
                            #echo "Setting permissions on ${WEB_ROOT}..."
                            #chown -R www-data:www-data "${WEB_ROOT}"
                            #find "${WEB_ROOT}" -type d -exec chmod 755 {} +
                            #find "${WEB_ROOT}" -type f -exec chmod 644 {} +
                            #echo "Permissions set."

                            echo "Deployment completed successfully."
                            # Uncomment next line to test rollback
                            # exit 1
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

                stage('Verify deployment') { // Noddy check that the site is up
                    when {
                        expression { hashSame == false }
                    }
                    steps {
                        sh '''#!/bin/bash
                            set -euo pipefail
                            echo "Verifying deployment at ${WEB_ROOT}..."

                            if ! test -f "${WEB_ROOT}/20.0/index.html"; then
                                echo "ERROR: Verification failed - index.html not found in ${WEB_ROOT}."
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
