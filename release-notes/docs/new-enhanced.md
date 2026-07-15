# New Features, Changes, and Enhancements

This page describes the changes and new features in Dyalog v21.0 compared with Dyalog v20.0.

<p style="color:red;">This document is currently being developed and will not be finalised until nearer the release of Dyalog v21.0.</p>

## Language Changes

### System Functions

The following system functions have been added:

- [`⎕SYSTEM`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/system/) – System Information<br />This returns a namespace providing information about the current Dyalog interpreter and the host environment.

The following system functions have been enhanced:

- [`⎕CSV`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/csv/) – Comma Separated Values<br />A new variant option, **ForceQuotes**, has been added. This specifies when exported data has quotes around character/numeric fields.

### I-beams

!!! Warning "Warning"  
    Any service provided using an I-Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I&#8209;Beams in applications should, therefore, be carefully isolated in cover-functions that can be adjusted if necessary.

The following I-beams have been deprecated:

- [`43⌶`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/i-beam/monadic-operator-generator/) – Monadic Operator Generator (introduced in Dyalog v20.0)  
The functionality provided by `43⌶632` is now provided by a new `[...]` mechanism – see [Generics (.NET)](https://docs.dyalog.com/21.0/net-interface-guide/dotnet-classes/advanced-techniques/#generics) and [Generics (.NET Framework)](https://docs.dyalog.com/21.0/net-framework-interface-guide/dotnet-classes/advanced-techniques/#generics). As alternative values of `Y` are not available, the I-beam has been deprecated and scheduled for removal in Dyalog v22.0; it could be reintroduced with new `Y` values in a later release.

- [`739⌶`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/i-beam/temporary-directory/) – Temporary Directory (introduced in Dyalog v17.0)
The functionality provided by `739⌶` is now provided by `⎕SYSTEM` (specifically, `⎕SYSTEM.Directories.Temp` replaces `739⌶0`). It is scheduled for removal in 2029.

## Interfaces

### .NET Interface

Square brackets (`[...]`) are now used to apply type arguments when instantiating generic methods, classes, and interfaces; this supersedes the I-beam that was used previously. For more information, see [Generics](https://docs.dyalog.com/21.0/net-interface-guide/dotnet-classes/advanced-techniques/#syntax).

### .NET Framework Interface

Support for.NET _generics_ was previously only available for the .NET Interface – it is now also available in the .NET Framework Interface. This means that the .NET Framework Interface now supports creating concrete versions of generic classes, instantiating them, and calling generic methods. For more information, see [Generics](https://docs.dyalog.com/21.0/net-framework-interface-guide/dotnet-classes/advanced-techniques/#generics).
