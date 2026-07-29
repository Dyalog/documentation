# User Interaction & Events

## Giving Control to the User

As we have seen, `⎕WC` and `⎕WS` are used to build up the definition of the user-interface as a hierarchy of **objects** with **properties**. Notice that the interface is defined not only in terms of its appearance and general behaviour, but also by specification of the Event property, in terms of how it reacts to user actions.

Once you have defined your interface, you are ready to give control to the user. This is simply done by calling `⎕DQ`. Alternatively, you may use the Wait method (if appropriate) which is identical to `⎕DQ` in its operation.

`⎕DQ` performs several tasks. Firstly, it displays all objects that have been created but not yet drawn. When you create objects, Dyalog APL/W automatically buffers the output so as to avoid unpleasant flashing on the screen. Output is flushed when APL requires input (at the 6-space prompt) and by `⎕DQ`. Thus if you write a function that creates a Form containing a set of controls, nothing is drawn until, later on in the function, you call `⎕DQ`. At this point the Form and its contents are displayed in a single screen update, which is visually more pleasing than if they were drawn one by one. A second task for `⎕DQ` is to cause the system to wait for user events. Objects that you create are immediately active and capable of generating events. During development and testing, you can immediately use them without an explicit *wait*. However, unless your application uses the **Session** in conjunction with GUI objects you must call `⎕DQ` to cause the application to wait for user input. In a run-time application, `⎕DQ` is **essential**.

The argument to `⎕DQ` specifies the objects with which the user may interact. Objects may be specified by name or by reference. If the argument is `#`, `'#'` or `'.'`, the user may interact with **all** active objects owned by the current thread **and** with any new objects which are created in callback functions. If not, the argument should specify refs to or names of  one or more top-level objects such as Form, PropertySheet, Clipboard, or a single modal object such as FileBox, Locator, MsgBox or Menu. All specified objects must be owned by the current thread.

In general, `⎕DQ` first updates the screen with any pending changes, then hands control to the user and waits for an event. If its argument is `#`, `'#'`, or `'.'`, `⎕DQ` processes events for all active objects, that is, for those objects and their children whose Active property is 1. If the right argument specifies one or more top-level objects (such as Form, PropertySheet), `⎕DQ` processes events for all of these objects and their children, and (if the current thread is thread 0) for the Root object, but ignores any others, even though they may be currently active.

If the right argument specifies a single modal object, `⎕DQ` activates the object, handles user-interaction with it, and then deactivates it when the user has finished. An event is generated according to the manner in which the user terminated.

Events are managed by both the Operating System and by `⎕DQ` using a **queue**. A detailed understanding of how the queue works is not absolutely necessary, and you may skip the following explanation. However, if you are planning to develop major applications using the GUI, please continue.

## The Event Queue

There are in fact two separate queues, one maintained by Windows and one internal to APL. The Windows queue is used to capture all events that APL needs to process. These include events for your GUI objects as well as other events concerned with APL's own Session Window, Edit Windows, etc. At various points during execution, APL reads events from the Windows queue and either processes them immediately or, if they are events concerned with objects you have defined with `⎕WC`, APL places them on its own internal queue. It is this queue to which `⎕DQ` looks for its next event.

When `⎕DQ` receives an event, it can either ignore it, process it internally, execute a string, call a callback function, or terminate according to the action you have defined for that event. The way you define different actions is described in detail later in this Chapter.

If you have disabled a particular event by setting its action code to `¯1`, `⎕DQ` simply ignores it. For example, if you set the action code of a KeyPress event to `¯`1, keystrokes in that object will be ignored. If you have told `⎕DQ` to process an event normally (the default action code of 0) `⎕DQ` performs the default processing for the event in question. For example, the default processing for a KeyPress event in an Edit object is to display the character and move the input cursor.

If you have associated a string or a callback function with a particular event in a particular object, `⎕DQ` executes the string or invokes the callback function for you. During the execution of the string or the callback function, the user may cause other events. If so, these are added to APL's internal queue but they are not acted upon immediately. When the execution of the string or the callback function terminates, control returns to `⎕DQ` which once more looks to the internal queue. If another event has been added while the callback function was running, this is read and acted upon. If not, `⎕DQ` looks to the Windows queue and waits for the next event to occur.

If you have associated an **asynchronous** callback function with an event (by appending the character "&" to the name of the function), `⎕DQ` starts the callback function in a new thread and is then immediately ready to process the next event; `⎕DQ` does not wait for an asynchronous callback function to complete.

If `⎕DQ` reads an event with an associated action code of 1, it terminates and returns the **event message** which was generated by the event, as a result. The normal processing for the event is not actioned. During the time between `⎕DQ` terminating and you calling it again, events are discarded. Events are only stored up in the queue if `⎕DQ` is active (that is, there is a `⎕DQ` in the state indicator). It is therefore usually better to process events using callback functions.

