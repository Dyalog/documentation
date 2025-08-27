<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FSTAC FSTAC
</div>






<h1 class="heading"><span class="name">File Set Access</span> <span class="command">{R}←X ⎕FSTAC Y</span></h1>


## Access code 8192


`Y` must be a simple integer scalar or 1 or 2 element vector containing the file tie number followed by an optional passnumber. If the passnumber is omitted it is assumed to be zero.


`X` must be a valid access matrix, that is, a 3-column integer matrix with any number of rows.  The function sets access control for a set of specific users (1<sup>st</sup> column) and file operations (2<sup>nd</sup> column) with specified passnumbers ( 3<sup>rd</sup> column). Note that a 0 in the 1<sup>st</sup> column specifies **all** users, a `¯1` in the 2<sup>nd</sup> column specifies **all** file operations, and a `0` in the 3<sup>rd</sup> column specifies that **no** passnumber is required. For further details, see [File Access Control](../../../programming-reference-guide/component-files/component-files).


The shy result of `⎕FSTAC` is the tie number of the file.

<h2 class="example">Examples</h2>
```apl

      'SALES' ⎕FCREATE 1
      (3 3⍴28 2105 16385 0 2073 16385 31 ¯1 0) ⎕FSTAC 1
      ((⎕FRDAC 1)⍪21 2105 16385) ⎕FSTAC 1

       (1 3⍴0 ¯1 0)⎕FSTAC 2 ⍝ Let everyone do anything

```

!!! Info "Information"
    Component files that have both journalling and checksum properties set to `0` have been deprecated; from Dyalog v21.0, component files with this combination of properties will be read-only. Dyalog Ltd recommends using `⎕FPROPS` to convert any such files to have different properties. For information on how to identify component files that have both journalling and checksum properties set to `0` in your existing codebase, see the [Release Notes](../../../release-notes/announcements/deprecated-functionality/).

