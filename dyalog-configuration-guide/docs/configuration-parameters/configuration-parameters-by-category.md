---
search:
  exclude: true
---
# Configuration Parameters (by Category)

The following tables list the configuration parameters grouped by subject. Each parameter is described in full on its own page; the parameters are also listed alphabetically in the navigation pane.

## Session log and input buffers

These control the Session log and the buffers that hold input and function-key definitions.

|Name|Description|
|----|-----------|
|[`Log_File`](log-file.md)|The path (absolute, or relative to the working directory) and name of the Session log file|
|[`Log_File_InUse`](log-file-inuse.md)|Whether the Session log is saved to the Session log file and reloaded the next time a Session is started|
|[`Log_Size`](log-size.md)|The size of the Session log buffer|
|[`Session_File`](session-file.md)|The name of the file from which the Session (`⎕SE`) is loaded when Dyalog starts|
|[`History_Size`](history-size.md)|The size of the buffer used to store previously entered (input) lines in the Session|
|[`Input_Size`](input-size.md)|The size of the buffer used to store marked lines (lines awaiting execution) in the Session|
|[`PFKey_Size`](pfkey-size.md)|The size of the buffer used to store programmable function key definitions (see Program Function Key (`⎕PFKEY`))|
|[`Confirm_Session_Delete`](confirm-session-delete.md)|Whether you are prompted for confirmation when you delete lines from the Session log|

## Session appearance and behaviour

These control how the Session window looks and behaves.

|Name|Description|
|----|-----------|
|[`APLAN_FOR_OUTPUT`](aplan-for-output.md)|Whether Session output uses array notation when possible|
|[`DYALOG_GUTTER_ENABLE`](dyalog-gutter-enable.md)|Whether a gutter is displayed in the left-most column of the Session window|
|[`URLHighlight`](urlhighlight.md)|Whether URLs and links are highlighted in Session and Edit windows|
|[`StatusOnEdit`](statusonedit.md)|Whether a status bar is displayed along the bottom of individual Edit windows|
|[`ToolBarsOnEdit`](toolbarsonedit.md)|Whether tool bars are displayed along the top of individual Edit windows|
|[`AutoDPI`](autodpi.md)|Whether Dyalog registers the application as DPI-aware when it initialises, and so performs auto-scaling itself|
|[`Dyalog_Pixel_Type`](dyalog-pixel-type.md)|How the value `'Pixel'` of the `Coord` property is interpreted|
|[`ClassicMode`](classicmode.md)|Whether the Session operates in *Dyalog Classic mode*, in which the Editor and Tracer behave as they did in earlier versions of Dyalog|
|[`ClassicModeSavePosition`](classicmodesaveposition.md)|Whether the current size and location of the first editor and tracer windows are remembered for next time (saved in the Registry sub-folders `WindowRects/EditWindow` and `WindowRects/TraceWindow`)|
|[`SessionOnTop`](sessionontop.md)|Whether the Session can appear on top of Edit and Trace windows in Classic Dyalog mode|
|[`Dyalog_LineEditor_Mode`](dyalog-lineeditor-mode.md)|Whether multi-line input is enabled in the Session|
|[`DYALOG_NOPOPUPS`](dyalog-nopopups.md)|Whether a message box appears when Dyalog terminates unexpectedly|
|[`XPLookAndFeel`](xplookandfeel.md)|Whether *Native Look and Feel* is used, affecting the appearance of user-interface controls such as buttons|
|[`ShowStatusOnError`](showstatusonerror.md)|Whether the Status window is displayed automatically, when required, when Dyalog attempts to write output to it|

## Workspace defaults

These set the values that system variables and related flags take in a clear workspace.

