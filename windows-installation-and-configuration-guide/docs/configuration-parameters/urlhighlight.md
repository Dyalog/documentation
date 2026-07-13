# URLHighlight

Specifies whether or not URLs and links are highlighted in Session and Edit windows. Its value is either 1 (highlight) or 0. The default is 0.

If this option is selected, valid URLs are identified when the cursor is in the Session or in an Edit or Trace window. When the mouse pointer is over a URL, the URL is underscored and the appropriate items in the Session Popup menu are activated. These allow you to open the link or copy it to the clipboard.

You may also open a URL using Ctrl+Click (Left Mouse button).

Currently a URL string is defined to be a string starting with any of the following strings:

- http://
- https://
- www.
- mailto:

See also [Underline URLs and links](../configuring-the-ide/configuration-dialog/configuration-dialog-general-tab.md).
