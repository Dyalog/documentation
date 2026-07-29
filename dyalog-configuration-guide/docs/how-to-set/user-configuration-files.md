# User Configuration Files

A *user configuration file* defines configuration values for the current (and possibly only) user of the system. It typically configures the development environment, providing settings that are the same for all of that user's applications.

A user configuration file setting overrides the Registry and the built-in default, but is overridden by an environment variable, an application configuration file, and the command line (see [Order of Precedence](order-of-precedence.md)).

## UNIX and macOS

The first time a new version of Dyalog is launched it creates and initialises a version-specific user configuration file `$HOME/.dyalog/dyalog.<version-specific>.dcfg`, where the version-specific part comprises the version number, edition, and width. For example, a 64-bit Unicode edition of Dyalog 21.0 is identified as `210U64`. The name of this file should not be changed.

The first time any version of Dyalog is run, an additional file `$HOME/.dyalog/dyalog.dcfg` is created. Settings placed here apply irrespective of Dyalog version, so they need not be repeated in each version-specific file.

!!! Legacy "Legacy"
    Before Dyalog 18.0, configuration parameters could be set as environment variables in a `$HOME/.dyalog/dyalog.config` script. That script is no longer referenced; any settings to be retained must be moved into the appropriate `$HOME/.dyalog/dyalog.<version-specific>.dcfg` file.

## Microsoft Windows

The name of the user configuration file is given by the **UserConfigFile** parameter. On Windows this parameter is not set by default, but can be defined by the user.
