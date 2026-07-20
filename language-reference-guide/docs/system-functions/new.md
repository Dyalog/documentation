---
search:
  boost: 2
---

# <span>New Instance</span> `R←⎕NEW Y`{{key}}

`⎕NEW` creates a new instance of the Class, Dyalog GUI object, or .NET Type specified by `Y`.

`Y` must be a 1- or 2-item scalar or vector. The first item is a reference to a Class or to a .NET Type, or a character vector containing the name of a Dyalog GUI object.

The second item, if specified, contains the argument to be supplied to the Class or Type *Constructor* or a list of property/value pairs for a Dyalog GUI object.

The result `R` is a reference to a new instance of Class, Dyalog GUI object, or Type `Y`.

For further information, see *Interface Guide*.

## Class Example
```apl
:Class Animal
    ∇ Name nm
      :Access Public
      :Implements Constructor
      ⎕DF nm
    ∇
:EndClass ⍝ Animal
 
      Donkey←⎕NEW Animal 'Eeyore'
      Donkey
Eeyore
```

If `⎕NEW` is called with just a Class reference (that is, without parameters for the Constructor), the default constructor will be called. A default constructor is defined by a niladic function with the :Implements Constructor attribute. For example, the Animal Class may be redefined as:
```apl
:Class Animal
    ∇ NoName
      :Access Public
      :Implements Constructor
      ⎕DF 'Noname'
    ∇
    ∇ Name nm
      :Access Public
      :Implements Constructor
      ⎕DF nm
    ∇
:EndClass ⍝ Animal

      Horse←⎕NEW Animal
      Horse
Noname
```

## .NET Examples
```apl
      ⎕USING←'System' 'System.Web.Mail,System.Web.dll'
      dt←⎕NEW DateTime (2006 1 1)
      msg←⎕NEW MailMessage
      ⎕NC 'dt' 'msg' 'DateTime' 'MailMessage'
9.2 9.2 9.6 9.6
```

Note that **.NET Types** are accessed as follows.

If the name specified by the first item of `Y` would otherwise generate a `VALUE ERROR`, and `⎕USING` has been set, APL attempts to load the Type specified by `Y` from the .NET assemblies (DLLs) specified in `⎕USING`. If successful, the name specified by `Y` is entered into the SYMBOL TABLE with a name-class of `9.6`. Subsequent references to that symbol (in this case `DateTime`) are resolved directly and do not involve any assembly searching.

## Dyalog GUI Examples
```apl
      F←⎕NEW ⊂'Form'
      F
#.[Form]
```

To specify the initial values of any properties, `Y[2]` must be a vector (or scalar) of items each of which is of the form (PropertyName PropertyValue); the free-form syntax implemented by `⎕WC` and `⎕WS` is not allowed.
```apl
      ⎕NEW'Form'(⊂'Caption' 'Hello')
#.[Form]

```
```apl

      F←⎕NEW'Form'(('Caption' 'Hello')('Posn' (10 10)))
      F
#.[Form]
```

Note that as `⎕NEW` provides no facility to *name* a GUI object, the Event property should use the *onEvent* syntax so that a callback function (or the result of `⎕DQ`) receives a ref to the object. Otherwise, without the *onEvent* syntax, the first element of the argument to a callback function will contain a character vector such as `'[Form].[Button]'` which merely describes the type of the object but does not identify the object itself.
```apl
      cap←'Caption' 'Push Me'
      ev← 'Event' ('onSelect' 'foo')
      F.(B←⎕NEW'Button'#.(pos cap ev))

```

Note that you may not create an instance of OCXClass using `⎕NEW`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NEW NEW
</div>
