<h1 class="heading"><span class="name">Benefits Offered by Shared Code Files</span></h1>

Many large applications are currently forced to load more code than is necessary because it is difficult to predict precisely what code will be used. The main benefit of shared code files is that applications only load code and data on demand.

## Benefit 1

__Significantly reduced start-up times for applications__

Similarly, computational sub-processses (such as isolates) can be launched in a fraction of the time that would otherwise be required.

## Benefit 2

__Reduced workspace usage__

Workspace size can be reduced or more space can be used to execute code more efficiently. A shared code file is materialised one page at a time, as memory is referenced. This means that the contents of comments, which are typically in a separate part of the file from the actual code lines, are usually only read from file if the code is edited. Similarly, running a compiled function is unlikely to require loading the source of the function into virtual memory.

## Benefit 3

__Reduced file I/O and memory consumption__

This is most apparent on machines that run several processes using the same code and is due to the sharing of memory‑mapped files.

## Benefit 4

__More efficient application execution__

Objects residing in a shared code file remain outside the dynamic portion of the workspace unless they are modified. In some applications, this means that the complexity of the active workspace is significantly reduced. As a result, memory allocations are generally cheaper and less memory needs to be inspected and moved around when compactions occur.
