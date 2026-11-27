# Configuration Parameters

This section documents each Dyalog configuration parameter on its own page. A parameter page states what the parameter does, its valid values, its default (noting any difference between operating systems), and related parameters.

The parameters are listed alphabetically in the navigation pane. For a subject-based overview, see [Configuration Parameters by Category](configuration-parameters-by-category.md).

For how to give a parameter a value – on the command line, in a configuration file, as an environment variable, or in the Windows Registry – and for the order of precedence when a parameter is set in more than one place, see [How to Set Configuration Parameters](../how-to-set/overview.md).

You are not limited to the parameters used by Dyalog itself; you can also define parameters of your own.

## Specifying size-related parameters

Several configuration parameters define a size, such as [maxws](maxws.md) or [log_size](log-size.md).

The value of such a parameter is an integer, optionally followed immediately by a single character that denotes the units:

| Character | Units |
|-----------|-------|
| `K`       | KiB   |
| `M`       | MiB   |
| `G`       | GiB   |
| `T`       | TiB   |
| `P`       | PiB   |
| `E`       | EiB   |

If no character is given, the units are assumed to be KiB. Specifying an invalid value prevents Dyalog from starting.
