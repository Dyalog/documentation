# <span>TCPSocket</span> <span>Object</span>

[Parents](../parentlists/tcpsocket.md), [Children](../childlists/tcpsocket.md), [Properties](../proplists/tcpsocket.md), [Methods](../methodlists/tcpsocket.md), [Events](../eventlists/tcpsocket.md)

**Purpose:** The TCPSocket object provides an interface to TCP/IP.

**Description**

The TCPSocket object provides an event-driven mechanism to communicate with
other programs (including Dyalog APL) via TCP sockets. Dyalog recommends that Conga is used in preference to TCPSockets in new applications.

The [SocketType](../properties/sockettype.md) property is a
character vector that specifies the type of the TCP/IP socket. This is either '`Stream'` (the
default), or `'UDP'`. [SocketType](../properties/sockettype.md) must be defined when the object is created and cannot be set or changed using `⎕WS`.

The Style property is a character vector that specifies the type of data
transmitted or received by the socket; it may be `'Char'`,
`'Raw'`, or `'APL'`.
The value `'APL'` is valid only if the [SocketType](../properties/sockettype.md) is '`Stream'`.

The [Encoding](../properties/encoding.md) property is a character
vector that specifies how character data are encoded or translated. The possible
values are `'None'`, `'UTF-8'`, `'Classic'`
or `'Unicode'`, depending upon the value of the Style
property.

[LocalAddr](../properties/localaddr.md) and [LocalPort](../properties/localport.md) properties identify your end of the connection; [RemoteAddr](../properties/remoteaddr.md) and [RemotePort](../properties/remoteport.md) identify the other end of
the connection. The values of the two sets of properties are clearly
symmetrical; your [LocalAddr](../properties/localaddr.md) is your
partner's [RemoteAddr](../properties/remoteaddr.md), and there are
strict rules concerning which of them you and your partner may set. See the
individual descriptions of these properties for details.

The [SocketNumber](../properties/socketnumber.md) property is the
Window handle of the socket attached to the TCPSocket object and is generally a
read-only property. The only time that [SocketNumber](../properties/socketnumber.md) may be specified is when a server replicates (clones) a listening socket to
which a client has just connected.
