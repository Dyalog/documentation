# <span>State</span> <span>Property</span>

**Applies To:** [Button](../objects/button.md), [Form](../objects/form.md), [SubForm](../objects/subform.md), [TabButton](../objects/tabbutton.md), [ToolButton](../objects/toolbutton.md)

**Description**

This property determines the state of a [Button](../objects/button.md), [TabButton](../objects/tabbutton.md), [ToolButton](../objects/toolbutton.md), [Form](../objects/form.md), or [SubForm](../objects/subform.md). It is a single number with the value 0 (the default), 1, or 2 ([Form](../objects/form.md) and [SubForm](../objects/subform.md)).

If the [Style](style.md) property is `'Push'`, a State of 0 means that the pushbutton is displayed normally (out). If its State is 1, the pushbutton is displayed depressed (in).

If the [Style](style.md) property is `'Radio'` or `'Check'`, 0 means "not selected" and 1 means "selected". Note that only one of a group of buttons with [Style ](style.md)`'Radio'` that share the same parent may have State 1. Setting State to 1 automatically deselects all the others in the group.

For a [Form](../objects/form.md) or [SubForm](../objects/subform.md), a value of State of 0 means that the [Form](../objects/form.md) is currently displayed in its "normal" state. 1 means that the [Form](../objects/form.md) is currently minimised (displayed as an icon). The value 2 indicates that the [Form](../objects/form.md) is maximised and displayed full-screen. The State of a [Form](../objects/form.md) can be changed using [`⎕WS`](../../../language-reference-guide/system-functions/ws).
