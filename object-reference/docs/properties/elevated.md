# <span>Elevated</span> <span>Property</span>

**Description**

The [Elevated](elevated.md) property applies only to a [Button](../objects/button.md) whose Style is `'CommandLink'`.

Elevated is a Boolean scalar with a default value of 0. When set to 1, the icon on the CommandLink button changes from a "green arrow" to a "shield". This is intended to convey to the user that the action associated with the [Button](../objects/button.md) requires *Elevation*. This is a feature of *User Account Control* in Windows 7. See your Windows documentation for further information. Note that APL does not take any action (other than to cause the icon to change) when Elevated is set to 1. This is the responsibility of the programmer.

**Application**

Objects: [Button](../objects/button.md)
