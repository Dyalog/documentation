# <span>TCPSocket</span> <span>Object</span>

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

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Calendar](../objects/calendar.md), [CoolBand](../objects/coolband.md), [DateTimePicker](../objects/datetimepicker.md), [Form](../objects/form.md), [NetType](../objects/nettype.md), [OLEClient](../objects/oleclient.md), [OLEServer](../objects/oleserver.md), [PropertyPage](../objects/propertypage.md), [Root](../objects/root.md), [SubForm](../objects/subform.md), [TCPSocket](../objects/tcpsocket.md)

Children: [Bitmap](../objects/bitmap.md), [BrowseBox](../objects/browsebox.md), [Clipboard](../objects/clipboard.md), [Cursor](../objects/cursor.md), [FileBox](../objects/filebox.md), [Font](../objects/font.md), [Form](../objects/form.md), [Icon](../objects/icon.md), [ImageList](../objects/imagelist.md), [Locator](../objects/locator.md), [Menu](../objects/menu.md), [Metafile](../objects/metafile.md), [MsgBox](../objects/msgbox.md), [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md), [Printer](../objects/printer.md), [PropertySheet](../objects/propertysheet.md), [TCPSocket](../objects/tcpsocket.md), [Timer](../objects/timer.md), [TipField](../objects/tipfield.md)

Properties: [ChildList](../properties/childlist.md), [CurrentState](../properties/currentstate.md), [Data](../properties/data.md), [Encoding](../properties/encoding.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [KeepOnClose](../properties/keeponclose.md), [LocalAddr](../properties/localaddr.md), [LocalAddrName](../properties/localaddrname.md), [LocalPort](../properties/localport.md), [LocalPortName](../properties/localportname.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [RemoteAddr](../properties/remoteaddr.md), [RemoteAddrName](../properties/remoteaddrname.md), [RemotePort](../properties/remoteport.md), [RemotePortName](../properties/remoteportname.md), [SocketNumber](../properties/socketnumber.md), [SocketType](../properties/sockettype.md), [Style](../properties/style.md), [TargetState](../properties/targetstate.md), [Type](../properties/type.md)

Methods: [Detach](../methodorevents/detach.md), [TCPGetHostID](../methodorevents/tcpgethostid.md), [TCPSend](../methodorevents/tcpsend.md), [TCPSendPicture](../methodorevents/tcpsendpicture.md), [Wait](../methodorevents/wait.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [TCPAccept](../methodorevents/tcpaccept.md), [TCPClose](../methodorevents/tcpclose.md), [TCPConnect](../methodorevents/tcpconnect.md), [TCPError](../methodorevents/tcperror.md), [TCPGotAddr](../methodorevents/tcpgotaddr.md), [TCPGotPort](../methodorevents/tcpgotport.md), [TCPReady](../methodorevents/tcpready.md), [TCPRecv](../methodorevents/tcprecv.md)
