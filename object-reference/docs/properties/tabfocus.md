# <span>TabFocus</span> <span>Property</span>

**Applies To:** [TabControl](../objects/tabcontrol.md)

**Description**

The TabFocus property specifies the focus behaviour for the [TabControl](../objects/tabcontrol.md) object and may

TabFocus is a character vector that may be `'Normal'` (the default), `'Never'` or `'ButtonDown'`.

If TabFocus is `'Normal'`, the tabs or buttons in a [TabControl](../objects/tabcontrol.md) do not immediately receive the input focus when clicked, but only when clicked a second time. This means that, normally, when the user circulates through the tabs, the input focus will be given to the appropriate control in the associated SubForm. However, if the user clicks twice in succession on the same tab or button, the [TabControl](../objects/tabcontrol.md) itself will receive the input focus.

If TabFocus is `'ButtonDown'`, the tabs or buttons in a [TabControl](../objects/tabcontrol.md) receive the input focus when clicked.

If TabFocus is `'Never'`, the tabs or buttons in a [TabControl ](../objects/tabcontrol.md)*never* receive the input focus. This allows the user to circulate through a set of tabbed SubForms without ever losing the input focus to the [TabControl](../objects/tabcontrol.md) itself.
