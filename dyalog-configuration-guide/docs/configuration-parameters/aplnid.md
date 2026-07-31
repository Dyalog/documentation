# aplnid

The *user number* used by the component file system to control file sharing and security. When a user creates a component file, their user number is recorded in the file to identify them as its owner.

Valid values, and how the user number is obtained, depend on the operating system:

- Microsoft Windows: **aplnid** is an integer from `0` to `65535`. To share component files or external variables across a network, each user must have a unique **aplnid**. A value of `0` causes the user to bypass APL's access-control-matrix mechanism.
- UNIX and macOS: the user number is obtained from the operating system (UID) and **aplnid** is not used. If the user is `root`, APL's access-control mechanism is ignored.

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->
