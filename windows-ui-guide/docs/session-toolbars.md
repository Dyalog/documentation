<h1 class="heading"><span class="name"> The Session Toolbars</span></h1>

The Session toolbars are contained by four separate CoolBand objects, allowing you to configure their order in whichever way you choose. 

The bitmaps for the buttons displayed on the session tool bar are implemented by three ImageList objects owned by the CoolBar `⎕SE.cbtop`. These represent the ToolButton images in their normal, highlighted and inactive states and are named `iln`, `ilh` and `ili` respectively. These images derive from three bitmap resources contained in `dyalog.exe` named `tb_normal`, `tb_hot` and `tb_inactive`.

## The Toolbars

| -------------------- | --- |
| Workspace Operations | ![](img/ws-session-toolbar.png) |
| Object Operations    | ![](img/object-session-toolbar.png) |
| Tools                | ![](img/tool-session-toolbar.png) |
| Edit Operations      | ![](img/edit-session-toolbar.png) |
| Session Operations   | ![](img/session-session-toolbar.png) |


## Workspace (WS) Operations

| Button | Operation  | Description |
|--------|-------| --- |
| ![](img/clear-workspace-icon.png) | Clear Workspace  | Executes the system operation `[WSClear]` which asks for confirmation, then clears the workspace |
| ![](img/load-workspace-icon.png) | Load Workspace   | Executes the system operation `[WSLoad]` which displays a file selection dialog box and loads the selected workspace |
| ![](img/copy-workspace-icon.png) | Copy Workspace   | Executes the system operation `[WSCopy]` which displays a file selection dialog box and copies the (entire) selected workspace |
| ![](img/save-workspace-icon.png) | Save Workspace   | Executes the system operation `[WSSaveas]` which displays a file selection dialog box and saves the workspace in the selected file |
| ![](img/export-workspace-icon.png) | Export Workspace | Executes the system operation `[MakeExe]` which re-exports the workspace using the settings, parameters and options that were previously selected using the *Create Bound File* dialog |
<!-- | ![](img/print-functions-icon.png) ![](img/nlf-disabled/print-workspace-icon.png) | Print Functions  | Executes the system operation `[PrintFnsInNS]` that prints all the functions and operators in the current namespace | -->

## Object Operations

| Button  | Operation  | Description |
| --- | ---  | --- |
| ![](img/copy-object-icon.png) | Copy Object  | Executes the system operation `[ObjCopy]` which copies the contents of the current object to the clipboard |
| ![](img/paste-object-icon.png) | Paste Object | Executes the system operation `[ObjPaste]` which copies the contents of the clipboard into the current object, replacing its previous value |
| ![](img/print-object-icon.png) | Print Object | Executes the system operation `[ObjPrint]` . Prints the current object. Note that if the object is being edited, the version of the object displayed in the edit window is printed. |
| ![](img/edit-object-icon.png) | Edit Object  | Executes the system operation `[Edit]` which edits the current object using the standard system editor |
| ![](img/edit-numbers-icon.png) | Edit in Array Notation | Edits the object in [array notation](../../programming-reference-guide/introduction/arrays/array-notation). |
| ![](img/sharpplot-icon.png) | SharpPlot    | Executes a defined function in `⎕SE` that runs the Chart Wizard to plot the current object using the `]chart` User Command. |


## Tools

| Button  | Operation  | Description |
| --- | ---  | --- |
| ![](img/search-icon.png) | Search | Executes the system operation `[WSSearch]` which displays the *Workspace Search* tool |
| ![](img/explorer-icon.png) | Explorer | Executes the system operation `[Explorer]` which displays the *Workspace Explorer* tool |
| ![](img/clear-all-stops-icon.png) | Clear all Stops | Executes the system operation `[ClearTSM]` which clears all `⎕STOP` , `⎕MONITOR` and `⎕TRACE` settings |
<!-- | ![](img/line-numbers-icon.png) ![](img/nlf-disabled/line-numbers-icon.png) | Line Numbers | Executes the system operation `[LineNumbers]` which toggles the display of line numbers in edit and trace windows on and off | -->

## Edit Operations

| Button  | Operation  | Description |
| --- | ---  | --- |
| ![](img/copy-selection-icon.png) | Copy Selection | Executes the system operation `[Copy]` which copies the selected text to the clipboard |
| ![](img/paste-selection-icon.png) |  Paste Selection | Executes the system operation `[Paste]` which pastes the text in the clipboard into the current window at the insertion point |
| ![](img/recall-last-icon.png) | Recall Last | Executes the system operation `[Undo]` which recalls the previous input line from the input history stack |
| ![](img/recall-next-icon.png) | Recall Next | Executes the system operation `[Redo]` which recalls the next input line from the input history stack |

## Session Operations

| Button  | Operation  | Description |
| --- | ---  | --- |
| ![](img/load-workspace-icon.png) | Load Session | Executes the system operation `[SELoad]` which displays a file selection dialog box and loads the selected Session File |
| ![](img/boxing-icon.png) | Boxing On/Off | Executes the user command `]boxing` to toggle boxing on/off. |
| ![](img/select-font-combo.png) | Select Font | Selects the font to be used in the Session window |
| ![](img/select-fontsize-spinner.png) | Select Font Size | Selects the size of the font to be used in the Session window |
