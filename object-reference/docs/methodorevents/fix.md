---
search:
  exclude: true
---

# <span>Fix</span> <span>Event 820</span>

**Description**

If enabled, this event is reported when the user attempts to fix an object from the Editor window. It is reported immediately, before the user's action is processed in any way by the Editor.

The default action is to check whether the object has changed. If not, no further action takes place. If the object has changed, the system validates the contents of the Edit window, and either displays an error dialog or fixes a new version of the object in the workspace. If the user action was to fix and exit (EP), the Edit window is closed unless the validation failed.

If the callback function returns 0, the default action is  aborted in its entirety (not even the validation takes place) and the Edit window remains open.

You may not generate the event using `⎕NQ`, or call it as a method.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 7-element vector as follows :

|-----|---------|-----------------------------------------------------------------------------------------------------|
|`[1]`|Object   |ref to the Editor object                                                                             |
|`[2]`|Event    |`'Fix'` or 820                                                                                       |
|`[3]`|Contents |the contents of the Edit window, as a vector of character vectors                                    |
|`[4]`|Space    |ref to the namespace in which the object will be fixed                                               |
|`[5]`|Old Name |a character vector containing the original name of the object when it was opened by the Editor       |
|`[6]`|New Name |a character vector containing the  new name of the object. This is empty if the object is a variable.|
|`[7]`|File Name|a character vector containing the name of the file (if any) associated with the object.              |

For objects whose names are part of the content of the Edit window, this event is not reported if the name is missing or invalid. Instead the system will display an error dialog box.

**Application**

Objects: [Editor](../../../windows-ui-guide/the-session-object/session-object)
