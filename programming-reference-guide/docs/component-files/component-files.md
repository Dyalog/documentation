# Component Files

## Overview

A **component file** is a data file maintained by Dyalog APL. It contains a series of APL arrays known as **components** which are accessed by reference to their relative position or **component number** within the file. Component files are just like other data files and there are no special restrictions imposed on names or sizes.

A set of system functions is supplied to perform a range of file operations. These provide facilities to create or delete files, and to read and write components. Facilities are also provided for multi-user access, including the capability to determine who may do what, and file locking for concurrent updates.

## Tying and Untying Files

To access an existing component file it must be **tied**, that is, opened for use. The tie may be **exclusive** (single-user access) or **shared** (multi-user access). A file is **untied**, that is, closed, using `⎕FUNTIE` or on terminating Dyalog APL. File ties survive `)LOAD`, `⎕LOAD` and `)CLEAR` operations.

## Tie Numbers

A file is tied by associating a **file name** with a **tie number**. Tie numbers are integers in the range 1 - 2147483647 and, you can supply one explicitly, or have the interpreter allocate the next available one by specifying 0. The system functions which tie files return the tie number as a "shy" result.

## Creating and Removing Files

A component file is created using `⎕FCREATE` which automatically ties the file for exclusive use. A newly created file is empty, that is, contains 0 components. A file is removed with `⎕FERASE`, although it must be exclusively tied to do so.

## Adding and Removing Components

Components are added to a file using `⎕FAPPEND` and removed using `⎕FDROP`. Component numbers are allocated consecutively starting at 1. Thus a new component added by `⎕FAPPEND` is given a component number which is one greater than that of the last component in the file. Components may be removed from the beginning or end of the file, but not from the middle. Component numbers are therefore contiguous.

## Reading and Writing Components

Components are read using `⎕FREAD` and overwritten using `⎕FREPLACE`. There are no restrictions on the size or type of array which may replace an existing component. Components are accessed by component number.

## Component Information

In addition to the data held in a component, the user ID that wrote it and the time at which it was written is also recorded.

## Multi-User Access

`⎕FSTIE` ties a file for **shared** (that is, multi-user) access. This kind of access would be appropriate for a multi-user UNIX system, a network of single user PCs, or multiple APL tasks under Microsoft Windows.

`⎕FHOLD` provides the means for the user to temporarily prevent other co-operating users from accessing one or more files. This is necessary to allow a single logical update involving more than one component, and perhaps more than one file, to be completed without interference from another user. `⎕FHOLD` is applicable to External Variables as well as Component Files

## File Access Control

There are two levels of file access control. As a regular file, the operating system read/write controls for owner and other users apply. In addition, Dyalog manages its own access controls using the **access matrix**. This is an integer matrix with 3 columns and any number of rows. Column 1 contains user numbers, column 2 an encoding of permitted file operations, and column 3 passnumbers. Each row specifies which file operations may be performed by which user(s) with which passnumber. A value of 0 in column 1 specifies all users. A value of `¯1` in column 2 specifies all file operations. A value of 0 in column 3 specifies no passnumber. If any row of the access matrix contains `(0 ¯1 0)` it specifies that all users may perform all file operations with no passnumber.

### User Number

Under Windows, this is a number which is defined by the **aplnid** parameter.   If you intend to use Dyalog's **access matrix** to control file access in a multi-user environment, it is desirable to allocate to each user, a distinct **user number**. However, if you intend to rely on underlying operating system controls, allocating a user number of 0 (the default installation value) to everyone is more appropriate.  Under non-Windows platforms the User Number is set to be the effective user-id of the APL process and cannot be altered. In both cases, a user number of 0 causes APL to circumvent the access matrix mechanism described below.

## Permission Code

This is an integer representation of a Boolean mask. Each bit in the mask indicates whether or not a particular file operation is permitted as follows:
```other
┌──┬──┬──┬──┬──┬──┬─┬─┬─┬─┬─┬─┬─┬─┬─┐ Bit No.
│15│14│13│12│11│10│9│8│7│6│5│4│3│2│1│
└──┴──┴──┴──┴──┴──┴─┴─┴─┴─┴─┴─┴─┴─┴─┘  File      Access
  ↑  ↑  ↑  ↑  ↑  ↑   ↑   ↑ ↑ ↑ ↑ ↑ ↑   Operation   Code
  │  │  │  │  │  │   │   │ │ │ │ │ │
  │  │  │  │  │  │   │   │ │ │ │ │ └── ⎕FREAD         1
  │  │  │  │  │  │   │   │ │ │ │ └──── ⎕FTIE          2
  │  │  │  │  │  │   │   │ │ │ └────── ⎕FERASE        4
  │  │  │  │  │  │   │   │ │ └──────── ⎕FAPPEND       8
  │  │  │  │  │  │   │   │ └────────── ⎕FREPLACE     16
  │  │  │  │  │  │   │   └──────────── ⎕FDROP        32
  │  │  │  │  │  │   │
  │  │  │  │  │  │   └──────────────── ⎕FRENAME     128
  │  │  │  │  │  │
  │  │  │  │  │  └──────────────────── ⎕FRDCI       512
  │  │  │  │  └─────────────────────── ⎕FRESIZE    1024
  │  │  │  └────────────────────────── ⎕FHOLD      2048
  │  │  └───────────────────────────── ⎕FRDAC      4096
  │  └──────────────────────────────── ⎕FSTAC      8192
  └─────────────────────────────────── ⎕FHIST     16384
```

