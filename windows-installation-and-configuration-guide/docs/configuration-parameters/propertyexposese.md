# PropertyExposeSE

Each workspace contains a flag that specifies whether or the names of Properties, Methods and Events of the Session object are exposed. If set, you may query/set the Properties of `⎕SE` and invoke `⎕SE` Methods directly as if they were variables and functions respectively. As a consequence, these names may not be used for global variables in the `⎕SE` namespace. This parameter determines the default value of the flag in a `CLEAR WS`.

See also [Expose properties of Session Namespace](../configuring-the-ide/configuration-dialog/configuration-dialog-object-syntax-tab.md).
