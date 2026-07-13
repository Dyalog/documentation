# AutoFormat

This parameter specifies whether or not you want automatic formatting of Control Structures in functions. The default value is 1 which means that formatting is done automatically for you when a function is opened for editing or converted to text by `⎕CR`,  `⎕NR` and `⎕VR`. Automatic formatting first discards all leading spaces in the function body. It then prefixes all lines with a single space except those beginning with a label or a comment symbol (this has the effect of making labels and comments stand out). The third step is to indent Control Structures. The size of the indent depends upon the **TabStops** parameter. To turn off automatic formatting, set **AutoFormat** to 0.

See also [Autoformat functions](../configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab.md).