For example, if bits 1, 4 and 6 are set and all other relevant bits are zero only `⎕FREAD`, `⎕FAPPEND` and `⎕FDROP` are permitted. A convenient way to set up the mask is to sum the access codes associated with each operation.

For example, the value 41 (1+8+32) authorises `⎕FREAD`, `⎕FAPPEND` and `⎕FDROP`. A value of `¯1` (all bits set) permits all operations. Thus by subtracting the access codes of operations to be forbidden, it is possible to permit all but certain types of access. For example, a value of `¯133` (`¯1- 4+128`) permits all operations except `⎕FERASE` and `⎕FRENAME`. Note that the value of unused bits is ignored. Any non-zero permission code allows `⎕FSTIE` and `⎕FSIZE`. `⎕FCREATE`, `⎕FUNTIE`, `⎕FLIB`, `⎕FNAMES` and `⎕FNUMS` are not subject to access control. Passnumbers may also be used to establish different levels of access for the same user.

When the user attempts to tie a file using `⎕FTIE` or `⎕FSTIE` a row of the access matrix is selected to control this and subsequent operations.

If the user is the owner, and the owner's user ID does not appear in the access matrix, the value (`⎕AI[1] ¯1 0`) is conceptually appended to the access matrix. This ensures that the owner has full access rights unless they are explicitly restricted.

The chosen row is the first row in which the value in column 1 of the access matrix matches the user ID and the value in column 3 matches the supplied passnumber which is taken to be zero if omitted.

If there is no match of user ID and passnumber in the access matrix (including implicitly added rows) then no access is granted and the tie fails with a FILE ACCESS ERROR.

Once the applicable row of the access matrix is selected, it is used to verify all subsequent file operations. The passnumber used to tie the file MUST be used for every subsequent operation. Secondly, the appropriate bit in the permission code corresponding to the file operation in question must be set. If either of these conditions is broken, the operation will fail with `FILE ACCESS ERROR`.

If the access matrix is changed while a user has the file tied, the change takes immediate effect. When the user next attempts to access the file, the applicable row in the access matrix will be reselected subject to the supplied passnumber being the same as that used to tie the file. If access with that password is rescinded the operation will fail with `FILE ACCESS ERROR`.

When a file is created using `⎕FCREATE`, the access matrix is empty. At this stage, the owner has full access with passnumber 0, but no access with a non-zero passnumber. Other users have no access permissions. Thus only the owner may initialise the access matrix.

### User 0

If a user has an **aplnid** of 0, the access matrix and supplied passnumbers are ignored. This user is granted full and unrestricted access rights to all component files, subject only to underlying operating system restrictions.

### General File Operations

`⎕FLIB` gives a list of **component files** in a given directory. `⎕FNAMES` and `⎕FNUMS` give a list of the names and tie numbers of tied files. These general operations which apply to more than one file are not subject to access controls.

### Component File System Functions

See *Language Reference* for full details of the syntax of these system functions.

|-------------------------|--------------------------------------------|
|General                                                              ||
|`⎕FAVAIL`                |Report file system availability             |
|File Operations                                                      ||
|`⎕FCREATE`               |Create a file                               |
|`⎕FTIE`                  |Tie an existing file (exclusive)            |
|`⎕FSTIE`                 |Tie an existing file (shared)               |
|`⎕FUNTIE`                |Untie file(s)                               |
|`⎕FCOPY`                 |Copy a file                                 |
|`⎕FERASE`                |Erase a file                                |
|`⎕FRENAME`               |Rename a file                               |
|File information                                                     ||
|`⎕FHIST`                 |Report file events                          |
|`⎕FNUMS`                 |Report tie numbers of tied files            |
|`⎕FNAMES`                |Report names of tied files                  |
|`⎕FLIB`                  |Report names of component files             |
|`⎕FPROPS`                |Report file properties                      |
|`⎕FSIZE`                 |Report size of file                         |
|Writing to the file                                                  ||
|`⎕FAPPEND`               |Append a component to the file              |
|`⎕FREPLACE`              |Replace an existing component               |
|Reading from a file                                                  ||
|`⎕FREAD`                 |Read one or more components                 |
|`⎕FRDCI`                 |Read component information                  |
|Manipulating a file                                                  ||
|`⎕FDROP`                 |Drop a block of components                  |
|`⎕FRESIZE`               |Change file size (forces a compaction)      |
|`⎕FCHK`                  |Check and repair a file                     |
|Access manipulation                                                  ||
|`⎕FSTAC`                 |Set file access matrix                      |
|`⎕FRDAC`                 |Read file access matrix                     |
|Control multi-user access                                            ||
|`⎕FHOLD`                 |Hold file(s) - see later section for details|

