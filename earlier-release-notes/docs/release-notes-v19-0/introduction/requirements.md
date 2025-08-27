<h1 class="heading"><span class="name">System Requirements</span></h1>

## Microsoft Windows

Dyalog version 19.0 is supported on versions of Microsoft Windows from Windows 10 or Windows Server 2016 upwards.

The Dyalog version 19.0 .NET Framework interface requires version 4.0 or greater of Microsoft .NET Framework. It does *not* operate with earlier versions of the .NET Framework. In addition:

- .NET Framework version 4.5 is needed for full Data Binding support (including support for the INotifyCollectionChanged interface, which is used by Dyalog to notify a data consumer when the contents of a variable, that is data bound as a list of items, changes).
- .NET Framework version 4.6 is needed to run the Syncfusion libraries supplied with Dyalog version 19.0.
- IIS needs to be installed before installing Dyalog APL in order to access the examples in the `Samples/asp.net` sub-directory – if IIS and ASP.NET are not present, the `asp.net` sub-directory will not be installed during the Dyalog installation.

Note that .NET Framework is specific to Microsoft Windows; the cross-platform .NET is also supported (see below).

## AIX

Dyalog version 19.0 requires AIX 7.2 or higher, and a POWER9 chip or higher.

## Raspberry Pi

Dyalog 32-bit Unicode supports 32-bit Raspberry Pi OS Buster or later but is not supported on the Raspberry Pi Pico. There is no 64-bit version of Dyalog for the Pi, nor will the 32-bit version run under 64-bit Raspberry Pi OS.

## Non-Pi Linux

Dyalog version 19.0 only exists as 64-bit interpreters – there are no 32-bit versions.  It is built on Ubuntu 20.04; it should run on all recent distributions. For further information, see [the Dyalog UNIX and Linux forum.](https://forums.dyalog.com/viewforum.php?f=20)

## macOS

Dyalog version 19.0 (64-bit version; there is no 32-bit version) is supported on both Intel and ARM processors. The macOS version required for Dyalog version 19.0 on each is:

- on Intel: macOS 11.6.1 (Big Sur) onwards
- on ARM: macOS 13.4.1 (Ventura) onwards

Dyalog for ARM is only supported on Macs with an ARM processor. Dyalog for Intel is supported on Macs with an Intel chip or Macs with an ARM chip and Rosetta enabled. Each has its own shared libraries. These, and any other customisations, must match the Dyalog installation.

## Cross-platform Microsoft .NET Interface

The Dyalog version 19.0 .NET interface requires version 8.0 of Microsoft .NET or higher.

## HTMLRenderer and Chromium Embedded Framework (CEF)

The HTMLRenderer is supported on the following platforms:

- Windows
- macOS (both Intel and ARM-based)
- Linux 

It is not supported on the Raspberry Pi

To see which version of CEF was used when the HTMLRenderer was built, query the CEFVersion property of an instance of the HTMLRenderer:
```apl
      'hr' ⎕WC 'HTMLRenderer'
      hr.CEFVersion[2 3]⍝ CEF Maj Version and Commit No
121 3
```
