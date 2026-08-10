# How to Set Configuration Parameters

A configuration parameter can be set from any of the following sources:

- the [command line](command-line.md) used to start Dyalog
- an [application configuration file](application-configuration-files.md)
- an [environment variable](environment-variables.md)
- a [user configuration file](user-configuration-files.md)
- the [Windows Registry](registry.md) (Microsoft Windows only)
- the interpreter's [built-in defaults](built-in-defaults.md)

When the same parameter is set in more than one source, the [order of precedence](order-of-precedence.md) determines which value is used. This gives a great deal of flexibility: a usual value can be defined in a configuration file and then temporarily overridden from the command line.

Dyalog Ltd recommends configuration files for all run-time applications, in preference to environment variables.

## References to Other Configuration Parameters

A string value can refer to another configuration parameter, wherever it is defined, using square-bracket delimiters. For example, `MySetting: "[DYALOG]/MyFile"` replaces `[DYALOG]` with the value of the **DYALOG** parameter. If the string inside the brackets is `.`, it is replaced with the path of the directory containing the configuration file itself.

If the referenced parameter is not defined, no substitution takes place and the reference, including its brackets, remains in place. To include a literal square bracket in a string, prefix it with a `\` character.

On Microsoft Windows, `[=DOCUMENTS]` is a pre-defined substitution parameter that is replaced with the location of the user's Documents folder (for example, `C:\Users\Bob\Documents`).
