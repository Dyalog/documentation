---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕EXCEPTION EXCEPTION
</div>

# <span>Exception</span> `R←⎕EXCEPTION`{{key}}

This is a system object that identifies the most recent *Exception* thrown by a Microsoft .NET object.

`⎕EXCEPTION` derives from the Microsoft .NET class System.Exception. Among its properties are the following, all of which are strings:

|------------|-------------------------------------------------------------------|
|`Source`    |The name of the .NET namespace in which the exception was generated|
|`StackTrace`|The calling stack                                                  |
|`Message`   |The error message                                                  |

```apl
      ⎕USING←'System'
      DT←⎕NEW DateTime (100000 0 0)
EXCEPTION: Year, Month, and Day parameters describe an un-representable DateTime.
      DT←⎕NEW DateTime(100000 0 0)
     ∧
      ⎕EN
90
```
```apl
      ⎕EXCEPTION.Message
Year, Month, and Day parameters describe an un-representable DateTime.

      ⎕EXCEPTION.Source
mscorlib

      ⎕EXCEPTION.StackTrace
   at System.DateTime.DateToTicks(Int32 year,
                                  Int32 month, Int32 day)

   at System.DateTime..ctor(Int32 year,
                            Int32 month, Int32 day)
```

Similarly to GUI objects, `⎕EXCEPTION` is not preserved across a save/load cycle if the workspace is loaded in a different interpreter.

!!! note
    `⎕SIGNAL` can be used to reset the value of this system constant.
