---
search:
  boost: 2
---

# <span>Query External Variable</span> `R←⎕XT Y`{{key}}

For an [external variable](#external-variables), this function returns the name of the file that the variable is associated with. [Dyadic `⎕XT`](xt-dyadic.md) associates a variable with a file.

!!! Legacy "Legacy"
    External variables are retained for backwards compatibility purposes, and are scheduled for removal in a future release. Dyalog Ltd recommends using [`⎕MAP`](map.md) or [component files](../../programming-reference-guide/introduction/component-files.md) instead. Support for external variables is enabled by default. Setting the [`DYALOG_EXTVAR_SUPPORTED`](../../windows-installation-and-configuration-guide/configuration-parameters/dyalog-extvar-supported.md) configuration parameter to `0` disables it, and `⎕XT` then signals `SYNTAX ERROR`. The [Release Notes](../../release-notes/announcements/deprecated-functionality.md) describe how to find uses of external variables in existing code.

<h2 class="example">Example</h2>

```apl
      'array' ⎕XT 'V'
      ⎕XT 'V'
array
      ⍴⎕XT 'G'
0
```

## Right Argument

`Y` is a simple character scalar or vector, the name of a variable.

## Result

`R` is the name of the file that is associated with the variable, as it was given when the variable was associated with it. `R` is `''` if the variable is not an external variable, or if it is associated with a temporary file.

## External Variables

An external variable is a variable whose value is stored in a file instead of in the workspace. Assigning a value to it, or to part of it, updates the file, and using it reads its value from the file. Otherwise, it behaves like any other variable. An expression that uses an external variable needs only temporary workspace, usually for part of its value. An external variable cannot hold a namespace, a reference to one, or its [`⎕OR`](or.md), and assigning one signals `DOMAIN ERROR`.

The file keeps the value when the variable is expunged, when a function in which it is localised returns, or when the session ends, and the file can then be associated with another variable. [`⎕NERASE`](nerase.md) erases the file.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XT XT
</div>
