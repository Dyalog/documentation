# Order of Precedence

When a configuration parameter is set in more than one place, Dyalog applies the following order of precedence. Each source overrides those below it:

1. [Command line](command-line.md) settings, which override
2. [Application configuration file](application-configuration-files.md) settings, which override
3. [Environment variable](environment-variables.md) settings, which override
4. [User configuration file](user-configuration-files.md) settings, which override
5. [Windows Registry](registry.md) settings (Microsoft Windows only), which override
6. [Built-in defaults](built-in-defaults.md).

!!! Info "Information"
    The Registry step applies to Microsoft Windows only. On UNIX and macOS there is no Registry, so a user configuration file setting is overridden only by the sources above it.

The value actually in force for a given parameter, after the precedence rules have been applied, can be queried from within Dyalog with `2 ⎕NQ '.' 'GetEnvironment' name` or with the `]Config` user command.
