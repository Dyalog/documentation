# <span>RemotePort</span> <span>Property</span>

**Description**

The RemotePort property is a scalar integer in the range 1-65536 that identifies the [port number](../miscellaneous/port-number.md) associated with a service on a remote computer.

RemotePort may only be specified by a client [TCPSocket](../objects/tcpsocket.md) that is intended to make a connection with a server. Furthermore, it must be specified in the `⎕WC` statement that creates the [TCPSocket](../objects/tcpsocket.md) object and it may not subsequently be changed using `⎕WS`.

Note that you may use *either* RemotePort *or* [RemotePortName](remoteportname.md) to identify the remote service. If you know the port number, it is normally quicker to specify RemotePort. However unless it is a *well known port number*, the use of a port name is generally more flexible. If you specify both properties, the value of [RemotePortName](remoteportname.md) will be ignored.

For a server [TCPSocket](../objects/tcpsocket.md), RemotePort is determined by the [port number](../miscellaneous/port-number.md) of the connecting process and is a read-only property.

**Application**

Objects: [TCPSocket](../objects/tcpsocket.md)
