# <span>TCPClose</span> <span>Event 374</span>

**Description**

If enabled, this event is reported when the remote end of a TCP/IP connection breaks the connection.

You may not disable or nullify the operation by setting the action code for the event to `¯1` or by returning 0 from a callback function. You may also not call TCPClose as a method or generate this event artificially using `⎕NQ`.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'TCPClose'` or 374    |

**Application**

Objects: [TCPSocket](../objects/tcpsocket.md)
