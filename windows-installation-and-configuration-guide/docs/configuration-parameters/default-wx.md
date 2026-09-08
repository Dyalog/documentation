# Default_WX

This parameter specifies the value of `⎕WX` in a clear workspace. This in turn determines whether or not the names of properties, methods and events of GUI objects are exposed. If set (`⎕WX` is 1), you may query/set properties and invoke methods directly as if they were variables and functions respectively. As a consequence, these names may not be used for global variables in GUI objects.

See also [Expose properties of GUI Namespaces](../configuring-the-ide/configuration-dialog.md#object-syntax-tab) and the [`⎕WX` field on the Session tab](../configuring-the-ide/configuration-dialog.md#session-tab).
