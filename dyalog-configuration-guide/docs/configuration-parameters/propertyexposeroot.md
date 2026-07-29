# PropertyExposeRoot

The default value, in a clear workspace, of the flag that specifies whether the names of the properties, methods, and events of the Root object are exposed. When set, the properties of Root can be queried and set, and its methods invoked, as if they were variables and functions, so those names cannot also be used for global variables in the workspace.

Valid values are:

- `0` : the names are not exposed
- `1` : the names are exposed

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->

Related parameters: [PropertyExposeSE](propertyexposese.md), [Default_WX](default-wx.md).

See also the [Object Syntax tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-object-syntax-tab.md) of the Windows Configuration Dialog.
