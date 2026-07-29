# Enable_CEF

Whether the [Chromium Embedded Framework (CEF)](https://en.wikipedia.org/wiki/Chromium_Embedded_Framework) is enabled. When disabled, an attempt to create an [HTMLRenderer](../../../object-reference/objects/htmlrenderer) object fails with an error message.

Valid values are:

- `0` : CEF is disabled
- `1` : CEF is enabled

Default is `1`, except when Dyalog is not running under a desktop (for example, in a PuTTY session), where the default is `0`.

!!! Info "Information"
    The value of **Enable_CEF** in the Windows Registry or a configuration file is currently ignored; only a value set on the command line or as an environment variable is honoured, otherwise the default is used. Under UNIX and macOS, Auxiliary Processors cannot be used while CEF is enabled.
