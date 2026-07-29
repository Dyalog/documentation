# <span>TCPReady</span> <span>Event 379</span>

**Description**

If enabled, this event is reported when the TCP/IP buffers are free and there is no data waiting to be sent in the internal APL queue.

This event is provided to enable you to control the transmission of a large amount of data that cannot be handled in a single call to [TCPSend](./tcpsend.md).

The amount of data that the system can handle in one go is limited by TCP/IP buffers, the speed of the network, and the amount of Windows memory and disk space available for buffering.

You may not disable or nullify the operation by setting the action code for the event to `¯1` or by returning 0 from a callback function. However, you *may* call TCPReady as a method or generate this event artificially using `⎕NQ`.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'TCPReady'` or 379    |

**Application**

Objects: [TCPSocket](../objects/tcpsocket.md)
