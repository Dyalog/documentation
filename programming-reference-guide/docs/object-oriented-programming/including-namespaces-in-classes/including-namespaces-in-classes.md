#  Including Namespaces in Classes

A Class may import methods from one or more plain Namespaces. This allows several Classes to share a common set of methods, and provides a degree of multiple inheritance.

To import methods from a Namespace `NS`, the Class Script must include a statement:
```apl
:Include NS
```

When the Class is fixed by the editor or by `⎕FIX`, all the defined functions and operators in Namespace `NS` are included as methods in the Class. The functions and operators which are brought in as methods from the namespace `NS` are treated exactly as if the source of each function/operator had been included in the class script at the point of the `:Include` statement. For example, if a function contains `:Signature` or `:Access` statements, these will be taken into account. Note that such declarations have no effect on a function/operator which is in an ordinary namespace.

Dfns and dops in `NS` are also included in the Class but as *Private members*, because dfns and dops may not contain `:Signature` or `:Access` statements. Variables and Sub-namespaces in `NS` are **not** included.

Note that objects imported in this way are not actually *copied*, so there is no penalty incurred in using this feature. Additions, deletions and changes to the functions in `NS` are immediately reflected in the Class.

If there is a member in the Class with the same name as a function in `NS`, the Class member takes precedence and supersedes the function in `NS`.

Conversely, functions in `NS` will supersede members of the same name that are inherited from the Base Class, so the precedence is:

> **Class** supersedes
> > **Included Namespace**, supersedes
> > > **Base Class**

Any number of Namespaces may be included in a Class and the `:Include` statements may occur anywhere in the Class script. However, for the sake of readability, it is recommended that you have `:Include` statements at the top, given that any definitions in the script will supersede included functions and operators.

For information on copying classes that reference namespaces in this way, see  [Referenced Objects](../../../../language-reference-guide/system-commands/copy).
