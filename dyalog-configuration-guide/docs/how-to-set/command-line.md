# Command Line

A configuration parameter can be set on the command line that starts Dyalog, by giving the parameter name and its value. A command line setting takes precedence over every other source (see [Order of Precedence](order-of-precedence.md)), which makes it convenient for temporarily overriding a value defined elsewhere.

For example, a usual workspace size can be defined in a [user configuration file](user-configuration-files.md) through the **MAXWS** parameter and then superseded for a single Session by giving a different **MAXWS** on the command line.

Parameter names given on the command line are not case-sensitive.
