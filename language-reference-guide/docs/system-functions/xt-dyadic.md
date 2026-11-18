---
search:
  boost: 2
---

# <span>Associate External Variable</span> `{R}←X ⎕XT Y`{{key}}

This function makes a variable an [external variable](#external-variables) by associating it with a file. [Monadic `⎕XT`](xt-monadic.md) returns the file that an external variable is associated with.

!!! Info "Information"
    External variables have been deprecated, and are scheduled for removal in a future release. Dyalog Ltd recommends using [`⎕MAP`](map.md) or [component files](../../programming-reference-guide/introduction/component-files.md) instead. Support for external variables is enabled by default. Setting the [`DYALOG_EXTVAR_SUPPORTED`](../../windows-installation-and-configuration-guide/configuration-parameters/dyalog-extvar-supported.md) configuration parameter to `0` disables it, and `⎕XT` then signals `SYNTAX ERROR`. The [Release Notes](../../release-notes/announcements/deprecated-functionality.md) describe how to find uses of external variables in existing code.

<h2 class="example">Examples</h2>

A new external variable has no value until one is assigned:

```apl
      'array.dxv' ⎕XT 'V'
      V
VALUE ERROR
      V
      ∧
```

The value is stored in the file, not in the workspace:

```apl
      w←⎕WA
      V←⍳100000
      w-⎕WA
32
```

An external variable is used, and assigned to in part, like any other variable:

```apl
      V←⍳5
      +/V
15
      V[3]←⊂'ABC'
      V,←⊂2 4⍴⍳8
      ⍴V
6
      V[1 2 4 5 6]×←10
      V
10 20  ABC  40 50  10 20 30 40
                   50 60 70 80
```

The file keeps the value, and can be associated with another variable:

```apl
      ⎕EX'V'
      'array.dxv' ⎕XT 'F'
      F
10 20  ABC  40 50  10 20 30 40
                   50 60 70 80
```

## Left Argument

`X` is a simple character scalar or vector, the name of the file. Under Microsoft Windows, a name without an extension gets the extension `.DXV`. If the file does not exist, it is created. Under Unix, `X` can also be [empty](#temporary-files). If another variable is associated with the file, `⎕XT` signals `FILE TIED`.

## Right Argument

`Y` is a simple character scalar or vector, the name of the variable. The name of a function, operator, label, or namespace signals `DOMAIN ERROR`. If the variable already has a value, the value is discarded, and the variable gets the value in the file, or no value if the file holds none. If the variable is already an external variable, it is associated with the new file instead.

## Result

`R` is the name of the file, including any extension that `⎕XT` added, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

## External Variables

An external variable is a variable whose value is stored in a file instead of in the workspace. Assigning a value to it, or to part of it, updates the file, and using it reads its value from the file. Otherwise, it behaves like any other variable. An expression that uses an external variable needs only temporary workspace, usually for part of its value. An external variable cannot hold a namespace, a reference to one, or its [`⎕OR`](or.md), and assigning one signals `DOMAIN ERROR`.

The file keeps the value when the variable is expunged, when a function in which it is localised returns, or when the session ends, and the file can then be associated with another variable. [`⎕NERASE`](nerase.md) erases the file.

## Temporary Files

Under Unix, an empty `X` associates the variable with a temporary file, which is erased when the variable stops being external:

```apl
      ''⎕XT'TEMP'
      TEMP←⍳10
      +/TEMP×TEMP
385
      ⎕EX'TEMP'
```

## Shared Access

A new file is created with read and write access for its owner only. An existing file with these permissions is opened for exclusive use by its owner. If the permissions of the file let other users read and write it, it is opened for shared use, and several users or tasks can use the external variable at the same time. [`⎕FHOLD`](fhold.md) can co-ordinate them. Exclusive use is faster, because it lets the interpreter buffer the file instead of reading and writing it directly every time. Under Unix, the operating system changes the permissions of a file. Under Microsoft Windows, the function `XVAR` in the `util` workspace does.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XT XT
</div>
