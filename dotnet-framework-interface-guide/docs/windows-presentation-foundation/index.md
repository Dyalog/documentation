<h1 class="heading"><span class="name">Windows Presentation Foundation</span></h1>

Windows Presentation Foundation (WPF) is a graphical system that includes a programmable Graphical User Interface. It is supplied as a set of Microsoft .NET assemblies, and is supported on all current Microsoft Windows platforms.

The WPF GUI is more sophisticated and powerful than either Dyalog's own built-in GUI or the GUI provided by Windows Forms.

Like any other set of .NET classes, WFP can be integrated into Dyalog applications through the .NET interface. Dyalog users can, therefore, develop GUI applications that are based on WPF as an alternative to the built-in Dyalog GUI or  Windows Forms.

In addition to its advanced GUI capabilities, WPF supports _data binding_. Data binding is complex, but essentially it allows a property of a user-interface object (such as the <code class="language-nonAPL">Text</code> property of a <code class="language-nonAPL">TextBox</code> object) to be bound to some data, so that when the data changes, the bound property of the object changes.

Dyalog includes a data binding function in the form of an I-beam – `2015⌶` – that supports data binding to APL arrays and namespaces. This function might be replaced by one or more system functions in a future Dyalog version.

A WPF GUI can be built dynamically by creating a set of component objects (using `⎕NEW`) in a similar way to the Dyalog GUI and Windows Forms. However, the same user interface can instead be specified statically using XAML, a text mark-up system  that describes the GUI using XML. When combined with data binding, this allows the application logic and the user interface to be developed and maintained separately.

!!! Legacy "Legacy"
    Dyalog v19.0 and earlier included a licence to use the [Syncfusion](https://www.syncfusion.com/) library of WPF controls. This is no longer included with Dyalog, and you must not use Syncfusion controls in application development or distribute them with run-time applications unless you purchase a licence to do so from them directly.
