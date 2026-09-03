# Enable_CEF

This parameter is a Boolean value with a default value of 1. If set to 0, it disables the [Chromium Embedded Framework (CEF).](https://en.wikipedia.org/wiki/Chromium_Embedded_Framework) and an attempt to create an [HTMLRenderer](../../../object-reference/objects/htmlrenderer) object will fail with an error message.

!!! Info "Information"
    The value of the **Enable_CEF** parameter defined in the Microsoft Windows Registry or in a configuration file is ignored; only the value set in the command line or as an environment variable is honoured. If not defined in this way, the default value is used.
