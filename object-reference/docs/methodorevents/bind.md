# <span>Bind</span> <span>Method</span>

The Bind method packages the active workspace as a file. On any supported platform, the following expression creates a .NET assembly in `<filename>` that contains the APL code in the classes in the active workspace:

```apl
      2 ⎕NQ '.' 'Bind' <filename> 'Library'
```

!!! windows "Dyalog on Microsoft Windows"
    This use of the Bind method is similar to selecting **File** > **Export...** in the Session; see [Creating Executables and COM Servers](../../windows-installation-and-configuration-guide/creating-executables.md).

!!! Info "Information"
    The full description of the Bind method is in preparation.

## Application

Objects: [Root](../objects/root.md)
