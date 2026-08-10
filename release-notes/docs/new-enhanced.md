# New Features, Changes, and Enhancements

This page describes the changes and new features in Dyalog v21.0 compared with Dyalog v20.0.

## Language Changes

### System Functions

The following system functions have been added:

- [`⎕SYSTEM`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/system/) – System Information  
This returns a namespace providing information about the current Dyalog interpreter and the host environment.

The following system functions have been enhanced:

- [`⎕CSV`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/csv/) – Comma Separated Values  
A new variant option, **ForceQuotes**, has been added. This specifies when exported data has quotes around character/numeric fields.
- [`⎕DT`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/dt/) – Datetime  
The ability to extract datetimes from text-formatted datetimes, as well as the functionality previously provided by [`1200⌶`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/i-beam/format-datetime/), has been added:
    - The left argument `X` has been extended; its single element or either/both of the elements in its 2-element vector can now also be character vectors (not scalars) comprising patterns that describe how a datetime is, or is to be, formatted as text. 
	- The right argument `Y` has been extended; it can now be a character vector, formatted according to a *formatting pattern* (known as by a *text-formatted datetime*).
    - Two new variant options have been added:
	    - **Dictionary** specifies a namespace that contains additional or replacement names for the months (and so on) and/or predefined patterns, for languages and language regions.
		- **Language** specifies the language used for formatting and matching datetimes.
- [`⎕UCS`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/ucs/) – Unicode Convert  
The optional left argument `X` can now be a 2-element nested array when performing UTF-8 conversions; setting the second element to `83` enables the direct creation and consumption of integers in the range `¯128` to `+127`.

### I-beams

!!! Warning "Warning"  
    Any service provided using an I-Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I&#8209;Beams in applications should, therefore, be carefully isolated in cover-functions that can be adjusted if necessary.
	
The following I-beams have been deprecated:

- [`43⌶`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/i-beam/monadic-operator-generator/) – Monadic Operator Generator (introduced in Dyalog v20.0)  
The functionality provided by `43⌶632` is now provided by a new `[...]` mechanism – see [Generics (.NET)](https://docs.dyalog.com/21.0/net-interface-guide/dotnet-classes/advanced-techniques/#generics) and [Generics (.NET Framework)](https://docs.dyalog.com/21.0/net-framework-interface-guide/dotnet-classes/advanced-techniques/#generics). As alternative values of `Y` are not available, the I-beam has been deprecated and scheduled for removal in Dyalog v22.0; it could be reintroduced with new `Y` values in a later release.
- [`739⌶`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/i-beam/temporary-directory/) – Temporary Directory (introduced in Dyalog v17.0)  
The functionality provided by `739⌶` is now provided by `⎕SYSTEM` (specifically, `⎕SYSTEM.Directories.Temp` replaces `739⌶0`). It is scheduled for removal in 2029.
- [`1200⌶`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/i-beam/format-datetime/) – Format Date-Time (introduced in Dyalog v18.0)  
The functionality provided by `1200⌶` is now provided by `⎕DT`. It is scheduled for removal in 2029.

## Objects

The following objects have been enhanced:

- [Form](https://docs.dyalog.com/21.0/object-reference/objects/form/) object – four properties can now be changed after creation using `⎕WS`. These are [HelpButton](https://docs.dyalog.com/21.0/object-reference/properties/helpbutton/), [MaxButton](https://docs.dyalog.com/21.0/object-reference/properties/maxbutton/), [MinButton](https://docs.dyalog.com/21.0/object-reference/properties/minbutton/), and [SysMenu](https://docs.dyalog.com/21.0/object-reference/properties/sysmenu/).
- [Printer](https://docs.dyalog.com/21.0/object-reference/objects/printer/) object – two new properties have been added:
    - The [Dirty](https://docs.dyalog.com/21.0/object-reference/properties/dirty/) property indicates whether the current page is considered to have content.
    - The [PagesBeginDirty](https://docs.dyalog.com/21.0/object-reference/properties/pagesbegindirty/) property indicates whether a new page in a document will be printed even if it has no content.

## Development Environment Changes

### Configuration Parameters

The following configuration parameters have been added:

- [`DYALOG_EXTVAR_SUPPORTED`](https://docs.dyalog.com/21.0/windows-installation-and-configuration-guide/configuration-parameters/dyalog-extvar-supported/)  
This specifies whether support for external variables is enabled.

- [`LAYOUT_FILE`](https://docs.dyalog.com/21.0/windows-installation-and-configuration-guide/docs/configuration-parameters/layout-file/) (Microsoft Windows only)  
This specifies the path (absolute or relative to the working directory) and name of the Session layout file.

### Configuration Settings

The following changes have been made to configuration settings:

- Substitutions can now be made within any configuration settings; previously this only worked within configuration files. It remains unsupported beyond configuration settings, for example, `)LOAD [DYALOG]/myws.dws` is not valid. There is a small chance that existing configuration settings could now see unintended substitution; to ensure that this does not happen, when including literal square brackets in a string, the `[` should be prefixed with a backslash, that is `/[` (the backslash is removed from the subsequent value).
- On Microsoft Windows, `[=DOCUMENTS]` is pre-defined to refer to the location of the user's Documents folder (for example, **C:\Users\Bob\Documents**).

### Microsoft Windows IDE

The following changes have been made to the Microsoft Windows IDE:

- The purpose and items in the [**Layout** menu](https://docs.dyalog.com/21.0/windows-ui-guide/session-menubar/#the-layout-menu) have been changed:
    - Selections from the **Layout** menu now apply to the layout of the Session and of the tools that are docked in it, including the Editor and the Debugger, rather than only to the Debugger.
	- The **Debugger on the left** item has been removed.
	- A new item, **Open...**, displays the **Open Session layout** dialog box.
    - A new item, **Classic with Vertical Inline Tracing**, configures the Session as with Classic Dyalog mode but with the Left Argument pane docked above the Tracer and the Right Argument pane docked below it. 	
- A new **Open Session layout** dialog box has been added. This enables the selection of a Session layout file (that is, a **.layout** file).
	
## Interfaces

### .NET Interface

Square brackets (`[...]`) are now used to apply type arguments when instantiating generic methods, classes, and interfaces; this supersedes the I-beam that was used previously. For more information, see [Generics](https://docs.dyalog.com/21.0/net-interface-guide/dotnet-classes/advanced-techniques/#syntax).

### .NET Framework Interface

Support for.NET _generics_ was previously only available for the .NET Interface – it is now also available in the .NET Framework Interface. This means that the .NET Framework Interface now supports creating concrete versions of generic classes, instantiating them, and calling generic methods. For more information, see [Generics](https://docs.dyalog.com/21.0/net-framework-interface-guide/dotnet-classes/advanced-techniques/#generics).
