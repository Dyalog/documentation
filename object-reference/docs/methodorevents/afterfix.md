---
search:
  exclude: true
---

# <span>AfterFix</span> <span>Event 822</span>

**Description**

If enabled, this event is reported immediately after the Editor has successfully fixed a new object, or a new version of an object, in the workspace.

You may not nullify or modify the event with a 0-returning callback, nor may you generate the event using `⎕NQ`, or call it as a method. However, returning 0 from a callback will cause the Edit window to remain open if the user action was Fix and Exit (EP).

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 7-element vector as follows :

|-----|---------|-----------------------------------------------------------------------------------------------------------------|
|`[1]`|Object   |ref to the Editor object                                                                                         |
|`[2]`|Event    |`'AfterFix'` or 822                                                                                              |
|`[3]`|Contents |the contents of the Edit window, as a vector of character vectors                                                |
|`[4]`|Space    |ref to the namespace in which the object will be fixed                                                           |
|`[5]`|Old Name |a character vector containing the original name of the object when it was opened by the Editor                   |
|`[6]`|New Name |a character vector containing the  name of the object which was fixed. This is empty if the object is a variable.|
|`[7]`|File Name|a character vector containing the name of the file (if any) associated with the object.                          |

**Application**

Objects: [Editor](../../../windows-ui-guide/the-session-object/session-object)
