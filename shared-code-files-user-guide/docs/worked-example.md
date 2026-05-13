<h1 class="heading"><span class="name">Worked Example</span></h1>

This annotated example demonstrates the use of some of the [I-Beam functions](../technical-details/#technical-reference.md) related to shared code files (examples of assimilate and detach are not included).

First, load the dfns workspace:
```apl
      )LOAD dfns
C:\...\ws\dfns.dws saved Sun Apr 12 17:18:38 2015

An assortment of D Functions and Operators.

      tree #                ⍝ Workspace map.
      ↑¯10↑↓attrib ⎕nl 3 4  ⍝ What's new?
      ⍕notes find 'Word'    ⍝ Apropos "Word".
      ⎕ed'notes.contents'   ⍝ Workspace overview.
```

Now compute the size of all the functions, variables and namespaces in the workspace (approximately 6 MB):
```apl
      +/⎕SIZE ⎕NL ⍳10
5947936
```

Define a helper function called saveDWX to create a shared code file:
```apl
      saveDWX←8667⌶
```

Create a shared code file containing everything in the dfns workspace, mapped at virtual memory address 1:
```apl
      saveDWX 1 'dfns.dwx'
```

If this fails due to the file already existing, then  erase it and try again:
```apl
      saveDWX 1 'dfns.dwx'
DOMAIN ERROR: Shared code file already exists
      saveDWX 1 'dfns.dwx'
     ∧
```
```apl
      ⎕NDELETE 'dfns.dwx'
      saveDWX 1 'dfns.dwx'
```

Clear the workspace and define two new helper functions, attachDWX and listDWX:
```apl
      )CLEAR
clear ws
```
```apl
      attachDWX←8666⌶
      listDWX←8659⌶
```

Attach the shared code file to the active workspace and compute how much workspace was consumed in doing so:
```apl
      wa←⎕WA
```
```apl
      attachDWX 'dfns.dwx'
```
```apl
      ⎕WA-wa
¯64320
```

(rather than consuming space, 64 KB was released due to workspace reorganisation)

Check how many names are now visible in the workspace and call the `easter` function to find the date for Easter Sunday in 2015 (to prove that functions in the attached shared code file can be run successfully):
```apl
      ≢⎕NL ⍳10
273
```
```apl
      easter 2015
20150405
```

List the shared code files that are attached to the active workspace (the first column shows the slot identifier). Next, display the first 5 names made available by the shared code file in slot identifier 1:
```apl
      listDWX ⍬
1  dfns.dwx
```
```apl
      5↑1 listDWX ⍳10
Cholesky
NormRand
UndoRedo
X
_fk
```

Finally, verify that the result of [`⎕NL`](../../language-reference-guide/system-functions/nl) and the names exposed by the shared code file are identical (the only difference should be the three names defined since the [`)CLEAR`](../../language-reference-guide/system-commands/clear) operation):
```apl
      (⎕NL ⍳10)≡1 listDWX ⍳10
0
```
```apl
      ⍴1 listDWX ⍳10
270 12
```
```apl
      ⍴⎕NL ⍳10
273 12
```
```apl
      (↓⎕NL ⍳10)~↓1 listDWX ⍳10
attachDWX     listDWX       wa
```
