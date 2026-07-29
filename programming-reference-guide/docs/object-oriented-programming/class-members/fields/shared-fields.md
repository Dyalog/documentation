# Shared Fields

If a Field is declared to be *Shared*, it has the same value for every Instance of the Class. Moreover, the Field may be accessed from the Class itself; an Instance is not required.

The following example establishes a Shared Field called `Months` that contains abbreviated month names which are appropriate for the user's current International settings. It also shows that an arbitrarily complex statement may be used to initialise a Field.
```apl
:Class Example
    :Using System.Globalization
    :Field Public Shared ReadOnly Months←12↑(⎕NEW DateTimeFormatInfo).AbbreviatedMonthNames
:EndClass ⍝ Example
```

A Shared Field is not only accessible from an instance...
```apl
      EG←⎕NEW Example
      EG.Months
 Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov...
```

... but also, directly from the Class itself.
```apl
      Example.Months
Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov...
```

Notice that in this case it is necessary to insert a `:Using` statement (or the equivalent assignment to `⎕USING`) in order to specify the .NET search path for the DateTimeFormatInfo type. Without this, the Class would fail to fix.

You can see how the assignment works by executing the same statements in the Session:
```apl
      ⎕USING←'System.Globalization'
    12↑(⎕NEW DateTimeFormatInfo).AbbreviatedMonthNames
 Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov...
```
