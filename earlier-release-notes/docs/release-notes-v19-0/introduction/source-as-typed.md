<h1 class="heading"><span class="name">Source as Typed</span></h1>

## Historical Introduction

When an object containing executable code such as a function, operator, class, or namespace is defined in a workspace either by an editor or by the system function `⎕FX`, the object is tokenised into an internal form. Historically, this was the only form of the object, and both the editor and system functions like `⎕CR`, `⎕VR`, `⎕NR` reconstitute the source code from the internal form. This reconstituted source lacks extraneous white space and the precise numerical formatting that the user originally entered, for example.

When classes and scripted namespaces were introduced, the source code was stored in text form for these objects, as it was typed, in addition to the tokens which were still used at runtime. The function `⎕SRC` was added to return this text, and a new function `⎕FIX` was added to define objects that also have source code.

Subsequently, `⎕FIX` was extended to allow the definition of functions and operators which include source code, as well as the use of source files outside the workspace to store the source code of an object. However, unless a function or operator was defined using an external file, the editor continued to only store the tokenised form in the workspace, in order to save space.

## Current Behaviour

From version 19.0 onwards, the default is that the editor stores source code *as it was typed in by the user* for **all** objects, in addition to the tokenised form. When an object is defined from an external source file using `⎕FIX`, a copy of the source is also retained in the workspace.

In order to maintain backwards compatibility with applications that rely on the canonical representation returned by `⎕CR`, `⎕VR` , `⎕NR`, these functions continue to reconstitute the source from tokens; and `⎕FX` continues to only store the tokenised form. If you wish to access the source as typed, you should use `⎕SRC`, or `60 ⎕ATX`, and you should use `⎕FIX`, to define not only namespaces and classes but functions and operators as well.

When the user opens an object in the Editor, the saved source code is presented if it exists. If the object was defined from a file and the source held in the workspace differs from the contents of the file, the user will be asked to decide whether to use the file or break the link and use the source in the workspace. If no source code is available, it is reconstituted from the internal form.

Note however, that there is no mechanism to reconstitute a script, as a whole, from its tokenised form. If there is no source code, the Namespace or Class appears as if it were created using `⎕NS` rather than having originated from a script. It cannot be opened in the Editor and the result of `⎕SRC` is empty. However, the source code for individual functions and operators within the Namespace or Class will be reconstituted from their individual tokenised code when required.

The functions `⎕SRC` and `62 ⎕ATX` (most precise available source) use the same logic as described above to generate a result.

Source code saved in the workspace is compressed to minimise space usage.

Note that the white space in comment statements is retained in both the compiled form and compiled form of a function.

The Boolean parameter **DYALOG_DISCARD_FN_SOURCE**  (default 0) and `5172⌶` (Discard Source Information) allow the user to enable or disable this feature for functions and operators. The *AutoFormat Functions* option is automatically disabled if the **DYALOG_DISCARD_FN_SOURCE** parameter is 1. Note that the user can format code on demand).

`5171⌶` (Discard Source Information) discards source code and file information for scripted objects, namespaces, classes, functions, and operators that is saved in the workspace.

Note that, to ensure that they can be used by Classic Edition, the source code has been discarded from all the workspaces supplied by Dyalog as part of the distribution.

See also: [Discard Source Code](../language-reference-changes/discard-source-code.md) and [Discard Source Information](../language-reference-changes/discard-source-information.md).
