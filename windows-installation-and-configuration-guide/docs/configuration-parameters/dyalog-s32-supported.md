# DYALOG_S32_SUPPORTED

This parameter specifies whether support for small-span component files is enabled. When support is disabled, a small-span component file cannot be tied.

The values of the parameter are:

|---|-------------------------------------------------|
|0  |Support for small-span component files is disabled|
|1  |Support for small-span component files is enabled |

The default value of the parameter is 1.

!!! Info "Information"
    Small-span component files have been deprecated. Setting this parameter to 0 identifies whether an application still depends on them.
