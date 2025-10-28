<h1 class="heading"><span class="name">Introduction</span></h1>

Windows Presentation Foundation is a graphical system that includes  a programmable Graphical User Interface. It is supplied as a set of Microsoft .NET assemblies and is supported on all current Windows platforms.

The WPF GUI is in many ways more sophisticated and powerful than either Dyalog's own built-in GUI or the GUI provided by Windows Forms.

Like any other set of .NET classes, WFP can be integrated into Dyalog applications via the .NET interface. Dyalog users may therefore develop GUI applications that are based upon WPF as an alternative to the built-in Dyalog GUI or  Windows Forms.

Quite apart from its advanced GUI capabilities, WPF supports *data binding*. This is a complex subject, but putting it very simply, data binding allows  a property of a user-interface object (such as the Text property of a TextBox object) to be bound to some data. When the data changes, the bound property of the object changes and vice versa.

Dyalog includes a data binding function (`2015⌶`[^1]) which supports data binding to APL arrays and namespaces.

A WPF GUI can be built dynamically by creating a set of component objects (using `⎕NEW`) in a similar way to the Dyalog GUI and Windows Forms. However, the same user-interface can instead be specified statically using XAML, a text markup system  that describes the GUI using XML. Along with data binding, this feature allows the application logic and the user-interface to be developed and maintained separately.

The examples described in this section are provided in the workspace `WPFIntro.dws`

[^1]: This function may remain as an I-beam or be replaced by one or more system functions in a future Version of Dyalog.
