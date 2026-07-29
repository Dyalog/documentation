# Native Files

## Introduction

Dyalog includes a wide selection of functions that allow reading/writing to files containing text or binary data, as well as the manipulation of the host filesystem, for example, deleting files or creating directories.

The characteristics of host filesystems vary across different platforms and even across devices on the same platform. Different host operating systems provide access to their filesystems in largely incompatible ways. Nevertheless, the native file functions within Dyalog work in broadly the same way across all platforms, which makes it relatively straightforward to create applications which are portable across all Dyalog environments.

## Text Files

Characters within a text file may be encoded in one of a number of different ways, and different host environments tend to have different preferences. Although UTF-8 is increasingly becoming the _de facto_ encoding standard, other encoding formats exist (particularly in legacy environments) and there are still multiple conventions for representing line endings.

Dyalog includes two powerful functions – [`⎕NGET`](../language-reference-guide/system-functions/nget.md) and [`⎕NPUT`](../language-reference-guide/system-functions/nput.md) – which read and write text files to or from character arrays in the workspace. The encoding and line-ending types can be explicitly specified but by default `⎕NGET` will try to deduce the encoding automatically and `⎕NPUT` will use defaults appropriate for the host environment.

The search and replace functions [`⎕S`](../language-reference-guide/system-functions/s.md) and [`⎕R`](../language-reference-guide/system-functions/r.md) can also be used to read and write text files, filtering and modifying the content as they do so.

The simplest text files contain just plain text – variable length lines of text with no formatting such as italics etc. However, formatting or data encoding can be included within a text file using formats such markup (e.g. HTML and XML), character separated values (CSV) or JavaScript Object Notation (JSON). Dyalog includes the functions [`⎕XML`](../language-reference-guide/system-functions/xml.md), [`⎕CSV`](../language-reference-guide/system-functions/csv.md) and [`⎕JSON`](../language-reference-guide/system-functions/json.md) to decode or encode such file content.

## Binary Data Files

Binary data files contain data in application-specific format, and are rarely read or written by anything other than the application which creates them and understands their format. Dyalog provides a number of functions which allow a Dyalog application to manage its own binary data files or binary data files from any source, by allowing them to be read or written as sequences of bytes or words. Regions of binary files can also be locked to coordinate shared access to the files.

Files are tied (opened) using [`⎕NTIE`](../language-reference-guide/system-functions/ntie.md) or created using [`⎕NCREATE`](../language-reference-guide/system-functions/ncreate.md). Both of these functions return a numeric tie number by which the file is subsequently identified when read ([`⎕NREAD`](../language-reference-guide/system-functions/nread.md)), written ([`⎕NAPPEND`](../language-reference-guide/system-functions/nappend.md), [`⎕NREPLACE`](../language-reference-guide/system-functions/nreplace.md)), renamed ([`⎕NRENAME`](../language-reference-guide/system-functions/nrename.md)) locked or unlocked ([`⎕NLOCK`](../language-reference-guide/system-functions/nlock.md)) or (re)sized  ([`⎕NSIZE`](../language-reference-guide/system-functions/nsize.md), [`⎕NRESIZE`](../language-reference-guide/system-functions/nresize.md)). When a file tie is no longer needed it can be untied (closed) using [`⎕NUNTIE`](../language-reference-guide/system-functions/nuntie.md) or closed and the file deleted using [`⎕NERASE`](../language-reference-guide/system-functions/nerase.md). [`⎕NNUMS`](../language-reference-guide/system-functions/nnums.md) and [`⎕NNAMES`](../language-reference-guide/system-functions/nnames.md) report the numbers and names respectively of all currently tied files.

## Filesystem Manipulation

In addition to reading and writing files, an application may typically want to manipulate the filesystem in various ways. A diverse set of functions exist to do this: [`⎕MKDIR`](../language-reference-guide/system-functions/mkdir.md) creates directories, [`⎕NDELETE`](../language-reference-guide/system-functions/ndelete.md) deletes files and/or directories and their contents, [`⎕NMOVE`](../language-reference-guide/system-functions/nmove.md) and [`⎕NCOPY`](../language-reference-guide/system-functions/ncopy.md) move and copy files and/or directories and their contents. [`⎕NINFO`](../language-reference-guide/system-functions/ninfo.md) queries and sets properties such as size or modification date on files and directories, and can also query the contents of directories. [`⎕NEXISTS`](../language-reference-guide/system-functions/nexists.md) will report whether or not a name exists within the file system.

Additionally, `739⌶` can be used to obtain the name of the directory used by the host filesystem for temporary files (generally emptied at startup).

## Progress Callbacks

The native file functions `⎕NCOPY`, `⎕NMOVE`, and `⎕NINFO` support the **ProgressCallback** variant option to enable progress callbacks.

### Overview
If this option is enabled, the system function invokes an APL callback function at several stages as a file operation proceeds, meaning that the results of the system function can be accessed as they become available rather than waiting for them to all be available. A system object is used to communicate between the system function and the callback.

Each file operation has four distinct stages:

