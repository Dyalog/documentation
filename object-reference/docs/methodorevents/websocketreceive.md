# <span>WebSocketReceive</span> <span>Event 842</span>



**Applies To:** [HTMLRenderer](../objects/htmlrenderer.md)

**Description**


This event is triggered when data is received over a WebSocket. This event is reported for information only. The result (if any) of a callback function will be ignored.


Note that the WebSocket protocol provides for the possibility for the data to be sent in chunks, causing a succession of WebSocketReceive events. The FIN bit of the last chunk will be 1. The CEF does not currently implement "chunking", so FIN will always be 1.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 6-element vector as follows:


|-----|--------|-------------------------------------------------------------------------------|
|`[1]`|Object  |ref or character vector                                                        |
|`[2]`|Event   |`'WebSocketReceive'` or 842                                                    |
|`[3]`|ID      |Character vector containing the ID of the WebSocket                            |
|`[4]`|Data    |Character or integer vector.                                                   |
|`[5]`|FIN     |Boolean. 1 indicates that this is the last chunk; 0 that there is more to come.|
|`[6]`|Datatype|1 = character, 2 - numeric values in the range ¯128 to 127.                    |

<h2 class="example">Example</h2>
```apl
┌→────────────────────────────────────────────────────────────┐
│      ┌→───────────────┐ ┌→──────────────┐ ┌→──────────┐     │
│ #.hr │WebSocketReceive│ │5d61d8330065608│ │Hello World│ 1 1 │
│      └────────────────┘ └───────────────┘ └───────────┘     │
└∊────────────────────────────────────────────────────────────┘
```