|Name|Description|
|----|-----------|
|[`Default_DIV`](default-div.md)|The value of `⎕DIV` in a clear workspace|
|[`Default_IO`](default-io.md)|The value of `⎕IO` in a clear workspace|
|[`Default_ML`](default-ml.md)|The value of `⎕ML` (migration level) in a clear workspace|
|[`Default_PP`](default-pp.md)|The value of `⎕PP` (print precision) in a clear workspace|
|[`Default_PW`](default-pw.md)|The value of `⎕PW` in a clear workspace|
|[`Default_RTL`](default-rtl.md)|The value of `⎕RTL` (response time limit) in a clear workspace|
|[`Default_WX`](default-wx.md)|The value of `⎕WX` in a clear workspace|
|[`Auto_PW`](auto-pw.md)|Whether the value of `⎕PW` is derived automatically from the current width of the Session (Windows) or terminal (UNIX and macOS) window|
|[`PropertyExposeRoot`](propertyexposeroot.md)|The default value, in a clear workspace, of the flag that specifies whether the names of the properties, methods, and events of the Root object are exposed|
|[`PropertyExposeSE`](propertyexposese.md)|The default value, in a clear workspace, of the flag that specifies whether the names of the properties, methods, and events of the Session object (`⎕SE`) are exposed|

## Editor

These control the behaviour of the Editor.

|Name|Description|
|----|-----------|
|[`Confirm_Abort`](confirm-abort.md)|Whether you are prompted for confirmation when you abort an edit session after making changes to the object being edited|
|[`Confirm_Close`](confirm-close.md)|Whether you are prompted for confirmation when you close an edit window after making changes to the object being edited|
|[`Confirm_Fix`](confirm-fix.md)|Whether you are prompted for confirmation when you fix an object in the workspace after making changes in the editor|
|[`AutoFormat`](autoformat.md)|Whether Control Structures are formatted automatically when a function is opened for editing or converted to text by `⎕CR`, `⎕NR`, or `⎕VR`|
|[`AutoIndent`](autoindent.md)|Whether semi-automatic indentation is applied during editing, so that a new line in a function is indented by the same amount as the previous line|
|[`TabStops`](tabstops.md)|The number of spaces inserted by pressing the Tab key in the editor|
|[`DockableEditWindows`](dockableeditwindows.md)|Whether individual edit windows can be undocked from (and docked back into) the MDI Editor window|
|[`DoubleClickEdit`](doubleclickedit.md)|Whether double-clicking over a name invokes the editor|
|[`WrapSearch`](wrapsearch.md)|Whether Search/Replace in the editor stops at the top or bottom of the text (according to the direction of the search), or continues from the other end|
|[`WrapSearchMsgBox`](wrapsearchmsgbox.md)|Whether a message box is displayed to inform you when a wrapped search passes the start or end of the text|
|[`DYALOG_DISCARD_FN_SOURCE`](dyalog-discard-fn-source.md)|Whether source code is discarded when a function or operator is fixed by the editor or by `⎕FIX`|
|[`APLAN_FOR_EDITOR`](aplan-for-editor.md)|Whether new **Edit** windows containing arrays open using array notation when possible|
|[`InitFullScriptNormal`](initfullscriptnormal.md)|When the Editor is used to edit a script (such as a Class or Namespace) that is **not suspended**, this controls whether fixing the script and exiting the Editor re-fixes just the functions in the script, or re-executes the whole script (re-initialising any fields or variables defined within it)|
|[`InitFullScriptSusp`](initfullscriptsusp.md)|When the Editor is used to edit a script (such as a Class or Namespace) that is **suspended**, this controls whether fixing the script and exiting the Editor re-fixes just the functions in the script, or re-executes the whole script (re-initialising any fields or variables defined within it)|
|[`EditorState`](editorstate.md)|An internal parameter that records the state (normal or maximised) of the last edit window, so that the next edit window is created in the same state|

## Tracer

These control the behaviour of the Tracer.

