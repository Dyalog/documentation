# <span>OLEServer</span> <span>Object</span>

**Purpose:** The OLEServer object is used to establish a namespace as an OLE Server         object that can be used by an OLE Automation client.

**Description**

The OLEServer object allows you to export an APL namespace so that its
functions and variables become directly accessible to an OLE Automation client
application such as Microsoft Visual Basic or Microsoft Excel.

An OLEServer may be saved as an *out-of-process* OLE server (in a
workspace) or as an *in-process* OLE server (in a DLL). See *Interface
Guide* for details.

When you create an OLEServer object, APL allocates various OLE attributes to
it. For example, the CLSID, which uniquely identifies the object, is assigned at
this stage. However, the object is not actually *registered* until you
execute )SAVE.

Registration involves updating the Windows registry with information about
the object itself, such as its name, the command required to obtain it and so
forth. Registration also records information about all of the functions and
variables that your object exposes. Registration is therefore a non-trivial
operation and should be delayed until the point when you are ready to test your
OLEServer.

You may create an empty OLEServer object and then define functions and
variables within it. Alternatively, you may convert an existing namespace which
is already populated with functions and variables. The latter method is
recommended as it implies less registry activity during the development of the
object.

The [ExportedFns](../properties/exportedfns.md) and [ExportedVars](../properties/exportedvars.md) properties specify the names of the functions and variables that will be exposed
by the object to OLE clients.

The [RunMode](../properties/runmode.md) property is a character
vector that specifies how the object serves multiple clients. It may be `'MultiUse'` (the default), `'SingleUse'`, or `'RunningObject'`.

The [ShowSession](../properties/showsession.md) property is either 0
(the default) or 1 and specifies whether or not the APL Session window is
displayed when the first instance of the OLEServer is created.

[RunMode](../properties/runmode.md) and [ShowSession](../properties/showsession.md) apply only to *out-of-process* OLEServers.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [Form](../objects/form.md), [OLEServer](../objects/oleserver.md), [Root](../objects/root.md)

Children: [Bitmap](../objects/bitmap.md), [BrowseBox](../objects/browsebox.md), [Clipboard](../objects/clipboard.md), [Cursor](../objects/cursor.md), [FileBox](../objects/filebox.md), [Font](../objects/font.md), [Form](../objects/form.md), [Icon](../objects/icon.md), [ImageList](../objects/imagelist.md), [Menu](../objects/menu.md), [Metafile](../objects/metafile.md), [MsgBox](../objects/msgbox.md), [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md), [OLEServer](../objects/oleserver.md), [Printer](../objects/printer.md), [PropertySheet](../objects/propertysheet.md), [TCPSocket](../objects/tcpsocket.md), [Timer](../objects/timer.md), [TipField](../objects/tipfield.md)

Properties: [ChildList](../properties/childlist.md), [ClassID](../properties/classid.md), [ClassName](../properties/classname.md), [Data](../properties/data.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [ExportedFns](../properties/exportedfns.md), [ExportedVars](../properties/exportedvars.md), [Handle](../properties/handle.md), [KeepOnClose](../properties/keeponclose.md), [LastError](../properties/lasterror.md), [LateBind](../properties/latebind.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [RunMode](../properties/runmode.md), [ServerVersion](../properties/serverversion.md), [ShowSession](../properties/showsession.md), [Type](../properties/type.md), [TypeLibFile](../properties/typelibfile.md), [TypeLibID](../properties/typelibid.md)

Methods: [Detach](../methodorevents/detach.md), [OLERegister](../methodorevents/oleregister.md), [OLEUnregister](../methodorevents/oleunregister.md), [SetEventInfo](../methodorevents/seteventinfo.md), [SetFnInfo](../methodorevents/setfninfo.md), [SetVarInfo](../methodorevents/setvarinfo.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md)
