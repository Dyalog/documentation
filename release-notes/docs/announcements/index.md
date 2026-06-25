# Announcements

<p style="color:red;">This document is currently being developed and will not be finalised until nearer the release of Dyalog v21.0.</p>

Notice of new and planned additions, changes, removals, and deprecations in Dyalog v21.0 compared with Dyalog v20.0.

## Additions

T.B.A.

## Changes

T.B.A.

## Removals (Previously Announced)

### Raspberry Pi Platform

Dyalog v20.0 was the last release to be built for 32-bit Raspberry Pis; Dyalog v21.0 is only supported on 64-bit Raspberry Pis.

## Notice of Removals in Future Releases

### `43⌶` – Monadic Operator Generator  
This I-beam has been deprecated. It is scheduled for removal in Dyalog v22.0; it could be reintroduced in a later release.

### Legacy Workspaces
Dyalog v21.0 is the last major version that will support workspaces saved using Dyalog v11.0 or Dyalog v12.0 (workspaces saved using earlier versions are already unsupported). From Dyalog v22.0, the minimum version of a workspace that can be loaded will be v12.1.

To update workspaces that were saved using Dyalog v11.0 or v12.0 so that they can be loaded using a future version of Dyalog, you can use `)XLOAD` and `)SAVE` in any version of Dyalog from v12.1 to v21.0 inclusive. 

!!! Hint "Hints and Recommendations"  
    Dyalog Ltd recommends that workspaces are saved without any suspended functions on the stack before loading them into a newer interpreter. To achieve this, run `)RESET` before `)SAVE`.

### Small-span Component Files

Dyalog v16.0 was the last major version to support creating and updating small-span (32-bit) component files; in Dyalog v17.0 these files became read-only. The ability to access these files even in a read-only state will be removed in a future release (exact release to be decided, expected to be implemented by the year 2030).

### External Variables

The ability to create and update external variables will be removed in a future release (exact release to be decided, expected to be implemented by the year 2030).

### J0C0 Component Files

The ability to read component files that have both journalling and checksum properties set to `0` will be removed in a future release (exact release to be decided, expected to be implemented by the year 2040).

## Updates on Dyalog v20.0 Announcements

### Legacy Workspaces

Dyalog v20.0 was announced as the last major version that would support workspaces saved using Dyalog v11.0 or Dyalog v12.0. This support has been extended (see [Legacy Workspaces](#legacy-workspaces)), and workspaces saved using Dyalog v11.0 or Dyalog v12.0 are supported in Dyalog v21.0.

## Miscellaneous

### Documentation

T.B.A.

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

This list is not definitive and is subject to change.
