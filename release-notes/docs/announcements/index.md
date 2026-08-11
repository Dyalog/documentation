# Announcements

Notice of new and planned additions, changes, removals, and deprecations in Dyalog v21.0 compared with Dyalog v20.0.

## Changes

### APL Thread Scheduler

The APL thread scheduler is being enhanced over several releases. It is likely that the scheduling order will change in Dyalog v22.0; this will not affect most applications.

The APL thread scheduler checks that its own record of each thread's scheduling status is consistent – these checks are always enabled. A temporary I-beam, `4061⌶0`, returns the number of inconsistent thread statuses (`R[1]`) and missed thread wakeups (`R[2]`) that have been detected. A non-zero count means that the interpreter detected an inconsistency in its own scheduling, not that the application is at fault. In this situation, logging can be enabled and the application re-run to capture the details; relevant thread-switching warnings will be written to the log file specified by [`109⌶0`](https://docs.dyalog.com/21.0/language-reference-guide/primitive-operators/i-beam/log-file-for-deprecations/) (see [Deprecated Functionality](https://docs.dyalog.com/21.0/release-notes/announcements/deprecated-functionality/#identifying-deprecated-functionality-in-executed-code) for more information). If logging is not enabled, then the first time that a discrepancy is detected, a message is written to the Status window.

## Removals (Previously Announced)

### Raspberry Pi Platform

Dyalog v20.0 was the last release to be built for 32-bit Raspberry Pis. To run Dyalog v21.0 on 64-bit Raspberry Pis, use Dyalog for Linux (aarch64/DEB).

## Notice of Removals in Future Releases

!!! Info "Information"
    Dyalog Ltd strongly recommends identifying and replacing deprecated functioanlity at the earliest opportunity; see [Deprecated Functionality](https://docs.dyalog.com/21.0/release-notes/announcements/deprecated-functionality/) for information on how to identify deprecated functionality.

### `43⌶` – Monadic Operator Generator  
This I-beam has been deprecated. It is scheduled for removal in Dyalog v22.0; it could be reintroduced in a later release.

### `739⌶` – Temporary Directory  
This I-beam has been deprecated. It is scheduled for removal in 2029.

### `1200⌶` – Format Date-time  
This I-beam has been deprecated. It is scheduled for removal in 2029.

### Legacy Workspaces
Dyalog v21.0 is the last major version that will support workspaces saved using Dyalog v11.0 or Dyalog v12.0 (workspaces saved using earlier versions are already unsupported). From Dyalog v22.0, the minimum version of a workspace that can be loaded will be v12.1.

To update workspaces that were saved using Dyalog v11.0 or v12.0 so that they can be loaded using a future version of Dyalog, you can use `)XLOAD` and `)SAVE` in any version of Dyalog from v12.1 to v21.0 inclusive. 

!!! Hint "Hints and Recommendations"  
    Dyalog Ltd recommends that workspaces are saved without any suspended functions on the stack before loading them into a newer interpreter. To achieve this, run `)RESET` before `)SAVE`.

### Small-span Component Files

Dyalog v16.0 was the last major version to support creating and updating small-span (32-bit) component files; in Dyalog v17.0 these files became read-only. The ability to access these files even in a read-only state will be removed in a future release (exact release to be decided, expected to be implemented by the year 2030).

### External Variables

The ability to create and update external variables will be removed in a future release (exact release to be decided, expected to be implemented by the year 2030).

External variables are no longer supported by default; support for external variables can be re-enabled by setting the [`DYALOG_EXTVAR_SUPPORTED`](https://docs.dyalog.com/21.0/windows-installation-and-configuration-guide/configuration-parameters/dyalog-extvar-supported/) configuration parameter to `1`.

### J0C0 Component Files

Component files that have both journalling and checksum properties set to `0` can be tied and read, but cannot be created. The only amendments that are allowed to these files is to change the journalling and checksum properties using [`⎕FPROPS`](https://docs.dyalog.com/21.0/language-reference-guide/system-functions/fprops/).

The ability to read component files that have both journalling and checksum properties set to `0` will be removed in a future release (exact release to be decided, expected to be implemented by the year 2040).

## Updates on Dyalog v20.0 Announcements

### Legacy Workspaces

Dyalog v20.0 was announced as the last major version that would support workspaces saved using Dyalog v11.0 or Dyalog v12.0. This support has been extended (see [Legacy Workspaces](#legacy-workspaces)), and workspaces saved using Dyalog v11.0 or Dyalog v12.0 are supported in Dyalog v21.0.

## Miscellaneous

### Documentation

The process of moving documents from the [full documentation set](https://www.dyalog.com/documentation_210.htm) into an [open source GitHub project](https://github.com/Dyalog/documentation) is progressing.

Documents that are included in this project are no longer available as PDF files.

## Next Dyalog Version

### Expected Supported Platforms
The next version of Dyalog (Dyalog v22.0) is expected to be supported on the following platforms/operating systems:  

- IBM AIX:
    - AIX 7.3 SP4 onwards with a POWER9 chip or higher<br />NOTE: Minimum chip level might be revised upwards to POWER10
- Linux (including Raspberry Pi):
    - x86_64: Built on Ubuntu 22.04
    - ARM64: Built on Debian GNU/Linux 13
- macOS (Apple Silicon):
    - macOS 26.3 (Tahoe) onwards
- Microsoft Windows:
    - Windows 11 2H24 onwards (Windows Server 2016 onwards)

This list is likely to change before Dyalog v22.0 is released (more recent operating system versions are likely to be required).
