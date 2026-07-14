# <span>LocalPortName</span> <span>Property</span>

**Applies To:** [TCPSocket](../objects/tcpsocket.md)

**Description**

The LocalPortName property is a character vector that specifies the port name of the local service that you wish to offer as a server.

Note that you may use *either*[ LocalPort ](localport.md)*or* LocalPortName to identify the service. The use of LocalPortName is slightly slower but it avoids hard-coding the port number in your program and is generally more flexible. If you specify both properties, the value of LocalPortName will be ignored.

LocalPortName may be specified only by the process that is initiating the connection (the server) and must be set by the `⎕WC` statement that creates the [TCPSocket](../objects/tcpsocket.md). LocalPortName may not subsequently be changed using `⎕WS`.

When the specified port name has been resolved to a port number, the [TCPSocket](../objects/tcpsocket.md) will generate a [TCPGotPort](../methodorevents/tcpgotport.md) event and update the value of [LocalPort](localport.md) accordingly.

For a client [TCPSocket](../objects/tcpsocket.md), you may not specify LocalPortName and `⎕WG` returns an empty character vector.
