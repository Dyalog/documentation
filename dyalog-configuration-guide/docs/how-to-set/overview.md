# How to Set Configuration Parameters

A configuration parameter can be set from any of the following sources:

- the [command line](command-line.md) used to start Dyalog;
- an [application configuration file](application-configuration-files.md);
- an [environment variable](environment-variables.md);
- a [user configuration file](user-configuration-files.md);
- the [Windows Registry](registry.md) (Microsoft Windows only);
- the interpreter's [built-in defaults](built-in-defaults.md).

When the same parameter is set in more than one source, the [order of precedence](order-of-precedence.md) determines which value is used. This gives a great deal of flexibility: a usual value can be defined in a configuration file and then temporarily overridden from the command line.

Dyalog Ltd recommends configuration files for all run-time applications, in preference to environment variables.
