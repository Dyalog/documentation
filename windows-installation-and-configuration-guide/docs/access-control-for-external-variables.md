<h1 class="heading"><span class="name">Access Control for External Variables</span></h1>

External variables may be EXCLUSIVE or SHARED. An exclusive variable can only be accessed by the owner of the file. If you are on a Local Area Network (LAN) a shared external variable may be accessed (concurrently) by other users. The exclusive or shared status of an external variable is set by the `XVAR` function in the UTIL workspace.

Access to an external variable is faster if it has exclusive status than if it is shared. This is because if several users are accessing the file data must always be read and written directly to disk. If it has exclusive status, the system uses buffering and avoids disk accesses where possible.

!!! Info "Information"
    Support for external variables has been deprecated, and is scheduled for removal in a future release. For information on how to identify calls to external variables in your existing codebase, see the [Release Notes](../release-notes/announcements/deprecated-functionality.md).
