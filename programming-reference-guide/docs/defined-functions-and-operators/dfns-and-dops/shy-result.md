<h1 class="heading"><span class="name">Shy Result</span></h1>

Dfns are usually 'pure' functions that take arguments and return explicit results. Occasionally, however, the main purpose of the function might be a side-effect such as the display of information in the session, or the updating of a file, and the value of a result, a secondary consideration. In such circumstances, you might want to make the result 'shy', so that it is discarded unless the calling context requires it. This can be achieved by assigning a dummy variable after a (true) guard:
```apl
      log←{                   ⍝ Append ⍵ to file ⍺.
          tie←⍺ ⎕FSTIE 0      ⍝ tie number for file,
          cno←⍵ ⎕FAPPEND tie  ⍝ new component number,
          tie←⎕FUNTIE tie     ⍝ untie file,        
          1:rslt←cno          ⍝ comp number, shy result.
      }
```
