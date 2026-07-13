# <span>PaperSize</span> <span>Property</span>



**Applies To:** [Printer](../objects/printer.md)

**Description**


The PaperSize property specifies the size of paper to be used for printing


PaperSize may be a character vector containing the name of the paper size (for example, `'Legal 8 1/2 x 14 in'` or `'A4 210 x 297 mm'`) or a 2-element integer vector that specifies the desired height and width of the paper in tenths of a millimetre (for example, 3556 2159 or 2970 2099).


The default value of PaperSize is the name of the paper size associated with the current printer settings.


You can obtain a list of supported paper sizes from the [PaperSizes](papersizes.md) property.



