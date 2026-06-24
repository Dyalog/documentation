# New Features, Changes, and Enhancements

This page describes the changes and new features in Dyalog v21.0 compared with Dyalog v20.0.

<p style="color:red;">This document is currently being developed and will not be finalised until nearer the release of Dyalog v21.0.</p>

## Syntax Changes

T.B.A.

## Language Changes

### Primitive Functions/Operators

T.B.A.

### System Functions

The following system functions have been added:

- T.B.A.

The following system functions have been enhanced:

- [`⎕CSV`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/csv/) – Comma Separated Values<br />A new variant option, **ForceQuotes**, has been added. This specifies when exported data has quotes around character/numeric fields.

### I-beams

!!! Warning "Warning"  
    Any service provided using an I-Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I&#8209;Beams in applications should, therefore, be carefully isolated in cover-functions that can be adjusted if necessary.

The following I-beams have been added:

- T.B.A.

The following I-beams have been deprecated:

- `43⌶` – Monadic Operator Generator (introduced in Dyalog v20.0)  
The functionality provided by `43⌶632` is now provided by a new `[...]` mechanism – see [Generics (.NET)](https://docs.dyalog.com/21.0/net-interface-guide/dotnet-classes/advanced-techniques/#generics) and [Generics (.NET Framework)](https://docs.dyalog.com/21.0/net-framework-interface-guide/dotnet-classes/advanced-techniques/#generics). As alternative values of `Y` are not available, the I-beam has been deprecated and scheduled for removal in Dyalog v22.0; it could be reintroduced with new `Y` values in a later release.

The following I-beams have been removed:

- T.B.A.

## Development Environment Changes

T.B.A.

### Configuration Parameters

The following configuration parameters have been added:

- T.B.A.

### Command Shortcuts

The following command shortcuts have been extended:

- T.B.A.

### Microsoft Windows IDE

The following changes have been made to the Microsoft Windows IDE:

- T.B.A.
	
### TTY Interface

The following changes have been made to the TTY interface:

- T.B.A.

## Interfaces

### .NET Interface

Square brackets (`[...]`) are now used to apply type arguments when instantiating generic methods, classes, and interfaces; this supersedes the I-beam that was used previously. For more information, see [Generics](https://docs.dyalog.com/21.0/net-interface-guide/dotnet-classes/advanced-techniques/#syntax).

### .NET Framework Interface

Support for.NET _generics_ was previously only available for the .NET Interface – it is now also available in the .NET Framework Interface. This means that the .NET Framework Interface now supports creating concrete versions of generic classes, instantiating them, and calling generic methods. For more information, see [Generics](https://docs.dyalog.com/21.0/net-framework-interface-guide/dotnet-classes/advanced-techniques/#generics).
