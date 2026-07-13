# Properties

By default, Properties exposed by a COM object behave in the same way as Properties exposed by Dyalog APL Classes.

To query the value of a property, you simply reference it. To set the value of the property, you assign a new value to it. If the Property is an Indexed Property, you may use indexing to set or retrieve the value of a particular element.

Note that in previous versions of Dyalog APL,  indexed Properties of COM objects were exposed as Methods and for backwards compatibility this behaviour may be retained by setting `⎕WX` to 0 or 1 (the default value is 3). See Language Reference.

If the old (pre-Version 11.0) behaviour is selected., indexed properties are exposed as methods and you treat the property as if it were an APL function. To obtain the value of the property, you must call it monadically, specifying the required index (or other information) as the argument. To set the value of the property, you must call it dyadically, specifying the required index (or other information) as the right argument and the new value as the left argument.

The data type of the variable is reported by the `GetPropertyInfo` method. Conversion between APL data types and OLE data types is performed automatically.

If you attempt to set the value of a property to an something with an inappropriate data type, APL will generate a `DOMAIN ERROR`.

If you set the value to something of the correct data type, APL will pass it through the OLE interface. However, the OLE object may itself reject the new value. In this case, APL will also generate a `DOMAIN ERROR`. However, the OLE error information may be obtained from the `LastError` property of the object or Root. The error is also displayed in the Status Window.

Note that if `⎕WX` is 0 or 1, `)PROPS` and PropList  report the names of all of the properties of an object, regardless of whether the property is implemented as a variable or as a function. You can tell whether or not the property takes an argument (and therefore behaves as a function) from its property sheet, using GetPropertyInfo, or from the documentation for the object in question.

## Properties as Objects

Dyalog APL permits an object hierarchy to be represented by a namespace hierarchy. In other words, the relationship between one object and another is a parent-child relationship whereby one object owns and contains another.

Visual Basic has no such mechanism and the relationship between objects has to be specified in another way. This is commonly done using properties. For example, an object view of a bicycle could be a hierarchy consisting of a bicycle object that contains a Frame object, a FrontWheel object and a RearWheel object. In Visual Basic, you could represent this hierarchy as a Bicycle object having Frame, FrontWheel and RearWheel *properties* which are (in effect) pointers to the sub-objects. The properties are effectively used to tie the objects together.

An extension of this idea is the Visual Basic Collection object. This is a special type of object, that is somewhat similar to an array. It is used where one object may contain several objects of the same type. For example, a Wheel object could contain a Spokes collection object which itself contains a number of individual Spoke objects. Collection objects are usually implemented as properties.

When you reference the value of an object property, you will get a namespace.

Using the bicycle analogy, you could recreate the object hierarchy in the APL workspace as follows:
```apl
      'BIKE'  ⎕WC'OLEClient' 'EG.Bicycle'
      FRONT ← BIKE.FrontWheel
      REAR ← BIKE.RearWheel
```

The result would be three namespaces, one named `BIKE`, and two unnamed namespaces referenced by `FRONT` and `REAR`. Each contains the specific properties, methods and events exposed by the three corresponding objects.

Note however, that in this example `BIKE`, `FRONT` and `REAR` are all top-level namespaces; a proper parent/child representation can be achieved by making `FRONT` and `REAR` child namespaces of `BIKE`, for example:
```apl
      BIKE.FRONT ← BIKE.FrontWheel
      BIKE.REAR ← BIKE.RearWheel
```

or
```apl
      :With BIKE
          FRONT ← FrontWheel
          REAR ← RearWheel
      :EndWith
```

This example illustrates that when you work with an OLE object, you have a choice whether to represent an object hierarchy as a namespace *tree* or just as a collection of otherwise unrelated namespaces.
