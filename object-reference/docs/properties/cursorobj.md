# <span>CursorObj</span> <span>Property</span>

[**Applies To**](../propertyapplies/cursorobj.md)

**Description**


This property is used to associate a particular cursor with an object.




Its
value is either a simple scalar number which specifies a standard Windows
cursor, or the name of, or ref to, a [Cursor](../objects/cursor.md) object. The standard Windows cursors are :


|---|-------------------------------------------------|
|0  |arrow (Windows default)                          |
|1  |hourglass                                        |
|2  |crosshair                                        |
|3  |I-Beam                                           |
|4  |crossing vertical/horizontal double-headed arrows|
|5  |diagonal double-headed arrows (left-to-right)    |
|6  |vertical double-headed arrows                    |
|7  |diagonal double-headed arrows (right-to-left)    |
|8  |horizontal double-headed arrows                  |
|9  |upward pointing arrow                            |
|10 |box                                              |
|11 |crossing vertical/horizontal double-headed arrows|
|12 |no-entry sign                                    |
|13 |arrow with hourglass                             |
|14 |pointing hand                                    |



If CursorObj is set to anything other than an empty vector (which is the
default) it defines the appearance of the cursor when the mouse pointer is moved
into the object. If CursorObj is an empty vector, the shape of the cursor
remains unchanged when the mouse pointer enters the object. In effect, the
cursor is "inherited" from its parent. Exceptions to this rule are
certain objects which have special cursors by default.



If the value of CursorObj for the [Root](../objects/root.md) object
is set to anything other than an empty vector, it applies to **all**[ Form](../objects/form.md)s
and their children, irrespective of their own CursorObj values. Therefore, if
you want to indicate that your application is "working" and is not
responsive to input, you can simply do:
```apl
      '.' ⎕WS 'CursorObj' 1 ⍝ Hourglass cursor
```


Then to reset the application you do:
```apl
      '.' ⎕WS 'CursorObj' ''
```



