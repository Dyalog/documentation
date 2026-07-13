# <span>LocalAddr</span> <span>Property</span>



**Applies To:** [TCPSocket](../objects/tcpsocket.md)

**Description**


The LocalAddr property is a character vector that specifies the IP address of your computer. Its default value is `'0.0.0.0'`.


Unless your computer has more than one network adapter each identified by a different IP address, you do not need to specify LocalAddr. However, in this case you may use *either* LocalAddr *or*[ LocalAddrName](localaddrname.md) to identify the adapter. If you specify both properties, the value of [LocalAddrName](localaddrname.md) will be ignored.


Note that you may also set the value of LocalAddr to an empty character vector. In this case, the value returned by `⎕WG` will be `'0.0.0.0'`.


LocalAddr may only be specified in the `⎕WC` statement that creates the [TCPSocket](../objects/tcpsocket.md) and may not subsequently be changed using `⎕WS`.



