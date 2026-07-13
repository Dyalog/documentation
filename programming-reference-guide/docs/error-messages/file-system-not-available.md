




# <span>FILE SYSTEM NOT AVAILABLE</span> `28`



This error is generated if the operation system generates an unexpected error when attempting to get a lock on a component file.  See Dyalog Programming Reference Guide: Component Files for details.


This error has been seen  in Windows environments which have *opportunistic locks* (aka *oplocks*) enabled, either on the server that is running Dyalog APL, or on a server which has access to the same shared drives, or the disk array which contains the shared drives. In this scenario this error is not seen consistently, but rather is interspersed with other file-related errors. Oplocks should be disabled in environments where shared component files are used.


This error has also been seen when attempting to use component files on NFS mounted filesystems when the NFS lock daemon is not working properly: in this state component file operations may just hang (but can be interrupted) rather than this error being generated.



