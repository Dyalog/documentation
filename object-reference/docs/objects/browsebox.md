# <span>BrowseBox</span> <span>Object</span>

**Purpose:** The BrowseBox object allows the user to browse for and select a folder         or other resource.

**Description**

The BrowseBox object is a dialog box that allows the user to browse for and
			select a folder (directory) or other resource.

**For full functionality as described here, the BrowseBox object requires
the Windows Shell Library SHELL32.DLL Version 4.71 or higher. The BrowseBox
object also supports the enhanced functionality provided by SHELL32.DLL Version
5 (Windows 2000) if present.**

The [BrowseFor](../properties/browsefor.md) property specifies the
type of resource and may be `'Directory'`(the default), `'File'`, `'Computer'` or `'Printer'`.

The [StartIn](../properties/startin.md) property specifies the path
name where browsing should start.

The [HasEdit](../properties/hasedit.md) property specifies whether
or not the dialog box contains an edit field into which the user can type the
name of the folder or other resource, rather than browsing for it. The default
is 0.

A BrowseBox may only be used by the execution of a modal `⎕DQ`.
The action code for the FileBoxOK and FileBoxCancel events must be set to 1 so
that the appropriate result is returned by the modal `⎕DQ`.

After the user has pressed OK or Cancel, the [Target](../properties/target.md) property contains the name of the chosen folder or other resource.

<h2 class="example">Example</h2>
```apl
     ∇ DIR←{START_DIR}GetDir CAPTION;BB;MSG
[1]    ⍝ Ask user for a Directory name
[2]    ⍝ CAPTION specifies Caption for dialog box
[3]    ⍝ START_IN (optional) specifies starting directory
[4]    ⍝ DIR is empty if user cancels
[5]    :With 'BB'⎕WC'BrowseBox'
[6]        :If 2=⎕NC'START_DIR'
[7]            StartIn←START_DIR
[8]        :Else
[9]            StartIn←''
[10]       :EndIf
[11]       onFileBoxOK←onFileBoxCancel←1
[12]       Caption←CAPTION
[13]       HasEdit←1
[14]       MSG←⎕DQ''
[15]       :If 'FileBoxOK'≡2⊃MSG
[16]           DIR←Target ⍝ = 3⊃MSG
[17]       :Else
[18]           DIR←''
[19]       :EndIf
[20]   :EndWith
     ∇
```

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [OLEServer](../objects/oleserver.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [Root](../objects/root.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TCPSocket](../objects/tcpsocket.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Timer](../objects/timer.md)

Properties: [BrowseFor](../properties/browsefor.md), [Caption](../properties/caption.md), [ChildList](../properties/childlist.md), [Data](../properties/data.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [HasEdit](../properties/hasedit.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [StartIn](../properties/startin.md), [Target](../properties/target.md), [Translate](../properties/translate.md), [Type](../properties/type.md)

Methods: [Detach](../methodorevents/detach.md), [Wait](../methodorevents/wait.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [FileBoxCancel](../methodorevents/fileboxcancel.md), [FileBoxOK](../methodorevents/fileboxok.md)