|Name|Description|
|----|-----------|
|[`AddClassHeaders`](addclassheaders.md)|What the Tracer displays when tracing the execution of a function defined in a script|
|[`Trace_On_Error`](trace-on-error.md)|Whether the Tracer is deployed automatically when execution of a defined function halts with an untrapped error|
|[`Trace_Level_Warn`](trace-level-warn.md)|The maximum number of Trace windows displayed when an error occurs and `Trace_On_Error` is `1`|
|[`SingleTrace`](singletrace.md)|Whether there is a single Trace window or one Trace window per function|
|[`SkipLines`](skiplines.md)|Causes the Tracer to skip lines that contain no executable statement, with the exception of the first line of the function and, in a traditional function (not a dfn), the last line if it is a comment|
|[`TraceStopMonitor`](tracestopmonitor.md)|Which of the `⎕TRACE`, `⎕STOP`, and `⎕MONITOR` columns are displayed in Trace and Edit windows|

## Edit, Trace, and SM window geometry

These set the initial size, position, and staggering of Edit, Trace, and stand-alone `⎕SM` windows in Dyalog Classic mode.

|Name|Description|
|----|-----------|
|[`Edit_Cols`](edit-cols.md)|The initial width of an edit window, in character units|
|[`Edit_Rows`](edit-rows.md)|The initial height of an edit window, in character units|
|[`Edit_First_X`](edit-first-x.md)|The initial horizontal position, in character units, of the first edit window; subsequent edit windows are staggered from it|
|[`Edit_First_Y`](edit-first-y.md)|The initial vertical position, in character units, of the first edit window; subsequent edit windows are staggered from it|
|[`Edit_Offset_X`](edit-offset-x.md)|The number of characters by which an edit window is staggered horizontally from the previous one|
|[`Edit_Offset_Y`](edit-offset-y.md)|The number of characters by which an edit window is staggered vertically from the previous one|
|[`Trace_First_X`](trace-first-x.md)|The initial horizontal position, in character units, of the first Trace window; subsequent Trace windows are staggered from it|
|[`Trace_First_Y`](trace-first-y.md)|The initial vertical position, in character units, of the first Trace window; subsequent Trace windows are staggered from it|
|[`Trace_Offset_X`](trace-offset-x.md)|The number of characters by which a Trace window is staggered horizontally from the previous one|
|[`Trace_Offset_Y`](trace-offset-y.md)|The number of characters by which a Trace window is staggered vertically from the previous one|
|[`SM_Cols`](sm-cols.md)|The width, in characters, of the window used to display `⎕SM` when it is used stand-alone|
|[`SM_Rows`](sm-rows.md)|The height, in characters, of the window used to display `⎕SM` when it is used stand-alone|

## AutoComplete

These control the AutoComplete suggestion box.

|Name|Description|
|----|-----------|
|[`AutoComplete/Enabled`](autocomplete/enabled.md)|Whether AutoComplete is enabled|
|[`AutoComplete/PrefixSize`](autocomplete/prefixsize.md)|The threshold, in number of characters entered, before AutoComplete begins to display suggestions|
|[`AutoComplete/History`](autocomplete/history.md)|Whether AutoComplete maintains a list of previous auto-completions|
|[`AutoComplete/HistorySize`](autocomplete/historysize.md)|The number of previous auto-completions kept when `AutoComplete/History` is `1`|
|[`AutoComplete/ShowFiles`](autocomplete/showfiles.md)|Whether AutoComplete suggests directory and file names for the `)LOAD`, `)COPY`, and `)DROP` system commands|
|[`AutoComplete/Cols`](autocomplete/cols.md)|The maximum number of columns (width) in the AutoComplete pop-up suggestion box|
|[`AutoComplete/Rows`](autocomplete/rows.md)|The maximum number of rows (height) in the AutoComplete pop-up suggestion box|
|[`AutoComplete/CancelKey1`](autocomplete/cancelkey1.md)|The first of two possible keys that cancel (hide) the AutoComplete suggestion box|
|[`AutoComplete/CancelKey2`](autocomplete/cancelkey2.md)|The second of two possible keys that cancel (hide) the AutoComplete suggestion box|
|[`AutoComplete/CommonKey1`](autocomplete/commonkey1.md)|The key that auto-completes the *common prefix*: the longest string of leading characters of the currently selected name that is shared by at least one other name in the AutoComplete suggestion box|
|[`AutoComplete/CompleteKey1`](autocomplete/completekey1.md)|The first of two possible keys that select the current option from the AutoComplete suggestion box|
|[`AutoComplete/CompleteKey2`](autocomplete/completekey2.md)|The second of two possible keys that select the current option from the AutoComplete suggestion box|