### Using the Component File System

Let us suppose that you have written an APL system that builds a personnel database, containing the name, age and place of birth of each employee. Let us assume that you have created a variable `DATA`, which is a nested vector with each element containing a person's name, age and place of birth:
```apl
      DISPLAY 2↑DATA
.→-------------------------------------------------------.
| .→----------------------. .→-------------------------. |
| | .→-------.    .→----. | | .→------.    .→--------. | |
| | |Jonathan| 42 |Wales| | | |Pauline| 21 |Isleworth| | |
| | '--------'    '-----' | | '-------'    '---------' | |
| '∊----------------------' '∊-------------------------' |
'∊-------------------------------------------------------'
```

Then the following APL expressions can be used to access the database:

<h2 class="example">Example 1</h2>

Show record 2
```apl
      DISPLAY 2⊃DATA
.→-------------------------.
| .→------.    .→--------. |
| |Pauline| 21 |Isleworth| |
| '-------'    '---------' |
'∊-------------------------'
```

<h2 class="example">Example 2</h2>

How many people in the database?
```apl
           ⍴DATA
     123
```

<h2 class="example">Example 3</h2>

Update Pauline's age
```apl
           (2 2⊃DATA)←16
```

<h2 class="example">Example 4</h2>

Add a new record to the database
```apl
      DATA ,← ⊂'Maurice' 18 'London'
```

Now let's build a component file to hold our personnel database.

Create a new file, giving the file name, and the number you wish to use to identify it (the file tie number):
```apl
      'COMPFILE' ⎕FCREATE 1
```

If the file already exists, or you have already used this tie number, then APL will respond with the appropriate error message.

Now write the data to the file. We could write a function that loops to do this, but it is neater to take advantage of the fact that our data is a nested vector, and use each (`¨`).
```apl
      DATA ⎕FAPPEND¨ 1
```

Now we'll try our previous examples using this file.

<h2 class="example">Example 1</h2>

Show record 2
```apl
      DISPLAY ⎕FREAD 1 2
.→-------------------------.
| .→------.    .→--------. |
| |Pauline| 21 |Isleworth| |
| '-------'    '---------' |
'∊-------------------------'

```

<h2 class="example">Example 2</h2>

How many people in our database?
```apl
      ⎕FSIZE 1        ⍝ First component, next
1 125 10324 4294967295  ⍝ component, file size,
                        ⍝ maximum file size
```
```apl
      ¯1+2⊃⎕FSIZE 1   ⍝ Number of data items
```

The fourth element of `⎕FSIZE` indicates the file size limit. Dyalog APL does not impose a file size limit, although your operating system may do so, but the concept is retained in order to make this version of Component Files compatible with others.

<h2 class="example">Example 3</h2>

Update Pauline's age
```apl
        REC ← ⎕FREAD 1 2       ⍝ Read second component
        REC[2] ← 18            ⍝ Change age
        REC ⎕FREPLACE 1 2      ⍝ And replace component
```

<h2 class="example">Example 4</h2>

Add a new record
```apl
       ('Janet' 25 'Basingstoke') ⎕FAPPEND 1
```

<h2 class="example">Example 5</h2>

Rename our file
```apl
       'PERSONNEL' ⎕FRENAME 1
```

<h2 class="example">Example 6</h2>

Tie an existing file; give file name and have the interpreter allocate the next available tie number.
```apl
       'SALARIES' ⎕FTIE 0
  2
```

<h2 class="example">Example 7</h2>

Give everyone access to the PERSONNEL file
```apl
       (1 3⍴0 ¯1 0)⎕FSTAC 1
```

<h2 class="example">Example 8</h2>

Set different permissions on `SALARIES`.
```apl
       AM ← 1 3⍴1 ¯1 0    ⍝ Owner ID 1 has full access
       AM⍪← 102 1 0       ⍝ User ID 102 has READ only
       AM⍪← 210 2073 0    ⍝ User ID 210 has
                           ⍝ READ+APPEND+REPLACE+HOLD
```
```apl
       AM ⎕FSTAC 2        ⍝ Store access matrix
```

<h2 class="example">Example 9</h2>

Report on file names and associated numbers
```apl
        ⎕FNAMES,⎕FNUMS
 PERSONNEL  1
 SALARIES   2
```

<h2 class="example">Example 10</h2>

Untie all files
```apl
       ⎕FUNTIE ⎕FNUMS
```
