<h1 class="heading"><span class="name">Enumerations</span></h1>

An enumeration is a set of named constants that may apply to a particular operation. For example, when you open a file you typically want to specify whether the file is to be opened for reading, for writing, or for both. A method that opens a file will take a parameter that allows you to specify this. If this is implemented using an enumerated constant, the parameter may be one of a specific set of (typically) integer values; for example, 1=read, 2=write, 3=both read and write. However, to avoid using meaningless numbers in code, it is conventional to use names to represent particular values. These are known as *enumerated constants* or, more simply, as *enums*.

In the .NET Framework, *enums* are implemented as classes that inherit from the base class `System.Enum`. The class as a whole represents a set of enumerated constants; each of the constants themselves is represented by a static field within the class.

The next chapter deals with the use of `System.Windows.Forms` to create and manipulate the user interface. The classes in this .NET Namespace use *enums* extensively.

For example, there is a class named `System.Windows.Forms.FormBorderStyle` that contains a set of static fields named `None`, `FixedDialog`, `Sizeable`, and so forth. These fields have specific integer values, but the values themselves are of no interest to the programmer.

Typically, you use an enumerated constant as a parameter to a method or to specify the value of a property. For example, to create a Form with a particular border style, you would set its `BorderStyle` property to one of the members of the `FormBorderStyle` class, viz.
```apl
⎕USING←'System'
  ⎕USING,←⊂'System.Windows.Forms,system.windows.forms.dll'
f1←⎕NEW Form
f1.BorderStyle←FormBorderStyle.FixedDialog
FormBorderStyle.⎕NL ¯2 ⍝ List enum members
Fixed3D  FixedDialog  FixedSingle  FixedToolWindow  None 
Sizable  SizableToolWindow
```

An enum has a value, which you may use in place of the enum itself when such usage is unambiguous. For example, the `FormBorderStyle.Fixed3D` enum has an underlying value is 2:
```apl
     Convert.ToInt32 FormBorderStyle.Fixed3D
2
```

You could set the border style of the Form `f1` to `FormBorderStyle.Fixed3D` with the expression:
```apl
      f1.BorderStyle←2
```

However, this practice is not recommended. Not only does it make your code less clear, but also if a value for a property or a parameter to a method may be one of several different enum types, APL cannot tell which is expected and the call will fail.

For example, when the constructor for `System.Drawing.Font` is called with 3 parameters, the 3<sup>rd</sup> parameter may be either a `FontStyle` enum or a `GraphicsUnit` enum. If you were to call Font with a 3<sup>rd</sup> parameter of 1, APL cannot tell whether this refers to a `FontStyle` enum, or a `GraphicsUnit` enum, and the call will fail.
