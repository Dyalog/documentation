---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FCHK FCHK
</div>

<h1 class="heading"><span class="name">File Check and Repair</span> <span class="command">R←{X} ⎕FCHK Y</span></h1>

`⎕FCHK` validates and repairs component files, and validates files associated with external variables, following an abnormal termination of the APL process or operating system.

`Y` must be a simple character scalar or vector which specifies the name of the file to be exclusively checked or repaired. For component files, the file must be named in accordance with the operating system's conventions, and may be a relative or absolute pathname. The file must exist and must not be tied. If no file extension is supplied, the set of extensions specified by the  **CFEXT** parameter are tried one after another until the file is found or the set of extensions is exhausted. See [CFEXT](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters).

For files associated with external variables, any filename extension must be specified even if `⎕XT` would not require it. The file must exist and must not currently be associated with an external variable.

Options for `⎕FCHK` are specified using the Variant operator `⍠` or by the optional left argument `X`. The former is recommended but the older mechanism using the left argument is still supported.

In either case, the default behaviour is as follows:

1. If the file appears to have been cleanly untied previously, return `⍬`, that is, report that the file is good.
2. Otherwise, validate the file and return the appropriate result. If the file is corrupt, no attempt is made to repair it.

The result `R` is a vector of the numbers of missing or damaged components. `R` may include non-positive numbers of "pseudo components" that indicate damage to parts of the file other than in specific components:

|----|---------------------|
|`0` |ACCESS MATRIX.       |
|`¯1`|Free-block tree.     |
|`¯2`|Component index tree.|

Other negative numbers represent damage to the file metadata; this set may be extended in the future.

## Specifying options using Variant

Using Variant, the options are as follows:

- Task
- Repair
- Force

*Rebuild* causes the *file indices* to be discarded and rebuilt. *Repair* only takes place on files which have been checked and found to be damaged. It involves a rebuild, but that only takes place if it is needed. Note that Repair and Force only apply if Task is `'Scan'`.

### Task

|---------|----------------------------------------------------------------------------|
|Scan { .shaded } |causes the file to be checked and optionally repaired (see `'Repair'` below)|
|`Rebuild`|causes the file to be unconditionally rebuilt                               |

### Repair (principle option)

|---|-------------------------------------------------|
|0 { .shaded }  |do not repair                                    |
|`1`|causes the file to be repaired if damage is found|

### Force

|---|-------------------------------------------------------------------|
|0 { .shaded }   |do not validate the file if it appears to have been properly closed|
|`1`|validate the file even if it appears to have been properly closed  |

Default values are highlighted thus{ .shaded }  in the above tables.

<h2 class="example">Examples</h2>

To check a file and attempt to fix it if damage is found:
```apl
      (⎕FCHK ⍠ 1)'suspect.dcf'
```

To forcibly check a file and attempt to fix it if damage is found:
```apl
      (⎕FCHK ⍠ ('Repair' 1)('Force'1))'suspect.dcf'
```

### Specifying options using a left argument

Using the optional left-argument, `X` must be a vector of zero or more character vectors from among `'force'`, `'repair'` and `'rebuild'`, which determine the detailed operation of the function. Note that these options are case-insensitive.

- If `X` contains `'force'`, `⎕FCHK` will validate the file even if it appears to have been cleanly untied.
- If `X` contains `'repair'`, `⎕FCHK` will repair the file, following validation, if it appears to be damaged. This option may be used in conjunction with `'force'`.
- If `X` contains `'rebuild'`, `⎕FCHK` will repair the file unconditionally.

- If `X` contains `'force'`, `⎕FCHK` will validate the file even if it appears to have been cleanly untied.
- If `X` contains `'repair'`, `⎕FCHK` will repair the file, following validation, if it appears to be damaged. This option may be used in conjunction with `'force'`.
- If `X` contains `'rebuild'`, `⎕FCHK` will repair the file unconditionally.

Following a *check* of the file, a non-null result indicates that the file is damaged.

Following a *repair* of the file, the result indicates those components that could not be recovered. Un-recovered components will give a `FILE COMPONENT DAMAGED` error if read but may be replaced without error.

Repair can recover only check-summed components from the file, that is, only those components that were written with the checksum option enabled (see [File Properties](fprops.md)).

Following an operating system crash, repair may result in one or more individual components being rolled back to a previous version or not recovered at all, unless Journaling levels 2 or 3 were also set when these components were written.
