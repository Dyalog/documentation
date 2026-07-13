#  Introduction

OLE Automation is an inter-process communication mechanism created by Microsoft, based on a subset of Component Object Model (COM).

See (for example) [https://en.wikipedia.org/wiki/OLE_Automation](https://en.wikipedia.org/wiki/OLE_Automation).

OLE Automation allows you to drive one application from another and to mix code written in different programming languages.  In practical terms, this means that you may write a subroutine to perform calculations in (say) C++ and use the subroutine directly in Visual Basic 4 or Excel.  Equally, you could write the code in Visual Basic and call it from C++.  Dyalog APL/W is a fully subscribed member of this code-sharing club.

OLE Automation is, however, much more than just a mechanism to facilitate cross-application macros because it deals not just with subroutine calls but with *objects*.  An object is a combination of code and data that can be treated as a unit.  Without getting too deeply into the terminology, an object defines a *class*; when you work with an object you create one or more *instances* of that class.

There are two types of OLE object involved; OLE servers and ActiveX controls. There are two types of OLE server; in-process and out-of-process. In-process OLE servers and ActiveX controls are implemented as dynamic link libraries that are loaded into a host-process at run-time. Out-of-process OLE Servers are implemented as separate processes which may even run on a separate computer in a network.

Dyalog can act as a host for OLE servers and ActiveX controls, and you may also create OLE servers and ActiveX controls in Dyalog that can be hosted by other applications, including Microsoft Office programs.

## Architectural Issues

32-bit and 64-bit dynamic link libraries are compatible only with programs compiled for the same architecture, but a 64-bit process cannot load a 32-bit DLL and a 32-bit process cannot load a 64-bit DLL.

This means that the 64-bit Dyalog interpreter can only access a 64-bit in-process OLE servers and ActiveX Controls and the 32-bit Dyalog interpreter can only access 32-bit in-process COM servers and ActiveX controls.

Similarly, an in-process OLE server (dll) or ActiveXControl (ocx) saved by the 64-bit Dyalog interpreter cannot be used by a 32-bit application, and one saved by the 32-bit Dyalog interpreter cannot be used by a 64-bit application. If you try to do so, the application will generate an error. For example, if you were try to load the cfiles.dll or loan.dll saved as an in-process OLE server by the 64-bit Dyalog interpreter into a 32-bit version of Microsoft Excel, it would fail; as would a 32-bit Dyalog dll in a 64-bit version of Excel.

This restriction does not apply to out-of-process OLE servers, which are implemented as separate processes.

## Hosting OLE Servers and ActiveX Controls

This chapter describes how Dyalog APL can drive other applications using OLE Automation. In these circumstances, Dyalog APL is acting as an OLE *client*. The following chapters describe how you can build OLE servers and ActiveX controls in Dyalog.

An ActiveX control can be instantiated as a GUI object within a Dyalog APL Form, whereas an OLE Server either has no GUI component, or is a separate object. Otherwise, the two are very similar.

You can obtain lists of the OLE Servers and ActiveX Controls installed on your computer from the OLEServers and OLEControls properties of the system object `'.'`. These lists are obtained from your Windows Registry and therefore contain only those OLE objects that are correctly installed. Each OLE Server and OLE Control is identified by its name and class identifier. Either may be used to access it.

The list of COM servers reported by the OLEServers and OLEControls properties of Root return only those COM objects that can be accessed from that version of the Dyalog interpreter. 
