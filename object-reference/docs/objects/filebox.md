# <span>FileBox</span> <span>Object</span>

**Purpose:** Prompts user to select a file.

**Description**

The FileBox object implements the standard Windows FileSelection Dialog Box. This is a "modal" object. When you create a FileBox with [`⎕WC`](../../../language-reference-guide/system-functions/wc), it is initially invisible and the user cannot interact with it. To use it, you must execute [`⎕DQ`](../../../language-reference-guide/system-functions/dq) with the name of the FileBox as its right argument. This causes the FileBox to be displayed. During the "local" [`⎕DQ`](../../../language-reference-guide/system-functions/dq) the user may interact **only** with the FileBox, or with other applications. When the user terminates the operation (by pressing the "Save", "Open", or "Cancel" Buttons, or by closing the window) the "local" [`⎕DQ`](../../../language-reference-guide/system-functions/dq) terminates, and the FileBox disappears.

When the "local" [`⎕DQ`](../../../language-reference-guide/system-functions/dq) is terminated, the FileBox generates either an [FileBoxOK](../methodorevents/fileboxok.md)(71) or [FileBoxCancel](../methodorevents/fileboxcancel.md)(72) event. The former is generated when the user presses the "Save" or "Open" button; the latter when the user presses the "Cancel" button or closes the FileBox.

The [FileMode](../properties/filemode.md) property is a character vector which indicates the mode in which the selected file is going to be opened. [FileMode](../properties/filemode.md) may be `'Read'` (the default) or `'Write'`. If [FileMode](../properties/filemode.md) is `'Write'`, files listed in the File Selection Box are "greyed", although they may still be selected.

The [Caption](../properties/caption.md) property determines the text that appears in the title bar of the FileBox window. If undefined, [Caption](../properties/caption.md) defaults to "Save As" if [FileMode](../properties/filemode.md) is `'Write'` or to "Open" if [FileMode](../properties/filemode.md) is `'Read'`. Similarly, if [FileMode](../properties/filemode.md) is `'Write'`, the button captions are "Save" and "Cancel", and if [FileMode](../properties/filemode.md) is `'Read'` the button caption are "Open" and "Cancel".

The [Directory](../properties/directory.md) property contains a simple character vector which specifies the initial directory from which a list of suitable files is displayed.
```apl
      'F' ⎕WC 'FileBox' 'The FileBox Object' 'C:\WDYALOG'
      ⎕DQ 'F'
```

The [Style](../properties/style.md) property specifies whether the user may choose a single file name (`'Single'`  which is the default) or several file names (`'Multi')`.

The [Filters](../properties/filters.md) property is a nested scalar or vector containing a list of filters. Each filter is a 2-element vector of character vectors which contain a file type mask and a file type description respectively. The file type descriptions appear in a drop-down combo box labelled "List File of Type". When the user selects one of these, the currently selected directory is searched for files which match the corresponding mask. The default value of [Filters](../properties/filters.md) is an empty vector. This gives a file type mask of "*.*" and a file type description of "All Files (*.*)". Hence an empty vector is equivalent to `(⊂'*.*' 'All Files (*.*)').`

The [Index](../properties/index-property.md) property determines which of the filters is initially selected. Its default value is `⎕IO`.

Note that when [`⎕DQ`](../../../language-reference-guide/system-functions/dq) terminates with [FileBoxOK](../methodorevents/fileboxok.md), the [File](../properties/file.md), [Directory](../properties/directory.md), and [Index](../properties/index-property.md) properties are updated to reflect the contents of the fields within the FileBox.

The operating system imposes limits on both the length of the name of the file, and on the total path length. In version {{ version_majmin }}attempting to set the `File` or `Directory` Properties to too long a name will generate a DOMAIN ERROR, while attempting to use too long a File name within the FileBox will result in the appearence of an error MessageBox.

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md), [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [OLEServer](../objects/oleserver.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [Root](../objects/root.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TCPSocket](../objects/tcpsocket.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md)

Children: [Timer](../objects/timer.md)

Properties: [Caption](../properties/caption.md), [ChildList](../properties/childlist.md), [Data](../properties/data.md), [Directory](../properties/directory.md), [EdgeStyle](../properties/edgestyle.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [File](../properties/file.md), [FileMode](../properties/filemode.md), [Filters](../properties/filters.md), [Index](../properties/index-property.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [Style](../properties/style.md), [Type](../properties/type.md)

Methods: [Detach](../methodorevents/detach.md), [Wait](../methodorevents/wait.md)

Events: [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [FileBoxCancel](../methodorevents/fileboxcancel.md), [FileBoxOK](../methodorevents/fileboxok.md), [Select](../methodorevents/select.md)
