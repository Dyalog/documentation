# SkipLines

This parameter causes the Tracer to automatically skip lines that contain no executable statement, with the exception of the first line in the function, and in the case of a traditional function (not a dfn), the last line if it is a comment. SkipLines is an integer made up of the sum of the following values:

|---|----------------------------------------------------------------------------------------------------------------------------------------------------|
|1  |Skip blank lines. See also [Skip blank lines when tracing](../configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab.md) .    |
|2  |Skip comment lines. See also [Skip comment lines when tracing](../configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab.md) .|
|4  |Skip locals lines.  See also [Skip locals lines when tracing](../configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab.md) . |
