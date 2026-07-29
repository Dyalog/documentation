# <span>TCPGetHostID</span> <span>Method 376</span>

**Description**

This method is used to obtain the IP Address of your PC.

The TCPGetHostID method is niladic.

The (shy) result is a character string containing your IP address. If you have more than one, it will return the first.

For example:

```apl
      TCPCetHostID
193.32.236.43
```

**Application**

Objects: [Root](../objects/root.md), [TCPSocket](../objects/tcpsocket.md)
