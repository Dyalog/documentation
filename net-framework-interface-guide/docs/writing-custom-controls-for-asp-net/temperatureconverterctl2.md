<h1 class="heading"><span class="name">The TemperatureConverterCtl2 Control</span></h1>

The previous example showed how to compose an ASP.NET custom control from other standard controls. This example shows how you can instead generate standard form elements on the browser by rendering the HTML for them directly.

In the composite temperature control `TemperatureConverterCtl1`, discussed previously, all the data transfers between the browser and the server, relating to the standard child controls that it contains, are handled automatically by the controls themselves. Rendered controls require a bit more programming because it is up to the control developer to do the data transfer. The data transfer is managed through two interfaces, namely `IPostBackDataHandler` and `IPostBackEventHandler`. We will see how these interfaces are used later.

The `:Class` statement for `TemperatureConverterCtl2` specifies that it provides these interfaces.
```apl
:Class TemperatureConverterCtl2: Control,
                  System.Web.UI.IPostBackDataHandler,
                  System.Web.UI.IPostBackEventHandler
```

## Fahrenheit and Centigrade Values

Like the previous `TemperatureConverterCtl1` control, the `TemperatureConverterCtl2` maintains two public properties named `CentigradeValue` and `FahrenheitValue` using property *get* and property *set* functions.

This time, the control manages the current temperature values in two internal variables named `_CentigradeValue` and `_FahrenheitValue`, which we must initialise.
```apl
      _CentigradeValue←0
      _FahrenheitValue←0
```

The `CentigradeValue`'s `get` function simply returns the current value of `_CentigradeValue`. Its .NET Properties are defined as shown so that it is exported as a *property get* function for the `CentigradeValue` property, and returns a `Double`.
```apl
       ∇ C←get
        :Access Public
        :Signature Double←get
        C←_CentigradeValue
       ∇

```

The `CentigradeValue`'s `set` function simply resets the value of `_CentigradeValue` to that of its argument. Its .NET Properties are defined as shown so that it is exported as a *property set* function for the `CentigradeValue` property, and takes a `Double`.
```apl
       ∇ set C
        :Access Public
        :Signature set Double Value
        _CentigradeValue←C.NewValue
       ∇
```

The property *get* and property *set* functions for the `FahrenheitValue` property are similarly defined. The .signatures for these functions are similar to those for the `CentigradeValue` functions and are not shown.

## Rendering the Control

Like the `SimpleCtl` example described earlier in this Chapter, the `TemperatureConverterCtl2` control has a `Render` function that generates the HTML to represent its appearance, and in this case its behaviour too.
```apl
     ∇ Render output;C;F;BF;CF
[1]    :Access Public override
[2]    :Signature Render HtmlTextWriter output
[3]
[4]    F←'<h3>Fahrenheit <input name='
[5]    F,←UniqueID
[6]    F,←' id=FahrenheitValue type=text value='
[7]    F,←⍕_FahrenheitValue
[8]    F,←'></h3>'
[9]    output.Write⊂F
[10]
[11]   C←'<h3>Centigrade <input name='
[12]   C,←UniqueID
[13]   C,←' id=CentigradeValueKey type=text value='
[14]   C,←⍕_CentigradeValue
[15]   C,←'></h3>'
[16]   output.Write⊂C
[17]
[18]   BF←'<input type=button value=FahrenheitToCentigrade '
[19]   BF,←' onClick="jscript:'
[20]   BF,←Page.GetPostBackEventReference ⎕THIS'FahrenheitToCentigrade'
[21]   BF,←'">'
[22]   output.Write⊂BF
[23]
[24]   CF←'<input type=button value=CentigradeToFahrenheit '
[25]   CF,←' onClick="jscript:'
[26]   CF,←Page.GetPostBackEventReference ⎕THIS'CentigradeToFahrenheit'
[27]   CF,←'">'
[28]   output.Write⊂CF
[29]
[30]   output.WriteLine∘⊂¨'' '<br>' '<br>'
     ∇
```

