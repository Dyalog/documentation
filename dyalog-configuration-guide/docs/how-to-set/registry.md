# Registry

!!! Info "Information"
    The Windows Registry applies to Microsoft Windows only. On UNIX and macOS there is no Registry.

On Microsoft Windows, configuration parameters can be stored in the Registry. A Registry setting overrides only the built-in default; every other source overrides it (see [Order of Precedence](order-of-precedence.md)).

The Configuration Dialog reflects the values stored in the Registry and ignores any overriding values defined on the command line, in configuration files, or in environment variables. When a parameter is changed through the Configuration Dialog, the new value is recorded in the Registry, but it remains overridden by any source that takes precedence over the Registry.

Some parameters are stored in Registry sub-folders. A [configuration file](application-configuration-files.md) represents such a parameter as a nested object; see [Configuration File Structure](configuration-file-structure.md).
