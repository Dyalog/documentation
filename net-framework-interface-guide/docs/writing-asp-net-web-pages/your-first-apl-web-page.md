<h1 class="heading"><span class="name">Your first APL Web Page</span></h1>

The first web page example is `tutorial/intro1.aspx`, which is listed below. This page displays a button whose text is reversed each time you press it.

Note that the example is intended to be run in the framework of the tutorial and contains two lines of code (shown in italic) that refer to this framework and should be ignored.
```
<%@Register TagPrefix="tutorial" Namespace="Tutorial" Assembly="tutorial" %>
<script language="Dyalog" runat="server">
 
∇Reverse args
:Access public
:Signature Reverse Object,EventArgs
(⊃args).Text←⌽(⊃args).Text
∇
 
</script>
 
<html>
<body>
<Form runat=server>
      <asp:Button id="Pressme" 
      Text="Press Me"
      runat="server"
      OnClick="Reverse" 
      />
</form>
<tutorial:index runat="server"/>
</body>
</html>
```

In this example, the page language is defined in the `<script>` section to be `"Dyalog"`. This in turn is mapped to the `APLScript` compiler via information in the application's web.config file or the global IIS configuration file, `machine.config`.

The page layout is described in the section between the `<html>` and `</html>` tags. This page contains a Form in which there is a Button labelled (initially) "Press Me"

The Form and Button page elements may appear to be simple HTML, but in fact there is more to them than meets the eye and they are actually both types of ASP.NET *intrinsic controls*.

Firstly, the `runat="server"` attribute indicates that an HTML element should be parsed and treated as an HTML server control. Instead of being handled as pure text that is to be transmitted to the browser "as is", an HTML server control is effectively compiled into statements that then generate HTML when executed. Furthermore, an HTML server control can be accessed programmatically by code in the Script, whereas a pure HTML element cannot. On its own, `runat="server"` identifies the HTML element as a so-called *basic* intrinsic control.

When you add `runat="server"` to a Form, ASP.NET automatically adds other attributes that cause the values of its controls to be POSTed back to the same page. In addition, ASP.NET adds a HIDDEN control to the form and stores state information in it. This means that when the page is reloaded into the browser the state and contents of some or all of its controls can be maintained, without the need for you to write additional code.

The `asp:` prefix for the Button, identifies the control as a *special* ASP.NET intrinsic control. These are fully-fledged .NET Classes in the .NET Namespace `System.Web.UI.WebControls` that expose properties corresponding to the standard attributes that are available for the equivalent HTML element. You manipulate the control as an object, while it, at runtime, emits HTML that is inserted into the page.

At this point, it is instructive to study what happens when the page is first loaded and the appearance of the page is illustrated below.

![](../img/intro1-1.png)

The HTML that is transmitted to the browser is:
```html
<html>
<body>
	<form name="ctrl1" method="post" action="intro1.aspx" id="ctrl1">
<input type="hidden" name="__VIEWSTATE"
value="YTB6NTQ3ODg0MjcyX19feA==5725bd57" />

		<input type="submit" name="Pressme" value="Press Me"
id="Pressme" />
	</form>
</body>
</html>

```

Firstly, notice that, as expected, the contents of the `<script>` section are not present. Secondly, because the Form and Button are intrinsic controls, ASP.NET has added certain attributes to the HTML that were not specified in the source code.

The Button now has the added attribute `input type="submit"`, which means that pressing the Button causes the contents of the Form to be transmitted back to the sever.

The Form now has `method="post"` and `action="intro1.aspx"` attributes, which means that, when the Form is submitted, the data is POSTed back to `intro1.aspx`, the page that generated the HTML in the first place.

So when the user presses the button, the browser sends back a POST statement, with the contents of the Form, including the value of the HIDDEN field, requesting the browser to load `intro1.aspx`.

In the server, ASP.NET reloads the page and processes it again. In fact, because of the stateless nature of HTTP, the server does not know that it is reprocessing the same page, except that it is being executed by a POST command with the hidden data embedded in the Form that it put there the first time around. This is the mechanism by which ASP.NET *remembers* the state of a page from one invocation to another.

This time, because a POST back is loading the page, and because the `Pressme` button caused the POST, ASP.NET executes the function associated with its `onClick` attribute, namely the `APLScript` function `Reverse`.

When it is called, the argument supplied to Reverse contains two items. The first of these is an object that represents the control that generated the `onClick` event; the second is an object that represents the event itself. In fact, `Reverse` and its argument are very similar to a standard Dyalog callback function.

```apl
∇Reverse args
:Access public
:Signature Reverse Object,EventArgs
(⊃args).Text←⌽(⊃args).Text
∇
```

The code in the `Reverse` function is simple. The expression (`⊃args`) is a namespace reference (ref) to the Button, and (`⊃args`).Text refers to its Text property whose value is reversed. Note that `Reverse` could just as easily refer to the Button by name, and use `Pressme.Text` instead.

After pressing the button, the page is redisplayed as shown below:

![](../img/intro1-2.png)

This time, the HTML generated by `intro1.aspx` is:
```apl
<html>
<body>
	<form name="ctrl1" method="post" action="intro1.aspx" id="ctrl1">
<input type="hidden" name="__VIEWSTATE"
value="YTB6NTQ3ODg0MjcyX2Ewel9oejV6MXhfYTB6X2h6NXoxeF9hMHph
MHpoelRlXHh0X2VNIHNzZXJQeF9feF9feHhfeHhfeF9feA==45acf576"
/>

		<input type="submit" name="Pressme" value="eM sserP"
id="Pressme" />
	</form>
</body>
</html>

```

Returning to the `Reverse` function, note that the declaration statements at the top of the function are essential to make it callable in this context.

```apl
∇Reverse args
:Access public
:Signature Reverse Object,EventArgs
(⊃args).Text←⌽(⊃args).Text
∇
```

Firstly the `Reverse` function must be declared as a public member of the script. This is achieved with the statement.
```apl
:Access Public
```

Secondly, the .NET runtime will only call the function if it possesses the correct signature, which is derived from its parameters and their types.

The required signature for a method connected to an event, such as the OnClick event of a Button, is that it takes two parameters; the first of which is of type `System.Object` and the second is of type `System.EventArgs`. The `Reverse` function declares its parameters with the statements:
```apl
:Signature Reverse Object,EventArgs
```

Note that the parameter declarations do not include the `System` prefix. This is because when the script is compiled the names are resolved using the current value of `⎕USING`. When the `APLScript` is *compiled*, the default value for `⎕USING` is automatically defined to contain `System` along with most of the other namespaces that will be used when writing web pages

(Strictly speaking, the first argument is expected to be of type `System.Web.UI.WebControls.Button`, but as this type inherits ultimately from `System.Object` the function signature is satisfied.)

Note that if the `Reverse` function is defined with a signature that does not match that expected signature for the OnClick callback, the function will not be run.

Furthermore, if the function associated with the OnClick statement is not defined as a public method in the `APLScript` the page will appear to compile but the `Reverse` function will not get executed.

Note that unlike Web Services, there is no requirement for a `:Class` or `:EndClass` statement in the script. This is because a file with an `.aspx` extension implicitly generates a class that inherits from `System.Web.UI.Page`.
