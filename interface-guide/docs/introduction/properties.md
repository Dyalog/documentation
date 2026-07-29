# Properties

Properties may be set using the system functions `⎕WC` and `⎕WS` and their values may be retrieved using `⎕WG`.

If the system variable `⎕WX` is set to 1, properties may be set using assignment and referenced by name as if they were variables. This is generally faster and more convenient than using `⎕WS` and `⎕WG`.

Certain properties, in particular the Type property, can only be set using `⎕WC`. There is no obvious rule that determines whether or not a property can only be set by `⎕WC`; it is a consequence of the Windows API.

However, any property that can be set by `⎕WS` can be set using assignment and the values of all properties can be retrieved by direct reference or using `⎕WG`.

## Setting Properties with Assignment

You may set the value of a property using the assignment arrow `←`. For example:
```apl
      'F' ⎕WC 'Form'
```

The following statement sets the Caption property to the string "Hello World":
```apl
      F.Caption←'Hello World'
```

Strand assignment may be used to set several properties in a single statement:
```apl
      F.Size F.Posn←(40 50)(10 10)
```

However, distributed assignment is even more concise:
```apl
      F.(Size Posn)←(40 50)(10 10)
```

Normal namespace path rules apply, so the following are all equivalent:
```apl
      #.F.Caption←'Hello World'
```
```apl
      )CS F
#.F
      Caption←'Hello World'
      :With 'F'
          Caption←'Hello World'
          Posn←40 50
          Size←10 10
          ...
      :EndWith
```

Notice however, that used directly in this way, Property names are case-sensitive. The following expressions assign values to *variables* in F and have no effect on the Caption property.
```apl
      F.caption←'Hello World'
      F.CAPTION←'Hello World'
```

## Retrieving property values by reference

You may obtain the value of a property as if it were a variable, by simply referring to the property name. For example:
```apl
      F.Caption←'Hello World'
 
      F.Caption
Hello World
```

You can retrieve the values of several properties in one statement using strand notation:
```apl
      F.Caption F.Posn F.Size
 Hello World  40 50  10 10      
```

Although, once again, the use of parentheses is even more concise:
```apl
      F.(Caption Posn Size)
 Hello World  40 50  10 10      
```

Although setting and referencing a Property appears to be no different to setting and referencing a variable, it is not actually the same thing at all. When you set a Property (whether by assignment or using `⎕WC` or `⎕WS`) to a particular value you are making a request to Windows to do so; there is no guarantee that it will be honoured.

For example, having asked for a Font with face name of "Courier New", you cannot change its Fixed property to 0, because the Courier New font is always fixed pitch.
```apl
      'F'⎕WC'Font' 'Courier New'
1
      F.Fixed←0
      F.Fixed
1
```

## Setting Properties with `⎕WC`

Properties may also be set by the right argument of `⎕WC`. In these cases, they may be specified in one of two ways; either by their position in the argument, or by a keyword followed by a value. The keyword is a character vector containing the **name** of the property. Its value may be any appropriate array. Property names and value keywords are not case sensitive; thus `'Form'` could be spelled `'form'`, `'FORM'`, or even `'fOrM'`

The Type property, which specifies the type of the object, applies to **all** objects and is **mandatory**. It is therefore the first to be specified in the right argument to `⎕WC`, and is normally specified without the Type keyword. The value associated with the Type property is a character vector.

With the exception of Type, all other properties have default values and need only be specified if you want to override the defaults. For example, the following statements would give you a default Button in a default Group in a default Form:
```apl
  'form'      ⎕WC 'Form'
  'form.g'    ⎕WC 'Group'
  'form.g.b1' ⎕WC 'Button'
```

Properties are specified in a sequence chosen to put the most commonly used ones first. In practice, this allows you to specify most properties by position, rather than by keyword/value pairs. For example, the Caption property is deemed to be the "most used" property of a Button and is specified second after Type. The following two statements are therefore equivalent:
```apl
   'F1.B1' ⎕WC 'Button' 'OK'
   'F1.B1' ⎕WC 'Button' ('Caption' 'OK')
```

The third and fourth properties are (usually) Posn, which specifies the position of a child within its parent, and Size which specifies its size. The following statements all create a Form with an empty title bar, whose top left corner is 10% down and 20% across from the top left corner of the screen, and whose height is 60% of the screen height and whose width is 40% of the screen width.
```apl
   'form' ⎕WC 'Form' '' (10 20) (60 40)
   'form' ⎕WC 'Form' '' ('Posn' 10 20) ('Size' 60 40)
   'form' ⎕WC 'Form' '' ('Posn' 10 20) (60 40)
   'form' ⎕WC 'Form' ('Posn' 10 20) (60 40)
```

## Changing Property Values with `⎕WS`

Once you have created an object using `⎕WC`, you are free to alter most of its properties using `⎕WS`. However in general, those properties that define the overall structure of an object's window cannot be altered using `⎕WS`. Such *immutable* properties include Type and (for some objects) Style. Note that if you find that you do need to alter one of these properties dynamically, it is a simple matter to recreate the object with `⎕WC`.

