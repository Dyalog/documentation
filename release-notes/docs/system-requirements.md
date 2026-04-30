# System Requirements

<p style="color:red;">This document is currently being developed and will not be finalised until nearer the release of Dyalog v21.0.</p>

This page describes the hardware and software requirements for Dyalog v21.0. 

## Supported Dyalog Versions

Current version: Dyalog v21.0  
Previous supported versions: Dyalog v20.0 and v19.0  

Dyalog v18.2 and earlier versions are no longer supported.  

### Supported Platforms
Dyalog v21.0 is supported on the following platforms/operating systems:  

T.B.A.

## External .NET Requirements  

### .NET

T.B.A.

### Microsoft .NET Framework

T.B.A.  

## Chromium Embedded Framework (CEF)

T.B.A.

### HTMLRenderer

The HTMLRenderer is supported on the following platforms:  

* Linux (x86_64 only)
* macOS
* Microsoft Windows  

To see which version of CEF was used when the HTMLRenderer was built, query the `CEFVersion` property of an instance of the HTMLRenderer:
```apl
      'hr' ⎕WC 'HTMLRenderer'
      hr.CEFVersion[2 3]      ⍝ CEF major version and commit number
121 3
```
### Auxiliary Processors

If the configuration parameter `ENABLE_CEF` is `1`, Auxiliary Processors cannot be used (they hang on error). By default, `ENABLE_CEF` is `1` (unless you are not running under a desktop, for example, you are running Dyalog in a PuTTY session; in this case the default is `0`).

-->
