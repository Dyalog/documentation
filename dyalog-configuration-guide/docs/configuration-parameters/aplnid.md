# aplnid

Under Windows, this parameter specifies the *user number* that is used by the component file system to control file sharing and security. If you wish to share component files and/or external variables in a network it is essential that each user has a unique **aplnid** parameter. It may be any integer in the range 0 to 65535. Note that an **aplnid** value of 0 causes the user to bypass APL's access control matrix mechanism.

Under UNIX, the *user number* is obtained from the Operating System (UID) and **aplnid** is not used. If the user is "root", APL's access control mechanism is ignored.

When a user creates a component file, his *user number* is recorded in the file to identify him as its owner.
