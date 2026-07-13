# Interoperability

## Introduction

Workspaces and component files are stored on disk in a binary format. This format differs between machine architectures and among versions of Dyalog. For example, a file component written from Windows will have an internal format that is different from one written from AIX. Similarly, a workspace saved from Dyalog Version 19.0 will differ internally from one saved by a previous version of Dyalog APL.

It is convenient for versions of Dyalog APL running on different platforms to be able to
*interoperate* by sharing workspaces and component files. Component files and workspaces can generally be shared between Dyalog interpreters running on different platforms. However, this is not always possible and the following sections describe limitations in interoperability:

## Code and `⎕OR`s

Code that is saved in workspaces, or embedded within `⎕OR`s stored in component files, can only be read by the Dyalog version which saved them and later versions of the interpreter. In the case of workspaces, a load (or copy) into an older version would fail with the message:
```apl
this WS requires a later version of the interpreter.
```

Every time a  `⎕OR` 
object is read by a version later than that which created it, time may be spent in converting the internal representation into the latest form.  Dyalog recommends that  `⎕OR`s should not be used as a mechanism for sharing code or objects between different versions of APL.

## "Ordinary" Arrays

With the exception of the Unicode restrictions described in the following paragraphs, Dyalog APL provides interoperability for arrays that only contain (nested) character and numeric data. Such arrays can be stored in component files, or transmitted using
`TCPSocket` objects and Conga connections, and shared between all versions and across all platforms.

Full cross-platform interoperability of component files is only available for large-span component files.

## Object Representations (`⎕OR`)

An attempt to `⎕FREAD` a component containing a `⎕OR` that was created by a later version of Dyalog APL will generate `DOMAIN ERROR: Array is from a later version of APL`. This also applies to APL objects passed via Conga or TCPSockets, or objects that have been serialised using `220⌶`.

## 32 vs. 64-bit Interpreters

There is complete interoperability between 32- and 64-bit interpreters, except that:

- 32-bit interpreters are unable to work with arrays or workspaces greater than 2GB in size.
- Under Windows, a 32-bit version of Dyalog APL can only access 32-bit DLLs, and a 64-bit version of Dyalog APL can only access 64-bit DLLs. This is a Windows restriction.
- Objects saved in the workspace that are connected to external resources lose those connections when loaded or copied by an interpreter with different architecture.

In particular:

If a workspace containing:

- .NET objects, objects created by `⎕WC` , or instances of built-in objects (excluding instances of user-defined classes) created by `⎕NEW`.

or

- variables containing the `⎕OR` of or refs to such objects

is loaded by an interpreter with differing architecture (32 vs 64) from the version that saved it, Dyalog displays:

```apl
      GUI objects could not be recreated;
      the file is from an incompatible architecture
```

The names of all incompatible objects are instantiated as plain namespaces, with any compatible contents (such as functions and variables) preserved.

If a component containing the `⎕OR` of or refs to such objects is read by an interpreter with differing architecture (32 vs 64) from the version that wrote it, each incompatible object is instantiated as a plain namespace, preserving compatible contents as above.

## Unicode vs. Classic Editions

Two editions are available on some platforms. Unicode editions work with the entire Unicode character set. Classic editions (which are only available to commercial and enterprise users for legacy applications) are limited to the 256 characters defined in the atomic vector, `⎕AV`.

Component files have a Unicode property. When this is enabled, all characters will be written as Unicode data to the file. The Unicode property is set *on* by Unicode Editions and *off* by Classic Editions,  by default. The Unicode property can subsequently be toggled on and off using
`⎕FPROPS`.

When a Unicode edition writes to a component file that cannot contain Unicode data, character data is mapped using `⎕AVU`; it can therefore be read without problems by Classic editions.

A `TRANSLATION ERROR` will occur if a Unicode edition writes to a non-Unicode component  file (that is either a 32-bit file, or a 64-bit file when the Unicode property is currently off) if the data being written contains characters that are not in `⎕AVU`.

Likewise, a Classic edition will issue a `TRANSLATION ERROR` if it attempts to read a component containing Unicode data that is not in `⎕AVU` from a component file.

A `TRANSLATION ERROR` will also be issued when a Classic edition attempts to `)LOAD` or `)COPY` a workspace containing Unicode data that cannot be mapped to `⎕AV` using the `⎕AVU` in the recipient workspace. Note that the problematic Unicode data may be in that part of a workspace which holds the information needed to generate `⎕DM` and `⎕DMX`, so calling `)RESET` before `)SAVE` in the Unicode interpreter may eliminate the `TRANSLATION ERROR`s.

`TCPSocket` objects have an `APL` property that corresponds to the Unicode property of a file, if this is set to `Classic` (the default) the data in the socket will be restricted to `⎕AV`, if Unicode it will contain Unicode character data. As a result, `TRANSLATION ERROR`s can occur on transmission or reception in the same way as when updating or reading a file component.

The symbols `⊆`, `⍸`, `⍤`, `⍠`, `⌸`, `⌺` and `⍥`  used for the *nest/partition* and *where/interval index* functions and the *rank/atop*, *variant*, *key*, *stencil* and *over* operators respectively are available only in the Unicode edition. In the Classic edition, these symbols are replaced by `⎕U2286`, `⎕U2378`, `⎕U2364`, `⎕U2360`, `⎕U2338`, `⎕U233a` and `⎕U2365` respectively. In both Unicode and Classic editions, *variant* operator can be represented by `⎕OPT`.

## Very large array components

An attempt to read
a component greater than 2GB in 32-bit interpreters will result in a `WS FULL`.

## `TCPSocket` Objects and Conga

`TCPSocket` objects and Conga can be used to communicate between differing versions of Dyalog APL and are subject to similar limitations to those described above for component files.

## Auxiliary Processors

A Dyalog APL process is restricted to starting an AP of exactly the same architecture from the same operating system. In other words, the AP must share the same word-width and byte-ordering as its interpreter process.

## Session Files

Session (.dse) files can only be used on the platform on which they were created and
saved. Under Microsoft Windows, Session files may only be used by the  architecture (32-bit-or 64-bit) of the Version of Dyalog that saved them.

## Log Files

Log (.dlf) files can only be used by the version and edition with which they were created and saved.
