# Announcements

Notice of new and planned additions, changes, removals, and deprecations in Dyalog v20.0 compared with Dyalog v19.0.

## Additions

### New Glyph

A new glyph has been introduced:
  
* Glyph: `⍛` (Classic: `⎕U235B`)  
* Glyph name: Jot Underbar
* Keyboard key location: <kbd>&lt;APL key&gt;</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>
* Unicode code: U+235B

This glyph is needed for the new [_behind_](../../language-reference-guide/primitive-operators/behind/) operator that is introduced with Dyalog v20.0.

### New APL Font

The Dyalog v20.0 installation images include a preview of a new font, currently called APL387. The default font for APL within Dyalog remains APL385, but if this new font is well received it might become the default for future versions of Dyalog.

The font can be explored within the Microsoft Windows IDE (it can be selected from the drop-down font selection list) or at [https://dyalog.github.io/APL387](https://dyalog.github.io/APL387/).

The design of APL387 has not yet been finalised, and feedback is welcome. Please email your feedback to [support@dyalog.com](mailto:support@dyalog.com) or raise issues in the APL387 GitHub project ([https://github.com/Dyalog/APL387](https://github.com/Dyalog/APL387)).

!!! Info "Information"  
    Although Dyalog Ltd has commissioned the font, we hope that it will become widely used by the APL community. It is intended to be vendor-agnostic, and we believe that it includes all the APL characters used by all APL dialects. It intentionally has, and will continue to have, an extremely permissive licence.

### New Linux Platform

In addition to x86_64, Dyalog is now supported on Linux-based ARM64 platforms and, therefore, on software built on these, such as Raspberry Pi OS 64-bit and AWS containers. This applies to the Unicode edition only.

Images of docker containers that host Dyalog running on ARM64 Linux are available to download at [https://hub.docker.com/u/dyalog](https://hub.docker.com/u/dyalog).
 
!!! Info "Information"  
    The HTMLRenderer is not currently supported on Linux ARM64.

## Changes

### Defining Dfns with Unmatched Brackets

The rules around whether a function can be fixed have been tightened to prevent dfns with unmatched parentheses and brackets from being fixed. This is to accommodate array notation, which changes the meaning of parentheses and brackets that span more than one statement. TradFns will continue to fix as before, but subtle differences in how the code behaves might not be backwards-compatible and could have unexpected results.

    !!! Hint "Hints and Recommendations"
        If the enhanced restrictions cause problems for you, please contact [support@dyalog.com](mailto:support@dyalog.com) to discuss tools and techniques for mitigation.

## Removals (Previously Announced)

### Syncfusion

The Syncfusion library of WPF controls is no longer included with Dyalog. The Syncfusion licence provided with Dyalog v19.0 will continue to be valid for use with Dyalog v19.0, but from Dyalog v20.0 onwards anyone who is using Syncfusion will need to obtain a licence from [https://www.syncfusion.com](https://www.syncfusion.com/).

### Array Editor

David Liebtag's Array Editor is no longer part of Dyalog. Arrays can now be created and edited using [array notation](../../programming-reference-guide/introduction/arrays/array-notation/).

### macOS Platform

Dyalog v19.0 was the last release to be built for Intel-based Mac computers; Dyalog v20.0 is only supported on ARM-based Mac computers.

## Notice of Removals in Future Releases

### Raspberry Pi OS Platform

Dyalog v20.0 is the last release that will be supported on 32-bit Raspberry Pi OS.

### Legacy Workspaces

Dyalog v20.0 is the last major version that will support workspaces saved using Dyalog v11.0 or Dyalog v12.0 (workspaces saved using earlier versions are already unsupported). From Dyalog v21.0, the minimum version of a workspace that can be loaded will be v12.1.

To update workspaces that were saved using Dyalog v11.0 or v12.0 so that they can be loaded using a future version of Dyalog, you can use `)XLOAD` and `)SAVE` in any version of Dyalog from v12.1 to v20.0 inclusive. 

!!! Hint "Hints and Recommendations"  
    Dyalog Ltd recommends that workspaces are saved without any suspended functions on the stack before loading them into a newer interpreter. To achieve this, run `)RESET` before `)SAVE`.

### Small-span Component Files

Dyalog v16.0 was the last major version to support creating and updating small-span (32-bit) component files; in Dyalog v17.0 these files became read-only. The ability to access these files even in a read-only state will be removed in a future release (exact release to be decided, expected to be implemented by the year 2030).

### External Variables

The ability to create and update external variables will be removed in a future release (exact release to be decided, expected to be implemented by the year 2030).

### J0C0 Component Files

Dyalog v20.0 is the last major version that will support creating and updating component files that have both journalling and checksum properties set to `0`; from Dyalog v21.0 component files with this combination of properties will be read-only. The ability to access these files even in a read-only state will be removed in a future release (exact release to be decided, expected to be implemented by the year 2040).

## Updates on Dyalog v19.0 Announcements

### Performance Issues with Namespaces

A namespace performance issue was identified in Dyalog v19.0 that was especially noticeable with JSON imports. This has now been resolved, and the suggested workaround of assigning a name to the top-level namespace is no longer required.

### Hash and Lookup Tables

The performance of the set functions has been improved by increasing the amount of workspace allocated to the internal tables used by these functions.

## Miscellaneous

### Documentation

The process of moving all the documentation into an [open source GitHub project](https://github.com/Dyalog/documentation) has started. The aim of this is two-fold:

- All documentation will be available to view from a single online front-end; this is a long-term goal, and will take several releases to achieve.
- It will be easier for anyone to contribute to the Dyalog documentation set, either by making suggestions or by drafting amendments/enhancements.

To report an error or request a change in the documentation you can now:

- send an email to [docs@dyalog.com](mailto:docs@dyalog.com) – this can be done for any Dyalog document.
- [raise an issue](https://github.com/Dyalog/documentation/issues) directly in the GitHub project – this should only be done if the issue relates to a document that is in the GitHub project.

The GitHub project's [README file](https://github.com/Dyalog/documentation/blob/main/README.md) includes information on how to contribute by drafting amendments/enhancements.

In addition, the URLs and filenames of the PDFs and other downloadable documentation have changed from the format used in previous releases. See the [Dyalog v20.0 Documentation Centre](https://www.dyalog.com/documentation_200.htm) for links to these files.

## Next Dyalog Version

### Expected Supported Platforms
The next version of Dyalog (Dyalog v21.0) is expected to be supported on the following platforms/operating systems:  

- IBM AIX:
    - AIX 7.3 SP3 TL1 onwards with a POWER9 chip or higher<br />NOTE: Minimum chip level might be revised upwards to POWER10
- Linux:
    - x86_64: Built on Ubuntu 22.04
    - ARM64: Built on Debian GNU/Linux 13
- macOS (ARM-based, Apple M1 or later):
    - macOS 26.1 (Tahoe) onwards
- Microsoft Windows:
    - Windows 11 2H24 onwards (Windows Server 2016 onwards)
- Raspberry Pi (ARM-based, 64-bit Raspberry Pi OS only):  
    NOTE: Installed using the Linux ARM64 package
    - Not tested on Raspberry Pi Zero 2 W

This list is not definitive and is subject to change.