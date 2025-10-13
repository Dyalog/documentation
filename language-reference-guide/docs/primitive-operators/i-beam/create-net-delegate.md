
<!-- Hidden search keywords -->
<div style="display: none;">
  2016⌶
</div>






<h1 class="heading"><span class="name">Create .NET Delegate</span> <span class="command">R←2016⌶Y</span></h1>



!!! note
    **.NET Framework only**


.NET methods (and properties) may specify a parameter to be a *delegate*. A delegate is a place holder for a function, normally with a particular signature and result type, that should be  supplied when the method is called. Sometimes the signature of a .NET method that takes a delegate as a parameter does not provide enough information for Dyalog to determine automatically what type of  delegate is required. `2016⌶` allows you to specify the type so that Dyalog can perform the necessary conversion(s) at run-time.



`Y` is a 2-element array. The first element is a .NET type that inherits from the abstract .NET Class System.Delegate. The second item is either the name of or the `⎕OR` of an APL function which is to be invoked via a .NET method or property.


The result `R` is a ref to an instance of a .NET type specified by the first element of `Y`, which internally is associated with the function identified by the second element of `Y`.


<h2 class="example">Example</h2>
```apl
      ∇foo∇
     ∇ foo(ev arg)
[1]    ⍝ Callback for .NET method
     ∇
      ⎕USING←'System'
      del←2016⌶ EventHandler'foo'
      del
System.EventHandler

```


Then, when calling a .NET method that requires a Delegate of type System.Eventhandler, but whose signature is imprecise in this respect, the object `del` should be used instead.



