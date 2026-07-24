# <span>Animate</span> <span>Method 29</span>

**Description**

The Animate method enables you to produce special effects when showing or hiding objects. There are three types of animation: roll, slide, and alpha-blended fade.

The argument to Animate is a 1 or 2-element array as follows:

|-----|---------|-------|
|`[1]`|Effects  |integer|
|`[2]`|Play time|integer|

The value of the *Effects* parameter is the sum of the following flags:

|Flag           |Value |Description                                                                                                                                    |
|---------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|AW_HOR_POSITIVE|1     |Animates the window from left to right. This flag can be used with roll or slide animation. It is ignored when used with the AW_CENTER flag.   |
|AW_HOR_NEGATIVE|2     |Animates the window from right to left. This flag can be used with roll or slide animation. It is ignored when used with the AW_CENTER flag.   |
|AW_VER_POSITIVE|4     |Animates the window from top to bottom. This flag can be used with roll or slide animation. It is ignored when used with the AW_CENTER flag.   |
|AW_VER_NEGATIVE|8     |Animates the window from bottom to top. This flag can be used with roll or slide animation. It is ignored when used with the AW_CENTER flag.   |
|AW_CENTER      |16    |Makes the window appear to collapse inward if being hidden or expand outward if being displayed                                                |
|AW_SLIDE       |262144|Uses slide animation. By default, roll animation is used. This flag is meaningless on its own but is ignored when used with the AW_CENTER flag.|
|AW_BLEND       |524288|Uses a fade effect. This flag can be used only for a Form.                                                                                     |

The Playtime parameter is optional and specifies the length of time over which the animation is played in milliseconds. The default value depends upon the animation but is typically 200 milliseconds.

**Application**

Objects: [ActiveXControl](../objects/activexcontrol.md), [Animation](../objects/animation.md), [Button](../objects/button.md), [ButtonEdit](../objects/buttonedit.md), [Calendar](../objects/calendar.md), [ColorButton](../objects/colorbutton.md), [Combo](../objects/combo.md), [ComboEx](../objects/comboex.md), [CoolBar](../objects/coolbar.md), [DateTimePicker](../objects/datetimepicker.md), [Edit](../objects/edit.md), [Form](../objects/form.md), [Grid](../objects/grid.md), [Group](../objects/group.md), [Label](../objects/label.md), [List](../objects/list.md), [ListView](../objects/listview.md), [MDIClient](../objects/mdiclient.md), [ProgressBar](../objects/progressbar.md), [PropertyPage](../objects/propertypage.md), [RichEdit](../objects/richedit.md), [Scroll](../objects/scroll.md), [SM](../objects/sm.md), [Spinner](../objects/spinner.md), [Static](../objects/static.md), [StatusBar](../objects/statusbar.md), [SubForm](../objects/subform.md), [TabBar](../objects/tabbar.md), [TabControl](../objects/tabcontrol.md), [ToolBar](../objects/toolbar.md), [ToolControl](../objects/toolcontrol.md), [TrackBar](../objects/trackbar.md), [TreeView](../objects/treeview.md), [UpDown](../objects/updown.md)
