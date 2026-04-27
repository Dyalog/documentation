# Interoperability

Workspaces and component files are stored on disk in a binary format. This format differs between machine architectures and versions of Dyalog. For example, a component file written from Microsoft Windows will have an internal format that is different from one written from AIX. Similarly, a workspace saved in Dyalog v19.0 will differ internally from one saved in Dyalog v14.1.

It is convenient for versions of Dyalog running on different platforms to be able to interoperate by sharing workspaces and component files. Component files and workspaces can generally be shared between Dyalog interpreters running on different platforms. However, this is not always possible – this section describes the limitations of interoperability.

## "Ordinary" Arrays

With the exception of the Unicode restrictions described below, Dyalog provides interoperability for arrays that only contain character and numeric data. Such arrays can be stored in component files, or transmitted using Conga connections, and shared between all versions and across all platforms.  

## Code and Object Representations (`⎕OR`)
Code that is saved in workspaces, or embedded within `⎕OR`s stored in component files, cannot be read by earlier versions of Dyalog than the version that saved them. An attempt to read a component containing a `⎕OR` that was created by a later version of Dyalog will generate `DOMAIN ERROR: Array is from a later version of APL`. This also applies to APL arrays passed using Conga, or arrays that have been serialised using `220⌶`.

!!! Hint "Hints and Recommendations"
    Every time a `⎕OR` object is read by an interpreter that is either a different edition or a version later than that which created it, time is spent converting the internal representation into the latest form. Dyalog Ltd recommends that `⎕OR` should not be used as a mechanism for sharing code or objects between different versions of APL.

In the case of workspaces, a load (or copy) into an older version would fail with the message `this WS requires a later version of the interpreter`.

## 32-bit/64-bit Interpreters
There is complete interoperability between 32-bit and 64-bit interpreters, with the following exceptions:  

* 32-bit interpreters are unable to work with arrays or workspaces greater than 2GB in size.
* Under Microsoft Windows, a 32-bit version of Dyalog can only access 32-bit
DLLs, and a 64-bit version of Dyalog can only access 64-bit DLLs. This is a Windows restriction.
* Objects saved in the workspace that are connected to external resources lose
those connections when loaded or copied by an interpreter with different architecture.

In particular, if a workspace containing one of the following:  

* .NET objects
* objects created by `⎕WC`
* instances of built-in objects (excluding instances of user-defined classes) created by `⎕NEW`
* variables containing the `⎕OR` of, or refs to, such objects

is loaded by an interpreter with differing architecture (32/64) from the version that saved it, Dyalog displays `GUI objects could not be recreated; the file is from an incompatible architecture`. The names of all incompatible objects are instantiated as plain namespaces, with any compatible contents (such as functions and variables) preserved.

If a component file containing the `⎕OR` of, or refs to, such objects is read by an interpreter with differing architecture (32/64) from the version that wrote it, each incompatible object is instantiated as a plain namespace, preserving compatible contents.

## Unicode/Classic Editions
Two editions of Dyalog are available on some platforms:  

* Unicode editions work with the entire Unicode character set.
* Classic editions (which are only available to commercial and enterprise users for legacy applications) are limited to the 256 characters defined in the atomic vector, `⎕AV`.

The Classic edition is a legacy system. Although still maintained, the differences between Classic edition and Unicode edition are growing with each release of Dyalog. Increasingly, the functionality available through the Classic edition is not as rich as that of the Unicode edition; such functionality is highlighted in the documentation, but a few important differences are also highlighted below.

### Edition-specific Functionality

Functionality that is only available in the Unicode edition includes:  

* The .NET interface
* SharpPlot and SharpLeaf
* External workspaces
* On the Microsoft Windows operating system: Edit and Preview, and Microsoft Outlook integration
* Enhancements to the dfns workspace

Some behaviour is slightly different between Unicode and Classic editions. Specifically:  

* sorting using the _grade up_ and _grade down_ functions produces different results (and results of `⎕NL` are sorted differently)
* internal representations and data types for character data differ (impacts `⎕DR` and `⎕MAP`)
* the output from `⎕NA`
* in the Classic edition, default keyboard mappings differ from the documentation on a few keys: `⌶`, `⍷`, `⍪`, `⍫`, `!`, and `⍨`

Functionality that is only available in the Classic edition includes:  

* `⎕NXLATE` (this is only used in the Unicode edition to process files created in the Classic edition)
* `⎕Uxxxx` equivalents for glyphs (see [Typing Glyphs](#typing-glyphs))
* defining IDE colours in a Output Translate table (**win.dot**)
* switching to traditional APL keyboard by double-clicking on the status bar

### Typing Glyphs

The Classic interpreter is not able to process glyphs that are not in `⎕AV`, and instead uses/displays system functions formatted as `⎕Uxxxx` values (where `xxxx` is the Hexadecimal code point). These are:

|Glyph|Classic replacement|Description|
|---|----|----------------------------------|
| `⊆` | `⎕U2286` | _nest_/_partition_ function |
| `⍸` | `⎕U2378` | _where_/_interval index_ function |
| `⌸` | `⎕U2338` | _key_ operator |
| `⌺` | `⎕U233A` | _stencil_ operator |
| `⍛` | `⎕U235B` | _behind_ operator |
| `⍠` | `⎕U2360` | _variant_ operator |
| `⍤` | `⎕U2364` | _atop_/_rank_ operator|
| `⍥` | `⎕U2365` | _over_ operator |

In both Unicode and Classic editions, `⎕OPT` can be used instead of the _variant_ operator.

Any further glyphs that are introduced to Dyalog and are not already part of `⎕AV` will also have `⎕Uxxxx` representations in the Classic edition.

A translateable workspace can be opened in either edition; the appropriate representation for the edition will automatically be applied.

Classic edition: `⎕FIX`, Link, SALT, and Editor automatically translate Unicode glyphs as required.

### Component Files

Component files have a Unicode property. When this is enabled, all characters can be written as Unicode data to the file. By default, the Unicode property is switched on for Unicode editions and off for Classic editions. This property can be changed using the [`⎕FPROPS`](../../language-reference-guide/system-functions/fprops/) system function.

When a Unicode edition writes to a component file that cannot contain Unicode data, character data is mapped using `⎕AVU`; it can, therefore, be read without problems by Classic editions.

A `TRANSLATION ERROR` will be generated if:  

* a Unicode edition writes to a non-Unicode component file (that is, either a 32-bit file or a 64-bit file when the Unicode property is currently off) if the data being written contains characters that are not in `⎕AVU`.
* a Classic edition attempts to read a component containing Unicode data that is not in `⎕AVU` from a component file.

### Workspaces

A `TRANSLATION ERROR` will be generated if a Classic edition attempts to `)LOAD` or `)COPY` a workspace containing Unicode data that cannot be mapped to `⎕AV` using the `⎕AVU` in the recipient workspace. The problematic Unicode data might be in the part of a workspace that holds the information needed to generate `⎕DM` and `⎕DMX`; in this situation, calling `)RESET` before `)SAVE` in the Unicode interpreter might eliminate the `TRANSLATION ERROR`s.

## Session Files
Session files (**.dse**) can only be used on the platform on which they were created and saved. Under Microsoft Windows, Session files can only be used by an interpreter with the same architecture (32&#8209;bit/64&#8209;bit) as the interpreter that saved them.

## Log Files
Log files (**.dlf**) can only be used by the version and edition of Dyalog with which they were created and saved. 







