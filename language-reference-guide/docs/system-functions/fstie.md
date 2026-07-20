---
search:
  boost: 2
---

# <span>File Share Tie</span> `{R}←X ⎕FSTIE Y`{{key}}

`Y` must be 0 or a simple 1 or 2 element integer vector containing an available file tie number to be associated with the file for further file operations, and an optional passnumber.  If the passnumber is omitted it is assumed to be zero.  The tie number must not already be associated with a tied file.

`X` must be a simple character scalar or vector which specifies the name of the file to be tied.  The file must be named in accordance with the operating system's conventions, and may be specified with a relative or absolute pathname. If no file extension is supplied, the set of extensions specified by the  **CFEXT** parameter are tried one after another until the file is found or the set of extensions is exhausted. See [ CFEXT](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters).

The file must exist and be accessible by the user.  If it is already tied by another task, it must not be tied exclusively.

The shy result of `⎕FSTIE` is the tie number of the file.

## Automatic Tie Number Allocation

A tie number of 0 as argument to a create, share tie or exclusive tie operation, allocates the first (closest to zero) available tie number and returns it as an explicit result. This allows you to simplify code. For example:

from:
```apl
      tie←1+⌈/0,⎕FNUMS  ⍝ With next available number,
      file ⎕FSTIE tie   ⍝ ... share tie file.
```

to:
```apl
      tie←file ⎕FSTIE 0 ⍝ Tie with 1st available number.
```

<h2 class="example">Example</h2>
```apl
      'SALES' ⎕FSTIE 1
 
      '../budget/COSTS' ⎕FSTIE 2
```

# Variant Options
## Mode

Writing to a component file is not always permitted. For example, restrictions on writing to a component file might be imposed by operating system permissions, the host filesystem, or individual component file property settings.

The **Mode** variant option specifies whether the file that is being tied will only be read or must be writeable. Possible values are:

- `P` (tied as **p**ermitted) – the file will be tied for write access if possible, otherwise for read access only. If the file permissions do not allow the file to be written to, any subsequent attempt to write to it will fail. This is the default.
- `R` (**r**ead mode) – the file will be tied for read access only; any subsequent attempt to write to it will fail.
- `W` (**w**rite mode) – if the file permissions do not allow the file to be written to, the attempt to tie it will fail.

The **Mode** variant option is independent of any [file access controls managed using an access matrix](../../../programming-reference-guide/component-files/component-files/#file-access-control).

<h3 class="example">Example</h3>

```apl
      'cf' (⎕FSTIE⍠'Mode' 'W') 1
FILE ACCESS ERROR: cf.dcf: File is not writable
      'cf'(⎕FSTIE⍠'Mode' 'W')1
                ∧
```

!!! Info "Information"
    Small-span (32-bit) component files are currently read-only; this support is scheduled for removal in a future release, after which it will not be possible to tie small-span component files. Dyalog Ltd recommends using `⎕FCOPY` to convert any such files to large-span (64-bit). For information on how to identify calls to small-span component files in your existing codebase, see the [Release Notes](../../../release-notes/announcements/deprecated-functionality/).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FSTIE FSTIE
</div>