## Assignment and reference to the Event Property

There are a number of special considerations when using assignment and reference to the Event property.

You can set the action for a single event by prefixing the Event name by "on". For example, to set the action of a MouseUp event on a Form `F` to execute the callback function `FOO`:
```apl
      F.onMouseUp←'UP'
      F.onMouseUp
 #.UP
```

Notice that the value returned (`#.UP`) is not necessarily exactly the same as you set it (`UP`).

If you reference the Event property, you will obtain all the current settings, reported in order of their internal event number. Notice the use of distributed strand notation to set more than one event in the same statement.
```apl
      F.(onMouseUp onMouseDown)←'UP' ('DOWN' 42)
      F.Event
  onMouseDown  #.DOWN  42   onMouseUp  #.UP  
```

If you set the Event property using assignment, all the event actions are redefined, that is, previous event settings are lost. For example:
```apl
      F.(onMouseUp onMouseDown)←'UP' ('DOWN' 42)
      F.Event
  onMouseDown  #.DOWN  42   onMouseUp  #.UP  
 
      F.Event←'onMouseMove' 'MOVE'
      F.Event
  onMouseMove  #.MOVE  
```

The All event can also be set by assignment, and it too clears previous settings. Notice too that a subsequent reference to a specific event using the "on" prefix, will report the "All" setting, unless it is specifically reset.
```apl
      F.(onMouseUp onMouseDown)←'UP' ('DOWN' 42)
      F.Event
  onMouseDown  #.DOWN  42   onMouseUp  #.UP  
 
      F.onAll←'FOO'
      F.Event
  onAll  #.FOO  
 
      F.onMouseMove
 #.FOO
 
      F.Event←'onMouseMove' 'MOVE'
      F.Event
  onMouseMove  #.MOVE  
 
```

If no events are set, the result obtained by `⎕WG` and the result obtained by referencing Event directly are different:
```apl
      'F'⎕WC'Form'
      DISPLAY 'F'⎕WG'Event'
.→--.
|0 0|
'~--'
      DISPLAY F.Event
.⊖------------.
| .→--------. |
| | .⊖. .⊖. | |
| | | | | | | |
| | '-' '-' | |
| '∊--------' |
.∊------------.
```

## Callback Functions

By setting the action code to 1 for all the events you are interested in, you could write the control loop in your application as:
```apl
   Loop:  Event ← ⎕DQ 'system'
          test Event[1] (object name)
          and  Event[2] (event code)
          →Label
```
```apl
   Label: process event for object
          →Loop
```

However, such code can be error prone and difficult to maintain. Another limitation is that events that occur between successive calls on `⎕DQ` are discarded.

An alternative is to use callback functions. Not only do they encourage an object-oriented modular approach to programming, but they can also be used to validate the user's actions and prevent something untoward happening. For example, a callback function can prevent the user from terminating the application at an inappropriate point. The use of callback functions will also produce applications that execute faster than those that process events by exiting `⎕DQ` and looping back again as above.

You associate a callback function with a particular event or set of events in a given object. There is nothing to prevent you from using the same callback function with several objects, but it only makes sense to do so if the processing for the event(s) is common to all of them. The object that caused the event is identified by the first element of the right argument when the callback is invoked.

When an event occurs that has an action set to a character vector, the system looks for a function with that name. If none exists `⎕DQ` terminates with a `VALUE ERROR`. If the function does exist, it is called. If the callback function was called `FOO` and it stopped on line [1], the state indicator would be:
```apl
      )SI
FOO[1]*
⎕DQ
...
```

A callback function may be defined with any syntax, that is, it may be dyadic, monadic, or niladic. If it is monadic or dyadic, `⎕DQ` calls it with the event message as its right argument. If the function is dyadic, its left argument will contain the value of the array that was associated with the event.

A callback function is otherwise no different from any other function that you can define. Indeed there is nothing to prevent you from calling one explicitly in your code. For example, a callback function that is invoked automatically could call a second callback function directly, perhaps to simulate another event.

By default, a callback function is run synchronously. This means that `⎕DQ` waits for it to return a result before attempting to process any other events. Events that are generated by Windows while the callback function is running are simply queued.

Alternatively, you may specify that a callback function is to be run **asynchronously**. In this case, `⎕DQ` starts the function in a new thread, but instead of waiting for it to complete, proceeds immediately to the next event in the queue. See Asynchronous Callbacks for further information.

## Modifying or Inhibiting the Default Processing

It is often desirable to inhibit the normal processing of an event, and it is occasionally useful to substitute some other action for the default. One way of inhibiting an event is to set its action code to `¯1`. However this mechanism is non-selective and is not always applicable. You can use it for example to ignore **all** keystrokes, but not to ignore particular ones.

