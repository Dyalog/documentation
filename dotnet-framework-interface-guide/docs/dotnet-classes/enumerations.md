<h1 class="heading"><span class="name">Enumerations</span></h1>

An _enumeration_ is a set of named constants that can apply to a particular operation. For example, when opening a file you typically want to specify whether the file is to be opened for reading, for writing or for both. A method that opens a file will take a parameter that specifies this. If this is implemented using an enumerated constant, then the parameter can be one of a specific set of (typically) integer values, for example, 1 = read, 2 = write, 3 = read and write. However, to avoid using meaningless numbers in code, it is conventional to use names to represent particular values. These are known as _enumerated constants_ or, more simply, as _enums_.

In the .NET Framework, enums are implemented as classes that inherit from the <code class="language-nonAPL">System.Enum</code> base class. The class as a whole represents a set of enumerated constants; each of the constants is represented by a static field within the class.

[Using Windows Forms](../using-windows-forms.md) (and its sub-sections) describes the use of <code class="language-nonAPL">System.Windows.Forms</code> to create and manipulate the user interface. The classes in this .NET namespace use enums extensively. For example, the <code class="language-nonAPL">System.Windows.Forms.FormBorderStyle</code> class contains a set of static fields named <code class="language-nonAPL">None</code>, <code class="language-nonAPL">FixedDialog</code>, <code class="language-nonAPL">Sizeable</code>, and so on. These fields have specific integer values, but the values themselves are of no interest to the programmer.

Typically, an enumerated constant would be used as a parameter to a method or to specify the value of a property.

<h4 class="example">Example</h4>

To create a Form with a particular border style, set its <code class="language-nonAPL">BorderStyle</code> property to one of the members of the <code class="language-nonAPL">FormBorderStyle</code> class:
```apl
      ⎕USING←'System'

      ⎕USING,←⊂'System.Windows.Forms,system.windows.forms.dll'
      f1←⎕NEW Form
      f1.BorderStyle←FormBorderStyle.FixedDialog
      FormBorderStyle.⎕NL ¯2 ⍝ List enum members
      Fixed3D  FixedDialog  FixedSingle  FixedToolWindow  None  Sizable  SizableToolWindow
```

An enum has a value that can be used instead of the enum itself when such usage is unambiguous. For example, the <code class="language-nonAPL">FormBorderStyle.Fixed3D</code> enum has an underlying value of <code class="language-nonAPL">2</code>:
```apl
     Convert.ToInt32 FormBorderStyle.Fixed3D
2
```

This means that the scalar value 2 can be used to set the border style of the Form `f1` to <code class="language-nonAPL">FormBorderStyle.Fixed3D</code>:
```apl
      f1.BorderStyle←2
```

However, this practice is not recommended as not only does it make the code less clear, but also if a value for a property or a parameter to a method can be one of several different enum types, APL cannot tell which is expected and the call will fail. For example, when the constructor for <code class="language-nonAPL">System.Drawing.Font</code> is called with three parameters, the third parameter can be either a <code class="language-nonAPL">FontStyle</code> enum or a <code class="language-nonAPL">GraphicsUnit</code> enum. If <code class="language-nonAPL">Font</code> is called with a third parameter of <code class="language-nonAPL">1</code>, APL cannot identify whether this refers to a <code class="language-nonAPL">FontStyle</code> enum or a <code class="language-nonAPL">GraphicsUnit</code> enum, and the call will fail.
