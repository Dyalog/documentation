<h1 class="heading"><span class="name">LoadEnd</span> <span class="command">Event 836</span></h1>

|-----------|--------------------------------------------------------------|
|Applies To:|[HTMLRenderer](https://help.dyalog.com/19.0/index.htm#GUI/Objects/HTMLRenderer.htm)|

**Description**

A LoadEnd event is raised when a particular frame has finished loading. Multiple frames may be loading at the same time. Sub-frames may start or continue to load even after the main frame has finished loading.

A common technique is to wait for the main frame to finish loading before further interaction with the HTMLRenderer instance. In this case, you should set up an event handler on the LoadEnd event and check the 4th element which indicates if the loaded frame is the main frame.

You may use the [IsLoading](./isloading.md) property to check if the HTMLRenderer is still loading.

The event message reported as the result of [`⎕DQ`](https://help.dyalog.com/19.0/index.htm#Language/System%20Functions/dq.htm), or supplied as the right argument to your callback function, is a 5-element vector as follows :

|-----|------|------------------------------------------------------|
|`[1]`|Object|ref or character vector                               |
|`[2]`|Event |`'LoadEnd'` or 836                                    |
|`[3]`|url   |The URL of the loaded frame                           |
|`[4]`|Flag  |1 if the loaded frame is the "main" frame, 0 otherwise|
|`[5]`|Code  |The HTTP status code as a result of loading the frame |
