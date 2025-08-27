<h1 class="heading"><span class="name">Extension to Native File Functions</span></h1>

`⎕NMOVE` and `⎕NCOPY` now provide a feature to run an APL function as a callback during processing. This is implemented by the ProgressCallback Variant option.

## ProgressCallback Option

## Overview

If this option is enabled, the system function invokes an APL callback function as the file operation (move or copy) proceeds. A system object is used to communicate between the system function and the callback. The file operation has 4 distinct stages:

1. The start of the operation. The callback is invoked before any files are scanned or processed. This gives the application the opportunity to set parameters that control the frequency of callbacks during the operation itself.
2. The optional scan phase during which the system function enumerates the files that will be involved in the copy or move operation. The file count obtained is used to set the `Limit` field. The application may use this subsequently to indicate the degree of progress.
3. The main processing (move or copy) of the files.
4. The end of the operation.

The callback function is invoked once at the start of the operation, during the (optional) scan and processing stages, and finally once at the end of the operation. During the scan and processing stages, the `Skip` and `Delay` options provide alternative ways to control the frequency with which the callback is invoked.

If both options are 0, the callback will be invoked after every file is processed. However, if there are a large number of small files involved, and you simply want to update a progress bar, this may prove to be unnecessarily  frequent, and will increase the total time required to complete the operation.

If you want to update a progress bar regularly (for example every second), the `Delay` option (1000 = 1 second) is the better choice.  In other circumstances, you might choose to use `Skip`.

If you use both options, the callback will be invoked when *both* apply, so if you set `Skip` to 10 and `Delay` to 5000, the callback will be invoked after at least 10 files have been processed and at least 5 seconds have elapsed since the previous invocation of the callback.

The value of the ProgressCallback variant option may be:

|---------|------------------------------------------------------------------------------------------------------------------------|
|`fn`     |The name of the callback function.                                                                                      |
|`fn data`|The name of the callback function, and an array or namespace which is to be passed to the callback in its left argument.|

The right argument given to the callback function is a 3-element vector:

|-----|--------|------------------------------------------------------------------------------------------------------------------------|
|`[1]`|Function|Character vector which identifies the function that caused the callback to be executed; either `'⎕NCOPY'` or `'⎕NMOVE'.`|
|`[2]`|Event   |Character vector describing the event that lead to the callback being executed. See below.                              |
|`[3]`|Info    |Reference to a namespace containing information about the event. See below.                                             |

## Event

Event is a character vector which indicates the stage of the copy or move operation..

|---|---|
|`'Start'`|Reported by the first invocation of the callback which occurs before any files are scanned or processed. This may be used to set the parameters that control the operation. See **Options** .|
|`'Scan'`|Indicates that the system function is in the initial phase of scanning the files in order to calculate `Limit` . See **ScanFirst** .|
|`'Progress'`|Indicates that the system function is at the main stage of the operation and is moving or copying the files.|
|`'Done'`|Indicates that all files have been processed.|

Note that there will always be at least 2 invocations of the callback, to indicate the start and end of the operation.

## Info

Info is a ref to a namespace that contains information about the event. This namespace persists for the duration of the execution of the system function and contains the following fields:

|---|---|
|`Progress`|A number between `0` and `Limit` . When the event code is `'Start'` , `Progress` is `0` . Every time a file or directory is processed, `Progress` is increased by 1. Finally when the  event code is `'Done'` , `Progress` will be equal to `Limit` .|
|`Limit`|The maximum value of `Progress` . This value might change during the file operation if it doesn't do a full discovery first (the `ScanFirst` option is 0), or if the file structure changes between the scan and the copy/move.|
|`Last`|A vector of file names which have been processed since the last invocation of the callback function. The user can specify the maximum length of this vector by setting the `LastFileCount` option. The names in this list are the source names, and not the destination names. The `Last` vector is always empty when the event is `'Start'` , and it is cleared when going from the `'Scan'` phase to the `'Progress'` phase, to avoid any confusion.|
|`Data`|A field that is reserved for the user to store data which persists between invocations of the callback. It could for example be used to keep a sequence number, to count the number of times the callback had been run.|
|`Options`|This is a namespace which contains the information that controls the future execution of the callback. The options persist between the calls to the callback, so there is no need to set them again unless they should be changed. The fields and their default values are described below.|

## Options

This is a namespace which contains options that control future invocations of the callback. The options persist between these invocations, so there is no need to set them again unless they should be changed. The fields and their default values are:

|Field|Default|Description|
|---|---|---|
|`ScanFirst`|1|Specifies if the file operation should do a "scan pass" before moving/copying the files. This stage just enumerates  the files to determine how many there are. This will ensure `Limit` has a realistic value when the actual processing of the files happens. The overhead is small in comparision with the time it takes to process the files. The `ScanFirst` field is only inspected right after the first invocation of the callback function, with the event code `'Start'` .|
|`Delay`|0|Specifies the number of milliseconds to wait, until the callback will be called again. If all file operations finish before this time, the callback function is called anyway, with the event code `'Done'` . If a slow file operation is happening (such as copying a big file), the actual delay before the callback is invoked might be longer than the value of `Delay` .|
|`Skip`|0|Specifies a number of files to skip between invocations of the callback function. If you are only interested in getting a callback for each 10th file, you should set this option to 9 for example.|
|`LastFileCount`|1|An integer, specifying the maximum number of the latest filenames to be stored in the `Last` field. The default is to only store the last file processed, but if `Delay` or `Skip` are non-zero, multiple files could have been processed between calls to the callback function. A value of 5 for example, will make sure that the 5 last files processed before calling the callback, will have their names in the `Last` field. The `Last` field might have fewer elements than `LastFileCount` , if the number of files processed since the last call is less than `LastFileCount` . The special value `¯1` indicates that the `Last` field should contain **all** the last files since the last call (no limit).|

The result of the callback function must be a Boolean scalar, indicating whether or not the `⎕NCOPY` or `⎕NMOVE` should continue or stop.

1: Execution should continue.

0: Execution should stop. In this case, an `INTERRUPT` (event 1003) is signalled.