As we saw in the `SimpleCtl` example, the `Render` method will be called by ASP.NET with a parameter that represents an `HtmlTextWriter` object. This is represented by the APL local name `output`.

Lines[4-9] and lines [11-16] generate HTML that defines two text boxes in which the user may enter the Fahrenheit and centigrade values respectively. Lines[9&16] use the `Write` method of the `HtmlTextWriter` object to output the HTML.

Lines[5&12] obtain the fully qualified identifier for this particular instance of the `TemperatureConverterCtl2` control from its `UniqueID` property. This is a property, which it inherits from `Control` and is therefore also a property of the current (APL) namespace.

Lines[18-22] and Lines[24-28] generate and output the HTML to represent the two buttons that convert from Fahrenheit to Centigrade and from Centigrade to Fahrenheit respectively.

Lines[19-20] and [25-26]generate HTML that wires the buttons up to JavaScript handlers to be executed *by the browser*. The JavaScript simply causes the browser to execute a postback, that is, send the page contents back to the server. `GetPostBackEventReference` is a (shared) method provided by the `System.Web.UI.Page` class that generates a reference to a client-side script function. In this case it is called with two parameters, an object that represents the current instance of the `TemperatureConverterCtl2` control, and a string that will be passed to the server to indicate the cause of the postback (that is, which button was pressed). The first parameter is a reference to the current object, which is returned by the system function `⎕THIS`.

The client-side script is itself generated, and inserted into the HTML stream automatically.

To help to understand this process fully, it is instructive to examine the HTML that is generated by these functions. We will do this a bit later in the Chapter.

## Loading the Posted Data

Once the server-side control has rendered the HTML for the browser, the user is free to type numbers into the text boxes and to press the buttons.

When the user presses a button, the browser runs the client-side JavaScript code that in turn generates a postback to the server.

The `:Class` statement for  `TemperatureConverterCtl2` specifies that it supports the `IPostBackDataHandler` interface. This interface must be implemented by controls that want to receive postback data (that is, the contents of Form fields that the user may have entered or changed) `IpostBackDataHandler` has two methods `LoadPostData` and `RaisePostDataChangedEvent`. `LoadPostData` is automatically invoked when a postback occurs, and the postback data is supplied as a parameter.

So when the postback occurs, the server reloads the original page and, because this is a postback situation and our control has advertised the fact that it implements `IPostBackDataHandler`, ASP.NET invokes its `LoadPostBack` method. This method is called with two parameters. The first is a key and the second is a collection of name/value pairs. This contains the names of all the Form fields on the page (and there may be others not directly associated with our custom control) and the values they had when the user pressed the button. The key provides the means to extract the relevant part of this collection. The `LoadPostData` function is shown below.
```apl
     ∇ R←LoadPostData args;postDataKey;values;controlValues;new
[1]    :Signature Boolean←IPostBackDataHandler.LoadPostData String postDataKey,NameValueCollection values
[2]    postDataKey values←args
[3]    controlValues←values[⊂postDataKey]
[4]    new←ParseControlValues controlValues
[5]    R←∨/new=_FahrenheitValue _CentigradeValue
[6]    _FahrenheitValue _CentigradeValue←new
     ∇

```

Line[2] obtains the two parameters from the argument and Line[3] uses the key to extract the appropriate data from the collection. `ControlValues` is a comma-delimited string containing name/value pairs. The function `ParseControlValues` simply extracts the values from this string, that is, the contents of the Fahrenheit and Centigrade text boxes.

## Postback Events

The result of `LoadPostData` is Boolean and indicates whether or not any of the values in a control have changed. If the result is `True` (1), ASP.NET will next call the `RaisePostDataChanged` method. This method is called with no parameters and merely signals that something has changed. The control knows *what* has changed by comparing the old with the new, as in `LoadPostData[5]`.

Finally, the page framework calls the `RaisePostBackEvent` method, passing it a string that identifies the page element that caused the post back.