The syntax for `⎕WS` is identical to that of `⎕WC`. The following examples illustrate how the properties of a Button can be altered dynamically. Note that you can use `⎕WS` in a callback function to change the properties of any object, including the one that generated the event.

Create "OK" button at (10,10) that calls `FOO` when pressed
```apl
 'form.b1' ⎕WC 'Button' 'OK' (10 10)
```

Some time later, change caption and size
```apl
 'form.b1' ⎕WS ('Caption' 'Yes') ('Size' 20 15)
```

Note that if the right argument to `⎕WS` specifies a single property, it is not necessary to enclose it. How the Property List is Processed

The system is designed to give you as much flexibility as possible in specifying property values. You should find that any "reasonable" specification will be accepted. However, you may find the following explanation of how the right argument of `⎕WC` and `⎕WS` is parsed, useful. **The casual reader may wish to skip this page**.

Items in the right argument are processed one by one. If the next array in the argument is a simple array, or a nested array whose first element is not a character vector, the array is taken to be the value of the next property, taking the properties in the order defined for that object type.

When the system encounters a **nested array** whose first element is a character vector, it is checked against the list of property names. If it is not a property name, the entire array is taken to define the value of the next property as above.

If the first element **is** a property name, the remainder of the nested array is taken to be the value of the corresponding property. For convenience, considerable latitude is allowed in how the structure of the property value is specified.

After assigning the value, the parser resets its internal pointer to the property following the one named. Thus in the third and fourth examples on the preceding page, omitting the Size keyword is acceptable, because Size is the next property after Posn.

In the reference section for each object, you will find the list of properties applicable to that object, given in the order in which they are to be specified. This information is also reported by the PropList property, which applies to all objects. The list of properties may also be obtained by executing the system command `)PROPS` in an object's namespace.

## The Event Property

Of the many different properties supported, the Event property is rather special. Most of the other properties determine an object's appearance and general behaviour. The Event property, however, specifies how the application **reacts to the user**. Furthermore, unlike most other properties, it takes not a single value, but a set of values, each of which determines the action to be taken when a particular **event** occurs. In simple terms, an *event* is something that the user can do. For example, pressing a mouse button, pressing a key, selecting an item from a menu, are all examples of *events*.

Like any other property, the Event property may be set by assignment or using `⎕WC` and `⎕WS`. Using assignment, you can specify settings for the entire set of events, or you can set individual events one by one.

Each type of event has a *name* and a *number*. Although you may identify an event either by its name or by its number, the use of its name is generally preferable. The exception to this is user-defined events which may only be specified by number.

The list of events supported by a particular object is available from its EventList property, or by executing the system command `)EVENTS` in an object's namespace.

To specify an individual event, you assign the action to the event name which is optionally prefixed by the string `'on'`. For example, the name for the event that occurs when a user presses a key is `'KeyPress'`. To this you assign an *action*. Event *actions* are described in detail later in this chapter, but most commonly *action* is a character vector containing the name of a function. This is termed a *callback* function, because it will be automatically *called* for you when the corresponding event occurs. So if `F1` is a Form, the statement:
```apl
      F1.onKeyPress←'CHECK_KEY'
```

specifies that the system is to call the function `CHECK_KEY` whenever the user presses a key when `F1` has the input focus.

Using `⎕WC` and `⎕WS`, the same effect can be obtained by:
```apl
      'F1'⎕WC'Form' ('Event' 'onKeyPress' 'CHECK_KEY')
```

or
```apl
      'F1'⎕WS 'Event' 'onKeyPress' 'CHECK_KEY'
 
```

When a callback function is invoked, the system supplies an *event message* as its right argument, and (optionally) an array that you specify, as its left argument. The event message is a nested vector that contains information about the event. The first element of the event message is always either a *namespace reference* to the object that generated the event or a character vector containing its name.

To instruct the system to pass the object *name* instead of a *reference*, you must use the event name on its own (omitting the `'on'` prefix) or the event number. This method is retained for compatibility with previous versions of Dyalog APL that did not support namespace references.

For example, either of the following statements will associate the callback function `'CHECK_KEY'` with the KeyPress event. However, when `'CHECK_KEY'` is called, it will be called with the character string `'F1'` in the first element of the right argument (the event message) instead of a direct reference to the object `F1`.
```apl
      F1.Event←'KeyPress' 'CHECK_KEY'
      'F1'⎕WS 'Event' 'KeyPress' 'CHECK_KEY'
      'F1'⎕WS 'Event' 22 'CHECK_KEY'
```

Note that by default, all events are processed automatically by APL, and may be ignored by your application unless you want to take a specific action. Thus, for example, you don't have to handle Configure events when the user resizes your Form; you can just let APL handle them for you.

Before looking further into events, it is necessary to describe how control is passed to the user, and to introduce the concept of the *event queue*.

For further details, see the description of the Event property in the *Object Reference*.
