# <span>WebSocketError</span> <span>Event 844</span>



**Applies To:** [HTMLRenderer](../objects/htmlrenderer.md)

**Description**


This event is triggered an error occurs on the WebSocket.  It is for notification only.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows:


|-----|-------|---------------------------------------------------|
|`[1]`|Object |ref or character vector                            |
|`[2]`|Event  |`'WebSocketError'` or 844                          |
|`[3]`|ID     |Character vector containing the ID of the WebSocket|
|`[4]`|Message|The error message (character vector)               |



