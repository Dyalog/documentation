<h1 class="heading"><span class="name">APL Source Files</span></h1>

APL Source files contain definitions (the "source") of one or more named APL objects, that is, functions, operators, namespaces, classes, interfaces, and arrays. They cannot contain anything else. They are not workspace-oriented (although you can call workspaces from them) but are simply character files containing function bodies and expressions. This means that they would be valid right arguments to `2 ⎕FIX`.

APL Source files employ Unicode encoding, so you need a Unicode font with APL symbols, such as APL385 Unicode, to create or view them. They can be viewed and edited using any character-based editor that supports Unicode text files.

To enter Dyalog APL symbols into an APL Source file, you need the Dyalog Input Method Editor (IME) or other APL compatible keyboard. The Dyalog IME can be configured from the Dyalog Configuration dialog box. You can change the associated **.DIN** file or there are various other options. APL Source files can also be edited using Microsoft Word, although they must be saved as text files without any Word formatting. For more information, see the _Dyalog for Microsoft Windows Installation and Configuration Guide_.

There are three types of APL Source files that can be identified by three different file extensions:

- the **.aspx** extension specifies .NET classes that represent ASP.NET web pages.
- the **.asmx** extension specifies .NET classes that represent ASP.NET web services.
- the **.apl** extension can either specify .NET classes or could represent an APL application in a script format (as opposed to a workspace format). Such applications do not necessarily require .NET. **.apl** extensions can, optionally, be further categorised, for example:

    - **.apla** files contain array definitions
    - **.aplc** files contain class definitions
    - **.aplf** files contain function definitions
    - **.apli** files contain interface definitions
    - **.apln** files contain namespace definitions
    - **.aplo** files contain operator definitions
