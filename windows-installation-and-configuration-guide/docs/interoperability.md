<h1 class="heading"><span class="name">Interoperability</span></h1>

## Introduction

Workspaces and component files are stored on disk in a binary format (illegible to text editors). This format differs between machine architectures and among versions of Dyalog. For example, a file component written by a PC may well have an internal format that is different from one written by a UNIX machine. Similarly, a workspace saved from Dyalog Version {{ version_majmin }} will differ internally from one saved by a previous version of Dyalog APL.

It is convenient for versions of Dyalog APL running on different platforms to be able to
*interoperate* by sharing workspaces and component files. From Version 11.0, component files and workspaces can generally be shared between Dyalog interpreters running on different platforms. However, this is not always possible and the following sections describe limitations in interoperability:

## Code and `⎕OR`s

Code that is saved in workspaces, or embedded within `⎕OR`s stored in component files, can only be read by the Dyalog version which saved them and later versions of the interpreter. In the case of workspaces, a load (or copy) into an older version would fail with the message:
```apl
this WS requires a later version of the interpreter.
```

Every time a  `⎕OR` 
object is read by a version later than that which created it, time may be spent in converting the internal representation into the latest form.  Dyalog recommends that  `⎕OR`s should not be used as a mechanism for sharing code or objects between different versions of APL.

## "Ordinary" Arrays

With the exception of the Unicode restrictions described in the following paragraphs, Dyalog APL provides interoperability for arrays that only contain (nested) character and numeric data. Such arrays can be stored in component files - or transmitted using
`TCPSocket` objects and Conga connections, and shared between all versions and across all platforms.

Full cross-platform interoperability of component files is only available for large-span component files.

## Null Items (`⎕NULL`) and Compressed Components

`⎕NULL`s and components from compressed component files that were created in Version 18.0 and later can be brought into Versions 16.0, 17.0 and 17.1 provided that the  interpreters have been patched to  revision 38151 or higher.  Attempts to bring `⎕NULL` or compressed component into earlier versions of Dyalog APL or lower revisions of the aforementioned versions will fail with:
```apl
DOMAIN ERROR: Array is from a later version of APL.
```

## Object Representations (`⎕OR`)

An attempt to `⎕FREAD` a component containing a `⎕OR` that was created by a later version of Dyalog APL will generate `DOMAIN ERROR: Array is from a later version of APL`. This also applies to APL objects passed via Conga or TCPSockets, or objects that have been serialised using `220⌶`.

## 32 vs. 64-bit Component Files

It is no longer possible to *create* or write to small-span (32-bit) files; however it is still currently possible to *read* from small span files. Setting the second item of the right argument of `⎕FCREATE` to anything other than 64 will generate a `DOMAIN ERROR`.

Note that *small-span* (32-bit-addressing) component files cannot contain Unicode data. Unicode editions of Dyalog APL can only write character data which would be readable by a Classic
edition (consisting of elements of `⎕AV`).

## External Variables

External variables are subject to the same restrictions as small-span component files regarding Unicode data. External variables are unlikely to be developed further; Dyalog recommends that applications which use them should switch to using mapped files or traditional component files. Please contact Dyalog if you need further advice on this topic.

## 32 vs. 64-bit Interpreters

There is complete interoperability between 32- and 64-bit interpreters, except that 32-bit interpreters are unable to work with arrays or workspaces greater than 2GB in size.

Note however that under Windows a 32-bit version of Dyalog APL may only access 32-bit DLLs, and a 64-bit version of Dyalog APL may only access 64-bit DLLs. This is a Windows restriction.

## Unicode vs. Classic Editions

Two editions are available on some platforms. Unicode editions work with the entire Unicode character set. Classic editions (which are only available to commercial and enterprise users for legacy applications) are limited to the 256 characters defined in the atomic vector, `⎕AV`.

Component files have a Unicode property. When this is enabled, all characters will be written as Unicode data to the file. The Unicode property is always off for small-span (32-bit addressing) files, as these cannot contain Unicode data. For large-span (64-bit addressing) component files, the Unicode property is set *on* by Unicode Editions and *off* by Classic Editions,  by default. The Unicode property can subsequently be toggled on and off using
`⎕FPROPS`.

When a Unicode edition writes to a component file that cannot contain Unicode data, character data is mapped using       `⎕AVU`; it can therefore be read without problems by Classic editions.

A `TRANSLATION ERROR` will occur if a Unicode edition writes to a non-Unicode component  file (that is either a 32-bit file, or a 64-bit file when the Unicode property is currently off) if the data being written contains characters that are not in `⎕AVU`.

Likewise, a Classic edition will issue a `TRANSLATION ERROR` if it attempts to read a component containing Unicode data that is not in `⎕AVU` from a component file.

A `TRANSLATION ERROR` will also be issued when a Classic edition attempts to `)LOAD` or `)COPY` a workspace containing Unicode data that cannot be mapped to `⎕AV` using the `⎕AVU` in the recipient workspace.

`TCPSocket` objects have an `APL` property that corresponds to the Unicode property of a file, if this is set to `Classic` (the default) the data in the socket will be restricted to `⎕AV`, if Unicode it will contain Unicode character data. As a result, `TRANSLATION ERROR`s can occur on transmission or reception in the same way as when updating or reading a file component.

Some APL glyphs are only available in the Unicode edition, and need to be replaced with Unicode hex values in the Classic edition. These are:

|Glyph|Classic replacement|Description|
|---|----|----------------------------------|
| `⊆` | `⎕U2286` | _nest_/_partition_ function |
| `⍸` | `⎕U2378` | _where_/_interval index_ function |
| `⍤` | `⎕U2364` | _atop_/_rank_ operator|
| `⍠` | `⎕U2360` | _variant_ operator |
| `⌸` | `⎕U2338` | _key_ operator |
| `⌺` | `⎕U233A` | _stencil_ operator |
| `⍥` | `⎕U2365` | _over_ operator |
| `⍛` | `⎕U235B` | _behind_ operator |

In both Unicode and Classic editions, the _variant_ operator can also be represented by `⎕OPT`.

## Very large array components

An attempt to read
a component greater than 2GB in 32-bit interpreters will result in a `WS FULL`.

## TCPSockets and Conga

TCPSockets and Conga can be used to communicate between differing versions of Dyalog APL and are subject to similar limitations to those described above for component files.

## Auxiliary Processors

A Dyalog APL process is restricted to starting an AP of exactly the same architecture from the same operating system. In other words, the AP must share the same word-width and byte-ordering as its interpreter process.

## Session Files

Session (.dse) files can only be used on the platform on which they were created and
saved. Under Microsoft Windows, Session files may only be used by the  architecture (32-bit-or 64-bit) of the Version of Dyalog that saved them.
