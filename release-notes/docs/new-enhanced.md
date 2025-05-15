!!! Info "Information"  
    THIS DOCUMENT IS STILL UNDER DEVELOPMENT

# New Features, Changes, and Enhancements

This page describes the changes and new features in Dyalog v20.0 compared with Dyalog v19.0.

## Language Changes

### I-beams

!!! Warning "Warning"  
    Any service provided using an I-Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I-Beams in applications should, therefore, be carefully isolated in cover-functions that can be adjusted if necessary.

#### New I-beams

The following I-beams have been added:

- `13⌶` – Deprecated Features  
Records information in the log file set by 109⌶ about the specified deprecated feature names or keywords  
For more information, see xxxLINKxxx.
- `43⌶` – Monadic Operator Generator  
Generates a monadic operator with specified functionality. The functionality is currently limited to creating a .NET-specific operator that can create concrete versions of generic classes and execute generic methods.  
For more information, see xxxLINKxxx.
- `109⌶` – Log File for Deprecations  
Manages the file used to log the use of deprecated features.  
For more information, see xxxLINKxxx.
- `120⌶` – Generate UUID  
Generates a UUID (Universally Unique IDentifier) according to the RFC 9562 specification.  
For more information, see xxxLINKxxx.
- `3535⌶` – Scan For Deprecated Files  
Scans the specified directory (and, optionally, sub-directories) for deprecated saved workspaces, component files, and external variables.  
For more information, see xxxLINKxxx.
- `5581⌶` – Unicode Normal Forms  
Applies the specified Unicode normalisation form to given character data.
This is a temporary I-beam – it is expected that it will be superseded by a system function in Dyalog v21.0.  
For more information, see xxxLINKxxx.
- `8373⌶` – Shell Process Control  
Provides a way to determine the process IDs of processes started by `⎕SHELL`, as well as enabling the sending of signals to any of those processes.  
For more information, see xxxLINKxxx.

#### Removed I-beams

The following I-beams have been removed:

- `819⌶` – Case Convert (introduced in Dyalog v15.0)  
The functionality provided by this I-beam is available through the `⎕C` system function. For more information, see xxxLINKxxx.
- `8468⌶` – Hash Table Size (introduced in Dyalog v19.0)  
Temporary functionality used for identification of potential side-effects of a change that has now been implemented. No longer relevant.
- `8469⌶` – Lookup Table Size (introduced in Dyalog v19.0)  
Temporary functionality used for identification of potential side-effects of a change that has now been implemented. No longer relevant.

## User Interface Changes

xxx

## Other Changes

### PCRE Library

The Perl Compatible Regular Expressions (PCRE) library used by the interpreter has been upgraded from PCRE v8.45 to PCRE2 v10.45.

!!! Warning "Warning"
    Some semantic changes introduced with this upgrade could result in unexpected results when using `⎕R`, `⎕S`, or the search functionality within the Microsoft Windows IDE (and all tools that build on these) compared to results in Dyalog v19.0.