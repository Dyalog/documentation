---
search:
  boost: 2
---

# <span>System Information</span> `R←⎕SYSTEM`{{key}}

This function returns a namespace providing information about the current Dyalog interpreter and the host environment.

## Syntax

`⎕SYSTEM` is niladic.

<h3 class="example">Examples</h3>

Reporting the current directory:
```apl
      ⎕SYSTEM.Directories.Current
C:\Program Files\Dyalog\Dyalog APL-64 21.0 Unicode
```
Finding the operating system's preferred directory separator:
```apl
      ⎕SYSTEM.OS.DirectorySeparator
\
```
Getting the currently running APL interpreter's version number:
```apl
      ⎕SYSTEM.Executable.VersionNumber
21
```

The result `R` is a namespace in the root (`#` or `⎕SE`) of the current namespace. `R` contains only namespace members, each of which only contains variable members.

More members might be added in a future release of Dyalog, but `R` will remain serialisable using [`1∘⎕JSON`](json.md).

!!! Warning "Warning"
    Do not attempt to add or modify members (changes will not be persisted); only modify clones of the namespace (`⎕NS ⎕SYSTEM`). Note that this locks down dynamic values like `⎕SYSTEM.Directories.Current` and `⎕SYSTEM.OS.UTCOffset`.

## Members of the Result

### CommandLine
This namespace provides information about the command line expression used to start the interpreter. 

<h4>CommandLine.Args</h4>

The command line used to start the current executable, split on unquoted space sequences into a vector of character vectors.

<h4>CommandLine.CodeArgs</h4>

