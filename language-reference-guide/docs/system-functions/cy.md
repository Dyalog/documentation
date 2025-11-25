---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CY CY
</div>






<h1 class="heading"><span class="name">Copy Workspace</span> <span class="command">{R}←{X}⎕CY Y</span></h1>



`Y` must be a simple character scalar or vector identifying a saved workspace (or Session file).  `X` is optional.  If present, it must be a simple character scalar, vector or matrix or a vector of character vectors that specifies one or more APL names.


Each name in `X` is taken to be the name of an active object in the workspace identified by `Y`.  If `X` is omitted, the names of all defined active objects in that workspace are implied (defined functions and operators, variables, labels and namespaces).


Each object named in `X` (or implied) is copied from the workspace identified by `Y` to become the active object referenced by that name in the active workspace if the object can be copied.  A copied label is re-defined to be a variable of numeric type.  If the name of the copied object has an active referent in the active workspace, the name is disassociated from its value and the copied object becomes the active referent to that name.  In particular, a function in the state indicator which is disassociated may be executed whilst it remains in the state indicator, but it ceases to exist for other purposes, such as editing.


The shy result `R` is `0⍴⊂''`.



You may copy an object from a namespace by specifying its full pathname.  The object will be copied to the current namespace in the active workspace, losing its original parent and gaining a new one in the process.  You may only copy a GUI object into a namespace that is a suitable parent for that object.  For example, you could only copy a Group object from a saved workspace if the current namespace in the active workspace is itself a Form, SubForm or Group.


See [Copy Workspace](../system-commands/copy.md) for further information and, in particular, the manner in which dependent and referenced objects are copied, and copying objects from Session (.dse) files.

A `DOMAIN ERROR` is reported in any of the following cases:

- `Y` is ill-formed, or is not the name of a workspace with access authorised for the active user account.
- Any name in `X` is ill-formed.
- An object named in `X` does not exist as an active object in workspace named in `Y`.


An object being copied has the same name as an active label.


When copying data between Classic and Unicode Editions, `⎕CY` will fail and a `TRANSLATION ERROR` will be reported if *any* object in workspace `Y` fails conversion between Unicode and `⎕AV` indices, whether or not that object is specified by `X`. See [Note](avu.md#note) for further details.


A `WS FULL` is reported if the active workspace becomes full during the copying process.

<h2 class="example">Example</h2>
```apl
      ⎕VR'FOO'
     ∇ R←FOO
[1]    R←10
     ∇
      'FOO' ⎕CY 'BACKUP'
      ⎕VR'FOO'
     ∇ R←FOO X
[1]    R←10×X
     ∇
```


System variables are copied if explicitly included in the left argument, but not if the left argument is omitted.

<h2 class="example">Example</h2>
```apl
      ⎕LX
 
      ('⎕LX' 'X')⎕CY'WS/CRASH'
      ⎕LX
→RESTART
```


A copied object may have the same name as an object being executed.  If so, the name is disassociated from the existing object, but the existing object remains defined in the workspace until its execution is completed.

<h2 class="example">Example</h2>
```apl
      )SI
#.FOO[1]*
 
      ⎕VR'FOO'
     ∇ R←FOO
[1]    R←10
     ∇
 
      'FOO'⎕CY'WS/MYWORK'
 
      FOO
1 2 3
      )SI
#.FOO[1]*
      →⎕LC
10
 
```


