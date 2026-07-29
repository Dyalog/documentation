# Trace/Edit Tab

![configuration dialog trace edit tab](../../img/configuration-dialog-trace-edit-tab.png)

Table: Configuration dialog: Trace/Edit

|Label|Parameter|Description|
|---|---|---|
|Classic Dyalog mode|[ClassicMode](../../../../dyalog-configuration-guide/configuration-parameters/classicmode.md)|Selects pre-Version 9 behaviour for Edit and Trace windows.|
|Allow session above edit windows|[SessionOnTop](../../../../dyalog-configuration-guide/configuration-parameters/sessionontop.md)|Specifies whether or not the Session may appear on top of Edit and Trace Windows|
|Single trace window|[ SingleTrace](../../../../dyalog-configuration-guide/configuration-parameters/singletrace.md)|Specifies whether or not there is a single Trace window|
|Remember previous window position|[ClassicModeSavePosition](../../../../dyalog-configuration-guide/configuration-parameters/classicmodesaveposition.md)|Specifies whether or not the current size and location of the first of the editor and tracer windows are remembered in the registry for next time.|
|Allow floating edit windows|[DockableEditWindows](../../../../dyalog-configuration-guide/configuration-parameters/dockableeditwindows.md)|Allows individual Edit windows to be undocked from (and re-docked in) the main Edit window|
|Show status bars|[ StatusOnEdit](../../../../dyalog-configuration-guide/configuration-parameters/statusonedit.md)|Specifies whether or not status bars are displayed along the bottom of individual Edit windows|
|Show tool bars|[ ToolBarsOnEdit](../../../../dyalog-configuration-guide/configuration-parameters/toolbarsonedit.md)|Specifies whether or not tool bars are displayed along the top of individual Edit windows|
|Show trace stack on error|[Trace_On_Error](../../../../dyalog-configuration-guide/configuration-parameters/trace-on-error.md)|Specifies whether or not the Tracer is automatically invoked when an error or stop occurs in a defined function|
|Allow search to wrap|[ WrapSearch](../../../../dyalog-configuration-guide/configuration-parameters/wrapsearch.md)|Specifies whether or not Search/Replace in the Editor stops at the top or bottom of the text, or continues from the start or end as appropriate.|
|Show message box if text wraps|[ WrapSearchMsgBox](../../../../dyalog-configuration-guide/configuration-parameters/wrapsearchmsgbox.md)|Specifies whether or not a message box is displayed to inform the user when the search wraps.|
|Warn if trace stack bigger than|[Trace_Level_Warn](../../../../dyalog-configuration-guide/configuration-parameters/trace-level-warn.md)|Specifies the maximum stack size for automatic deployment of the Tracer.|
|Confirm edit window close on Close|[Confirm_Close](../../../../dyalog-configuration-guide/configuration-parameters/confirm-close.md)|Specifies whether or not a confirmation dialog is displayed if the user alters the contents of an edit window, then closes it without saving|
|Confirm edit window close on Edit (and Fix)|[Confirm_Fix](../../../../dyalog-configuration-guide/configuration-parameters/confirm-fix.md)|Specifies whether or not a confirmation dialog is displayed if the user alters the contents of an edit window, then saves it using *Fix* or *Exit*|
|Confirm edit window close on Abort|[Confirm_Abort](../../../../dyalog-configuration-guide/configuration-parameters/confirm-abort.md)|Specifies whether or not a confirmation dialog is displayed if the user alters the contents of an edit window, then aborts using|
|Autoformat functions|[ AutoFormat](../../../../dyalog-configuration-guide/configuration-parameters/autoformat.md)|Selects automatic indentation for Control Structures when function is opened for editing|
|Autoindent|[ AutoIndent](../../../../dyalog-configuration-guide/configuration-parameters/autoindent.md)|Selects semi-automatic indentation for Control Structures while editing|
|Double-click to Edit|[ DoubleClickEdit](../../../../dyalog-configuration-guide/configuration-parameters/doubleclickedit.md)|Specifies whether or not double-clicking  over a name invokes the editor|
|Skip blank lines when tracing|[ SkipLines](../../../../dyalog-configuration-guide/configuration-parameters/skiplines.md)|If enabled, this causes the Tracer to automatically skip blank lines.|
|Skip comment lines when tracing|[ SkipLines](../../../../dyalog-configuration-guide/configuration-parameters/skiplines.md)|If enabled, this causes the Tracer to automatically skip comment lines.|
|Skip locals lines when tracing|[ SkipLines](../../../../dyalog-configuration-guide/configuration-parameters/skiplines.md)|If enabled, this causes the Tracer to automatically skip locals lines.|
|Limit tracer display to current function in script|[AddClassHeaders](../../../../dyalog-configuration-guide/configuration-parameters/addclassheaders.md)|When Tracing the execution of a function in a script, the Tracer displays either just the first line of the script and the function in question (option enabled), or the entire script (option disabled).|
|Paste text as Unicode (Classic Edition only)|[ UnicodeToClipboard](../../../../dyalog-configuration-guide/configuration-parameters/unicodetoclipboard.md)|Specifies whether or not text transferred to and from the Windows clipboard is to be treated as Unicode|
|Tab stops every|[ TabStops](../../../../dyalog-configuration-guide/configuration-parameters/tabstops.md)|The number of spaces inserted by pressing Tab in an edit window|
|Exit and fix ...|[ InitFullScriptSusp](../../../../dyalog-configuration-guide/configuration-parameters/initfullscriptsusp.md)|See Fixing Scripts below|
|If not ...|[InitFullScriptNormal](../../../../dyalog-configuration-guide/configuration-parameters/initfullscriptnormal.md)|See Fixing Scripts below|

## Fixing Scripts

When using the Editor to edit  a script such as a Class or Namespace you can specify whether, when you Fix the script and Exit  the Editor, just the functions in the script are re-fixed, or whether the whole script is re-executed, thereby re-initialising any Fields or variables defined within.

These two actions always appear in the Editor File menu, but you can specify which is associated with the <EP> (Esc) key by selecting the appropriate option in the drop-downs labelled:

- Exit and save changes (EP) in a suspended class or namespace should fix:
- If not suspended fix:

In both cases, you may select either  *Only Functions* or         *Everything*.

The label for the corresponding items on the Editor File menu (see  Editor (The File Menu, editing a script)) will change according to which behaviour applies. Note that if you specify a keystroke for <S1> in the *Keyboard Shortcuts* tab, this will be associated with the unselected action.
