# <span>MultiSelect</span> <span>Property</span>

**Applies To:** [TabControl](../objects/tabcontrol.md)

**Description**

The [TabControl](../objects/tabcontrol.md) property specifies whether or not the user can select more than one button in a [TabControl](../objects/tabcontrol.md) at the same time, by holding down the Ctrl key when clicking.

MultiSelect is a single number with the value 0 (only 1 button may be selected) or 1 (more than one button may be selected); the default is 0.

MultiSelect apples only if the [Style](style.md) of the [TabControl](../objects/tabcontrol.md) is `'Buttons'` or `'FlatButtons'`, and is ignored if [Style](style.md) is `'Tabs'`.

Note that the [State](state.md) property of the associated [TabButton](../objects/tabbutton.md) object reports whether or not the button is selected.
