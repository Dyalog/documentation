# Creating Objects using NEW

With the introduction of Classes in Version 11.0, you may manipulate Dyalog GUI objects as Instances of built-in (GUI) Classes. This approach supplements (but does not replace) the use of `⎕WC`, `⎕WS` and so forth.

To create a GUI object using `⎕NEW`, the Class is given as the GUI Object name and the Constructor Argument as a vector of (Property Name / Property Value) pairs. For example, to create a Form:
```apl
      F1←⎕NEW 'Form' (⊂'Caption' 'Hello World')
```

However, only perfectly formed name/value pairs are accepted. The highly flexible syntax for specifying Properties by position and omitting levels of enclosure, that is supported by `⎕WC` and `⎕WS`, is not provided with `⎕NEW`.

Naturally, you may reference and assign Properties in the same way as for objects created using `⎕WC`:
```apl
      F1.Size
50 50
      F1.Size←20 30
```

Callbacks to regular defined functions in the Root or in another space, work in the same way too. If function `FOO` merely displays its argument:
```apl
     ∇ FOO M
[1]    ⎕←M
     ∇

      F1.onMouseUp←'#.FOO'
#.[Form]  MouseUp  78.57142639 44.62540...
```

The first item in the event message is a ref to the Instance of the Form.

To create a control such as a Button, it is only necessary to run `⎕NEW` inside a ref to the appropriate parent object. For example:
```apl
  B1←F1.⎕NEW 'Button' (('Caption' '&OK')('Size' (10 10)))
```

As illustrated in this example, it is not necessary to assign the resulting Button Instance to a name *inside* the Form (`F1` in this case). However, it is a good idea to do so that refs to Instances of controls are expunged when the parent object is expunged. In the example above, expunging `F1` will not remove the Form from the screen because `B1` still exists as a ref to the Button. So, the following is safer:
```apl
 F1.B1←F1.⎕NEW'Button'(('Caption' '&OK')('Size' (10 10)))
```

Or perhaps better still,
```apl
 F1.(B1←⎕NEW 'Button'(('Caption' '&OK')('Size' (10 10))))
```

As `⎕NEW` provides no facility to *name* a GUI object, the Event property should use the *onEvent* syntax so that a callback function (or the result of `⎕DQ`) receives a ref to the object. Otherwise, without the *onEvent* syntax, the first element of the argument to a callback function will contain a character vector such as `'[Form].[Button]'` which merely describes the type of the object but does not identify the object itself.
```apl
      cap←'Caption' 'Push Me'
      ev← 'Event' ('onSelect' 'foo')
      F.(B←⎕NEW'Button'#.(pos cap ev))

```
