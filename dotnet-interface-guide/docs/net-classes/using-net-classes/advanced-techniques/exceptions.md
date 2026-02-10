# Exceptions

When a .NET object generates an error, it does so by throwing an exception. An exception is a .NET class whose ultimate base class is System.Exception.

The system constant `⎕EXCEPTION` returns a reference to the most recently generated exception object.

For example, if you attempt to create an instance of a DateTime object with a year that is outside its range, the constructor throws an exception. This causes APL to report a (trappable) `EXCEPTION` error (error number 90) and access to the exception object is provided by `⎕EXCEPTION`.
```apl
      ⎕USING←'System'
      DT←⎕NEW DateTime (100000 0 0)
EXCEPTION: Year, Month, and Day parameters describe an un-representable DateTime.
      DT←⎕NEW DateTime (100000 0 0)
         ^		 
      ⎕EN
90
      ⎕EXCEPTION.Message
Year, Month, and Day parameters describe an un-representable DateTime.
			 
      ⎕EXCEPTION.Source
System.Private.CoreLib
			 
      ⎕EXCEPTION.StackTrace
at System.DateTime.DateToTicks(Int32 year, Int32 month, Int32 day)
at System.DateTime..ctor(Int32 year, Int32 month, Int32 day)
```

The result of `⎕EXCEPTION.StackTrace` can depend on the exact version of .NET – your result might look different, but if it includes `System.DateTime..ctor(Int32 year, Int32 month, Int32 day)` then it is showing the correct exception for this example.
