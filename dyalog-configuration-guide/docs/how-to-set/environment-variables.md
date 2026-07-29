# Environment Variables

A configuration parameter can be set as an environment variable in the environment from which Dyalog is started. An environment variable setting overrides a user configuration file, the Registry, and the built-in default, but is itself overridden by an application configuration file and by the command line (see [Order of Precedence](order-of-precedence.md)).

On UNIX and macOS, environment variable names are given in upper case, for example `MAXWS`. On Microsoft Windows, parameter names are not case-sensitive.

!!! Hint "Hints and Recommendations"
    Dyalog Ltd recommends that [configuration files](application-configuration-files.md) are used for all run-time applications, and that the use of environment variables for this purpose is eliminated. Configuration files are text-based, portable across platforms, and easily managed alongside application source code.