1. The start of the operation. The callback is invoked before any directories are scanned or files are processed. This gives the application the opportunity to set parameters that control the frequency of callbacks during the operation itself.
2. The optional scan phase during which the system function enumerates the files that will be involved in the copy or move operation. The file count obtained is used to set the `Limit` field. The application may use this subsequently to indicate the degree of progress.
3. The main processing of the files.
4. The end of the operation.

The callback function is invoked once at the start of the operation, during the (optional) scan and processing stages, and finally once at the end of the operation. During the scan and processing stages, the `Skip` and `Delay` options provide alternative ways to control the frequency with which the function is invoked.

If both options are 0, the callback will be invoked after every file is processed. However, if there are a large number of small files involved, and you simply want to update a progress bar, this may prove to be unnecessarily  frequent, and will increase the total time required to complete the operation.

If you want to update a progress bar regularly (for example every second), the `Delay` option (1000 = 1 second) is the better choice.  In other circumstances, you might choose to use `Skip`.

If you use both options, the callback will be invoked when *both* apply, so if you set `Skip` to 10 and `Delay` to 5000, the callback will be invoked after at least 10 files have been processed and at least 5 seconds have elapsed since the previous invocation of the callback.

The value of the **ProgressCallback** variant option may be:

|---------|------------------------------------------------------------------------------------------------------------------------|
|`fn`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|The name of the callback function.                                                                                      |
|`fn data`|The name of the callback function, and an array or namespace which is to be passed to the callback in its left argument.|

The right argument given to the callback function is a 3-element vector:

|-----|--------|------------------------------------------------------------------------------------------------------------------------|
|`[1]`|Function|Character vector which identifies the function that caused the callback to be executed.                                 |
|`[2]`|Event   |Character vector describing the event that lead to the callback being executed. See below.                              |
|`[3]`|Info    |Reference to a namespace containing information about the event. See below.                                             |

### Event

Event is a character vector which indicates the stage of the copy or move operation.

|---|---|
|`'Start'`|Reported by the first invocation of the callback which occurs before any files are scanned or processed. This may be used to set the parameters that control the operation. See **Options** .|
|`'Scan'`|Indicates that the system function is in the initial phase of scanning the files in order to calculate `Limit`. See **ScanFirst** .|
|`'Progress'`|Indicates that the system function is at the main stage of the operation and is processing the files.|
|`'Done'`|Indicates that all files have been processed.|

Note that there will always be at least 2 invocations of the callback, to indicate the start and end of the operation.

### Info

Info is a reference to a namespace that contains information about the event. This namespace persists for the duration of the execution of the system function and contains the following fields:

|---|---|
|`Progress`|A number between `0` and `Limit`. When the event code is `'Start'`, `Progress` is `0`. Every time a file or directory is processed, `Progress` is increased by 1. Finally when the  event code is `'Done'`, `Progress` will be equal to `Limit`.|
|`Limit`|The maximum value of `Progress`. This value might change during the file operation if it does not do a full discovery first (the `ScanFirst` option is 0), or if the file structure changes between the scan and the file operation.|
|`Last`|A vector of file names which have been processed since the last invocation of the callback function. The user can specify the maximum length of this vector by setting the `LastFileCount` option. The names in this list are the source names rather than the destination names. The `Last` vector is always empty when the event is `'Start'` and it is cleared when going from the `'Scan'` phase to the `'Progress'` phase, to avoid any confusion.|
|`Data`|A field that is reserved for the user to store data which persists between invocations of the callback. It could for example be used to keep a sequence number, to count the number of times the callback had been run.|
|`Options`|This is a namespace which contains the information that controls the future execution of the callback and it is described below.|

### Options

This Namespace contains options that control future invocations of the callback. The options persist between these invocations, so there is no need to set them again unless they should be changed. The fields and their default values are:

|Field|Default|Description|
|---|---|---|
|`ScanFirst`|1|Specifies if the file operation should do a "scan pass" before processing the files. This stage just enumerates  the files to determine how many there are. This will ensure `Limit` has a realistic value when the actual processing of the files happens. The `ScanFirst` field is only inspected right after the first invocation of the callback function, with the event code `'Start'`.|
|`Delay`|0|Specifies the number of milliseconds to wait until the callback will be called again. If all file operations finish before this time, the callback function is called anyway, with the event code `'Done'`. If a slow file operation is happening (such as copying a big file), the actual delay before the callback is invoked might be longer than the value of `Delay`.|
|`Skip`|0|Specifies a number of files to skip between invocations of the callback function. If you are only interested in getting a callback for each tenth file, you should set this option to 9, for example.|
|`LastFileCount`|1|An integer, specifying the maximum number of the latest filenames to be stored in the `Last` field. The default is to only store the last file processed, but if `Delay` or `Skip` are non-zero, multiple files could have been processed between calls to the callback function. A value of 5 for example, will make sure that the five last files processed before calling the callback, will have their names in the `Last` field. The `Last` field might have fewer elements than `LastFileCount`, if the number of files processed since the last call is less than `LastFileCount`. The value `¯1` indicates that the `Last` field should contain **all** the last files since the last call (no limit).|

The result of the callback function is a Boolean scalar indicating whether the system function should continue or stop:

1: Execution should continue.

0: Execution should stop. In this case, an `INTERRUPT` (event 1003) is signalled.
