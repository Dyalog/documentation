# <span>TCPAccept</span> <span>Event 371</span>

**Applies To:** [TCPSocket](../objects/tcpsocket.md)

**Description**

If enabled, this event is reported when a client connects to a server [TCPSocket](../objects/tcpsocket.md) object.

You may not disable or nullify the operation by setting the action code for the event to `¯1` or by returning 0 from a callback function. You may also not call TCPAccept as a method or generate this event artificially using `⎕NQ`.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 3-element vector as follows :

|-----|-------------|-----------------------|
|`[1]`|Object       |ref or character vector|
|`[2]`|Event        |`'TCPAccept'` or 371   |
|`[3]`|Socket handle|an integer             |

The socket handle reported by this event is the socket handle for the original listening socket that was associated with the [TCPSocket](../objects/tcpsocket.md) before the client connected.

If you want your server to remain available for other clients, you must create a new [TCPSocket](../objects/tcpsocket.md) object in a callback function attached to this event. The new [TCPSocket](../objects/tcpsocket.md) object must be created by cloning the original listening socket. This is done by specifying the socket handle as the value of its SocketNumber property. You may not specify any other properties (except Event and Data) in the `⎕WC` statement that creates the new clone object.

The default processing for this event is to close the socket handle reported by the 3<sup>rd</sup> element of the event message **unless** it has been associated with a new [TCPSocket](../objects/tcpsocket.md) object by the callback function as described above. You may prevent this from occurring by returning 0 from a callback function. This may be necessary in a multithreaded application.

You may not call TCPClose as a method or generate this event artificially using `⎕NQ`.
