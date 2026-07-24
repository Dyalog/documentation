# <span>TCPGotPort</span> <span>Event 378</span>

**Description**

If enabled, this event is reported when a port name (specified by the [RemotePortName](../properties/remoteportname.md) or [LocalPortName](../properties/localportname.md) property) is resolved to a port number.

You may not disable or nullify the operation by setting the action code for the event to `¯1` or by returning 0 from a callback function. You may also not call TCPGotPort as a method or generate this event artificially using `⎕NQ`.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'TCPGotPort'` or 378  |

Note that the port number is not reported in the event message but may be obtained from [RemotePort](../properties/remoteport.md) or [LocalPort](../properties/localport.md) as appropriate.

**Application**

Objects: [TCPSocket](../objects/tcpsocket.md)
