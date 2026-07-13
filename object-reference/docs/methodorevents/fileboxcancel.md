# <span>FileBoxCancel</span> <span>Event 72</span>



**Applies To:** [BrowseBox](../objects/browsebox.md), [FileBox](../objects/filebox.md)

**Description**


If enabled, this event is reported when a [FileBox](../objects/filebox.md) is closed because the user has pressed the "Cancel" button or closed it.


The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 3-element vector as follows :


|-----|---------|-----------------------------------------------------------------------------------|
|`[1]`|Object   |ref or character vector                                                            |
|`[2]`|Event    |`'FileBoxCancel'` or 72                                                            |
|`[3]`|File name|character vector containing the name of the currently selected file (empty if none)|



