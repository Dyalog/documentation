# IniFile

!!! Info "Information"
    This configuration parameter is only relevant on the Microsoft Windows operating system.

The name of the Windows Registry folder that holds the configuration parameters. For example, `INIFILE=Software\Dyalog\mysettings`.

Valid values are a Registry folder path.

Default depends on edition (64-bit and 32-bit versions respectively):

- Unicode edition:
  ```
  Software\Dyalog\Dyalog APL/W-64 {{ version_majmin }} Unicode
  Software\Dyalog\Dyalog APL/W {{ version_majmin }} Unicode
  ```
- Classic edition:
  ```
  Software\Dyalog\Dyalog APL/W-64 {{ version_majmin }}
  Software\Dyalog\Dyalog APL/W {{ version_majmin }}
  ```

See also the [General tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-general-tab) of the Windows Configuration Dialog.
