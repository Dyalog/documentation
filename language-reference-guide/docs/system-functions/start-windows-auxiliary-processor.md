---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CMD CMD
</div>






<h1 class="heading"><span class="name">Start Windows Auxiliary Processor</span> <span class="command">{R}←X ⎕CMD Y</span></h1>



Used dyadically, `⎕CMD` starts an Auxiliary Processor.  The effect, as far as the APL workspace is concerned, is identical under both Windows and UNIX, although the method of implementation differs.  `⎕CMD` is a synonym of `⎕SH`.  Either function may be used in either environment (Windows or UNIX) with exactly the same effect.  `⎕CMD` is probably more natural for the Windows user.  This section describes the behaviour of `⎕CMD` and `⎕SH` under Windows.  See ["Examples"](start-unix-auxiliary-processor.md) for a discussion of the behaviour of these system functions under UNIX.


`X` must be a simple character vector containing the name (or pathname) of a Dyalog APL Auxiliary Processor (AP). Although it is possible for users to create their own APs, Dyalog recommends that user write their own DLLs/shared libraries instead.


`Y` may be a simple character scalar or vector, or a vector of character vectors.  Under Windows the contents of `Y` are ignored.


`⎕CMD` loads the Auxiliary Processor into memory.  If no other APs are currently running, `⎕CMD` also allocates an area of memory for communication between APL and its APs.


The shy result `R` is the process id of the Auxiliary Processor task.



The effect of starting an AP is that one or more **external functions** are defined in the workspace.  These appear as locked functions and may be used in exactly the same way as regular defined functions.


When an external function is used in an expression, the argument(s) (if any) are passed to the AP for processing via the communications area described above.  APL halts whilst the AP is processing, and waits for a result.  Under Windows, unlike under UNIX, it is not possible for external functions to run in parallel with APL.


Although it is still possible for users to create their own APs, Dyalog strongly recommends creating shared libraries/DLLs instead.


