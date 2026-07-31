# Introduction

Dyalog is customised through *configuration parameters*. A configuration parameter controls some aspect of the interpreter or the development environment, from the maximum workspace size to the location of the Session log.

The same parameters apply across all supported operating systems, but a few are specific to one platform, and some take different default values on different platforms. Each parameter's own page states any such differences.

A configuration parameter can be set in several ways: on the command line, in an application configuration file, as an environment variable, in a user configuration file, in the Windows Registry (Microsoft Windows only), or left at its built-in default. When a parameter is set in more than one of these, a fixed [order of precedence](how-to-set/order-of-precedence.md) determines which setting wins. [How to Set Configuration Parameters](how-to-set/overview.md) describes each source in turn.

Parameter names are not case-sensitive when given on the command line, in configuration files, or in the Windows Registry. When a parameter is set as an environment variable on UNIX or macOS, its name is given in upper case.
