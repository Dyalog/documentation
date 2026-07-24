---
search:
  boost: 2
---

# <span>Search Path</span> `⎕PATH`

`⎕PATH` is a simple character vector representing a blank-separated list of namespaces.  It is approximately analogous to the PATH variable in Windows or UNIX.

The `⎕PATH` variable can be used to identify a namespace in which commonly used utility functions reside.  Functions or operators (**NOT** variables) which are copied into this namespace and *exported* (see [Export Object](export.md)) can then be used directly from anywhere in the workspace without giving their full path names. `⎕PATH` has Session scope.

<h2 class="example">Example</h2>

To make the `DISPLAY` function available directly from within any namespace.
```apl
      ⍝ Create and reference utility namespace.
      ⎕PATH←'⎕SE.util'⎕NS''
      ⍝ Copy DISPLAY function from UTIL into it.
      'DISPLAY'⎕SE.util.⎕CY'UTIL'
      ⍝ (Remember to save the session to file).  
```

In detail, `⎕PATH` works as follows:

When a reference to a name cannot be found in the current namespace, the system searches for it from left to right in the list of namespaces indicated by `⎕PATH`.  In each namespace, if the name references a defined function (or operator) *and* the export type of that function is non-zero (see [Export Object](export.md) ), then it is used to satisfy the reference.  If the search exhausts all the namespaces in `⎕PATH` without finding a qualifying reference, the system issues a `VALUE ERROR` in the normal manner.

The special character `↑` stands for the list of namespace ancestors:
```apl
       ## ##.## ##.##.## ...
```

In other words, the search is conducted upwards through enclosing namespaces, emulating the static scope rule inherent in modern block-structured languages.

Note that the `⎕PATH` mechanism is used ONLY if the function reference cannot be satisfied in the current namespace.  This is analogous to the case when the Windows or UNIX PATH variable begins with a `'.'`.

<h2 class="example">Examples</h2>
```other
   ⎕PATH               Search in ...

```
```other
1. '⎕SE.util'          Current space,   then
                       ⎕SE.util,        then
                       VALUE ERROR
 
2. '↑'                 Current space
                       Parent space: ##
                       Parent's parent space:  ##.##
                       ...
                       Root: # (or ⎕SE if current space
                                was inside ⎕SE)
                       VALUE ERROR
 
3. 'util ↑ ⎕SE.util'   Current space
                       util (relative to current space)
                       Parent space: ##
                       ...
                       Root: # or ⎕SE
                       ⎕SE.util
                       VALUE ERROR
```

Note that `⎕PATH` is a *session* variable.  This means that it is workspace-wide and survives `)LOAD` and `)CLEAR`. It can of course, be localised by a defined function or operator.

`⎕PATH` does not support derived functions and will not be extended to support them; nor will it be extended to support other types of functions that may be developed in the future. `⎕PATH` may therefore be considered an archaic feature.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PATH PATH
</div>
