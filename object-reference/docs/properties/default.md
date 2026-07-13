# <span>Default</span> <span>Property</span>



**Applies To:** [Button](../objects/button.md), [MsgBox](../objects/msgbox.md)

**Description**


This property determines which of a set of push buttons in a [Form](../objects/form.md), [SubForm](../objects/subform.md) or [MsgBox](../objects/msgbox.md) is the default button.



In a [Form](../objects/form.md) or [SubForm](../objects/subform.md), the Default [Button](../objects/button.md) will generate a [Select](../methodorevents/select.md) event (30) when the user presses the Enter key, even though the Default [Button](../objects/button.md) may not have the focus at the time.


If however, the user explicitly shifts the focus to another Push [Button](../objects/button.md), the automatic selection of the Default [Button](../objects/button.md) is disabled and the Enter key applies to the [Button](../objects/button.md) with the focus.


For a [Button](../objects/button.md), the Default property has the value 1 or 0. As only one [Button](../objects/button.md) can be the Default [Button](../objects/button.md), setting Default to 1 for a particular [Button](../objects/button.md) automatically sets Default to 0 for all others with the same parent.


In a [MsgBox](../objects/msgbox.md), Default specifies which button initially has the focus. It has the value 1, 2 or 3 corresponding to the three buttons that can be defined. See [Btns](btns.md) property for further details.


