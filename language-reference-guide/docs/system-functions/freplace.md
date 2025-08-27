<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FREPLACE FREPLACE
</div>

<h1 class="heading"><span class="name">File Replace Component</span> <span class="command">{R}←X ⎕FREPLACE Y</span></h1>

## Access code 16

`Y` must be a simple 2 or 3 element integer vector containing the file tie number, the component number, and an optional passnumber.  If the passnumber is omitted it is assumed to be zero.  The component number specified must lie within the file's component number limits.

`X` is any array (including, for example, the `⎕OR` of a namespace), and overwrites the value of the specified component.  The component information (see [File Read Component Information](frdci.md)) is also updated.

The shy result of `⎕FREPLACE` is the file index (component number of replaced record).

<h2 class="example">Example</h2>
```apl
      SALES←⎕FREAD 1 241
 
      (SALES×1.1) ⎕FREPLACE 1 241
```

Define a function to replace (index, value) pairs in a component file JMS.DCF:
```apl
Frep←{
    tie←⍺ ⎕FTIE 0
    _←{⍵ ⎕FREPLACE tie ⍺}/¨⍵
    ⎕FUNTIE tie
} 
 
      'jms'Frep(3 'abc')(29 'xxx')(7 'yyy')
```

!!! Info "Information"
    Component files that have both journalling and checksum properties set to `0` have been deprecated; from Dyalog v21.0, component files with this combination of properties will be read-only. Dyalog Ltd recommends using `⎕FPROPS` to convert any such files to have different properties. For information on how to identify component files that have both journalling and checksum properties set to `0` in your existing codebase, see the [Release Notes](../../../release-notes/announcements/deprecated-functionality/).
