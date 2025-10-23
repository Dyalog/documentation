# System Requirements

This page describes the hardware and software requirements for Dyalog v20.0. 

## Supported Dyalog Versions

Current version: Dyalog v20.0  
Previous supported versions: Dyalog v19.0 and v18.2  

Dyalog v18.0 and earlier versions are no longer supported.  

### Supported Platforms
Dyalog v20.0 is supported on the following platforms/operating systems:  

* IBM AIX:
    * AIX 7.2 SP2 TL2 onwards with a POWER9 chip or higher
* Linux:
    * x86_64: Built on Ubuntu 20.04
    * ARM64: Built on Debian GNU/Linux 12
* macOS (ARM-based, Apple M1 or later):
    *  macOS 13.4.1 (Ventura) onwards
* Microsoft Windows:
    * Windows 10 onwards (Windows Server 2016 onwards)
* Raspberry Pi (ARM-based): 
    * 32-bit: Raspberry Pi OS Buster or later  
    NOTE: Does not run on a 64-bit operating system
    * 64-bit: Raspberry Pi OS Bookworm or later  
    NOTE: Installed using the Linux ARM64 package
    * Not supported on Raspberry Pi Pico
## External .NET Requirements  

### .NET
The .NET interface requires version 8.0 of Microsoft .NET or higher.  

!!! Info "Information"
    Dyalog v20.0 supports .NET v8.0 and later, but is configured to support .NET v8.0 by default. To support a later version of .NET, minor amendments are needed to two of the files installed with Dyalog – see the [_.NET Interface Guide_](../../files/dotNET_Interface_Guide.pdf) for more information.

### Microsoft .NET Framework
The .NET Framework interface requires version 4.0 or greater of Microsoft .NET Framework. It does not operate with earlier versions of the .NET Framework. In addition:  

* Microsoft .NET Framework version 4.5 is needed for full data binding support.  
Note: This includes support for the <code class="language-other">INotifyCollectionChanged</code> interface, which is used by Dyalog to notify a data consumer when the contents of a variable that is data bound as a list of items changes.  
* IIS (and ASP.NET) need to be installed before installing Dyalog. If these are not present when Dyalog is installed, the **[DYALOG]/Samples/asp.net** directory will not be installed.  

## Chromium Embedded Framework (CEF)
Dyalog v20.0 is supplied with CEF version 138 on all supported platforms.

In versions of CEF supplied with earlier versions of Dyalog, pop-ups and light mode were enabled by default. This is no longer the situation. To minimise differences between Dyalog v19.0 and Dyalog v20.0 when using CEF-based applications, two temporary environment variables (not configuration parameters) have been introduced to preserve these settings for Dyalog v20.0 only. These are:

- DYALOG_CEF_ALLOW_POPUPS<br />Specifies whether pop-ups are disabled for CEF-based applications (the default for CEF v138 depends on the operating system). Possible values are:
    - `1` : pop-ups are not disabled (equivalent to <code class="language-nonAPL">--disable-popup-blocking</code>)
	- any other value is ignored, and CEF's default (as determined by the user's operating system preferences) is used.  
	
	The default is `1`.
	
- DYALOG_CEF_DARK_MODE<br />Specifies whether CEF-based applications are displayed in dark or light mode (the default for CEF v138 is dark mode). Possible values are:
    - `0` : display using light mode (equivalent to <code class="language-nonAPL">--force-light-mode</code>)
    - `1` : display using dark mode (equivalent to <code class="language-nonAPL">--force-dark-mode</code>)
	- `2` : display using CEF's default (as determined by the user's operating system preferences)  

    The default is `2`.

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