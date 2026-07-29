# SkipLines

Causes the Tracer to skip lines that contain no executable statement, with the exception of the first line of the function and, in a traditional function (not a dfn), the last line if it is a comment.

The value is the sum of the following:

- `1` : skip blank lines
- `2` : skip comment lines
- `4` : skip locals lines

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->

See also the [Trace/Edit tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab.md) of the Windows Configuration Dialog.
