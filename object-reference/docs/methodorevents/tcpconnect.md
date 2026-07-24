# <span>TCPConnect</span> <span>Event 372</span>

**Description**

If enabled, this event is reported when a server accepts the connection of a client [TCPSocket](../objects/tcpsocket.md) object and is reported by the client.

You may not disable or nullify the operation by setting the action code for the event to `¯1` or by returning 0 from a callback function. You may also not call TCPConnect as a method or generate this event artificially using `⎕NQ`.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'TCPConnect'` or 372  |

**Application**

Objects: [TCPSocket](../objects/tcpsocket.md)
