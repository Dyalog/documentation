# <span>DeleteTypeLib</span> <span>Method 521</span>

**Description**

The DeleteTypeLib method removes a loaded Type Library from the workspace.

The argument to DeleteTypeLib is as follows:

|-----|-------|----------------|
|`[1]`|TypeLib|character vector|

The Type Library may be identified by its name or by its class id.

The result is 0, 1 or `¯1`.

If successful, the specified Type Library, and all dependent Type Libraries not referenced by any other currently loaded Type Libraries, are removed from the active workspace. The result is 1.

If the specified Type Library is in use, no action is taken and the result is 0.

If the argument is not the name or CLSID of a loaded Type Library, no action is taken and the result is `¯1`.

**Application**

Objects: [Root](../objects/root.md)
