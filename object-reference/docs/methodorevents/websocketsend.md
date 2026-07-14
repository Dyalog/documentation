# <span>WebSocketSend</span> <span>Method 847</span>

**Applies To:** [HTMLRenderer](../objects/htmlrenderer.md)

**Description**

This method is used to send data to a WebSocket. The argument to WebSocketSend is a 2, 3 or 4-element vector as follows:

|-----|------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|`[1]`|ID    |Character vector containing the ID of the WebSocket                                                                                                |
|`[2]`|Data  |Character or integer vector. Integers must be in the range ¯128 to 255.                                                                            |
|`[3]`|FIN   |Boolean. 1 indicates that this is the last chunk; 0 that there is more to come.  This is not currently supported by the CEF and should be set to 1.|
|`[4]`|OpCode|Integer. 1 means UTF-8 data, 2 means binary data. Should be 0 if FIN is 0.                                                                         |

The result is 0.

<h2 class="example">Example</h2>
```apl
      hr.WebSocketSend  '5d61d8330065608'  'Hello World'
0
```
