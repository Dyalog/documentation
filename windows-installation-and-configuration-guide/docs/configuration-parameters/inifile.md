# IniFile

This parameter specifies the name of the Windows Registry folder that contains the configuration parameters described in this section. For example,
```apl
INIFILE=Software\Dyalog\mysettings
```

The default values for **IniFile**, for the 64-bit and 32-bit versions respectively, are:

## Unicode Edition
```apl
    Software\Dyalog\Dyalog APL/W-64 {{ version_majmin }} Unicode 
    Software\Dyalog\Dyalog APL/W {{ version_majmin }} Unicode
```

## Classic Edition
```apl
    Software\Dyalog\Dyalog APL/W-64 {{ version_majmin }}
    Software\Dyalog\Dyalog APL/W {{ version_majmin }}
```

See also [Configuration saved in](../configuring-the-ide/configuration-dialog/configuration-dialog-general-tab.md).
