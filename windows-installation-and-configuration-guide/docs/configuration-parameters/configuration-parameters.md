<h1 class="heading"><span class="name">Configuration Parameters</span></h1>

## Introduction

Dyalog APL is customised using a set of **configuration parameters**. These may be defined  in a number of ways, which take precedence as follows:

- Command-line settings
- Application configuration file settings
- Environment variable settings
- User configuration file settings
- Settings in the registry section defined by the **IniFile** parameter (Windows only)
- Built-in defaults

This scheme provides a great deal of flexibility, and a system whereby you can override one setting with another. For example, you can define your normal workspace size (*maxws*) in the Registry, but override it with a new value specified on the APL command line. The way this is done is described in the following section.

Furthermore, you are not limited to the set of parameters employed by APL itself as you may add parameters of your own choosing.

Although for clarity parameter names are given here in mixed case, they are case-independent under Windows. Under UNIX and Linux, if Dyalog parameters are specified as environment variables they must be named entirely in upper-case.

Note that the value of a parameter obtained by the GetEnvironment method (see [GetEnvironment](../../../object-reference/methodorevents/getenvironment)) uses exactly the same set of rules.

The following section details those parameters that are implemented by Registry Values in the top-level folder identified by **IniFile**. Values that are implemented in sub-folders are *mainly* internal and are not described in detail here. However, any Value that is maintained via a configuration dialog box will be named and described in the documentation for that dialog box in The APL Environment.

## Specifying Size-related Parameters

Several of the configuration parameters define sizes.

The value of the parameter must consist of an integer value, optionally followed immediately by a single character which denotes the units to be used. If the value contains no character the units are assumed to be KiB.

Valid values for units are:

K(KiB), M(MiB), G(GiB), T(TiB), P(PiB) and E(EiB).

Specifying an invalid value will prevent Dyalog APL from starting.

## Changing parameter values in the Registry

You can change parameters in the Registry in one of two ways:

- Using the Configuration dialog box that is obtained by selecting *Configure* from the *Options* menu on the Dyalog APL/W session. See ["The Configuration Dialog Box"](../configuring-the-ide/configuration-dialog/configuration-dialog-general-tab.md) for details.
- By directly editing the Windows Registry using `REGEDIT.EXE` or `REGEDIT32.EXE`. This is necessary for parameters that are not editable via the Configuration dialog box.

## Configuration Parameters

