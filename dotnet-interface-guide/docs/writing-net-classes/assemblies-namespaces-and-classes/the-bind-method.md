# The Bind Method

The `Bind` method is described in the Dyalog for Microsoft Windows Object Reference Guide. A subset of the `Bind` method can be used on any supported platform to export .NET assemblies. Specifically, the expression:
```apl
      2 ⎕NQ '.' 'Bind' <filename> 'Library'
```

creates a .NET assembly (in `<filename>`) that contains the APL code in the classes in the active workspace

This use of the `Bind` method is similar to selecting File > Export... in the Session.
