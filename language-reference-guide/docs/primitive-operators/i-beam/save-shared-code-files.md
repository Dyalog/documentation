
<!-- Hidden search keywords -->
<div style="display: none;">
  8667⌶
</div>

<h1 class="heading"><span class="name">Save Shared Code Files</span> <span class="command">{R}←{X} (8667⌶) Y</span></h1>

**Restriction**: 64-bit Unicode only

This saves a shared code file. For more information on shared code files, see the [_Shared Code Files User Guide_](../../../../files/Shared_Code_Files_User_Guide.pdf).

`Y` is 2-element vector of vectors in which:

- `Y[1]` is the slot identifier (an integer in the range 1-8) for the unique fixed virtual memory address at which to save the shared code file
- `Y[2]` is a character vector of the filename for the shared code file. If a filename extension is not provided, then **.dwx** is used. If a file of this name already exists, or the file cannot be created for any reason, then the operation will fail.

Optionally, `X` is a vector of character vectors or a matrix specifying the names of names of functions, operators and variables to save in the shared code file. If `X` is omitted, all functions, operators, and variables in the active workspace are saved in the shared code file.

<p class="example">Example</p>
```apl
      8667⌶ 1 'scf.dwx' 
```
