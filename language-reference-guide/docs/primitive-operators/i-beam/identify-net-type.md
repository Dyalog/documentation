
<!-- Hidden search keywords -->
<div style="display: none;">
  2017⌶
</div>






<h1 class="heading"><span class="name">Identify .NET Type</span> <span class="command">R←2017⌶Y</span></h1>



!!! note
    **.NET Framework only**


Returns the .NET Type of a named .NET class that is loaded in the current AppDomain. Note that System.Type.GetType requires the fully qualified name, that is, prefixed by the assembly name, whereas (`2017⌶`) does not.


`Y` is a character string containing the name of a .NET object. Unless the fully qualified name is given, the namespaces in the current AppDomain are searched in the order they are specified by  `⎕USING` or `:Using`.


If the object is identified in the current AppDomain, the result `R` is its Type. If not, the function generates `DOMAIN ERROR`.

<h2 class="example">Example</h2>
```apl
      ⎕USING←'System'
      2017⌶'DateTime'
System.DateTime
```



