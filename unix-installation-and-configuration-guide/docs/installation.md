<h1 class="heading"><span class="name">Installation</span></h1>

This manual covers the installation of the non-GUI version of Dyalog APL on AIX, and on Linux distributions which use either .rpm or .deb files for installing software. If you are using a Linux distribution which uses some other method, or you wish to have a non-default installation, then there are some suggestions about how such an installation might be completed.

Dyalog APL version {{ version_majmin }} is supplied in either 32 or 64 bit versions, and in either Classic or Unicode editions. The installation procedure for Dyalog APL is the same in each case. Note that the 64-bit versions of Dyalog APL will only run on a 64-bit operating systems; the 32-bit versions of Dyalog APL will run on both 32 and 64 bit operating systems.

It is assumed that in all cases the installation image has been downloaded into /tmp on the local machine.

The default installation subdirectory will be formed as:
```apl
/opt/mdyalog/{{ version_majmin }}/<APLWidth>/<APLEdition>
```

or, in the case of AIX:
```apl
/opt/mdyalog/{{ version_majmin }}/<APLWidth>/<APLEdition>/<platform>
```

So for example, Dyalog APL Version {{ version_majmin }} 64 bit Unicode for POWER9 hardware on AIX will by default be installed into
```apl
/opt/mdyalog/{{ version_majmin }}/64/unicode/p9        
```

whereas on a Linux distribution the equivalent version would be installed in
```apl
/opt/mdyalog/{{ version_majmin }}/64/Unicode        
```

This naming convention ensures that all versions and releases of Dyalog APL can be installed in parallel.

As part of installing Dyalog on Linux (including Pi) the script /usr/bin/dyalog is created; this is a copy of the $DYALOG/mapl script and can be used to start Dyalog APL. Note that this script will start the most recently installed version of Dyalog APL. This script is used in the target of the Dyalog APL icon on Linux desktops. If preferable, Dyalog can be started by calling the script mapl in the appropriate Dyalog installation directory.

When supplying updates or fixes, Dyalog issues a full installation image; this means that any file under the installation subdirectory may be overwritten. It is therefore strongly recommended that users do not alter issued files, as those changes could be lost if an update is installed.

## Installing under AIX

For each version of Dyalog APL on AIX, separate hardware-specific builds are created for each of the four combinations of 32 or 64 bit versions, Classic or Unicode editions. For version {{ version_majmin }} specific builds for p9 are created.
```apl
$ su -
# cd /opt
## cpio -icdvum </tmp/dyalog-unicode_20.0.51795_ppc64_p9.cpi
## exit
```

Dyalog APL is now installed. To run as any user, type
```apl
$ /opt/mdyalog/{{ version_majmin }}/64/unicode/p9/mapl
```

!!! note
    Version {{ version_majmin }} is compiled on AIX7.2.

## Installing on intel machines
### Installing on an RPM-based Linux Distribution
```apl
$ sudo rpm --install dyalog-unicode_20.0.51795_x86_64.rpm
```

Dyalog APL is now installed. To run as any user, type
```apl
$ dyalog
```
or
```apl
$ /opt/mdyalog/20.0/64/unicode/mapl
```

!!! note
    - It may be necessary to use the --force flag or equivalent if an earlier version of Dyalog APL is to be installed on the same server as a later version. This is safe since the versions have no files in common.
    - It has been noticed that in some circumstances the 32-bit installs fail on 64-bit operating systems due to a missing ncurses package. However, it appears that that package is indeed installed. What is required however is the 32-bit version: once installed, Dyalog APL will then install.

### Installing on a DEB-based Linux Distribution
```other
$ sudo apt install dyalog-unicode_20.0.51795_amd64.deb
```
Dyalog APL is now installed. To run as any user, type
```other
$ dyalog
```
or
```other
$ /opt/mdyalog/20.0/64/unicode/mapl
```

