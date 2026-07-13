# <span>RemoteAddr</span> <span>Property</span>



**Applies To:** [TCPSocket](../objects/tcpsocket.md)

**Description**


The RemoteAddr property is a character vector that specifies the IP address of the remote computer.


RemoteAddr may only be specified by a client [TCPSocket](../objects/tcpsocket.md) that is intended to make a connection with a server. Furthermore, it must be specified in the `⎕WC` statement that creates the [TCPSocket](../objects/tcpsocket.md) object and it may not subsequently be changed using `⎕WS`.


You may use either RemoteAddr or [RemoteAddrName](remoteaddrname.md) to identify the remote computer. If you know its IP address, it is normally quicker to specify RemoteAddr. If you specify both properties, the value of [RemoteAddrName](remoteaddrname.md) will be ignored.


For a server [TCPSocket](../objects/tcpsocket.md), RemoteAddr is determined by the IP address of the connecting process and is a read-only property.



