
<!-- Hidden search keywords -->
<div style="display: none;">
  2250⌶
</div>






<h1 class="heading"><span class="name">Verify .NET Interface</span> <span class="command">R←2250⌶Y</span></h1>



This function provides information about the Dyalog interface to .NET. The system attempts to load the Bridge DLL and reports the status of the .NET interface. It can be used to determine whether your .NET-related code can run, and also what sort of .NET support you have. It also means that you can suppress all messages that `⎕USING` would otherwise generate


The right argument `Y` is zero:


The result `R` is a 3-element nested array:


|Item  |Description                                                                                                                                                                       |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`R[1]`|Numeric. ¯1: the interface is not supported 0: the interface is not configured 1: the interface is configured to use .NET 2: the interface is configured to use the .NET Framework|
|`R[2]`|Boolean 0 or 1. 1 : the Bridge DLL was successfully loaded. 0 : the Bridge DLL failed to load, or was not attempted.                                                              |
|`R[3]`|A character vector containing error messages generated during load.                                                                                                               |


## Examples (Windows)
```apl

      ⎕←2 ⎕NQ '.' 'GetEnvironment' 'Dyalog_NETCore'

      ⎕←2250⌶0
┌─┬─┬┐
│2│1││
└─┴─┴┘

```
```apl

      ⎕←2 ⎕NQ '.' 'GetEnvironment' 'Dyalog_NETCore'
1
      ⎕←2250⌶0
┌─┬─┬┐
│1│1││
└─┴─┴┘

```

## Implementation Note


The underlying code is run once only and the results cached, so all subsequent calls to `2250⌶` will return the same result as the first time.


