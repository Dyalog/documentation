---
search:
  boost: 2
---

# <span>Compact Component File</span> `{R}←⎕FRESIZE Y`{{key}}

This function compacts a component file, removing the gaps left by dropped components and by components replaced with smaller arrays, and releasing the space to the operating system. It requires [access code](../../programming-reference-guide/component-files/component-files.md#permission-code) 1024. [Dyadic `⎕FRESIZE`](fresize-dyadic.md) also sets the maximum size of the file.

<h2 class="example">Example</h2>

Dropping the first of two components leaves the file the same size, until `⎕FRESIZE` compacts it:

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

## Right Argument

`Y` is a simple integer scalar or vector:

|Item |Content|
|-----|-------|
|`⊃Y`|The tie number of the file|
|`2⊃Y` (optional)|The passnumber; the default is `0`|

## Result

`R` is the tie number of the file, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

## Compaction

Compaction moves the components of the file towards its start, closing the gaps between them, and then truncates the file, releasing the free space to the operating system. The maximum size of the file is unchanged.

For a large file with many components, compaction can take a significant time. Any interrupt entered at the keyboard during compaction is ignored.

!!! Info "Information"
    Component files that have both journalling and checksum properties set to `0` have been deprecated, and component files with this combination of properties are read-only. Dyalog Ltd recommends using [`⎕FPROPS`](fprops.md) to convert any such files to have different properties. For information on how to identify component files that have both journalling and checksum properties set to `0` in your existing codebase, see the [Release Notes](../../release-notes/announcements/deprecated-functionality.md).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FRESIZE FRESIZE
</div>
