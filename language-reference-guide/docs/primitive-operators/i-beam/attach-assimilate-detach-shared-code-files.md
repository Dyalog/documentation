
<!-- Hidden search keywords -->
<div style="display: none;">
  8666⌶
</div>


<h1 class="heading"><span class="name">Attach/Assimilate/Detach Shared Code Files</span> <span class="command">{R}←{X} (8666⌶) Y</span></h1>

**Restriction**: 64-bit Unicode only

The value of `Y` specifies whether this attaches, assimilates, or detaches shared code files. For more information on shared code files, see the [_Shared Code Files User Guide_](../../../../files/Shared_Code_Files_User_Guide.pdf).

**Attach Shared Code Files**

`Y` is a vector of character vectors of shared code files to load, or a single character vector (a character scalar is not acceptable). If filename extensions are not provided, then **.dwx** is used. The path can be absolute or relative to current location; there is no sensitivity to `WSPATH`.

Optionally, `X` is a list of nameclass identifiers to be brought over (cannot include sub-classes). The default is `2 3 4 9` (variables, functions, operators, and namespaces respectively).

The effect of attaching shared code files is analogous to performing a [`)PCOPY`](../../system-commands/pcopy.md) from the shared code files, that is:

- names that already have a definition are preserved unaltered; if the same name appears in more than one shared code file, then the files are searched in the specified order and the first occurrence of the name is used.
- names in attached files immediately affect the results of system functions that provide metadata, such as `⎕NL` or `⎕NC`.

If any shared code files are already attached, then they are detached from the active workspace before new shared code files are attached. Multiple shared code files cannot be attached using separate calls to `8666⌶`.

**Assimilate Shared Code Files**

`Y` is `⎕NULL`.

All referenced objects in the shared code files are copied into the active workspace. The active workspace then contains all the code and data that was visible to it when the shared code files were attached; it can then be saved and used independently of the shared code files. The shared code files that are attached to the active workspace are then disconnected from the active workspace.

Significant space might be required to assimilate all the code in the shared code files into the active workspace. If a `WSFULL` error occurs then the operation will fail; it cannot be rolled back, and leaves the workspace in an indeterminate (but consistent) state. In this situation, the shared code files are not disconnected from the active workspace as doing so could result in further errors.

Only things that are the current referent are copied. The process is driven from the data not the name; this means that if multiple shared code files that include the same names are attached, then only the first of these names is external and that is the one that gets copied.

**Detach Shared Code Files**

`Y` is `0⍴⊂''`, that is, a zero-length list of names.

Any existing attached shared code files are detached.

Detaching shared code files results in data being copied from the shared code files as needed. However, namespaces are always copied when a shared code file is first attached.

Before a shared code file is disconnected from the active workspace:

- if a name that was brought into the active workspace when the shared code file was attached has not had its associated code/data changed, then the name is expunged from the active workspace.
- if a name in the active workspace embeds references to objects residing in a shared code file, then the entire definitions of the referenced objects are copied (assimilated) into the active workspace. This includes (for example), tacit functions that are derived from functions in a shared code file and arrays that contain references to data in a shared code file. These objects must still be functional following the disconnect.

As shared code files are read-only, they cannot be updated while they are in use. Instead, if a shared code file needs to be updated, it must be rebuilt. When a new version of a shared code file becomes available, anyone using the old version should detach it and attach the new one instead as soon as is practical.
