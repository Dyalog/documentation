# Dyalog_NETCore

!!! Info "Information"
    This configuration parameter is only relevant when using .NET or .NET Framework.

Whether the .NET interface is used in preference to the .NET Framework interface.

Valid values are:

- `0` : the .NET Framework interface is used
- `1` : the .NET interface is used

Default depends on operating system:

- Microsoft Windows: `0`
- other platforms that support .NET: `1`
