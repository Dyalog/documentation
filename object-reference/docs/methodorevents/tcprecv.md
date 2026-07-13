# <span>TCPRecv</span> <span>Event 373</span>



**Applies To:** [TCPSocket](../objects/tcpsocket.md)

**Description**


If enabled, this event is reported when data is received by a [TCPSocket](../objects/tcpsocket.md) object.


You may not disable or nullify the operation by setting the action code for
the event to `¯1` or by returning 0 from a
callback function. You may also not call TCPRecv as a method or generate this
event artificially using `⎕NQ`.


The event message reported as the result of `⎕DQ`,
or supplied as the right argument to your callback function, is a 5-element
vector as follows :


|-----|-----------|-----------------------|
|`[1]`|Object     |ref or character vector|
|`[2]`|Event      |`'TCPRecv'` or 373     |
|`[3]`|Data       |the data received      |
|`[4]`|IP address |character vector       |
|`[5]`|Port number|integer                |


Elements [4-5] refer to the IP address and port number of the remote process
that sent the data.


If the [SocketType](../properties/sockettype.md) is `'Stream'`,
this information will be identical to the values of the [RemoteAddr](../properties/remoteaddr.md) and [RemotePort](../properties/remoteport.md) respectively.


If the [SocketType](../properties/sockettype.md) is `'UDP'` and there is potentially more than one partner sending you data, the IP address
and port number information provided by the TCPRecv event is more reliable than
the current values of [RemoteAddr](../properties/remoteaddr.md) and [RemotePort](../properties/remoteport.md) as these may already have changed.


