<h1 class="heading"><span class="name"> The Session Toolbars</span></h1>

The Session toolbars are contained by four separate CoolBand objects, allowing you to configure their order in whichever way you choose. The tool buttons appear differently according to whether or not Native Look and Feel is enabled.

The bitmaps for the buttons displayed on the session tool bar are implemented by three ImageList objects owned by the CoolBar `⎕SE.cbtop`. These represent the ToolButton images in their normal, highlighted and inactive states and are named `iln`, `ilh` and `ili` respectively. These images derive from three bitmap resources contained in `dyalog.exe` named `tb_normal`, `tb_hot` and `tb_inactive`.

If Native Look and Feel is enabled all three bitmap resources are mapped to a different set of images which are capable of  reflecting the *Visual Styles* in use.

## Native Look and Feel Enabled

![](img/ws-session-toolbar.png)

![](img/object-session-toolbar.png)

![](img/tool-session-toolbar.png)

![](img/edit-session-toolbar.png)

![](img/session-session-toolbar.png)

## Native Look and Feel Disabled

![](img/nlf-disabled/ws-session-toolbar.png)

![](img/nlf-disabled/object-session-toolbar.png)

![](img/nlf-disabled/tool-session-toolbar.png)

![](img/nlf-disabled/edit-session-toolbar.png)

![](img/nlf-disabled/session-session-toolbar.png)

## Workspace (WS) Operations

| Button | Operation  | Description |
|--------|-------| --- |
| ![](img/clear-workspace-icon.png) ![](img/nlf-disabled/clear-workspace-icon.png) | Clear Workspace  | Executes the system operation `[WSClear]` which asks for confirmation, then clears the workspace |
| ![](img/load-workspace-icon.png) ![](img/nlf-disabled/load-workspace-icon.png) | Load Workspace   | Executes the system operation `[WSLoad]` which displays a file selection dialog box and loads the selected workspace |
| ![](img/copy-workspace-icon.png) ![](img/nlf-disabled/copy-workspace-icon.png) | Copy Workspace   | Executes the system operation `[WSCopy]` which displays a file selection dialog box and copies the (entire) selected workspace |
| ![](img/save-workspace-icon.png) ![](img/nlf-disabled/save-workspace-icon.png) | Save Workspace   | Executes the system operation `[WSSaveas]` which displays a file selection dialog box and saves the workspace in the selected file |
| ![](img/export-workspace-icon.png) ![](img/nlf-disabled/reexport-workspace-icon.png) | Export Workspace | Executes the system operation `[MakeExe]` which re-exports the workspace using the settings, parameters and options that were previously selected using the *Create Bound File* dialog |
<!-- | ![](img/print-functions-icon.png) ![](img/nlf-disabled/print-workspace-icon.png) | Print Functions  | Executes the system operation `[PrintFnsInNS]` that prints all the functions and operators in the current namespace | -->

## Object Operations

| Button  | Operation  | Description |
| --- | ---  | --- |
| ![](img/copy-object-icon.png) ![](img/nlf-disabled/copy-object-icon.png) | Copy Object  | Executes the system operation `[ObjCopy]` which copies the contents of the current object to the clipboard |
| ![](img/paste-object-icon.png) ![](img/nlf-disabled/paste-object-icon.png) | Paste Object | Executes the system operation `[ObjPaste]` which copies the contents of the clipboard into the current object, replacing its previous value |
| ![](img/print-object-icon.png) ![](img/nlf-disabled/print-object-icon.png) | Print Object | Executes the system operation `[ObjPrint]` . Prints the current object. Note that if the object is being edited, the version of the object displayed in the edit window is printed. |
| ![](img/edit-object-icon.png) ![](img/nlf-disabled/edit-object-icon.png) | Edit Object  | Executes the system operation `[Edit]` which edits the current object using the standard system editor |
| ![](img/edit-numbers-icon.png) ![](img/nlf-disabled/edit-numbers-icon.png) | Edit using Array Notation | Edits the object using [array notation](../../programming-reference-guide/introduction/arrays/array-notation). |
| ![](img/sharpplot-icon.png) ![](img/nlf-disabled/sharpplot-icon.jpg) | SharpPlot    | Executes a defined function in `⎕SE` that runs the Chart Wizard to plot the current object using the `]chart` User Command. |


## Tools

| Button  | Operation  | Description |
| --- | ---  | --- |
| ![](img/search-icon.png) ![](img/nlf-disabled/search-icon.png) | Search | Executes the system operation `[WSSearch]` which displays the *Workspace Search* tool |
| ![](img/explorer-icon.png) ![](img/nlf-disabled/explorer-icon.png) | Explorer | Executes the system operation `[Explorer]` which displays the *Workspace Explorer* tool |
| ![](img/clear-all-stops-icon.png) ![](img/nlf-disabled/clear-all-stops-icon.png) | Clear all Stops | Executes the system operation `[ClearTSM]` which clears all `⎕STOP` , `⎕MONITOR` and `⎕TRACE` settings |
<!-- | ![](img/line-numbers-icon.png) ![](img/nlf-disabled/line-numbers-icon.png) | Line Numbers | Executes the system operation `[LineNumbers]` which toggles the display of line numbers in edit and trace windows on and off | -->

## Edit Operations

| Button  | Operation  | Description |
| --- | ---  | --- |
| ![](img/copy-selection-icon.png) ![](img/nlf-disabled/copy-selection-icon.png) | Copy Selection | Executes the system operation `[Copy]` which copies the selected text to the clipboard |
| ![](img/paste-selection-icon.png) ![](img/nlf-disabled/paste-selection-icon.png) |  Paste Selection | Executes the system operation `[Paste]` which pastes the text in the clipboard into the current window at the insertion point |
| ![](img/recall-last-icon.png) ![](img/nlf-disabled/recall-last-icon.png) | Recall Last | Executes the system operation `[Undo]` which recalls the previous input line from the input history stack |
| ![](img/recall-next-icon.png) ![](img/nlf-disabled/recall-next-icon.png) | Recall Next | Executes the system operation `[Redo]` which recalls the next input line from the input history stack |

## Session Operations

| Button  | Operation  | Description |
| --- | ---  | --- |
| ![](img/load-workspace-icon.png) ![](img/nlf-disabled/load-session-icon.png) | Load Session | Executes the system operation `[SELoad]` which displays a file selection dialog box and loads the selected Session File |
| ![](img/boxing-icon.png) ![](img/nlf-disabled/boxing-icon.png) | Boxing On/Off | Executes the user command `]boxing` to toggle boxing on/off. |
| ![](img/select-font-combo.png) | Select Font | Selects the font to be used in the Session window |
| ![](img/select-fontsize-spinner.png) | Select Font Size | Selects the size of the font to be used in the Session window |
