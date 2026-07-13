# Auxiliary Processors

Auxiliary Processors (APs) are non-APL programs which provide Dyalog APL users with additional facilities.  They run as separate tasks, and communicate with the Dyalog APL interpreter through pipes (UNIX) or via an area of memory (Windows).  Typically, APs are used where speed of execution is critical, such as in screen management software, or for utility libraries.  Auxiliary Processors may be written in any compiled language, although 'C' is preferred and is directly supported.

When an Auxiliary Processor is invoked from Dyalog APL, one or more *external functions* are fixed in the active workspace.  Each external function behaves as if it was a locked defined function, but is in effect an entry point into the Auxiliary Processor.  An external function occupies only a negligible amount of workspace.

Although Auxiliary Processors are still supported, Dyalog recommends that DLLs/shared libraries, called via the `⎕NA` interface should be used on all platforms in future, and that existing APs are converted to DLLs/shared libraries.
