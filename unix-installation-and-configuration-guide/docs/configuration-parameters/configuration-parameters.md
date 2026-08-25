# Configuration Parameters

Dyalog can be customised using configuration parameters. These can be set in various ways; if a configuration parameter is set in multiple places the following descending order of precedence applies:

1. command line settings
2. application configuration file settings
3. environment variable settings
4. user configuration file settings
5. built-in defaults

This provides a great deal of flexibility, enabling a user to override one setting with another. For example, a "usual" workspace size (**MAXWS**) can be defined in the user configuration file, but be temporarily superseded by entering a different value when starting a Dyalog Session from the command line.

For more information on configuration files, see [Configuration Files](configuration-files.md). For more information on environment variables, see [Environment Variables](environment-variables.md).

## References to Other Configuration Parameters

Configuration parameters can include references to other configuration parameters using square bracket delimiters. For example, `MySetting: "[DYALOG]/MyFile"` will replace `[DYALOG]` with the value of the **DYALOG** configuration parameter.

If the referenced configuration parameter is not defined then no substitution will take place; the reference, including the square bracket delimiters, will remain in place.

To include literal square brackets in a string, prefix them with a `\` character.
