---
search:
  boost: 2
---

# <span>Compact Component File</span> `{R}←⎕FRESIZE Y`{{key}}

## Access code 1024

`Y` must be a simple integer scalar or 1 or 2 element vector containing the file tie number followed by an optional passnumber.  If the passnumber is omitted it is assumed to be zero.

An attempt to update a component file that would cause it to exceed its [maximum size](fresize-dyadic.md) will fail with a `FILE FULL` error (21). `⎕FRESIZE` compacts the file. This process removes any gaps in the file caused by replacing a component with a shorter array. Any interrupt entered at the keyboard during the compaction is ignored.

During compaction, the file is restructured by reordering the components and by amalgamating the free areas at the end of the file. The file is then truncated and excess disk space is released back to the operating system. For a large file with many components, this process may take a significant time.

The shy result of `⎕FRESIZE` is the tie number of the file.

<h2 class="example">Example</h2>
```apl
      'test'⎕FCREATE 1 ⋄ ⎕FSIZE 1
1 1 304 1.844674407E19
      (10 1000⍴1.1)⎕FAPPEND 1 ⋄ ⎕FSIZE 1
1 2 81104 1.844674407E19
      (10 1000⍴1.1)⎕FAPPEND 1 ⋄ ⎕FSIZE 1
1 3 161240 1.844674407E19
      ⎕FDROP 1 1 ⋄ ⎕FSIZE 1
2 3 161312 1.844674407E19
      ⎕FRESIZE 1 ⋄ ⎕FSIZE 1
2 3 80568 1.844674407E19
```

!!! Info "Information"
    Component files that have both journalling and checksum properties set to `0` have been deprecated; from Dyalog v21.0, component files with this combination of properties will be read-only. Dyalog Ltd recommends using `⎕FPROPS` to convert any such files to have different properties. For information on how to identify component files that have both journalling and checksum properties set to `0` in your existing codebase, see the [Release Notes](../../../release-notes/announcements/deprecated-functionality/).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FRESIZE FRESIZE
</div>
