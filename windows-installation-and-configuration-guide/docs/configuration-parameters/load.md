<h1 class="heading"><span class="name">Load</span></h1>

This parameter is a character string that specifies the name of a workspace, or a directory or text file containing APL source code, to be loaded when Dyalog starts.

If Load specifies a text file, `2 ⎕FIX` is used to import the file contents and associate that file with each of the objects that have been fixed in the workspace.

If Load specifies a directory, Link is used to associate the directory with the active workspace and to import the code.
 For more information about Link, see [https://dyalog.github.io/link](https://dyalog.github.io/link).

The **Load** parameter will normally be specified on the command line or in a Configuration file.

Having loaded the workspace, or fixed the code from the named file or directory, Dyalog executes the expression specified by the `LX` parameter if it is set. See [LX](lx.md).

If `LX` is not set, Dyalog checks whether or not the **-x** command line option was specified. If so, no further action is taken. See [-x](../apl-command-line.md#command-line).

Otherwise, Dyalog executes an expression which is derived as follows.

If the value of Load is a directory, Dyalog will execute the expression:
```apl
 Run ,⊂<Load>
```

where `<Load>` is the value of the **Load** parameter.

If the value of Load is the name of a file, Dyalog determines whether or not the file is a workspace by its internal signature.

If the file is a workspace the expression to be executed is specified by its `⎕LX`. See [Latent Expression](../../../../language-reference-guide/system-functions/lx).

Otherwise, if the file extension is `.aplf` `.aplc` or `.apln` the expression is shown in the table below, where `filename` is the file name specified by the **Load** parameter without its extension.

|File Extension|Type                 |Expression          |
|--------------|---------------------|--------------------|
|`.aplf`       |Function source code |`filename 0⍴⊂''`    |
|`.aplc`       |Class source code    |`filename.Run 0⍴⊂''`|
|`.apln`       |Namespace source code|`filename.Run 0⍴⊂''`|

## Notes

- The **Load** parameter overrides a workspace name specified as the last item on the command line.
- The argument `0⍴⊂''` may change in a future version of Dyalog.
- Nothing is executed when code is loaded from source files that define operators (`.aplo`) or Interfaces (`.apli`).
