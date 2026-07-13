




# <span>Erase Object</span> `)ERASE nms`



This command erases named global defined objects (functions, operators, variables, namespaces and GUI objects) from the active workspace or current namespace.


If a named object is a function or operator in the state indicator, or the object is an operand of an operator in the state indicator, or the object is a function whose left argument is being executed, the object remains defined until its execution is completed or it is no longer referenced by an operator in the state indicator.  However, the name is available immediately for other uses.



If a named object is a GUI object, the object and all its children are deleted and removed from the screen.


If an object is not erased for any reason, the system reports  `not found`  followed by the name of the object.


Erasing objects such as external functions may have other implications: see [Expunge Object](../system-functions/ex.md) for details.

<h2 class="example">Example</h2>
```apl
      )ERASE FOO A ⎕IO
not found ⎕IO
```


