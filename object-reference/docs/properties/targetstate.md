# <span>TargetState</span> <span>Property</span>

**Applies To:** [TCPSocket](../objects/tcpsocket.md)

**Description**

The TargetState property reflects the intended final state of a [TCPSocket](../objects/tcpsocket.md) object. Its possible values are as follows:

|------|------|
|Stream|UDP   |
|Client|Open  |
|Server|Bound |
|Closed|Closed|

Setting TargetState to Closed is the recommended way to close a socket. It informs APL that you want the socket to be closed, but only when it is safe to
do so. When all the data has been sent, the [TCPSocket](../objects/tcpsocket.md) will generate a [TCPClose](../methodorevents/tcpclose.md) event which, unless a callback function decides otherwise, will cause the [TCPSocket](../objects/tcpsocket.md) object to disappear.

To control socket closure, you may execute the following steps:

1. Set TargetState to Closed
2. **Either:**
    1. continue processing **or**
    2. wait (using `⎕DQ`) for the [TCPSocket](../objects/tcpsocket.md) to disappear **or**
    3. wait (using `⎕DQ`) for the [TCPClose](../methodorevents/tcpclose.md) event




