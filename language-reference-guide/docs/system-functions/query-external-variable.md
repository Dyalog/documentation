---
search:
  boost: 2
---

# <span>Query External Variable</span> `R←⎕XT Y`{{key}}

`Y` must be a simple character scalar or vector which is taken to be a variable name.  `R` is a simple character vector containing the file reference of the external array associated with the variable named by `Y`, or the null vector if there is no associated external array.

<h2 class="example">Example</h2>
```apl
      ⎕XT'V'
EXT\ARRAY
 
      ⍴⎕XT'G'
0
 
```

!!! Info "Information"
    Support for external variables has been deprecated. They are no longer supported by default, although setting the [DYALOG_EXTVAR_SUPPORTED](../../../windows-installation-and-configuration-guide/configuration-parameters/dyalog-extvar-supported) configuration parameter to `1` reinstates support (support is scheduled for removal in a future release). For information on how to identify uses of external variables in your existing codebase, see the [Release Notes](../../../release-notes/announcements/deprecated-functionality/).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕XT XT
</div>