!!! note
    - It may be necessary to use the --force flag or equivalent if an earlier version of Dyalog APL is to be installed on the same server as a later version. This is safe since the versions have no files in common.
    - It has been noticed that in some circumstances the 32-bit installs fail on 64-bit operating systems due to a missing ncurses package. However, it appears that that package is indeed installed. What is required however is the 32-bit version: once installed, Dyalog APL will then install.

## Installing on arm machines
### Installing on an RPM-based Linux Distribution
```apl
$ sudo rpm --install dyalog-unicode_20.0.51795_aarch64.rpm
```

Dyalog APL is now installed. To run as any user, type
```apl
$ dyalog
```
or
```apl
$ /opt/mdyalog/20.0/64/unicode/mapl
```

!!! note
    - It may be necessary to use the --force flag or equivalent if an earlier version of Dyalog APL is to be installed on the same server as a later version. This is safe since the versions have no files in common.


### Installing on a DEB-based Linux Distribution
```other
$ sudo apt install dyalog-unicode_20.0.51795_aarch64.deb
```
Dyalog APL is now installed. To run as any user, type
```other
$ dyalog
```
or
```other
$ /opt/mdyalog/20.0/64/unicode/mapl
```

!!! note
    - It may be necessary to use the --force flag or equivalent if an earlier version of Dyalog APL is to be installed on the same server as a later version. This is safe since the versions have no files in common.
    - It has been noticed that in some circumstances the 32-bit installs fail on 64-bit operating systems due to a missing ncurses package. However, it appears that that package is indeed installed. What is required however is the 32-bit version: once installed, Dyalog APL will then install.


## Installing in a non-default location

It is possible to install Dyalog APL for UNIX in non-default locations, without the need for root privileges.

For all UNIXes,

```other
cd <directory under which I wish to install Dyalog APL>
```

For AIX:

```other
cpio -icvdum <installation_image.cpi
```

For .deb based Linux distributions:

```other
/usr/bin/dpkg --extract installation_image.deb
```

For .rpm based Linux distributions
```other
rpm2cpio installation_image.rpm | cpio -icdvum
```

## Deinstalling Dyalog APL

In the following examples, it is assumed that only Dyalog APL 20.0 64-bit Unicode is installed on the server; the commands to delete directories will need to be more specific if multiple versions of Dyalog APL are installed.

Should it be necessary to deinstall Dyalog APL, then the process is:

### Deinstalling under AIX
```apl
su -
cd /opt
rm -rf mdyalog/20.0
```

### Deinstalling on an RPM-based Linux Distribution
```other
su -
rpm -e dyalog-unicode_20.0.51795_x86_64
cd /opt
rm -rf mdyalog/20.0
exit
```

### Deinstalling on a DEB-based Linux Distribution
```other
sudo su -
apt-get purge dyalog-unicode-200
cd /opt
rm -rf mdyalog/20.0
exit
```

## Upgrading APL

### Applying a later release of the same version

In general Dyalog will issue a new installation image if a problem is discovered which requires a new version of the interpreter. Dyalog recommends that the entire installation image is installed over the existing installation, but that is not essential. Particularly in a live environment it may be preferable to install only a revised interpreter. This can be done by extracting the individual files from the installation image, and copying them into the correct place in the installation directory tree. To apply a fix image, run the appropriate installation command with the -force option if appropriate. Be aware: the process of installing a later installation image over an already installed version of Dyalog APL WILL result in all files being overwritten. If you have changed any, it will be necessary to take copies of them, and then to reapply local alterations to the new files. Please contact support@dyalog.com for further advice.

For rpm-based installation, run
```
sudo --Uvh <new installation image>
```

For deb-based installation, run
```
sudo dpkg -i <new installation image>
```

See https://packages.dyalog.com/ for details of updating on the Pi.

### Upgrading from an earlier version

Newer versions of Dyalog APL will be placed in new subdirectories, rather than in the same location as the currently installed versions. This means that both old and new versions can be run in parallel, but extra disk space in /opt will be required to cater for the multiple releases. Note however that once a workspace has been saved in a later version of Dyalog APL, it is most likely that it will not be possible to `)LOAD` or `)COPY` the workspace by an earlier version. Once happy with the new version, then de-install the earlier version.
