# UnicodeToClipboard

!!! Info "Information"
    This configuration parameter is only relevant when using the Classic edition of Dyalog.

Whether text transferred to and from the Windows clipboard is treated as Unicode text.

Valid values are:

- `0` : the symbols in `⎕AV` are mapped to ASCII text (0–255); APL symbols are mapped to ASCII symbols by their position in the Dyalog APL font
- `1` : the symbols in `⎕AV` are mapped to Unicode text; APL symbols are mapped to their genuine Unicode equivalents

Default is `0`.

See also the [Trace/Edit tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab) of the Windows Configuration Dialog.
