<h1 class="heading"><span class="name">Introduction</span></h1>

`APLScript` is a Dyalog scripting language. It was originally designed specifically to program ASP.NET Web Pages and Web Services, but it has been extended to be of more general use outside the Microsoft .NET environment.

`APLScript` is not workspace oriented (although you can call workspaces from it) but is simply a character file containing function bodies and expressions.

`APLScript` files may be viewed and edited using any character-based editor which supports Unicode text files, such as `Notepad`. `APLScript` files may also be edited using Microsoft Word, although they must be saved as text files without any Word formatting.

`APLScript` files employ Unicode encoding so you need a Unicode font with APL symbols, such as APL385 Unicode, to view them. In order to type Dyalog symbols into an `APLScript` file, you also need the Dyalog Input Method Editor (IME), or other APL compatible keyboard.

If you choose to use the Dyalog IME it can be configured from the Dyalog *Configuration* dialog. You may change the associated `.DIN` file and various other options. See *Unicode Input Tab (Unicode Edition Only)*.

There are basically three types of APLScript files that may be identified by three different file extensions. APLScript files with the extension `.aspx` and `.asmx` specify .NET classes that represent ASP.NET Web Pages and Web Services respectively. APLScript files with the extension `.apl` may specify .NET classes or may simply represent an APL application in a script format as opposed to a workspace format. Such applications do not necessarily require the Microsoft .NET Framework.
