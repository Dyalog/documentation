# Internal Structure

If you are going to make a lot of use of APL files in your systems, it is useful for you to have a rough idea of how Dyalog APL organises and manages the disk area used by such files.

The internal structure of external variables and component files is the same, and the examples given below apply to both.

Consider a component file with 3 components:
```apl
        'TEMP' ⎕FCREATE 1
        'One' 'Two' 'Three' ⎕FAPPEND¨1
```

Dyalog APL will write these components onto contiguous areas of disk:
```apl
.-.   .-.   .-.
|1|   |2|   |3|
.-----.-----.-------.
| One | Two | Three |
--------------------.
```

Replace the second component with something the same size:
```apl
        'Six' ⎕FREPLACE 1 2
```

This will fit into the area currently used by component 2.
```apl
.-.   .-.   .-.
|1|   |2|   |3|
.-----.-----.-------.
| One | Six | Three |
--------------------.
```

If your system uses fixed length records, then the size of your components never change, and the internal structure of the file remains static.

However, suppose we start replacing larger data objects:
```apl
        'Bigger One' ⎕FREPLACE 1 1
```

This will not fit into the area currently assigned to component 1, so it is appended to the end of the file. Dyalog APL maintains internal tables which contain the location of each component; hence, even though the components may not be physically stored in order, they can always be accessed in order.
```apl
      .-.   .-.     .-.
      |2|   |3|     |1|
.-----.-----.-------.------------.
|⎕⎕⎕⎕⎕| Six | Three | Bigger One |
---------------------------------.
```

The area that was occupied by component 1 now becomes free.

Now we'll replace component 3 with something bigger:
```apl
        'BigThree' ⎕FREPLACE 1 3
```

Component 3 is appended to the end of the file, and the area that was used before becomes free:
```apl
      .-.                .-.          .-.
      |2|                |1|          |3|
.-----.------------------.------------.----------.
|⎕⎕⎕⎕⎕| Six |⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕| Bigger One | BigThree |
-------------------------------------------------.
```

Dyalog APL keeps tables of the size and location of the free areas, as well as the actual location of your data. Now we'll replace component 2 with something bigger:
```apl
        'BigTwo' ⎕FREPLACE 1 2
```

Free areas are used whenever possible, and contiguous holes are amalgamated.
```apl
            .-.          .-.          .-.
            |2|          |1|          |3|
.-----------.------------.------------.----------.
|⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕|BigTwo|⎕⎕⎕⎕⎕| Bigger One | BigThree |
-------------------------------------------------.
```

You can see that if you are continually updating your file with larger data objects, then the file structure can become fragmented. At any one time, the disk area occupied by your file will be greater than the area necessary to hold your data. However, free areas are constantly being reused, so that the amount of unused space in the file will seldom exceed 30%.

Whenever you issue a monadic `⎕FRESIZE` command on a component file, Dyalog APL COMPACTS the file; that is, it restructures it by reordering the components and by amalgamating the free areas at the end of the file. It then truncates the file and releases the disk space back to the operating system (note that some versions of UNIX do not allow the space to be released). For a large file with many components, this process may take a significant time.

## Error Conditions
```apl
FILE SYSTEM NOT AVAILABLE
```

A `FILE SYSTEM NOT AVAILABLE` (Error code 28) error will be generated if the operating system returns an unexpected error when attempting to get a lock on a component file. In Windows environments this may indicate that *opportunistic locks* (aka *oplocks*) are in use; they should be disabled if Dyalog components files are being used.
```apl
FILE SYSTEM TIES USED UP
```

A `FILE SYSTEM TIES USED UP` (Error code 30) error will be generated when an attempt is made to open more component files than is possible.
```apl
FILE TIED 
```

A `FILE TIED` error is reported if you attempt to tie a file which another user has exclusively tied.

## Limitations

### File Tie Quota

The File Tie Quota is the maximum number of files that a user may tie concurrently. Dyalog APL itself allows a maximum of 1024 under UNIX and 512 under Windows, although in either case your installation may impose a lower limit. When an attempt is made to exceed this limit, the report `FILE TIE QUOTA` (Error code 31) is given. This error will also be generated if an attempt is made to exceed the maximum number of open files that is imposed by the operating system.

### File Name Quota

Dyalog APL records the names of each user's tied files in a buffer of 40960 bytes. When this buffer is full, the report `FILE NAME QUOTA USED UP` (Error code 32) will be given. This is only likely to occur if long pathnames are used to identify files.