This member is intended to ease usage of APL shell scripts. It is equivalent to [CommandLink.Args](#commandlineargs) but omits everything up to and including `-script`. If Dyalog is started without `-script` then nothing is omitted.

<h4>CommandLine.Full</h4>

The full command line used to start the current executable as a simple character vector.

### Directories
This namespace provides pertinent locations in the file system.

<h4>Directories.Current</h4>

The current working directory.

<h4>Directories.Initial</h4>

The directory from which Dyalog was started.

<h4>Directories.Temp</h4>

The operating system's recommended location for temporary files.

This location is for an individual user and can be cleaned up without warning, so use it only as a place to put files that will immediately be used and will not be needed later.

It is good practice to [delete](ndelete.md) such files when no longer needed.

### Executable
This namespace provides information about the specific interpreter instance in which `⎕SYSTEM` was called.

<h4>Executable.Bits</h4>

Indicates whether the interpreter is a 64- or 32-bit application.

!!! Warning "Warning"
    Do not confuse this with the bit width of the operating system; some 64-bit operating systems can run 32-bit interpreters (but not the other way round).

<h4>Executable.BuildTarget</h4>

_For Dyalog internal use only._

<h4>Executable.BuildType</h4>

_For Dyalog internal use only._

<h4>Executable.Path</h4>

The full file path to the interpreter's executable file.

<h4>Executable.RideConnected</h4>

Boolean indicating whether (`1`) or not (`0`) there is an active connection using the RIDE protocol.

<h4>Executable.Runtime</h4>

Boolean indicating whether (`1`) or not (`0`) this is a runtime interpreter.

<h4>Executable.Unicode</h4>

Boolean indicating whether (`1`) or not (`0`) the interpreter can represent characters outside [`⎕AV`](av.md).

<h4>Executable.Vendor</h4>

The originator of the interpreter, that is, `'Dyalog'`.

<h4>Executable.Version</h4>

The interpreter's full version number as three integers indicating the major release, minor release, and build number. For example, `21 0 53977`

<h4>Executable.VersionMoniker</h4>

A six-character shorthand for the `Version`'s first two elements together with `Unicode` and `Bits`, for example `210U64`.

This is particularly useful to find out where the [Session Initialisation](../../../windows-ui-guide/the-session-object/session-initialisation/) looks for a **StartupSession** directory on Unix, namely in `'dyalog.',Executable.VersionMoniker,'.files'` inside the user's home directory (<code class="language-nonAPL">$HOME</code>).

<h4>Executable.VersionNumber</h4>

The version number as a single number, for example, `21.3`.

This is useful for comparing version numbers to deal with varying feature sets. For example:

```apl
:If 22≤Executable.VersionNumber
    source←⎕APLAN array
:Else
    source←⎕SE.Dyalog.Array.Serialise array
:EndIf
```

### Features
This namespace provides information about optional or versioned functionality inside the interpreter.

<h4>Features.DDE</h4>

Boolean indicating whether (`1`) or not (`0`) [Dynamic Data Exchange](../../../interface-guide/dde/introduction/) is available.

<h4>Features.DotNet</h4>

Full version number of the available .NET (possibly .NET Framework) as three integers indicating the major release, minor release, and build number, for example, `4 8 9325`. If no .NET is available, this is `0 0 0`.

Related indications whether (`1`) or not (`0`):

- .NET or .NET Framework is available: `0≠⊃⎕SYSTEM.Features.DotNet`
- .NET Framework is in use: `4=⊃⎕SYSTEM.Features.DotNet`
- .NET (non-Framework) is in use: `5≤⊃⎕SYSTEM.Features.DotNet`

<h4>Features.Interactive</h4>

Boolean indicating whether (`1`) or not (`0`) an interactive session is available.

Examples of non-interactive interpreters include the runtime and shell script interpreters.

<h4>Features.OLE</h4>

Boolean indicating whether (`1`) or not (`0`) [Object Linking and Embedding](../../../interface-guide/ole-client/introduction/) is available.

<h4>Features.PCRE</h4>

Full version of the built-in [Perl Compatible Regular Expressions](../../pcre-specifications/) engine, for example `10 47`.

### Host
This namespace provides information about network identity.

<h4>Host.ComputerName</h4>

The name of the machine, which is the [hostname](https://en.wikipedia.org/wiki/Hostname) under Unix and the [NetBIOS name](https://en.wikipedia.org/wiki/NetBIOS#NetBIOS_name) under Microsoft Windows.

<h4>Host.DNSDomainName</h4>

The [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) domain of the machine.

<h4>Host.EffectiveUserId</h4>


The [Effective User Identifier](https://en.wikipedia.org/wiki/User_identifier#Effective_user_ID) is a non-negative integer on Unix and `¯1` on Microsoft Windows.

<h4>Host.EffectiveUserName</h4>

The character vector name associated with the current Effective User Identifier on Unix and `''` on Microsoft Windows.

<h4>Host.FQDN</h4>

The [fully qualified domain name](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) of the current machine as a character vector.

<h4>Host.GroupId</h4>


A character vector which on Microsoft Windows is the [Security Identifier](https://en.wikipedia.org/wiki/Security_Identifier) (with the [relative identifier](https://en.wikipedia.org/wiki/Relative_identifier) section removed) and on Unix is the [Group identifier](https://en.wikipedia.org/wiki/Group_identifier).

<h4>Host.GroupName</h4>

The character vector group identifier on Unix and `''` on Microsoft Windows.

<h4>Host.NetBIOSDomainName</h4>

The character vector NetBIOS domain name on Microsoft Windows and `''` on Unix.

<h4>Host.UserId</h4>

On Microsoft Windows, this is the [relative identifier](https://en.wikipedia.org/wiki/Relative_identifier). On Unix, the identifier of the currently logged-in user. Note that this is always a character vector, even on Unix where the value looks like a number.

<h4>Host.UserName</h4>

The currently logged-in user.

### OS
This namespace provides information about the operating system.

<h4>OS.Bits</h4>

Indicates whether a 64- or 32-bit architecture.

!!! Warning "Warning"
    This is not necessarily the same as the bit width of the executable system; 64-bit operating systems can run 32-bit interpreters (but not the other way round).

<h4>OS.Description</h4>

The operating system's self-description ("pretty name"). For example, `Debian GNU/Linux 13 (trixie)` or `Microsoft Windows 11 Pro`.

!!! Warning "Warning"
    This is slow on AIX because the operating system takes a significant amount of time to deliver its description.

<h4>OS.DirectorySeparator</h4>

The preferred separator character used in file paths – either `'/'` or `'\'`.

<h4>OS.Family</h4>

Either `'Windows'` or `'Unix'`.

<h4>OS.LibcPath</h4>

The character vector location of the [C standard library](https://en.wikipedia.org/wiki/C_standard_library) on Unix and `''` on Microsoft Windows.

<h4>OS.Name</h4>

One of `'Windows'`, `'macOS'`, `'AIX'`, or `'Linux'`.

<h4>OS.Newline</h4>

Numeric vector of Unicode code points for the operating system's newline sequence – either `(10 ⋄)` or `13 10`. It can be converted to a character vector with `⎕UCS ⎕SYSTEM.OS.Newline`.

<h4>OS.NullDevice</h4>

The filename associated with the [null device](https://en.wikipedia.org/wiki/Null_device).

<h4>OS.PathSeparator</h4>

The character used to separate multiple filenames in a single character vector. This is `';'`  on Microsoft Windows and `':'` on Unix.

<h4>OS.SharedLibraryExtension</h4>

The preferred file extension for [shared libraries](https://en.wikipedia.org/wiki/Shared_library) – one of `'.dll'` (Microsoft Windows), `'.dylib'` (macOS), or `'.so'` (Linux).

<h4>OS.UTCOffset</h4>

The number of hours by which the current local time zone (with [daylight saving time](https://en.wikipedia.org/wiki/Daylight_saving_time) taken into account) is offset from [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).

For example, if the local time is 07:00 while UTC is 10:00, then `⎕OS.UTCOffset` is `¯3`.

<h4>OS.Version</h4>

A three-element integer vector:

- Microsoft Windows: major and minor version and build number
- Linux: major, minor, and patch version
- AIX: version and release number, followed by a `0`

!!! Warning "Warning"
    Microsoft has made both Windows 10 and Windows 11 identify themselves as "Windows 10".
    
    The following expression will determine whether a reported version 10 is truly 10: `((10=⊃)∧22000>⊢/)⎕SYSTEM.OS.Version`.

<h4>OS.VolumeSeparator</h4>

The character used to separate the [volume](https://en.wikipedia.org/wiki/Volume_(computing)) from the rest of a file path – one of `'/'` or `':'`.

### Process
This namespace provides information about the interpreter's operating system process.

<h4>Process.Id</h4>

Non-negative integer [process identifier](https://en.wikipedia.org/wiki/Process_identifier) (PID) of the interpreter.

<h4>Process.LaunchTarget</h4>

The fully qualified path of the file or directory loaded at startup. This is set by either a workspace name on the [APL command line](../../../windows-installation-and-configuration-guide/apl-command-line/) or using the [LOAD configuration parameter](../../../windows-installation-and-configuration-guide/configuration-parameters/load/).

<h4>Process.ParentId</h4>

Non-negative integer [process identifier](https://en.wikipedia.org/wiki/Process_identifier) of the process that launched the interpreter. Always `¯1` on Microsoft Windows.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SYSTEM SYSTEM
</div>
