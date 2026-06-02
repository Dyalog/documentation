<h1 class="heading"><span class="name">Code-Behind</span></h1>

It can be desirable to separate the code content of a page completely from the HTML and other text, layout or graphical information by placing it in a separate file. In ASP.NET parlance, this technique is known as _code-behind_.

**[DYALOG]\Samples\asp.net\tutorial\intro5.aspx** illustrates this technique.
```nonAPL
<%@Page Language="Dyalog" Inherits="FruitSelection" src="fruit.apl" %>
<%@Register TagPrefix="tutorial" Namespace="Tutorial" Assembly="tutorial" %>
<html>
<head>
<title>Code behind: separating your code from the page layout</title>
<link rel="stylesheet" type="text/css" href="apl.css">
</head>
<body>
<h1>intro5: Code Behind</h1>
<p>This example illustrates how you can separate your code from the page layout.</p>
<form  runat="server" >
<asp:DropDownList id="list"
	runat="server"
	autopostback="true"
	OnSelectedIndexChanged="Select"/>
<p><asp:Label id="out" runat="server" /></p>
</form>
</body>
<tutorial:index runat="server"/>
</html>

```

This example is intended to be run in the framework of the tutorial; the two lines of code that refer to this framework (they each contain the word "tutorial") should be ignored.

The statement:
```nonAPL
%@Page Language="Dyalog" Inherits="FruitSelection" src="fruit.apl" %>
```

says that this page, when compiled, should inherit from a class called <code class="language-nonAPL">FruitSelection</code>; this class is written in the "Dyalog" language, and its source code resides in a file called **fruit.apl**. <code class="language-nonAPL">FruitSelection</code> is effectively the base class for the **.aspx** page.

In this example, **fruit.apl** is another text file containing the code and comprises:
```apl
:Class FruitSelection: System.Web.UI.Page
:Using System

∇Page_Load
:Access Public
:if 0=IsPostBack
    list.Items.Add ⊂'Pears'
    list.Items.Add ⊂'Nectarines'
    list.Items.Add ⊂'Strawberries'
:endif
∇

∇Select args
:Access public
:Signature Select Object,EventArgs
out.Text←'You selected ',list.SelectedItem.Text
∇
:EndClass
```

The file requires `:Class` and `:EndClass` statements. These tell the Dyalog .NET Compiler the name of the class being defined and the name of its base class. When the source code is in a **.aspx** file, this information is provided automatically by the Dyalog .NET Compiler.

The name of the class (in this case, <code class="language-nonAPL">FruitSelection</code>) must be the same name as is referenced in the **.aspx** web page file (**intro5.aspx**). The base class must be <code class="language-nonAPL">System.Web.UI.Page</code>.

The body of the script is the same as the script section in the example in **[DYALOG]\Samples\asp.net\tutorial\intro3.aspx** (see [The Page_Load Event](the-page-load-event.md)) – only the names of the fruit have been changed so that it is clear which example is being executed.
