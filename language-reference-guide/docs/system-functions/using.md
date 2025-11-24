---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕USING USING
</div>






<h1 class="heading"><span class="name">Using (Microsoft .NET Search Path)</span> <span class="command">⎕USING</span></h1>



`⎕USING` specifies a list of Microsoft .NET Namespaces that are to be searched for a reference to a .NET class. `⎕USING` has Namespace scope.


`⎕USING` is a vector of character vectors each element of which contains 1 or 2 comma-delimited strings. The first string specifies the name of a .NET namespace; the second specifies the *pathname* of an assembly file. This may be a full pathname or a relative one, but must include the file extension (`.dll`). If just the file name is specified, it is assumed to be located in the standard  .NET Framework directory that was specified when the .NET Framework was installed (for example, `C:\Windows\Microsoft.NET\Framework64\v4.0.30319`)



It is convenient to treat .NET namespaces and assemblies in pairs. For example:
```apl
⎕USING←'System,mscorlib.dll'
  ⎕USING,←⊂'System.Windows.Forms,System.Windows.Forms.dll'  ⎕USING,←⊂'System.Drawing,System.Drawing.dll'
```


Note that because Dyalog APL automatically loads `mscorlib.dll` (which contains the most commonly used classes in the `System` Namespace), it is not actually necessary to specify it explicitly in `⎕USING`.


`⎕USING` has Namespace scope, that is, each Dyalog namespace, class or instance has its own value of `⎕USING` that is initially inherited from its parent space but which may be separately modified. `⎕USING` may also be localised in a function header, so that different functions can declare different search paths for .NET namespaces/assemblies.


If `⎕USING` is empty (`⎕USING←0⍴⊂''`), APL will not search for .NET classes in order to resolve names which would otherwise give a `VALUE ERROR`.


Assigning a simple character vector to `⎕USING` is equivalent to setting it to the enclose of that vector. The statement (`⎕USING←'')` does not empty `⎕USING`, it sets it to a single empty element, which gives access to `mscorlib.dll` and the  Bridge DLL without a namespace prefix.

## Notes

- The value of `⎕USING` is only used when an object is instantiated. Changing the value of `⎕USING` has no effect on objects that have already been instantiated in the active workspace.
- When a workspace containing .Net objects is saved, the names of the Net objects are saved with it but they are not automatically re-instantiated when the workspace is loaded or copied. A reference to such an orphaned object will report `(NULL)`. 
- Some functionality might work with .NET Framework or .NET but not both, for example, SharpPlot requires the .NET Framework and does not work with .NET itself.

<h2 class="example">Examples</h2>
```apl
  ⎕USING←'System'
  ]display ⎕USING
.→---------.
| .→-----. |
| |System| |
| '------' |
'∊---------'

⎕USING,←⊂'System.Windows.Forms,System.Windows.Forms.dll'
⎕USING,←⊂'System.Drawing,System.Drawing.dll'
```



An Assembly may contain top-level classes which are not packaged into .NET Namespaces. In this case, you omit the Namespace name. For example:
```apl
  ⎕USING←,⊂',.\LoanService.dll'
```



