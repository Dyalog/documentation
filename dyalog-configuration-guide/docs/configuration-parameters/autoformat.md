# AutoFormat

Whether Control Structures are formatted automatically when a function is opened for editing or converted to text by `⎕CR`, `⎕NR`, or `⎕VR`. Automatic formatting discards leading spaces in the function body, prefixes each line with a single space except those beginning with a label or comment symbol (so that labels and comments stand out), and indents Control Structures by the width given in [`TabStops`](tabstops.md).

Valid values are:

- `0` : no automatic formatting
- `1` : Control Structures are formatted automatically

Default is `1`.

Related parameters: [TabStops](tabstops.md), [AutoIndent](autoindent.md).

See also the [Trace/Edit tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab.md) of the Windows Configuration Dialog.
