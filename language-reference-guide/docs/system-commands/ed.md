




<h1 class="heading"><span class="name">Edit Object</span> <span class="command">)ED nms</span></h1>

`)ED` invokes the Dyalog editor and opens an Edit window for each of the objects specified in `nms`.

If a name includes the slash character  (`\` or `/`) it is taken to be the name of a file. See [Editing Scripts and Text Files](../../../windows-ui-guide/editing-scripts-and-text-files).

If a name is followed by a line number specified in square brackets, the Editor positions the cursor in the corresponding line. There must not be a space between the last character of the name and the `[`.

If a name is not already defined, it is assumed to be a function or operator unless `type` is also specified.

You can specify the type of a new object by prefixing its name with a single symbol:

|---|---------------------------|
|`∇`|function or operator       |
|`⍟`|Namespace script           |
|`○`|Class script               |
|`∘`|Interface                  |
|`→`|simple character vector    |
|`∊`|vector of character vectors|
|`-`|character matrix           |
|`⋄`|array: use array notation  |

If an existing object is named, any type specification in the command is ignored unless the type is `⋄`.

If the type is `⋄` and the name is either undefined or of an array, the Editor opens in array-notation mode.
The resulting array can be of any type or structure.


The first object named becomes the top window on the stack.
See the *Dyalog for Microsoft Windows UI Guide* or the *Dyalog for UNIX UI Guide* for details.


<h2 class="example">Examples</h2>
```apl

      )ED MYFUNCTION

      )ED MYFUNCTION[1000] YOURFUNCTION[3]

      )ED ∇FOO -MAT ∊VECVEC

```


Objects specified in `nms` that cannot be edited are silently ignored. Objects qualified with a namespace path  (for example, `a.b.c.foo`) are silently ignored if the namespace does not exist.



