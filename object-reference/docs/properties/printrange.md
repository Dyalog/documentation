# <span>PrintRange</span> <span>Property</span>

**Description**

The PrintRange property specifies the range of pages to be printed.

PrintRange may be an empty character vector (the default), or `'All'`, either of which will cause all pages to be printed.

Alternatively, PrintRange may be a 3 or 4-element nested array whose items are:

|-----|---------------------------------|
|`[1]`|`'Pages'`                        |
|`[2]`|Start page (integer)             |
|`[3]`|End page (integer)               |
|`[4]`|Maximum number of pages (integer)|

In this case, printing starts at the page specified to be 
the Start page, and ends at the page specified by End page or after the Maximum 
number of pages has been reached, whichever is sooner.

**Application**

Objects: [Printer](../objects/printer.md)
