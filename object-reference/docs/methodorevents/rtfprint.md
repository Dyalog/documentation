# <span>RTFPrint</span> <span>Method 461</span>

**Applies To:** [RichEdit](../objects/richedit.md)

**Description**

This method is used to print the contents ([RTFText](../properties/rtftext.md)) of a [RichEdit](../objects/richedit.md) object.

The argument to RTFPrint is `⍬`, or a 1 to 4-element array as follows:

|-----|----------------|---------------------------------------|
|`[1]`|Printer name    |Optional - character vector (see below)|
|`[2]`|Print range     |Optional - (see below)                 |
|`[3]`|Number of copies|Optional - Integer.                    |
|`[4]`|Collate         |Optional - 0 or 1                      |

*Printer name* may be the name of an existing Printer object, or the (Windows) name of an installed printer. If you use the latter, the document will be spooled immediately. An empty vector implies the default printer.

*Print range* may be a simple character vector containing `'All'`, `'Pages'`, or `'Selection'`. Alternatively, it may be a 3 or 4-element nested vector containing:

|-----|--------------------------------------|
|`[1]`|`'All'` , `'Pages'` , or `'Selection'`|
|`[2]`|Start page (integer)                  |
|`[3]`|End page (integer)                    |
|`[4]`|Maximum pages (ignored)               |
