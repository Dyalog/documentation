---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SYSTEM SYSTEM
</div>

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

The result `R` is a namespace in the root of the namespace where `⎕SYSTEM` was called (`#` or `⎕SE`) and contains only namespace members. Each sub-namespace contains only variable members.

!!! Info "Information"
    More members might be added in a future release of Dyalog, but `R` will remain serialisable using [`1⎕JSON`](json.md).

!!! Warning "Warning"
    Do attempt to add or modify members as changes will not be persisted. Instead, clone the namespace using `⎕NS ⎕SYSTEM` and modify the result, but note that this locks down dynamic values like `⎕SYSTEM.Directories.Current` and `⎕SYSTEM.OS.UTCOffset`.

## Members of the Result

### CommandLine
This namespace provides information about the command line expression used to start the interpreter. 

#### CommandLine.Args
The command line used to start the current executable, split on unquoted space sequences into a vector of character vectors.

#### CommandLine.CodeArgs
This member is intended to ease usage of APL shell scripts. It is equivalent to [CommandLink.Args](#[Args](#commandline-args) but omits everything up to and including `-script`. If Dyalog is started without `-script` then nothing is omitted.

#### CommandLine.Full
The full command line used to start the current executable as a simple character vector.

### Directories
This namespace provides pertinent locations in the file system.

#### Directories.Current
The current working directory.

!!! Hint "Hints and Recommendations"
    This can be changed using the `]CD` user command, but doing so after [tying component files](ftie.md) or [native files](ntie.md) or [associating external functions](na.md) can lead to data loss.

#### Directories.Initial
The directory from which Dyalog was started.

#### Directories.Temp
The operating system's recommended location for temporary files.

!!! Info "Information"
    This location is per-user and can get cleaned up without warning, so use it only as a place to put files that will immediately be used and will not be needed later. It is good practice to [delete](ndelete.md) such files when no longer needed.

### Executable
This namespace provides information about the specific interpreter instance wherein `⎕SYSTEM` was called.

#### Executable.Bits
Indicates whether the interpreter is a 64- or 32-bit application.

!!! Warning "Warning"
    Do not confuse this with the bit width of the operating system; 64-bit operating systems can run 32-bit interpreters (but not vice versa).

#### Executable.BuildTarget
_For Dyalog internal use only._

#### Executable.BuildType
_For Dyalog internal use only._

#### Executable.Path
The full file path to the interpreter's executable file.

#### Executable.RideConnected
Boolean indicating whether (`1`) or not (`0`) there is an active connection using the RIDE protocol.

#### Executable.Runtime
Boolean indicating whether (`1`) or not (`0`) this is a runtime interpreter.

#### Executable.Unicode
Boolean indicating whether (`1`) or not (`0`) the interpreter can represent characters outside [`⎕AV`](av.md).

#### Executable.Vendor
The originator of the interpreter, that is, `'Dyalog'`.

#### Executable.Version
The interpreter's full version number as three integers indicating the major release, minor release, and build number, for example, `21 0 53977`

#### Executable.VersionMoniker
A six-character shorthand for the for `Version`'s first two elements together with `Unicode` and `Bits`, for example `210U64`.

!!! Hint "Hints and Recommendations"
    This is useful for example to find out the where the [Session Initialisation](../../windows-ui-guide/the-session-object/session-initialisation) looks for a **StartupSession** directory on Unix, namely in `'dyalog.',Executable.VersionMoniker,'.files'` inside the user's home directory (`$HOME`).

#### Executable.VersionNumber
The version number as a single number, for example, `21.3`.

!!! Hint "Hints and Recommendations"
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

#### Features.DDE
Boolean indicating whether (`1`) or not (`0`) [Dynamic Data Exchange](../../interface-guide/dde/introduction/) is available.

#### Features.DotNet
Full version number of the available .NET (possibly .NET Framework) as three integers indicating the major release, minor release, and build number, for example, `4 8 9325`. If no .NET is available, this is `0 0 0`.

!!! Hint "Hints and Recommendations"
    Whether (`1`) or not (`0`) .NET Framework is in use is given by `4=⊃⎕SYSTEM.Features.DotNet`.

#### Features.Interactive
Boolean indicating whether (`1`) or not (`0`) an interactive session is available.

!!! Info "Information"
    Examples of non-interactive interpreters include the runtime and shell script interpreters.

#### Features.OLE
Boolean indicating whether (`1`) or not (`0`) [Object Linking and Embedding](../../interface-guide/ole-client/introduction) is available.

#### Features.PCRE
Full version of the built-in [Perl Compatible Regular Expressions](../pcre-specifications) engine, for example `10 47`.

!!! Hint "Hints and Recommendations"
    Whether (`1`) or not (`0`) PCRE2 is in use is given by `10≤⎕SYSTEM.Features.PCRE`, though Dyalog's switch from PCRE to PCRE2 precedes the addition of `⎕SYSTEM`.

### Host
This namespace provides information about network identity.

#### Host.ComputerName
The name of the machine, which is the [hostname](https://en.wikipedia.org/wiki/Hostname) under Unix and the [NetBIOS name](https://en.wikipedia.org/wiki/NetBIOS#NetBIOS_name) under Microsoft Windows.

#### Host.DNSDomainName
The [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) domain of the machine.

#### Host.EffectiveUserId

The [Effective User Identifier](https://en.wikipedia.org/wiki/User_identifier#Effective_user_ID) is a non-negative integer on Unix and `¯1` on Microsoft Windows.

#### Host.EffectiveUserName
The character vector name associated with the current Effective User Identifier on Unix and `''` on Microsoft Windows.

#### Host.FQDN
The [fully qualified domain name](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) of the current machine as a character vector.

#### Host.GroupId

A character vector which on Windows is the [Security Identifier](https://en.wikipedia.org/wiki/Security_Identifier) (with the [relative identifier](https://en.wikipedia.org/wiki/Relative_identifier) section removed) and on Unix is the [Group identifier](https://en.wikipedia.org/wiki/Group_identifier).

#### Host.GroupName
The name associated with the current group identifier. Always `''` on Microsoft Windows.

#### Host.NetBIOSDomainName
The NetBIOS domain name. Always `''` on Unix.

#### Host.UserId
On Microsoft Windows, this is the [relative identifier](https://en.wikipedia.org/wiki/Relative_identifier). On Unix, the identifier of the currently logged-in user. Note that this is always a character vector, even on Unix where the value looks like a number.

#### Host.UserName
The currently logged-in user.

### OS
This namespace provides information about the operating system.

#### OS.Bits
Indicates whether a 64- or 32-bit architecture.

!!! Warning "Warning"
    Do not confuse this with the bit width of the executable system; 64-bit operating systems can run 32-bit interpreters (but not vice versa).

#### OS.Description
One of `'Windows'`, `'macOS'`, `'AIX'` or `'Linux'`.

#### OS.DirectorySeparator
The preferred character separating file paths – either `'/'` or `'\'`.

#### OS.Family
Either `'Windows'` or `'Unix'`.

#### OS.LibcPath
The location of the [C standard library](https://en.wikipedia.org/wiki/C_standard_library). Always `''` on Microsoft Windows.

#### OS.Newline
Numeric vector of Unicode code points for the operating system's newline sequence – either `(10 ⋄)` or `13 10`.

!!! Hint "Hints and Recommendations"
    Convert this to a character vector with `⎕UCS ⎕SYSTEM.OS.Newline`.

#### OS.NullDevice
The filename associated with the [null device](https://en.wikipedia.org/wiki/Null_device).

#### OS.PathSeparator
The character used to separate multiple filenames in a single character vector, namely `';'`  on Microsoft Windows and `':'` on Unix.

#### OS.SharedLibraryExtension
The preferred file extension for [shared libraries](https://en.wikipedia.org/wiki/Shared_library) – one of `'.dll'`, `'.dyllb'`, or `'.so'`.

#### OS.UTCOffset
Number of hours that the local time zone is offset from [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).

!!! Hint "Hints and Recommendations"
    A positive number means the local time zone is ahead of UTC. A negative number means behind UTC. For example, if `⎕OS.UTCOffset` is `10`, then when it is noon UTC (12:00), it is 10 PM local time (`12+10`, that is, 22:00).

#### OS.Version
A three-element integer vector:

- Microsoft Windows: major and minor version and build number
- Linux: major, minor, and patch version
- AIX: version and release number, followed by a `0`

!!! Warning "Warning"
    Windows 11 identifies itself as "Windows 10". Whether (`1`) or not (`0`) Windows 10 is in use is given by `1 0 1≡10 22000⍸⎕SYSTEM.OS.Version`.

#### OS.VolumeSeparator
The character used to separate the [volume](https://en.wikipedia.org/wiki/Volume_(computing)) from the rest of a file path – one of `'/'` or `':'`.

### Process
This namespace provides information about the interpreter's operating system process.

#### Process.Id
Non-negative integer [process identifier](https://en.wikipedia.org/wiki/Process_identifier) (PID) of the interpreter.

#### Process.LaunchTarget
The fully qualified path of the file or directory loaded at startup. This is set by either a workspace name on the [APL command line](../../windows-installation-and-configuration-guide/apl-command-line) or using the [LOAD parameter](indows-installation-and-configuration-guide/configuration-parameters/load/).

#### Process.ParentId
non-negative integer [process identifier](https://en.wikipedia.org/wiki/Process_identifier) of the process that launched the interpreter. Always `¯1` on Microsoft Windows.
