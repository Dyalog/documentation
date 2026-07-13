# The Directory ~/.dyalog

In Version {{ version_majmin }} Dyalog APL by default creates a directory to hold various configuration and log files; in previous versions these files were located in differing directories. The contents of this directory are expected to be extended in future versions of Dyalog APL, and allow for multiple versions and editions of Dyalog APL to be run concurrently.

On Linux (including Raspberry Pi), macOS and AIX this directory is called .dyalog and is located in the user's home directory.

The default Dyalog startup script checks for the existence of the directory, and if it does not exist, creates it.

This directory now contains:

- the user configuration files *dyalog.dcfg* and *dyalog.<version-specific>.dcfg*, where the version-specific information comprises the version number, edition and width. For example, a 64-bit Unicode edition of Dyalog version 18.0 will be identified as *180U64*. The names/locations of these files should not be changed.
- the session log, which by default is called *default.dlf*
- the user command cache file, which by default is called *UserCommand20.cache*
- the file containing the SALT settings which is called *SALT.settings*

Note that many of the default names and locations can be altered. Remember that earlier versions of Dyalog will generate/use copies of these files in other locations: you may need to move or delete earlier versions of these files, or change the default values of their names and/or locations in earlier versions of Dyalog APL.
