# Overview

## What is an ActiveX Control ?

An ActiveX Control is a dynamic link library that represents a particular type of COM object. When an ActiveX Control is loaded by a host application, it runs *in-process*, that is, it is part of the host application's address space. Furthermore, an ActiveX Control typically has a *window* associated with it, which normally appears on the screen and has a user interface.

An ActiveX Control is usually stored in file with the extension .OCX. The functionality provided by the control can be supplied entirely by functions in that file alone, or can be provided by other dynamic link libraries that it loads and calls, that is, an ActiveX Control can be stand-alone or can rely on one or more other dynamic link libraries.

## What is a Dyalog APL ActiveX Control ?

An ActiveX Control written using Dyalog APL is also a file with a .OCX extension. The file combines a small dynamic link library *stub* and a workspace. The functionality of the control is provided by the functions and variables in the workspace combined with the dynamic link library version of Dyalog APL.

Note that an ActiveX Control written in Dyalog APL is a GUI object that has a visible appearance and a user interface.

To write an ActiveX Control in Dyalog APL, you use `⎕WC` to create an ActiveXControl object, as a child of a Form. An ActiveXControl is a container object, akin to a Group or a SubForm, that may contain a whole range of other controls such as Edit, Combo, Button and Grid objects. You may populate your ActiveXControl with other objects at this stage and save them in the workspace. However, you may prefer to create these sub-objects when an instance of the ActiveXControl is created. This happens when your control is loaded by a host application.

All the functions and variables that represent methods and properties through which the ActiveXControl object exports its functionality, reside within the ActiveXControl namespace.

You may turn a workspace containing one or more ActiveXControl objects into an installable OCX file by selecting the *Export* menu item  from the Session *File* menu.

Note that a single OCX file can therefore contain a number of ActiveX Controls.

When a Dyalog APL ActiveX Control is loaded by a host application, functions in the stub load the appropriate Dyalog APL dynamic link library (DyalogDLL for short) into the host application. Note that the Dyalog dll must either be on the system PATH or be in the same directory as the OCX file.

The Dyalog dll  copies the appropriate parts of the workspace from the .OCX. If the same host application starts a second (different) ActiveX Control written in Dyalog APL, the appropriate parts of the second workspace are merged with the first. For further details, see the section entitled Workspace Management.

## The Dyalog APL DLL

ActiveXControls are hosted (executed) by the Dyalog APL DLL. For further details, see [COM Objects and the Dyalog APL DLL](../../../windows-installation-and-configuration-guide/com-objects-and-the-dyalog-dll).

## Instance Creation

When a host application creates an instance of an ActiveXControl object, the new instance generates a Create event. It is recommended that you make any GUI objects that you need within the ActiveXControl *at this stage*, rather than making them in advance and saving them in the workspace.

The reason for this is that until an instance of an ActiveXControl is created, its Size and *ambient properties* are not known. Ambient properties include the font (which may affect the size and position of the internal controls) and background and foreground colours. These are specified by the host application and should normally be honoured by the ActiveXControl. Although when you are developing an ActiveXControl it will have a specific size, the size of an *instance* of the object cannot be predicted in advance because it is determined by the host application. This alone is sufficient reason to delay the creation of sub-objects inside the ActiveXControl until the Create event occurs.

In addition to the Create event, ActiveXControl objects support a PreCreate event. This event is always generated before a Create event and signals the creation of a newly cloned namespace. However, it is reported *before* the host application has assigned it a *window*. You may therefore not use the PreCreate event to create sub-objects, but you may use it for other initialisation tasks if applicable. Many host applications distinguish between design mode, when the user may just place controls in a GUI framework, and run mode when the controls become fully active. Some applications, such as Microsoft Access, do not require the control to appear fully in design mode, but instead represent the control by a simple rectangle or bitmap. In these cases, the ActiveXControl will generate a PreCreate event in design mode and not generate a Create event until run-time. Others, like Visual Basic, require that the control appears in design mode as it would appear in the final application. In these cases, the Create event follows immediately after PreCreate.

## Properties, Methods and Events

Typically, an ActiveX Control provides Properties, Methods and Events that allow the control to be configured and controlled by a host application.

The information about the properties, methods and events exported by an ActiveX Control is normally stored in its .OCX file. The information includes the name of each property and its data type, and the name and data type of each method and each of its arguments. The information for an event is similar to that for a method. In addition to these obligatory items, it is possible to include help strings and help ids which provide on-line documentation for the host application programmer

Dyalog APL provides facilities for you to specify all this information in one of two ways; using dialog boxes or by calling methods.

Firstly, the Properties dialog box for an ActiveXControl object includes three additional tabs named *COM Properties*, *COM Functions* and *COM Events*. These dialog boxes allow you to export variables as properties, to export functions as either properties or methods, and to export events. In addition, the individual Properties dialog boxes for all the functions and variables in an ActiveXControl namespace have an additional *COM Properties* tab which performs the same function. Examples of these dialog boxes are provided in the tutorial section of this chapter.

Secondly, the ActiveXControl object provides three (internal) methods that allow you to specify this information by executing APL statements. These methods are named SetVarInfo, SetFnInfo and SetEventInfo and examples of their use is given in the tutorial.

## Generating Events

Events that are generated by Dyalog APL GUI objects *inside* an ActiveXControl are purely internal events and are not detectable by a host application. However, an ActiveXControl object may generate an arbitrary event for a host application using `⎕NQ` with a left argument of 4.

An external event must have a name (numbers are not allowed) and may include one or more parameters that supply additional information. The name of the event and the name and data types of each of its parameters must be defined in advance using the COM Events tab of the Properties dialog box of the ActiveXControl object, or by calling its SetEventInfo method.

For example, the Dual control described in the tutorial has an event called ChangeValue1. This event supplies a parameter named Value1 that has a data type of VT_PTR  to VT_I4 (pointer to an integer). The Dual control *generates* the event for the host application by executing the statement:
```apl
      4 ⎕NQ '' 'ChangeValue1' Value1
```

where `Value1` is the new value of its internal Slider control.

A host application may choose to ignore an event generated by an ActiveXControl, or it may attach a callback function that performs some action in response to the event. A callback function in the host application receives the parameters supplied by the event as parameters to the function. If the host application is Dyalog APL itself, the callback function receives the parameters as part of the event message.

A host application callback function may not return a result. However, it may modify any of the parameters that were supplied as part of the event message if those parameters are defined as pointers (VT_PTR to xxx).

The result of `4 ⎕NQ` is therefore a vector whose elements correspond to the pointer parameters in the order they were specified. The result does not contain elements for parameters that were not exported as pointers and may therefore be empty. In the above example, the result of `4 ⎕NQ` is a 1-element vector containing the, possibly modified, value of `Value1`.