## Value Tips

These control the Value Tips shown when the mouse hovers over a name.

|Name|Description|
|----|-----------|
|[`ValueTips/Enabled`](valuetips/enabled.md)|Whether Value Tips are enabled|
|[`ValueTips/Delay`](valuetips/delay.md)|The delay, in milliseconds, before a Value Tip is displayed when the mouse hovers over a name|
|[`ValueTips/ColourScheme`](valuetips/colourscheme.md)|The colour scheme used to display a Value Tip when the mouse hovers over a name|

## Keyboard and input

These control keyboard layouts, translate tables, and how keystrokes are interpreted.

|Name|Description|
|----|-----------|
|[`APLK`](aplk.md)|The name of the Input Translate Table, which defines the keyboard layout|
|[`APLKeys`](aplkeys.md)|A search path for the Input Translate Table, useful when configuring a run-time application|
|[`APLT`](aplt.md)|The name of the Output Translate Table|
|[`APLTrans`](apltrans.md)|A search path for the Output Translate Table, useful when configuring a run-time application|
|[`InitialKeyboardLayout`](initialkeyboardlayout.md)|The name of the keyboard to be selected on start-up|
|[`InitialKeyboardLayoutInUse`](initialkeyboardlayoutinuse.md)|Whether the keyboard given by `InitialKeyboardLayout` is selected as the current keyboard layout when an APL Session starts|
|[`InitialKeyboardLayoutShowAll`](initialkeyboardlayoutshowall.md)|Whether all installed keyboards are listed in the choice of keyboards on the Unicode Input tab of the Configuration dialog|
|[`OverstrikesPopup`](overstrikespopup.md)|Whether the Overstrikes popup is enabled|
|[`ResolveOverstrikes`](resolveoverstrikes.md)|Whether an APL composite symbol can be entered using overstrikes|
|[`UseXCV`](usexcv.md)|How the common copy (Ctrl+C), cut (Ctrl+X), and paste (Ctrl+V) keystrokes are processed|
|[`UnicodeToClipboard`](unicodetoclipboard.md)|Whether text transferred to and from the Windows clipboard is treated as Unicode text|
|[`KeyboardInputDelay`](keyboardinputdelay.md)|The delay, in milliseconds, before the system reacts to a keystroke by updating the name of the Current Object in the Session status bar (see The Current Object) and offering a list of names for auto-completion (see the Auto Complete tab)|
|[`WantsSpecialKeys`](wantsspecialkeys.md)|A list of applications (for example, `putty.exe`) that use the command strings in the Input Translate Tables|
|[`mapchars`](mapchars.md)|The mapping between `⎕AV` and the font must be strictly one-to-one|

## Start-up and workspace loading

These control what is loaded and run when Dyalog starts, and where workspaces are found.

