# Disposing of .NET Objects

.NET objects are managed by the .NET Common Language Runtime (CLR). The CLR allocates memory for an object when it is created, and deallocates this memory when it is no longer required.

When the (last) reference from Dyalog to a .NET object is expunged by `⎕EX` or by localisation, the system marks the object as unused, leaving it to the CLR to deallocate the memory that it had previously allocated to it (when appropriate – even though Dyalog has dereferenced the APL name, the object could potentially still be referenced by another .NET class).

Deallocated memory might not be reused immediately and might never be reused,  depending on the algorithms used by the CLR garbage disposal.

Furthermore, a .NET object can allocate unmanaged resources (such as window handles) which are not automatically released by the CLR.

To allow the programmer to control the freeing of resources associated with .NET objects in a standard way, many objects implement the IDisposable interface which provides a Dispose() method. The C# language provides a `using` control structure that automates the freeing of resources. Crucially, it does so irrespective of how the flow of execution exits the control structure, even as a result of error handling. This obviates the need for the programmer to call Dispose() explicitly wherever it may be required.

This programming convenience is provide in Dyalog by the `:Disposable ... :EndDisposable` control structure. For more information on this control structure, see the Dyalog Programming Reference Guide.
