# <span>LoadEnd</span> <span>Event 836</span>

**Description**

A LoadEnd event is raised when a particular frame has finished loading. Multiple frames may be loading at the same time. Sub-frames may start or continue to load even after the main frame has finished loading.

A common technique is to wait for the main frame to finish loading before further interaction with the HTMLRenderer instance. In this case, you should set up an event handler on the LoadEnd event and check the 4th element which indicates if the loaded frame is the main frame.

You may use the [IsLoading](../properties/isloading.md) property to check if the HTMLRenderer is still loading.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 5-element vector as follows :

|-----|------|------------------------------------------------------|
|`[1]`|Object|ref or character vector                               |
|`[2]`|Event |`'LoadEnd'` or 836                                    |
|`[3]`|url   |The URL of the loaded frame                           |
|`[4]`|Flag  |1 if the loaded frame is the "main" frame, 0 otherwise|
|`[5]`|Code  |The HTTP status code as a result of loading the frame |

**Application**

Objects: [HTMLRenderer](../objects/htmlrenderer.md)