|Name|Description|
|----|-----------|
|[`Load`](load.md)|The name of a workspace, or of a directory or text file containing APL source code, to be loaded when Dyalog starts|
|[`LX`](lx.md)|An expression to be executed after Dyalog has started and loaded a workspace or a text file of APL source code (see `Load`)|
|[`MaxWS`](maxws.md)|The amount of memory allocated to the workspace at start-up|
|[`WSPath`](wspath.md)|The workspace search path: a list of directories searched, in order, when you `)LOAD` or `)COPY` a workspace, or start an Auxiliary Processor, without giving an explicit path|
|[`WSEXT`](wsext.md)|Workspace filename extensions|
|[`ConfigFile`](configfile.md)|The name of the application configuration file|
|[`UserConfigFile`](userconfigfile.md)|The name of the user configuration file|
|[`IniFile`](inifile.md)|The name of the Windows Registry folder that holds the configuration parameters|
|[`DyalogStartup`](dyalogstartup.md)|The name of a file containing APL code to be run each time Dyalog starts|
|[`DyalogStartupSE`](dyalogstartupse.md)|One or more *Session initialisation* directories containing APL code to be installed in `⎕SE`|
|[`DyalogStartup_X`](dyalogstartup-x.md)|During Session initialisation, code is loaded from the directories given by `DyalogStartupSE` into a corresponding namespace tree in `⎕SE`, and is then optionally executed|

## Interpreter and runtime

These control aspects of the running interpreter.

|Name|Description|
|----|-----------|
|[`qcmd_timeout`](qcmd-timeout.md)|The length of time, in milliseconds, that Dyalog waits for the execution of a Windows command to start|
|[`Dyalog_NETCore`](dyalog-netcore.md)|Whether the .NET interface is used in preference to the .NET Framework interface|
|[`Enable_CEF`](enable-cef.md)|Whether the Chromium Embedded Framework (CEF) is enabled|
|[`APL_MAX_THREADS`](apl-max-threads.md)|The maximum number of system threads used for parallel execution|
|[`CMD_PREFIX and CMD_POSTFIX`](cmd-prefix-and-cmd-postfix.md)|Strings within which operating-system commands given as the arguments to `⎕CMD`, `⎕SH`, `)CMD`, and `)SH` are wrapped, so that the command arguments run under a non-standard command shell|
|[`Serial`](serial.md)|Your Dyalog serial number|
|[`DYALOG_SERIAL`](dyalog-serial.md)|Your Dyalog serial number|

## Shutting down

These control what is saved when Dyalog terminates, and running as a service.

|Name|Description|
|----|-----------|
|[`SaveContinueOnExit`](savecontinueonexit.md)|Whether the current workspace is saved as `CONTINUE.DWS` before Dyalog terminates|
|[`SaveSessionOnExit`](savesessiononexit.md)|Whether the current Session is saved in the Session file before Dyalog terminates|
|[`SaveLogOnExit`](savelogonexit.md)|Whether the Session log is saved before Dyalog terminates|
|[`RunAsService`](runasservice.md)|Whether Dyalog runs as a service: it does not prompt for confirmation when the user logs off, and the interpreter continues to run across the logoff/logon process|

## Installation locations, help, and URLs

These give the locations of Dyalog components and of help and web resources.

|Name|Description|
|----|-----------|
|[`Dyalog`](dyalog.md)|The directory in which Dyalog is installed|
|[`localdyalogdir`](localdyalogdir.md)|The directory in which Dyalog is installed on the client, in a client/server installation|
|[`DyalogInstallDir`](dyaloginstalldir.md)|The full pathname of the directory in which Dyalog is installed|
|[`ProgramFolder`](programfolder.md)|The folder in which the Dyalog program icons are installed|
|[`DyalogLink`](dyaloglink.md)|The directory containing the code for Link|
|[`DyalogHelpDir`](dyaloghelpdir.md)|The location of the HTML-based help used when help is requested from the Session (from the Help menu or by pressing `F1`)|
|[`DyalogWebSite`](dyalogwebsite.md)|The URL of the Dyalog web site|
|[`DyalogEmailAddress`](dyalogemailaddress.md)|The contact email address for Dyalog Ltd|
|[`ExternalHelpURL`](externalhelpurl.md)|The URL used when `UseExternalHelpURL` is `1` and Dyalog displays help for external objects (such as .NET types) through the Microsoft Document Explorer and online help (for example from Visual Studio)|
|[`UseExternalHelpURL`](useexternalhelpurl.md)|Whether Dyalog uses the Microsoft Document Explorer and online help to display help for external objects, such as .NET types|

