<h1 class="heading"><span class="name">Clear Workspace</span> <span class="command">)CLEAR</span></h1>

This command clears the active workspace and gives the report "`clear ws"`. The active workspace is lost. The name of a clear workspace is `CLEAR WS`. [System Variables](../../system-functions/system-functions-by-category/#system-variables) are initialised with their default values.

In GUI implementations of Dyalog, `)CLEAR` expunges all GUI objects, discards any unprocessed events in the event queue and resets the properties of the `Root` object `'.'` to their default values.

Apart from .NET objects, the contents of the session namespace `⎕SE` are not affected. .NET objects in `⎕SE` are disconnected from .NET because `)CLEAR` closes the current .NET AppDomain.
