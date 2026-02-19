# Enabling the .NET Interface

The .NET interface is enabled when the DYALOG_NETCORE configuration parameter is set to 1; this is the default setting on Linux (including the Raspberry Pi) and macOS. On Microsoft Windows the default setting is 0 for backwards compatibility (a setting of 0 enables the .NET Framework interface).

The .NET interface and .NET Framework interface cannot be enabled simultaneously.

For information on how to set configuration parameters, see the appropriate Dyalog for <operating system> Installation and Configuration Guide. To check the value of DYALOG_NETCORE, enter the following  when in a Session:
```apl
+2 ⎕NQ'.' 'GetEnvironment' 'DYALOG_NETCORE'
```

If the result is `1` (or empty on Linux/macOS), then the .NET interface is enabled.
