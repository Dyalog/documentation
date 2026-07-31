---
search:
  boost: 2
---

# <span>Exclusive File Tie</span> `{R}←X ⎕FTIE Y`{{key}}

## Access code 2

`Y` must be 0 or a simple 1 or 2 element integer vector containing an available file tie number to be associated with the file for further file operations, and an optional passnumber.  If the passnumber is omitted it is assumed to be zero.  The tie number must not already be associated with a share tied or exclusively tied file.

`X` must be a simple character scalar or vector which specifies the name of the file to be exclusively tied.  The file must be named in accordance with the operating system's conventions, and may be a relative or absolute pathname. If no file extension is supplied, the set of extensions specified by the  **CFEXT** parameter are tried one after another until the file is found or the set of extensions is exhausted. See [ CFEXT](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters).

The file must exist and  the user must have write access to it.  It may not already be tied by another user.

## Automatic Tie Number Allocation

A tie number of 0 as argument to a create, share tie or exclusive tie operation, allocates the first (closest to zero) available tie number, and returns it as an explicit result. This allows you to simplify code. For example:

from:
```apl
      tie←1+⌈/0,⎕FNUMS ⍝ With next available number,
      file ⎕FTIE tie   ⍝ ... tie file.
```

to:
```apl
      tie←file ⎕FTIE 0 ⍝ Tie with first available number.
```

The shy result of `⎕FTIE` is the tie number of the file.

<h2 class="example">Examples</h2>
```apl
      'SALES' ⎕FTIE 1
 
      '../budget/COSTS' ⎕FTIE  2
 
      '../budget/expenses' ⎕FTIE 0
3
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
      'cf' (⎕FTIE⍠'Mode' 'W') 1
FILE ACCESS ERROR: cf.dcf: File is not writable
      'cf'(⎕FTIE⍠'Mode' 'W')1
                ∧
```

!!! Info "Information"
    Small-span (32-bit) component files are currently read-only; this support is scheduled for removal in a future release, after which it will not be possible to tie small-span component files. Dyalog Ltd recommends using `⎕FCOPY` to convert any such files to large-span (64-bit). For information on how to identify calls to small-span component files in your existing codebase, see the [Release Notes](../../../release-notes/announcements/deprecated-functionality/).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FTIE FTIE
</div>
