# <span>Printer</span> <span>Object</span>



[Parents](../parentlists/printer.md), [Children](../childlists/printer.md), [Properties](../proplists/printer.md), [Methods](../methodlists/printer.md), [Events](../eventlists/printer.md)



**Purpose:** To provide printer output.

**Description**


The [PName](../properties/pname.md) property is a character vector which specifies the name of an installed printer and the device to which it is attached. The name and device are separated by a comma (,). All valid values of [PName](../properties/pname.md) can be obtained from the [PrintList](../properties/printlist.md) property of the [Root](root.md) object.



If not specified, the default value of [PName](../properties/pname.md) is `(⊃'.' ⎕WG 'PrintList')`.


The [DevCaps](../properties/devcaps.md) property reports the size of the printable area of the page in pixels (dots) and in millimetres. It also reports the number of colours available. This is 2 on a monochrome printer (black and white), although grey scales may be available.


The [FontList](../properties/fontlist.md) property provides a list of fonts that are applicable and includes TrueType and printer fonts. This list is typically different from that obtained from the [FontList](../properties/fontlist.md) property on the [Root](root.md) object which lists those fonts that apply to the screen.


The Orientation property specifies the orientation of the page and may be either `'Portrait'` or `'Landscape'`.


The graphics objects listed above may be printed in much the same way as they may be displayed on a [Form](form.md) or [Static](static.md). The differences are :


Once an object has been created, it will be printed, even if its name is subsequently expunged.


An object does not **replace** an existing one which has the same name.


The act of changing one or more properties of a named object causes the object to be printed a second time. For example, changing the [Posn](../properties/posn.md) of an object will print it again at a different place.


In general it is recommended that you use unnamed objects for printing.


The Printer object five methods :


|---------------------------------------------------|-----|----------------------------------|
|Name                                               |Event|Description                       |
|[Print](../methodorevents/print.md)                |100  |Sends output to print spooler     |
|[Setup](../methodorevents/setup.md)                |101  |Displays Printer Set-up dialog box|
|[NewPage](../methodorevents/newpage.md)            |102  |Throws a new page                 |
|[Abort](../methodorevents/abort.md)                |103  |Aborts the print job              |
|[RTFPrintSetup](../methodorevents/rtfprintsetup.md)|460  |Displays Printer Set-up dialog box|

<h2 class="example">Examples</h2>


Start a print job on the default printer
```apl
      'PR1' ⎕WC 'Printer'
```


Write a centred heading at the top of the page using a proportional font
```apl
      'PR1.' ⎕WC 'Text' 'Report Title' (0 50)('HAlign' 1) ('FontObj' 'Roman' 64)
```


Draw a line across the page, 2 pixels wide
```apl
      'PR1.' ⎕WC 'Poly' (2(0 100)) ('LWidth' 2)
```


Print a character matrix. Note that a fixed width font is used.
```apl
      REPORT ← 'I6' ⎕FMT ?20 6⍴1000
      'PR1.' ⎕WC 'Text' REPORT (10 0)('FontObj' 'DyalogAPL')
```


Throw a new page
```apl
      PR1.NewPage
```


Spool output
```apl
      ⎕EX 'PR1'
```


