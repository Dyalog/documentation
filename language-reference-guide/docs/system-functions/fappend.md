<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FAPPEND FAPPEND
</div>






<h1 class="heading"><span class="name">File Append Component</span> <span class="command">{R}←X ⎕FAPPEND Y</span></h1>


## Access code 8


`Y` must be a simple integer scalar or a 1 or 2 element vector containing the file tie number followed by an optional passnumber.  If the passnumber is omitted it is assumed to be zero. Subject to a few restrictions, `X` may be any array.


The shy result `R` is the number of the component to which `X` is written, and is 1 greater than the previously highest component number in the file, or 1 if the file is new.

<h1 class="example">Examples</h1>
```apl
      (1000?1000) ⎕FAPPEND 1
 
      ⎕←(2 3⍴⍳6) 'Geoff' (⎕OR'FOO') ⎕FAPPEND 1
12
 
      ⎕←A B C ⎕FAPPEND¨1
13 14 15

Dump←{
    tie←⍺ ⎕FCREATE 0              ⍝ create file.
    (⎕FUNTIE tie){}⍵ ⎕FAPPEND tie ⍝ append and untie.
}
```

!!! Info "Information"
    Component files that have both journalling and checksum properties set to `0` have been deprecated; from Dyalog v21.0, component files with this combination of properties will be read-only. Dyalog Ltd recommends using `⎕FPROPS` to convert any such files to have different properties. For information on how to identify component files that have both journalling and checksum properties set to `0` in your existing codebase, see the [Release Notes](../../../release-notes/announcements/deprecated-functionality/).
