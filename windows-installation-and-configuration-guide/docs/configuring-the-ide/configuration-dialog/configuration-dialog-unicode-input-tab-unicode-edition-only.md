# Unicode Input Tab (Unicode Edition Only)

Unicode Edition can optionally select your APL keyboard each time you start APL. To choose this option, select one of your installed APL keyboards, enable the *Activate selected keyboard* checkbox, then click *OK*

![configuration dialog unicode input tab](../../img/configuration-dialog-unicode-input-tab.png)

Table: Configuration dialog: Unicode Input

|Label|Parameter|Description|
|---|---|---|
|Activate selected keyboard|[InitialKeyboardLayoutInUse](../../configuration-parameters/initialkeyboardlayoutinuse.md)|If checked, the specified APL keyboard is activated on start-up.|
|Show keyboards for all Languages|[InitialKeyboardLayoutShowAll](../../configuration-parameters/initialkeyboardlayoutshowall.md)|If checked, all installed keyboards are displayed. Otherwise, only Dyalog keyboards are shown|
|Keyboard|[InitialKeyboardLayout](../../configuration-parameters/initialkeyboardlayout.md)|the APL keyboard to be selected.|
|Configure Layout|&nbsp;|Displays thefollowng dialog box.|

## Input Method Editor Properties

![ime properties](../../img/ime-properties.png)

Table: Dyalog Input Method Editor Properties

|Label|Parameter|Description|
|---|---|---|
|Use Ctrl-X,C,V for clipboard|[UseXCV](../../configuration-parameters/usexcv.md)|specifies whether or not the commonly used keystrokes for copy, cut and paste  are recognised as such.|
|Enable Backtick Keyboard introducer|&nbsp;|&nbsp;|
|Enable Overstrikes|[ResolveOverstrikes](../../configuration-parameters/resolveoverstrikes.md)|1 = enable overstrikes. 0 = disable overstrikes|
|Overstrikes do not require the OS introducer key|&nbsp;|1 = IME identifies overstrike operation automatically 0 = IME requires the <OS> key (default Ctrl+Bksp) to signal an overstrike operation|
|Use Overstrike popup|[OverstrikesPopup](../../configuration-parameters/overstrikespopup.md)|1 = enable the overstrike popup. 0 = disable the overstrike popup|
