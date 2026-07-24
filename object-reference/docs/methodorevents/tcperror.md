# <span>TCPError</span> <span>Event 370</span>

**Description**

This event is generated when a fatal TCP/IP error occurs and is reported by a [TCPSocket](../objects/tcpsocket.md) object.

The default processing for this event is to display a message box containing details of the TCP/IP error. You may disable the display of this message box by setting the action code for the event to `¯1` or by returning 0 from a callback function attached to it.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 3-element vector as follows :

|-----|----------|-----------------------|
|`[1]`|Object    |ref or character vector|
|`[2]`|Event     |`'TCPError'` or 370    |
|`[3]`|Error code|a number               |
|`[4]`|Error text|a character vector     |

**Application**

Objects: [TCPSocket](../objects/tcpsocket.md)
