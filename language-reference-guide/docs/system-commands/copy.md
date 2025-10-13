




<h1 class="heading"><span class="name">Copy Workspace</span> <span class="command">)COPY {ws {nms}}</span></h1>



This command brings all or selected global objects `nms` from a stored workspace (or session file) with the given name.  A stored workspace is one which has previously been saved with the system command `)SAVE` or the system function `⎕SAVE`.


See [Programmer's Guide: "Workspaces"](../../../programming-reference-guide/introduction/workspaces) for the rules for specifying a workspace name.


If the list of names is excluded, all defined objects (including namespaces) are copied.


If the workspace name identifies a valid, readable workspace, the system reports the workspace name, "`saved`" and the date and time when the workspace was last saved.


<h2 class="example">Examples</h2>
```apl
      )COPY WS/UTILITY
WS/UTILITY saved Mon Nov  1 13:11:19 1992
 
      )COPY TEMP ⎕LX FOO X A.B.C
./TEMP saved Mon Nov  1 14:20:47 1992
not found X
```


Copied objects are defined at the global level in the active workspace.  Existing global objects in the active workspace with the same name as a copied object are replaced.  If the copied object replaces either a function in the state indicator, or an object that is an operand of an operator in the state indicator, or a function whose left argument is being executed, the original object remains defined until its execution is completed or it is no longer referenced by an operator in the state indicator.  If the workspace name is not valid or does not exist or if access to the workspace is not authorised, the system reports `ws not found`.


You may copy an object from a namespace by specifying its full pathname.  The object will be copied to the current namespace in the active workspace, losing its original parent and gaining a new one in the process.  You may only copy a GUI object into a namespace that is a suitable parent for that object.  For example, you could only copy a Group object from a saved workspace if the current namespace in the active workspace is itself a Form, SubForm or Group.


If the workspace name identifies a file that is not a workspace, the system reports `bad ws`.


If the source workspace is too large to be loaded, the system reports `ws too large`.


When copying data between Classic and Unicode Editions, `)COPY` will fail with `TRANSLATION ERROR` if *any* object in the source workspace fails conversion between Unicode and `⎕AV` indices, whether or not that object is specified by `nms`. See [Atomic Vector - Unicode](../system-functions/avu.md) for further details.


If `ws` is omitted, the file open dialog box is displayed and all objects copied from the selected workspace.


If the list of names is included, the names of system variables may also be included and copied into the active workspace.  The global referents will be copied.


If an object is not found in the stored workspace, the system reports `not found` followed by the name of the object.

## Dependent Objects


If the list of names includes the name of:

- an Instance of a Class but not the Class itself
- a Class but not a Class upon which it depends
- an array or a namespace that contains a ref to another namespace, but not the namespace to which it refers


the dependent object(s) **will also be copied** but will be **unnamed** and **hidden**. In such as case, the system will issue a warning message.


For example, if a saved workspace named CFWS contains a Class named `#.CompFile` and an Instance (of `CompFile`) named `icf`,
```apl
      )COPY CFWS icf
.\CFWS saved Fri Mar 03 10:21:36 2006
copied object created an unnamed copy of class #.CompFile
```


The existence of a hidden copy can be confusing, especially if it is a hidden copy of an object which had a name which is in use in the current workspace. In the above example, if there is a class called `CompFile` in the workspace into which `icf` is copied, the copied instance may *appear* to be an instance of the *visible* `CompFile`, but it will actually be an instance of the hidden `CompFile` - which may have very different (or perhaps worse: very slightly different) characteristics to the named version.


If you copy a Class without copying its Base Class, the Class can be used (it will use the invisible copy of the Base Class), but if you edit the Class, you will either be unable to save it because the editor cannot find the Base Class, or - if there is a visible Class of that name in the workspace - it will be used as the Base Class.


In the latter case, the invisible copy which was brought in by `)COPY` will now disappear, since there are no longer any references to it - and if these two Base Classes were different, the behaviour of the derived Class will change (and any changes made to the invisible Base Class since it was copied will be lost).

## Referenced Objects


If you copy a Class or a namespace that is referenced by a Class as its Base Class or via a `:Include` statement, the referring Class will continue to refer to the original definition of the copied name which will be retained for that purpose. The Class can be made to refer to the copied definition of that name by refixing it.

<h2 class="example">Example</h2>


The current workspace has a class named `pete` whose Base class is called `base`.
```apl
:Class pete: base
:EndClass

:Class base
    ∇ r←foo n
      :Access Public
      r←'Original'n
    ∇
:EndClass

```

A second workspace named `copy.dws` contains a different version of the `base` class:
```apl
:Class base
    ∇ r←foo n
      :Access Public
      r←'Copied'n
    ∇
:EndClass

      )COPY copy.dws base
copy.dws saved Thu Nov 22 16:24:27 2018
      inst←⎕NEW pete
      inst.foo 1
Original  1

      ⎕FIX ⎕SRC pete
      inst←⎕NEW pete
      inst.foo 1
Copied  1
```

## Copying Objects from Session Files

You may also copy objects from session (.dse) files, although with certain restrictions.

<h2 class="example">Example</h2>
```
        )COPY C:\Users\Pete\Desktop\pete.dse ⎕SE.UCMD
C:\Users\Pete\Desktop\pete.dse saved Wed Oct 14 ...

```

- You can copy a function or variable from any namespace under a saved `⎕SE`, no matter what your current namespace is.
- You can copy any namespace without GUI from a saved `⎕SE`, no matter what you current namespace is.
- You can copy any namespace with GUI from a saved `⎕SE` as long as your current namespace is the same as the parent namespace of the namespace you are trying to copy

<h2 class="example">Examples</h2>

In the following example, the *not copied* cases occur because the current namespace is not an appropriate parent for the object in question.
```
      )CS #
#
      )COPY C:\Users\...\pete.dse ⎕SE.Dyalog.Callbacks
C:\Users\...\pete.dse saved Wed Oct 14 15:31:14 2015

```
```
       )COPY C:\Users\...\pete.dse ⎕SE.cbbot
C:\Users\...\pete.dse saved Wed Oct 14 15:31:14 2015
not copied cbbot

```
```
       )CS ⎕SE
⎕SE
      )COPY C:\Users\...\pete.dse ⎕SE.cbbot
C:\Users\...\pete.dse saved Wed Oct 14 15:31:14 2015
      
      )COPY C:\Users\...\pete.dse ⎕SE.cbbot.bandsb1
C:\Users\...\pete.dse saved Wed Oct 14 15:31:14 2015
not copied bandsb1
```


