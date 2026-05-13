<h1 class="heading"><span class="name">Enumerations</span></h1>

An enumeration is a set of named constants that can apply to a particular operation. For example, when opening a file you typically want to specify whether the file is to be opened for reading, for writing or for both. A method that opens a file will take a parameter that specifies this. If this is implemented using an enumerated constant, then the parameter can be one of a specific set of (typically) integer values, for example, 1 = read, 2 = write, 3 = read and write. However, to avoid using ambiguous numbers in code, it is conventional to use names to represent particular values. These are known as _enumerated constants_ or, more simply, as _enums_.

In .NET, enums are implemented as classes that inherit from the <code class="language-nonAPL">System.Enum</code> base class. The class as a whole represents a set of enumerated constants; each of the constants is represented by a static field within the class.

Typically, an enumerated constant would be used as a parameter to a method or to specify the value of a property. For example, the <code class="language-nonAPL">DayOfWeek</code> property of the <code class="language-nonAPL">DateTime</code> object returns a value of <code class="language-nonAPL">Type System.DayOfWeek</code> (it is incidental that both the Type and property are called <code class="language-nonAPL">DayOfWeek</code>):
```apl
      ⎕USING←'' 'System'
      cal←⎕NEW DateTime(1981 09 23)
      cal.DayOfWeek
Wednesday
      cal.DayOfWeek.GetType
System.DayOfWeek
      System.DayOfWeek.⎕NL ¯2
Friday  Monday  Saturday  Sunday  Thursday  Tuesday  Wednesday
```

The function <code class="language-nonAPL">System.Convert.ToBase64String</code> has some constructor overloads that take an argument of Type <code class="language-nonAPL">System.Base64FormattingOptions</code>, which is an enum:
```apl
    System.Convert.ToBase64String
System.String ToBase64String(Byte[])
...
      System.Base64FormattingOptions.⎕NL ¯2
InsertLineBreaks  None
```

Hence:
```apl
      (⎕UCS 13 )∊ System.Convert.ToBase64String(⊂⍳100) System.Base64FormattingOptions.InsertLineBreaks
1
      (⎕UCS 13 )∊ System.Convert.ToBase64String(⊂⍳100) System.Base64FormattingOptions.None
0
```

An enum has a value that can be used in place of the enum itself when such usage is unambiguous. For example, the <code class="language-nonAPL">System.Base64FormattingOptions.InsertLineBreaks</code> enum has an underlying value of `1`:
```apl
      Convert.ToInt32 Base64FormattingOptions.InsertLineBreaks
1
```

This means that the scalar value `1` can be used as the second parameter to <code class="language-nonAPL">ToBase64String</code>:
```apl
      (⎕UCS 13 )∊ System.Convert.ToBase64String(⍳100) 1
1
```

However, this practice is not recommended. Not only does it make the code less clear, but also if a value for a property or a parameter to a method can be one of several different enum types, APL cannot tell which is expected and the call will fail.
