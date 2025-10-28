<h1 class="heading"><span class="name">The SimpleCtl Control</span></h1>

The `SimpleCtl` Class is illustrated below:
```apl
:Class SimpleCtl: Control                       
:Access public                                  
:Using System                                   
:Using System.Collections.Specialized,System.dll
:Using System.Web,System.Web.dll                
:Using System.Web.UI                            
:Using System.Web.UI.WebControls                
:Using System.Web.UI.HtmlControls               
                                                
    ∇ Render output;HTML                        
      :Access public override                 
      :Signature Render  HtmlTextWriter output
      HTML←'<h3>Hello World</h3>'               
      output.WriteLine⊂HTML                     
    ∇                                           
                                                
:EndClass ⍝ SimpleCtl                           
```

The `Render` function **supercedes** (see [:Access Statement](../../../programming-reference-guide/defined-functions-and-operators/traditional-functions-and-operators/control-structures/class-declaration-statements/access)) the `Render` method that `SimpleCtl` has inherited from its base class, `System.Web.UI.Control`.

The `Render` method defined by the `System.Web.UI.Control` base class is `void` and takes a parameter of type `HtmlTextWriter`. When the `SimpleCtl` control is referenced in a Web Page, ASP.NET creates an instance of it and calls its `Render` method because it is a `Control` and is expected to have one. Moreover, ASP.NET supplies an object of type `HtmlTextWriter` as its parameter. You do not need to worry where this object came from, or what it actually represents. You need only know that an `HtmlTextWriter` provides a method called `WriteLine` that may be used to output a text string to the browser. The mechanics of how this actually happens are handled by the `HtmlTextWriter` object itself.

In APL terms, the argument to our `Render` function, `output`, will be a namespace reference, and the function can simply call its `WriteLine` method with a character vector argument. This argument can contain any valid HTML string and defines the appearance of the `SimpleCtl` control.

Using the `:Signature` statement, the `Render` function is defined to have the same syntax as the method it overrides, that is, it does not return a result  `void` and takes a single parameter of type `HtmlTextWriter`. Note that to successfully replace the base class method, the `Render` function must have exactly this *:Signature*.

## Using SimpleCtl

Our `SimpleCtl` control may now be included in any .NET Web Page from which `temp.dll` is accessible. The file `samples\asp.net\temp\Simple.aspx` is simply an example. The fact that this control is written in Dyalog is immaterial.
```xml
<%@ Register TagPrefix="Dyalog"
             Namespace="DyalogSamples" Assembly="temp" %>

<html>
<body>
<Dyalog:SimpleCtl runat=server/>
</body>
</html>

```

The first line of the script specifies that any controls referenced later in the script that are prefixed by `Dyalog:`, refer to custom controls in the .NET Namespace called `DyalogSamples` which is located in the Assembly `temp.dll` in the `bin` subdirectory.

![](../img/simplectl3.png)
