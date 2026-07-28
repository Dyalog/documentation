# Application Configuration Files

An *application configuration file* holds the configuration values associated with a specific application. It is created by the user and is normally stored alongside the application.

When Dyalog starts, it derives the name of the application configuration file as follows:

- the name given in the **ConfigFile** parameter, if it is set; otherwise
- the name of the workspace or script loaded at start-up (through the **Load** parameter) with its extension replaced by `.dcfg`, if that file exists; otherwise
- no application configuration file is used.

An application configuration file setting overrides an environment variable, a user configuration file, the Registry, and the built-in default (see [Order of Precedence](order-of-precedence.md)).

Configuration files use JSON5 (a superset of JSON) syntax and are portable across all platforms that Dyalog supports. Both application and user configuration files can *cascade*: a file can extend another with the `Extend` key, inheriting its settings and optionally overriding them. For the file format, cascading, arrays, and references between parameters, see [Configuration File Structure](configuration-file-structure.md).

!!! Warning "Warning"
    Although user credentials such as login details or passwords can be placed in a configuration file, Dyalog strongly recommends against this, even when the credentials are encrypted, as it is a significant security risk.
