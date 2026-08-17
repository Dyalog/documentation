# Load

The name of a workspace, or of a directory or text file containing APL source code, to be loaded when Dyalog starts. It is normally given on the command line or in a configuration file, and overrides a workspace name given as the last item on the command line.

- If **Load** names a text file, `2 ⎕FIX` imports its contents and associates the file with each fixed object.
- If **Load** names a directory, Link associates the directory with the active workspace and imports the code (see [Link](https://dyalog.github.io/link)).

Having loaded the workspace or fixed the code, Dyalog executes the expression given by [`LX`](lx.md) if it is set. If `LX` is not set and the `-x` command-line option was given, no further action is taken. Otherwise Dyalog derives an expression to execute:

- if **Load** is a directory, `Run ,⊂<Load>`;
- if **Load** is a workspace (determined by its internal signature), the expression given by its [`⎕LX`](../../../language-reference-guide/system-functions/lx);
- otherwise, for a source file, according to its extension:

|File Extension|Type|Expression|
|---|---|---|
|`.aplf`|Function source code|`filename 0⍴⊂''`|
|`.aplc`|Class source code|`filename.Run 0⍴⊂''`|
|`.apln`|Namespace source code|`filename.Run 0⍴⊂''`|

where `filename` is the **Load** value without its extension. Nothing is executed for operator (`.aplo`) or interface (`.apli`) source files. (The argument `0⍴⊂''` might change in a future version.)

Related parameters: [LX](lx.md).
