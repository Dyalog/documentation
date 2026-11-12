---
search:
  boost: 2
---

# <span>Resize Component File</span> `{R}←X ⎕FRESIZE Y`{{key}}

This function sets the maximum size of a component file, and [compacts](#compaction) the file as [monadic `⎕FRESIZE`](fresize-monadic.md) does. It requires [access code](../../programming-reference-guide/component-files/component-files.md#permission-code) 1024.

<h2 class="example">Example</h2>

Once the file has a maximum size, an update that would make it larger fails:

```apl
      'test'⎕FCREATE 1
      (10 1000⍴1.1)⎕FAPPEND 1 ⋄ ⎕FSIZE 1
1 2 81104 1.844674407E19
      100000 ⎕FRESIZE 1 ⋄ ⎕FSIZE 1
1 2 80896 100000
      (10 1000⍴1.1)⎕FAPPEND 1
FILE FULL: test.dcf: File size limit reached
      (10 1000⍴1.1)⎕FAPPEND 1
                   ∧
```

## Left Argument

`X` is an integer scalar, the maximum size of the file, in bytes. `0` means the largest size that a component file can have.

The maximum size is stored in the file, and applies until it is changed. An update that would make the file larger than its maximum size signals `FILE FULL`. If `X` is smaller than the size of the file after [compaction](#compaction), `FILE FULL` is signalled and the maximum size is not changed.

## Right Argument

`Y` is a simple integer scalar or vector:

|Item |Content|
|-----|-------|
|`⊃Y`|The tie number of the file|
|`2⊃Y` (optional)|The passnumber; the default is `0`|

## Result

`R` is the tie number of the file, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

## Compaction

Compaction moves the components of the file towards its start, closing the gaps between them, and then truncates the file, releasing the free space to the operating system.

For a large file with many components, compaction can take a significant time. Any interrupt entered at the keyboard during compaction is ignored.

!!! Info "Information"
    Component files that have both journalling and checksum properties set to `0` have been deprecated, and component files with this combination of properties are read-only. Dyalog Ltd recommends using [`⎕FPROPS`](fprops.md) to convert any such files to have different properties. For information on how to identify component files that have both journalling and checksum properties set to `0` in your existing codebase, see the [Release Notes](../../release-notes/announcements/deprecated-functionality.md).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FRESIZE FRESIZE
</div>
