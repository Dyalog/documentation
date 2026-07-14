# <span>SocketType</span> <span>Property</span>

**Applies To:** [TCPSocket](../objects/tcpsocket.md)

**Description**

The SocketType property is a character vector that specifies the type of the TCP/IP socket. This is either [`Stream`](../miscellaneous/stream-sockets.md) (which is the default), or [`UDP`](../miscellaneous/user-datagram-protocol-udp.md).

SocketType must be defined when the object is created and may not be set or changed using `⎕WS`.

For two Dyalog applications to communicate, their [TCPSocket](../objects/tcpsocket.md) objects must have the same SocketType.
