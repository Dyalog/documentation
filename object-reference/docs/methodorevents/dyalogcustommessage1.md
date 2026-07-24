# <span>DyalogCustomMessage1</span> <span>Event 95</span>

**Description**

This event allows external applications and dynamic link libraries to insert
events into the Dyalog APL/W message queue.

DyalogCustomMessage1 may be invoked from a C program as follows:
```apl
msg=RegisterWindowMessage("DyalogCustomMessage1");
SendMessage(hWnd,msg,wParam,lParam);
```

where hWnd is the window handle of the object in the Dyalog APL
Workspace. If the object is a [Form](../objects/form.md), this may be
obtained using FindWindow(). If not, hwnd may be passed to the external process
as an argument to a function.

The parameters wParam and lParam are reported as
numeric arguments to the APL callback function.

NOTE: It is not possible to pass pointers to data in wParam or lParam.
When the APL callback executes the pointers may not be valid.

If a callback function is attached to the event, the callback function will
be run when the event reaches the top of the queue.

This event is reported for information alone. You may not disable or nullify
the event by setting the action code for the event to `¯1` or by returning 0 from a callback function.

The result of a callback function is **not** returned to the external
application.

The event message reported as the result of `⎕DQ`,
or supplied as the right argument to your callback function, is a 4-element
vector as follows :

|-----|------|------------------------------|
|`[1]`|Object|ref or character vector       |
|`[2]`|Event |`'DyalogCustomMessage1'` or 95|
|`[3]`|wparam|integer                       |
|`[4]`|lparam|integer                       |

**Application**

Objects: [Form](../objects/form.md)
