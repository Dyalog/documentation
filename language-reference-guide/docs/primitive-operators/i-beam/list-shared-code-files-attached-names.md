
<!-- Hidden search keywords -->
<div style="display: none;">
  8659⌶
</div>

<h1 class="heading"><span class="name">List Shared Code Files/Attached Names</span> <span class="command">{R}←{X} (8659⌶) Y</span></h1>

**Restriction**: 64-bit Unicode only

The value of `Y` specifies whether this returns a list of the shared code files that are attached to the current workspace or the names in a specific shared code file. For more information on shared code files, see the [_Shared Code Files User Guide_](../../../../files/Shared_Code_Files_User_Guide.pdf).

**List shared code files**

Y` is `⍬`

`X` is ignored.

`R` is a 2-column matrix listing the shared code files that are attached to the current workspace:

- `[;1]` is the slot identifier for the fixed virtual memory address of the shared code file.
- `[;2]` is the name (including the filename extension) of the shared code file that was loaded.

The rows of the matrix (one row for each shared code file) are ordered to correspond to the order in which the shared code files were specified when they were originally attached, that is, in the right argument to `8666⌶` (see ADD XREF).

**List attached names**

`Y` is an integer vector that would be a valid right argument to `⎕NL`; it identifies the nameclasses and subclasses for which the names should be listed.

`X` is the slot identifier (an integer in the range 1-8) for the unique fixed virtual memory address of the shared code file.

`R` lists the names in the shared code file identified by slot. If any element of `Y` is negative, then positive values in `Y` are treated as if they were negative and `R` is a vector of character vectors. Otherwise, `R` is a simple character matrix. 
