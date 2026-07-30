# New Features, Changes, and Enhancements

This page describes the changes and new features in Dyalog v21.0 compared with Dyalog v20.0.

<p style="color:red;">This document is currently being developed and will not be finalised until nearer the release of Dyalog v21.0.</p>

## Language Changes

### System Functions

The following system functions have been added:

- [`⎕SYSTEM`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/system/) – System Information  
This returns a namespace providing information about the current Dyalog interpreter and the host environment.

The following system functions have been enhanced:

- [`⎕CSV`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/csv/) – Comma Separated Values  
A new variant option, **ForceQuotes**, has been added. This specifies when exported data has quotes around character/numeric fields.
- [`⎕DT`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/dt/) – Datetime  
The functionality previously provided by [`1200⌶`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/i-beam/format-datetime/) is now available using `⎕DT`:
    - The left argument `X` has been extended; its single element or either/both of the elements in its 2-element vector can now also be character vectors (not scalars) comprising patterns that describe how a datetime is, or is to be, formatted as text. 
	- The right argument `Y` has been extended; it can now be a character vector, formatted according to a *formatting pattern* (known as by a *text-formatted datetime*).
    - Two new variant options have been added:
	    - **Dictionary** specifies a namespace that contains additional or replacement names for the months (and so on) and/or predefined patterns, for languages and language regions.
		- **Language** specifies the language used for formatting and matching datetimes.
- [`⎕UCS`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/ucs/) – Unicode Convert  
The optional left argument `X` can now be a 2-element nested array when performing UTF-8 conversions; setting the second element to `83` enables the direct creation and consumption of 8-bit integers.

### I-beams

!!! Warning "Warning"  
    Any service provided using an I-Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I&#8209;Beams in applications should, therefore, be carefully isolated in cover-functions that can be adjusted if necessary.
	
The following I-beams have been added:

- [`4061⌶`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/i-beam/thread-discrepancy-counts/) – Thread Discrepancy Counts  
Reports the number of inconsistent thread statuses and missed thread wakeups that have been detected by the APL thread scheduler.  

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

## Interfaces

### .NET Interface

Square brackets (`[...]`) are now used to apply type arguments when instantiating generic methods, classes, and interfaces; this supersedes the I-beam that was used previously. For more information, see [Generics](https://docs.dyalog.com/21.0/net-interface-guide/dotnet-classes/advanced-techniques/#syntax).

### .NET Framework Interface

Support for.NET _generics_ was previously only available for the .NET Interface – it is now also available in the .NET Framework Interface. This means that the .NET Framework Interface now supports creating concrete versions of generic classes, instantiating them, and calling generic methods. For more information, see [Generics](https://docs.dyalog.com/21.0/net-framework-interface-guide/dotnet-classes/advanced-techniques/#generics).
