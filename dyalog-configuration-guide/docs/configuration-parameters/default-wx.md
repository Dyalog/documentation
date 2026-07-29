# Default_WX

The value of [`⎕WX`](../../../language-reference-guide/system-functions/wx) in a clear workspace. This determines whether the names of the properties, methods, and events of GUI objects are exposed: when they are (`⎕WX` is `1`), properties can be queried and set, and methods invoked, as if they were variables and functions, so those names cannot also be used for global variables in GUI objects.

Valid values are those of `⎕WX`: `0`, `1`, or `3`.

Default is `3`.
<!-- REVIEW(default): ⎕WX clear-workspace default not stated in the migrated source; confirm (expected 3). -->

!!! Info "Information"
    UNIX and macOS versions of Dyalog have no GUI objects, but `⎕SE` is present, so `⎕WX` still affects expressions such as `⎕SE.PropList`.

See also [Expose properties of GUI Namespaces](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-object-syntax-tab) in the Windows Configuration Dialog.
