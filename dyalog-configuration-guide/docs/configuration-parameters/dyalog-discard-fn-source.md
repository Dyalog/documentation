# DYALOG_DISCARD_FN_SOURCE

Whether source code is discarded when a function or operator is fixed by the editor or by `⎕FIX`.

Valid values are:

- `0` : source code is retained in the workspace, and is presented for editing as it was previously saved
- `1` : source code is discarded when an object is fixed (source code already retained in the workspace is not deleted)

Default is `0`.

For more information, see [Discard Source Information](../../../language-reference-guide/primitive-operators/i-beam/discard-source-information) and [Source as Typed](../../../earlier-release-notes/release-notes-v19-0/introduction/source-as-typed).
