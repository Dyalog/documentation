<h1 class="heading"><span class="name">File permissions and <span class="command">⎕FSTAC</span></span></h1>

Dyalog APL is a well behaved UNIX program and honours all standard UNIX file permissions. Commands such as `⎕FLIB` and `)LIB` read the magic number (the first few bytes) of each file in the directory in order to determine whether each file is a component file or workspace respectively; if the APL process cannot read those bytes, then it will assume that the file is not a component file or workspace.

Under UNIX, the first element of `⎕AI` is the user's effective uid, and `⎕AN` reports the user's real name, as it appears in /etc/passwd. When a component file is newly created, its UNIX file permissions will be defined by the umask for the effective user id. The APL file access matrix will be `(0 3⍴0)`, which means that even if the user's UNIX file permissions are such that anyone can read and write to the file, only the user in question will be able to access the file using Dyalog APL component file system functions. To allow any user to access the file (assuming that the UNIX file permissions are suitable) then run
```apl
      (1 3⍴0 ¯1 0)⎕FSTAC tieno
```

Any user with an effective uid 0 will be able to access any component file, irrespective of the file access matrix.