Synchronous callback functions provide an additional mechanism which allows you to selectively inhibit default processing of an event. The mechanism also allows you to modify the event in order to achieve a different effect.

For example, you can use a callback function to ignore a **particular** keystroke or set of keystrokes, or even to replace the original keystroke with a different one. Similarly, you can use a callback function to selectively ignore a LostFocus event to prevent the user from leaving an input field if the data in the field is invalid. Callback functions therefore give you much finer control over event processing. The mechanism uses the result returned by the callback function and operates as follows.

When an event occurs that has a synchronous callback function attached, `⎕DQ` invokes the callback function (passing it the event message as its right argument) before performing any other action and waits for the callback to complete. When the callback function terminates (exits) `⎕DQ` examines its result.

If the callback function returned no result, or returned a scalar 1 or the identical event message with which it was invoked, `⎕DQ` then carries out the default processing for the event in question. If the callback function returned a 0, `⎕DQ` takes no further action. Finally, if the callback returns a **different** event message (from the one supplied as its right argument), `⎕DQ` performs the default processing associated with the new event rather than with the original one.

For example, consider a callback function attached to a KeyPress event in an Edit object. When the user presses a key, for the sake of example, the unshifted "a" key, `⎕DQ` invokes the callback function, passing it the corresponding event message as its right argument. This event message includes information about which key was pressed, in this case "a". The various possibilities are:

- If the callback function returns a value of 1 or the same event message with which it was invoked, `⎕DQ` carries out the default processing for the original event. In this case a lower-case "a" is displayed in the field.
- If the callback function returns a value of 0, `⎕DQ` takes no further action and (unless code in the callback function actions the keystroke directly) the keystroke is ignored.
- If the callback function modifies the event message and changes the key from an "a" to a "b", `⎕DQ` carries out the default processing associated with the *new* event, and displays a lower-case "b" instead.

Note that asynchronous callback functions may not be used to modify or inhibit the default processing because their results are ignored.

See also: [High-Priority Callback Functions](high-priority-callbacks.md).

## Generating Events using `⎕NQ`

The `⎕NQ` system function is used to generate events under program control and has several uses.

Firstly, it can be used to do something automatically for the user. For example, the following expression gives the input focus to the object `Form1.ED1.`
```apl
        ⎕NQ Form1.ED1 'GotFocus'
```

Secondly, `⎕NQ` can be used to generate user-defined events which trigger special actions either by invoking callback functions or by causing `⎕DQ` to terminate. For example, if you were to define the Event property on `'Form1'` as:
```apl
      'Form1' ⎕WS ('Event' 1001 'FOO')('Event' 1002 1)
```

The expression:
```apl
      ⎕NQ Form1 1001 'Hello' 42
```

would cause `⎕DQ` to invoke the function `FOO`, passing it the entire event message `(#.Form1 1001 'Hello' 42)` as its right argument. Similarly, the expression:
```apl
      ⎕NQ 'Form1' 1002 23.59
```

would cause `⎕DQ` to terminate with the array `('Form1' 1002 23.59)` as its result.

`⎕NQ` can be used to generate events in one of three ways which affect the **context** in which the event is processed.

If it is used monadically as in the examples above, or with a left argument of 0, `⎕NQ` adds the event specified in its right argument onto the bottom of the event queue. The event is then processed by `⎕DQ` when it reaches the head of the queue. You can add events to the queue **prior** to calling `⎕DQ`, or from within a callback function which is itself called by `⎕DQ`. In either case, the context in which the event is finally processed may be completely different from the context in which the event was placed on the queue. When used in this way, the result of `⎕NQ` is always an empty character vector.

If you use `⎕NQ` with a left argument of 1, the event is processed there and then by `⎕NQ` itself. If there is a callback function attached to the event, `⎕NQ` invokes it directly. Thus like `⎕DQ`, `⎕NQ` can appear in the state indicator `⎕SI` or `)SI`. This use of `⎕NQ` is used to generate an event for an object that is not currently included in a `⎕DQ`, and is the usual way of generating the special (non-user) events on the Printer and other objects. It is also used when you want to cause an event to occur **immediately** without waiting for any events already in the queue to be processed first. When used in this way, the result of `⎕NQ` is either an empty character vector, or the result of the callback function if one is attached.

If you use `⎕NQ` with a left argument of 2, APL immediately performs the default processing (if any) for the event, bypassing any callback function. This case of `⎕NQ` is often used *within* a callback function to put the object into the state that it would otherwise be in when the callback terminated. When used in this way, the result of `⎕NQ` is 1. To avoid processing the event twice, the callback function should return 0.

The use of `⎕NQ` with a left argument of 2, is the same as calling the event as a method, and this is discussed in the next section.

A left argument of 4 is a special case that is used by an ActiveXControl or NetType object to generate an event in its host application. See [Introduction](../activex-control/introduction.md) for details.
