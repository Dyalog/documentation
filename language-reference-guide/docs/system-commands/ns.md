

# <span>Create Namespace</span> `)NS {nm}`

`)NS` creates a **global** namespace and displays its full name, `nm`.

`nm` may be either a simple name or a compound name separated by `'.'`, including one of the special names `'#'` (Root) or `'##'` (Parent).

If `name` does not start with the special Root space identifier `'#'`, the new namespace is created relative to the current one.

If `name` is already in use for a workspace object other than a namespace, the command fails and displays the error message `Name already exists`.

If `name` is an existing namespace, no change occurs.

`)NS` with no `nm` specification displays the current namespace.

<h2 class="example">Examples</h2>
```apl
      )NS
#

      )NS W.X
#.W.X
 
      )CS W.X
#.W.X

      )NS Y.Z
#.W.X.Y.Z
 
      )NS
#.W.X

```
