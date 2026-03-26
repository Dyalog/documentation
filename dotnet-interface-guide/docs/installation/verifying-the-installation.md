# Verifying the Installation

Dyalog Ltd recommends that the following command is run at the start of any application that will use .NET:
```apl
      r←2250⌶⍬
```

This command identifies the state of the .NET interface while attempting to suppress all associated error messages (for more information on `2250⌶`, see the Dyalog APL Language Reference Guide):

- If `r≡1 1 ''` then the .NET interface should work
- If `r≡2 1 ''` then the .NET Framework interface should work (for more information see the Dyalog for Microsoft Windows .NET Framework Interface Guide)

For any other value of `r`, the interface will not work. An indication of why the interface is not working might be given in error messages in the status/Session window or  `r[3]`.

If the interface is not working correctly, then:

- ensure that .NET has been installed according to Microsoft's .NET documentation ([https://docs.microsoft.com/en-gb/dotnet/](https://docs.microsoft.com/en-gb/dotnet/)).
- check that DOTNET_ROOT is correctly set
- check that DYALOG_NETCORE is correctly set (that is, not set to 0)

If everything has been installed and enabled correctly, then the version of .NET in use will be returned by the following statement:
```apl
      ⎕USING←'System' ⋄ Environment.Version
```