The objective of these calls is to provide the control with the information it requires to synchronise its internal state with its appearance in the browser.

In this case, we are not interested in which of the two text box values the user has altered; what matters is which of the two buttons *FarenheitToCentigrade* or *CentigradeToFarenheit* was pressed. Therefore, in this case, the control uses `RaisePostBackEvent` rather than `RaisePostDataChanged` (or indeed, `LoadPostData` itself, which is another option). The reason is that `RaisePostBackEvent` receives the name of the button as its argument.

So in our case, the `RaisePostDataChanged` function does nothing. Nevertheless, it is essential that the function is provided and essential that it supports the correct public interface, namely that it takes no arguments are returns no result (`Void`).
```apl
     ∇ RaisePostDataChangedEvent
[1]  :Access public
[2]  :Signature RaisePostDataChangedEvent
[3]  ⍝ Do nothing
     ∇
```

The `RaisePostBackEvent` function simply switches on its argument, which is the name of the button that the user pressed, and recalculates `_CentigradeValue` or `_FahrenheitValue` accordingly.
```apl
     ∇ RaisePostBackEvent eventArgument
[1]    :Access public
[2]    :Signature RaisePostBackEvent  String eventArg
[3]    :Select eventArgument
[4]    :Case 'FahrenheitToCentigrade'
[5]        _CentigradeValue←F2C _FahrenheitValue
[6]    :Case 'CentigradeToFahrenheit'
[7]        _FahrenheitValue←C2F _CentigradeValue
[8]    :EndSelect
     ∇
```

Finally, the page framework calls the `OnPreRender` and `Render` functions again, which generate new HTML for the browser.

## Using the Control on a Page

So long as it has access to this `DLL`, our custom control may be accessed from any ASP.NET Web Page, and a simple example is shown below.
```xml
<%@ Register TagPrefix="Dyalog" Namespace="DyalogSamples"
                                Assembly="TEMP" %>

<html>
<body bgcolor="yellow">
<center>
<h2><font face="Verdana" color="black">
Temperature Control</font></h3>
<h3><font face="Verdana" color="black">
Server-Side Noncompositional control</font></h4>

<form runat=server>
<Dyalog:TemperatureConverterCtl2 id=TempCvtCtl2 
runat=server/>
</form>

</center>
</body>
</html>

```

The HTML that is generated by the control is illustrated below. Notice the presence of a JavaScript function named `__doPostBack`. This is generated by the `RegisterPostBackScript` method called from the `OnPreRender` function. The code that wires the buttons to this function was generated by the `GetPostBackEventReference` method called from the `Render` function.

```html
<html>
<body bgcolor="yellow">
<center>
<h2><font face="Verdana" color="black">Temperature Control</font></h2>
<h4><font face="Verdana" color="black">Server-Side Noncompositional control</font></h4>

 
<form name="ctrl1" method="post" action="temp2.aspx" id="ctrl1">
<input type="hidden" name="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" value="YTB6MTc3MzAxNzYxM19fX3g=9cfcfa5c" />

<script language="javascript">
<!--
	function __doPostBack(eventTarget, eventArgument) {
		var theform = document.ctrl1
		theform.__EVENTTARGET.value = eventTarget
		theform.__EVENTARGUMENT.value = eventArgument
		theform.submit()
	}
// -->
</script>

<h2>Fahrenheit <input name=TempCvtCtl2 id=FahrenheitValue type=text value=0></h2><h2>Centigrade <input name=TempCvtCtl2 id=CentigradeValueKey type=text value=0></h2><input type=button value=FahrenheitToCentigrade  onClick="jscript:__doPostBack('TempCvtCtl2','FahrenheitToCentigrade')"><input type=button value=CentigradeToFahrenheit  onClick="jscript:__doPostBack('TempCvtCtl2','CentigradeToFahrenheit')">
<br>
<br>

</form>

</center>
</body>
</html>
```

![](../img/temperatureconverterctl2.png)
