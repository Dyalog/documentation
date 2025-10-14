<h1 class="heading"><span class="name">Scan For Deprecated Files</span> <span class="command">R←{X}(3535⌶)Y</span></h1>

Scans a directory (and, optionally, sub-directories) for deprecated filetypes. For an overview of deprecated features, see [Deprecated functionality](../../../../programming-reference-guide/deprecated-functionality) in the _Dyalog Programming Reference Guide_.

`Y` is the name of the directory to scan.

`X` specifies whether sub-directories within `Y` should also be scanned. Possible values are:

- `0` – sub-directories are not scanned (this is the default).
- `1` – sub-directories are scanned.

`R` is a two-column matrix identifying the files which are deprecated, with one filename per row.

The files in `Y` (and, optionally, sub-directories of `Y`) are examined, and only the names of files that are deprecated or cannot be checked are included in `R`. The first column contains the filenames, and the second contains a vector of one or more labels indicating why the file is deprecated. The labels are release-dependent; for a list of valid labels see the [Release Notes](../../../../release-notes/announcements/deprecated-functionality). The rows in `R` are not sorted.

<h2 class="example">Example</h2>

```apl
      1(3535⌶)'.'
 ./J0C0.dcf             J0C0
 ./ws2000.dws           OLDWS
 ./XT.dxv               ⎕XT
 ./subdir/S32J0C0.dcf   J0C0  S32
```

See also [`13⌶` – Log use of deprecated features](log-use-of-deprecated-features.md).
