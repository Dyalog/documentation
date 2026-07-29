# Superseding Base Class Methods

Normally, a Method defined in a higher Class supersedes the Method of the same name that is defined in its Base Class, but only for calls made from above or within the higher Class itself (or an Instance of the higher Class). The base method remains available **in the Base Class** and is invoked by a reference to it *from within the Base Class*. This behaviour can be altered using the Overridable and Override key words in the `:Access` statement but only applies to Instance Methods.

If a Public Instance method in a Class is marked as *Overridable*, this allows a Class which derives from the Class with the Overridable method to supersede the Base Class method *in the Base Class*, by providing a method which is marked *Override*. The typical use of this is to replace code in the Base Class which handles an event, with a method provided by the derived Class.

For example, the base class might have a method which is called if any error occurs in the base class:
```apl
     ∇ ErrorHandler
[1]    :Access Public Overridable
[2]    ⎕←↑⎕DM
     ∇
```

In your derived class, you might supersede this by a more sophisticated error handler, which logs the error to a file:
```apl
     ∇ ErrorHandler;TN
[1]    :Access Public Override
[2]    ⎕←↑⎕DM
[3]    TN←'ErrorLog'⎕FSTIE 0
[4]    ⎕DM ⎕FAPPEND TN
[5]    ⎕FUNTIE TN
     ∇
```

If the derived class had a function which was not marked Override, then function in the derived class which called `ErrorHandler` would call the function as defined in the derived class, but if a function in the base class called `ErrorHandler`, it would still see the base class version of this function. With Override specified, the new function supersedes the function as seen by code in the base class. Note that different derived classes can specify different Overrides.

In C#, Java and some other compiled languages, the term *Virtual* is used in place of *Overridable*, which is the term used by Visual Basic and Dyalog APL.
