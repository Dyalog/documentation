# APL and DDE in Practice

The interface between Dyalog APL/W and DDE is provided by Shared Variables which are implemented as closely as possible in accordance with the APL Standard. There are however some conflicts between Shared Variables and the way in which DDE works. These impose certain restrictions.

The APL Shared Variable concept is based upon the *peer-to-peer* communications model where each partner has equal rights and equal control. DDE however is based upon the *client-server* model whereby data (normally) flows from server to the client at the client's request. This in turn has two major implications. Firstly, a client must **initiate** a DDE conversation. A server may only respond to a request from a client for a connection; it may not itself start a conversation. Secondly a server cannot specify to which client it wishes to communicate. In terms of the APL standard, this means that if a shared variable is to act as a server it must be made the subject of a *general offer*. A shared variable that is to act as a client must be the subject of a *specific offer* Furthermore, as in any DDE conversation there must be one server and one client, it means that two APL workspaces can share variables only if one makes a general offer and one makes a specific offer.

An APL application registers itself as a potential server, or initiates a DDE conversation as a client, by making a Shared Variable offer using `⎕SVO`. The offer is either a general offer, which corresponds to a DDE server, or a specific offer which is a client.

Note that, as mentioned in the introduction, DDE does not preclude two-way data transfer, despite its insistence on a client-server relationship. Thus the establishment of a shared variable as a server or as a client does not force the data transfer to be one-way. The choice of whether APL is to act as a server or as client may in practice be determined by convenience.

## APL as the Client

To initiate a DDE conversation with a server, you use `⎕SVO` as follows:
```apl
      'DDE:appln|topic' ⎕SVO 'var item'
```

where:

|-------|-----------------------------------------------------------------------------|
|`appln`|is the name of the server application.                                       |
|`topic`|is the server topic (usually the name of a document).                        |
|`var`  |is the name of the APL variable.                                             |
|`item` |is the name of the item with which the variable is to be associated (shared).|

For example, the following statement would associate the variable `SALES` with the block of cells R1C1 to R10C10 in an Excel spreadsheet called "Budget".
```apl
      'DDE:EXCEL|BUDGET' ⎕SVO 'SALES R1C1:R10C10'
2
```

Note that the result of `⎕SVO` is the *degree of coupling*. This has the value 2 if the connection is complete (the server has responded) and 1 if it has not. In practice it is a little more complicated than this, because the result actually depends upon the type of DDE link that has been established.

In principle, the type of link is determined by the client. However, because the server may refuse to accept a particular type of link, it can actually be a result of *negotiation* between the two applications.

When the shared variable is offered as a client, APL **always** requests a warm link from the server. If the server refuses a warm link, APL instead requests the current value of the data item (a cold link), and, if the server responds, APL stores the value in the variable. In either case, the degree of coupling is set to 2 if the connection was successful.

## Executing Commands in the Server

As mentioned in the Introduction, it is possible for a client to instruct a server to execute a command by sending it a DDE_EXECUTE message. This is intended to allow the client to condition the environment in which the server is operating and not (as one might first expect) to execute a command which directly returns a result. In fact the only response from a server to a DDE_EXECUTE message is a positive or negative acknowledgement, the meaning of which is application dependent.

You can establish a shared variable as a channel for sending DDE_EXECUTE messages by assigning it a surrogate name of `'⍎'`, the APL execute symbol. After sharing, you send commands to the server as DDE_EXECUTE messages by assigning them, as character vectors, to the shared variable. Following each such assignment, the value of the shared variable is reset to 1 if the server responded with a positive acknowledgement, or 0 if it responded with a negative acknowledgement. This should be interpreted with reference to the server application documentation. Note that most applications require that commands are surrounded by square brackets but several commands may be sent at a time. The following examples use Microsoft Excel Version 2.0 as the server :

## Establish a link to Excel's SYSTEM topic
```apl
      'DDE:EXCEL|SYSTEM' ⎕SVO 'X ⍎'
2
```

## Instruct EXCEL to open a spreadsheet file
```apl
      X←'[OPEN(c:\mydir\mysheet.xls)]'
      X
1
```

## Instruct EXCEL to select a range of cells
```apl
      X←'[SELECT("R1C1:R5C10")]'
      X
1
```

## Carry out two commands in one call
```apl
      CMD1←'[OPEN(c:\mydir\mysheet.xls)]'
      CMD2←'[SELECT("R1C1:R5C10")]'
      X←CMD1,CMD2
      X
1
```

## APL as the Server

A DDE conversation is initiated by a client, and not by a server. If you wish to act as a server, it is therefore necessary to register this fact with the APL interpreter so that it will subsequently respond to a client on your behalf. This is done by making a *general* *offer* using `⎕SVO` as follows:
```apl
      'DDE:' ⎕SVO 'var item'
```

where:

|------|-----------------------------------------------------------------------------|
|`var` |is the name of the APL variable.                                             |
|`item`|is the name of the item with which the variable is to be associated (shared).|

Notice that in this case, the left argument to `⎕SVO` specifies only the protocol, `'DDE'`. APL automatically defines the application name and topic to be `'DYALOG'` and `⎕WSID` respectively. The DDE *item* is specified in the right argument as either the name of the variable, or, optionally, as its external name or surrogate.

To allow another application to act as a client, you must have previously published the name(s) of the items which are supported. For example, if your APL application provides `SALES` information, the following statement could be used to establish it as a server for this item:
```apl
      'DDE:' ⎕SVO 'X1 SALES'
1
```

In the case of a single general offer, the result of `⎕SVO` will always be 1. When subsequently a client application attempts to initiate a conversation with a server with the application name `'DYALOG'` and topic `⎕WSID`, the APL interpreter will respond and complete the connection.

At this point, if and when the client has requested a hot or warm link to the item *SALES*, the degree of coupling (which is reported by using `⎕SVO` monadically) becomes 2, that is:
```apl
      ⎕SVO 'X1'
2
```