## Component files and interoperability

These control component-file defaults and the interoperability of code and data across versions.

|Name|Description|
|----|-----------|
|[`APL_FCREATE_PROPS_C`](apl-fcreate-props-c.md)|The default checksum level for newly-created component files|
|[`APL_FCREATE_PROPS_J`](apl-fcreate-props-j.md)|The default journaling level for newly-created component files|
|[`APL_FAST_FCHK`](apl-fast-fchk.md)|Whether `⎕FCHK` is optimised so that it can reliably determine that a component file was properly untied and so need not be checked (this can be overridden with the `⎕FCHK` `force` option)|
|[`CFEXT`](cfext.md)|Component file filename extensions, determining the file search order when a component file is tied|
|[`APL_CODE_E_MAGNITUDE`](apl-code-e-magnitude.md)|The magnitude at or above which numbers in function bodies are descanned (written out as their character representation, for example by `⎕CR`) in exponential format|
|[`APL_COMPLEX_AS_V12`](apl-complex-as-v12.md)|Whether code developed with Version 12.1 or earlier keeps its original behaviour with respect to complex numbers|
|[`File_Stack_Size`](file-stack-size.md)|The number of most-recently-used workspaces displayed in the Session File menu|
|[`aplnid`](aplnid.md)|The *user number* used by the component file system to control file sharing and security|

## Errors and diagnostics

These control aplcore files, error reporting, and event logging.

|Name|Description|
|----|-----------|
|[`AplCoreName`](aplcorename.md)|The directory and name of the file in which an *aplcore* is saved|
|[`MaxAplCores`](maxaplcores.md)|The maximum number of *aplcore* files retained|
|[`APL_TextInAplCore`](apl-textinaplcore.md)|Whether certain information is written to an *aplcore* file when a system error occurs|
|[`DMXOutputOnError`](dmxoutputonerror.md)|Which windows `⎕DMX` error messages are displayed in|
|[`PassExceptionsToOpSys`](passexceptionstoopsys.md)|The default state of the *Pass Exception* check box in the System Error dialog box|
|[`ErrorOnExternalException`](erroronexternalexception.md)|The behaviour when a system exception occurs in a call on an external DLL or shared library|
|[`DYALOG_EVENTLOGGINGLEVEL`](dyalog-eventlogginglevel.md)|Whether a log entry is written to the Windows Event Log when Dyalog would otherwise pop up a message box because of an unexpected termination|
|[`DYALOG_EVENTLOGNAME`](dyalog-eventlogname.md)|The name of the Windows Event Log to which an event message is written (or the source of the event message, depending on the Registry entries defined) when Dyalog would otherwise pop up a message box because of an unexpected termination|

## Ride

These control the interpreter's use of the Ride protocol.

|Name|Description|
|----|-----------|
|[`RIDE_Init`](ride-init.md)|This parameter determines how the interpreter should behave with respect to the Ride protocol|
|[`Ride_Spawned`](ride-spawned.md)|Whether `⎕SR` and `)SH` are disabled|

## User commands

These control the user-command framework.

|Name|Description|
|----|-----------|
|[`UCMDCacheFile`](ucmdcachefile.md)|The name of the User Command cache file|

## Miscellaneous

|Name|Description|
|----|-----------|
|[`Greet_Bitmap`](greet-bitmap.md)|The filename of a bitmap displayed during initialisation of the Dyalog application, typically to show a product logo from a run-time application|
|[`yy_window`](yy-window.md)|How Dyalog interprets a 2-digit year number (for `⎕SM` and GUI edit fields that use a 2-digit year format such as `MM/DD/YY`)|
