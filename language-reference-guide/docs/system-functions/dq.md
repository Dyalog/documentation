---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DQ DQ
</div>






<h1 class="heading"><span class="name">Dequeue Events</span> <span class="command">{R}←⎕DQ Y</span></h1>



**Windows only.**


`⎕DQ` awaits and processes events.  `Y` specifies the GUI objects(s) for which events are to be processed.  Objects are identified by their names, as character scalars/vectors, or by namespace references. These may be objects of type Root, Form, Locator, FileBox, MsgBox, PropertySheet, TCPSocket, Timer, Clipboard and pop-up Menu. Sub-objects (children) of those named in `Y` are also included.  However, any objects which exist, but are not named in `Y`, are effectively disabled (do not respond to the user).



If `Y` is `#`, `'#'`, or `'.'`, all objects currently owned and subsequently created by the current thread are included in the `⎕DQ`. Note that because the Root object is owned by thread 0, events on Root are reported only to thread 0.


If `Y` is empty it specifies the object associated with the current namespace and is only valid if the current space is one of the objects listed above.


Otherwise, `Y` contains the name(s) of or reference(s) to the objects for which events are to be processed.  Effectively, this is the list of objects with which the user may interact.  A `DOMAIN ERROR` is reported if an element of `Y` refers to anything other than an existing "top-level" object.


Associated with every object is a set of events.  For every event there is defined an "action" which specifies how that event is to be processed by `⎕DQ`.  The "action" may be a number with the value `0`, `1` or `¯1`,  a character vector containing the name of a "callback function", or a character vector containing the name of a callback function coupled with an arbitrary array.  Actions can be defined in a number of ways, but the following examples will illustrate the different cases.
```apl
      OBJ ⎕WS 'Event' 'Select' 0
 
      OBJ ⎕WS 'Event' 'Select' 1
 
      OBJ ⎕WS 'Event' 'Select' 'FOO'
 
      OBJ ⎕WS 'Event' 'Select' 'FOO' 10
 
      OBJ ⎕WS 'Event' 'Select' 'FOO&'
```


These are treated as follows:

## Action = 0 (the default)


`⎕DQ` performs "standard" processing appropriate to the object and type of event.  For example, the standard processing for a KeyPress event in an Edit object is to action the key press, that is, to echo the character on the screen.

## Action = `¯`1


This disables the event.  The "standard" processing appropriate to the object and type of event is **not** performed, or in some cases is reversed.  For example, if the "action code" for a KeyPress event (22) is set to `¯1`,  `⎕DQ` simply ignores all keystrokes for the object in question.

## Action = 1


`⎕DQ` terminates and returns information pertaining to the event (the **event message**) in `R` as a nested vector whose first two elements are the name of the object (that generated the event) and the event code.  `R` may contain additional elements depending upon the type of event that occurred.

## Action = fn {larg}


`fn` is a character vector containing the name of a *callback* function.  This function is automatically invoked by `⎕DQ` whenever the event occurs, and **prior** to the standard processing for the event.  The callback is supplied the **event message** (see above) as its right argument, and, if specified, the array `larg` as its left argument.  If the callback function fails to return a result, or returns the scalar value 1,  `⎕DQ` then performs the standard processing appropriate to the object and type of event.  If the callback function returns a scalar 0, the standard processing is not performed or in some cases is reversed.


If the callback function returns its event message with some of the parameters changed, these changes are incorporated into the standard processing.  An example would be the processing of a keystroke message where the callback function substitutes upper case for lower case characters. The exact nature of this processing is described in the reference section on each event type.

## Action = `⍎`expr


If `Action` is set to a character vector whose first element is the execute symbol (`⍎`) the remaining string will be executed automatically whenever the event occurs.  The default processing for the event is performed first and may not be changed or inhibited in any way.

## Action = fn& {larg}


`fn` is a character vector containing the name of a *callback* function.  The function is executed in a new thread. The default processing for the event is performed first and may not be changed or inhibited in any way.


# The Result of `⎕DQ`


`⎕DQ` terminates, returning the shy result `R`, in one of four instances.


Firstly, `⎕DQ` terminates when an event occurs whose "action code" is 1.  In this case, its result is a nested vector containing the **event message** associated with the event.  The structure of an event message varies according to the event type (see *Object Reference*).  However, an event message has at least two elements of which the first is a ref to the object or a character vector containing the name of the object, and the second is a character vector or numeric code which identifies the event type.



`⎕DQ` also terminates if all of the objects named in `Y` have been deleted.  In this case, the result is an empty character vector.  Objects are deleted either using `⎕EX`, or on exit from a defined function or operator if the names are localised in the header, or on closing a form using the system menu.


Thirdly, `⎕DQ` terminates if the object named in its right argument is a special *modal* object, such as a `MsgBox`, `FileBox` or `Locator`, and the user has finished interacting with the object (for example, by pressing an "OK" button).  The return value of `⎕DQ` in this case depends on the action code of the event.


Finally, `⎕DQ` terminates with a `VALUE ERROR` if it attempts to execute a callback function that is undefined.