<style>
  .2col {
    columns: 2;
    column-rule: 1px solid currentColor;
    column-gap: 2em;
  }
  .2col > a {
    display: block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
</style>

<div class="2col">

[APLAN_FOR_EDITOR](./aplan-for-editor.md)
[APLAN_FOR_OUTPUT](./aplan-for-output.md)
[AddClassHeaders](./addclassheaders.md)
[AplCoreName](./aplcorename.md)
[APLK](./aplk.md)
[APLKeys](./aplkeys.md)
[APLNID](./aplnid.md)
[APLT](./aplt.md)
[APLTrans](./apltrans.md)
[APL_CODE_E_MAGNITUDE](./apl-code-e-magnitude.md)
[APL_COMPLEX_AS_V12](./apl-complex-as-v12.md)
[APL_FAST_FCHK](./apl-fast-fchk.md)
[APL_FCREATE_PROPS_C](./apl-fcreate-props-c.md)
[APL_FCREATE_PROPS_J](./apl-fcreate-props-j.md)
[APL_MAX_THREADS](./apl-max-threads.md)
[APL_TextInAplCore](./apl-textinaplcore.md)
[AutoComplete/CancelKey1](autocomplete/cancelkey1.md)
[AutoComplete/CancelKey2](autocomplete/cancelkey2.md)
[AutoComplete/Cols](autocomplete/cols.md)
[AutoComplete/CommonKey1](autocomplete/commonkey1.md)
[AutoComplete/CompleteKey1](autocomplete/completekey1.md)
[AutoComplete/CompleteKey2](autocomplete/completekey2.md)
[AutoComplete/Enabled](autocomplete/enabled.md)
[AutoComplete/History](autocomplete/history.md)
[AutoComplete/HistorySize](autocomplete/historysize.md)
[AutoComplete/PrefixSize](autocomplete/prefixsize.md)
[AutoComplete/Rows](autocomplete/rows.md)
[AutoComplete/ShowFiles](autocomplete/showfiles.md)
[AutoDPI](./autodpi.md)
[AutoFormat](./autoformat.md)
[AutoIndent](./autoindent.md)
[Auto_PW](./auto-pw.md)
[CFEXT](./cfext.md)
[ClassicMode](./classicmode.md)
[ClassicModeSavePosition](./classicmodesaveposition.md)
[CMD_PREFIX and CMD_POSTFIX](./cmd-prefix-and-cmd-postfix.md)
[ConfigFile](./configfile.md)
[Confirm_Abort](./confirm-abort.md)
[Confirm_Close](./confirm-close.md)
[Confirm_Fix](./confirm-fix.md)
[Confirm_Session_Delete](./confirm-session-delete.md)
[Default_DIV](./default-div.md)
[Default_IO](./default-io.md)
[Default_ML](./default-ml.md)
[Default_PP](./default-pp.md)
[Default_PW](./default-pw.md)
[Default_RTL](./default-rtl.md)
[Default_WX](./default-wx.md)
[DMXOutputOnError](./dmxoutputonerror.md)
[DockableEditWindows](./dockableeditwindows.md)
[DoubleClickEdit](./doubleclickedit.md)
[Dyalog](./dyalog.md)
[DyalogEmailAddress](./dyalogemailaddress.md)
[DyalogHelpDir](./dyaloghelpdir.md)
[DyalogInstallDir](./dyaloginstalldir.md)
[DyalogLink](./dyaloglink.md)
[DyalogStartup](./dyalogstartup.md)
[DyalogStartupSE](./dyalogstartupse.md)
[DyalogStartup_X](./dyalogstartup-x.md)
[DyalogWebSite](./dyalogwebsite.md)
[DYALOG_DISCARD_FN_SOURCE](./dyalog-discard-fn-source.md)
[DYALOG_EVENTLOGGINGLEVEL](./dyalog-eventlogginglevel.md)
[DYALOG_EVENTLOGNAME](./dyalog-eventlogname.md)
[DYALOG_GUTTER_ENABLE](./dyalog-gutter-enable.md)
[DYALOG_INITSESSION](../../../release-notes-v19-0/configuration-parameters/dyalog-initsession)
[Dyalog_LineEditor_Mode](./dyalog-lineeditor-mode.md)
[Dyalog_NETCore](./dyalog-netcore.md)
[DYALOG_NOPOPUPS](./dyalog-nopopups.md)
[Dyalog_Pixel_Type](./dyalog-pixel-type.md)
[DYALOG_SERIAL](./dyalog-serial.md)
[EditorState](./editorstate.md)
[Edit_Cols](./edit-cols.md)
[Edit_First_X](./edit-first-x.md)
[Edit_First_Y](./edit-first-y.md)
[Edit_Offset_X](./edit-offset-x.md)
[Edit_Offset_Y](./edit-offset-y.md)
[Edit_Rows](./edit-rows.md)
[ENABLE_CEF](./enable-cef.md)
[ErrorOnExternalException](./erroronexternalexception.md)
[ExternalHelpURL](./externalhelpurl.md)
[File_Stack_Size](./file-stack-size.md)
[Greet_Bitmap](./greet-bitmap.md)
[History_Size](./history-size.md)
[IniFile](./inifile.md)
[InitFullScriptNormal](./initfullscriptnormal.md)
[InitFullScriptSusp](./initfullscriptsusp.md)
[InitialKeyboardLayout](./initialkeyboardlayout.md)
[InitialKeyboardLayoutInUse](./initialkeyboardlayoutinuse.md)
[InitialKeyboardLayoutShowAll](./initialkeyboardlayoutshowall.md)
[Input_Size](./input-size.md)
[KeyboardInputDelay](./keyboardinputdelay.md)
[Load](./load.md)
[localdyalogdir](./localdyalogdir.md)
[Log_File](./log-file.md)
[Log_File_InUse](./log-file-inuse.md)
[Log_Size](./log-size.md)
[LX](./lx.md)
[MapChars](./mapchars.md)
[MaxAplCores](./maxaplcores.md)
[MaxWS](./maxws.md)
[OverstrikesPopup](./overstrikespopup.md)
[PassExceptionsToOpSys](./passexceptionstoopsys.md)
[PFKey_Size](./pfkey-size.md)
[ProgramFolder](./programfolder.md)
[PropertyExposeRoot](./propertyexposeroot.md)
[PropertyExposeSE](./propertyexposese.md)
[QCMD_Timeout](./qcmd-timeout.md)
[ResolveOverstrikes](./resolveoverstrikes.md)
[RIDE_Init](./ride-init.md)
[RIDE_Spawned](./ride-spawned.md)
[RunAsService](./runasservice.md)
[SaveContinueOnExit](./savecontinueonexit.md)
[SaveLogOnExit](./savelogonexit.md)
[SaveSessionOnExit](./savesessiononexit.md)
[Serial](./serial.md)
[SessionOnTop](./sessionontop.md)
[Session_File](./session-file.md)
[ShowStatusOnError](./showstatusonerror.md)
[SingleTrace](./singletrace.md)
[SkipLines](./skiplines.md)
[SM_Cols](./sm-cols.md)
[SM_Rows](./sm-rows.md)
[StatusOnEdit](./statusonedit.md)
[TabStops](./tabstops.md)
[ToolBarsOnEdit](./toolbarsonedit.md)
[TraceStopMonitor](./tracestopmonitor.md)
[Trace_First_X](./trace-first-x.md)
[Trace_First_Y](./trace-first-y.md)
[Trace_Level_Warn](./trace-level-warn.md)
[Trace_Offset_X](./trace-offset-x.md)
[Trace_Offset_Y](./trace-offset-y.md)
[Trace_On_Error](./trace-on-error.md)
[UCMDCacheFile](./ucmdcachefile.md)
[UnicodeToClipboard](./unicodetoclipboard.md)
[URLHighlight](./urlhighlight.md)
[UseExternalHelpURL](./useexternalhelpurl.md)
[UserConfigFile](./userconfigfile.md)
[UseXCV](./usexcv.md)
[ValueTips/ColourScheme](valuetips/colourscheme.md)
[ValueTips/Delay](valuetips/delay.md)
[ValueTips/Enabled](valuetips/enabled.md)
[WantsSpecialKeys](./wantsspecialkeys.md)
[WrapSearch](./wrapsearch.md)
[WrapSearchMsgBox](./wrapsearchmsgbox.md)
[WSEXT](./wsext.md)
[WSPath](./wspath.md)
[XPLookAndFeel](./xplookandfeel.md)
[YY_Window](./yy-window.md)

</div>
