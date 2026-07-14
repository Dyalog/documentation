# <span>Handle</span> <span>Property</span>

[**Applies To**](../propertyapplies/handle.md)

**Description**

This is a read-only property that reports the *handle* associated with an object. For a visual object, such as a [Form](../objects/form.md) or a [Button](../objects/button.md), this is the window handle. For a [Printer](../objects/printer.md), it is the *printer device context*.

This handle allows you to access the corresponding object directly with Windows API functions via `⎕NA`. This facility must be used with care and the responsibility for its behaviour is entirely yours. Do NOT use it to delete an object. This will cause APL to crash.

An example of the use of the Handle property is to set tab stops in a [List](../objects/list.md) object. This is illustrated by the following function:
```apl
     ∇ obj TABSTOPS stops;I;LB_SETTABSTOPS;SetTabStops;sink;args
[1]   ⍝ Sets the tabstops in the List Box OBJ to be at
[2]   ⍝ stops Horizontal Dialog units.
[3]   ⍝ Sends LB_SETTABSTOPS (402) to the List Box
[4]   ⍝ See Windows SDK for Details.
[5]
[6]    I←obj ⎕WG'Items'
[7]
[8]    LB_SETTABSTOPS←402
[9]    'SetTabStops'⎕NA'U4 USER32|SendMessageA U4 U4 U4 <U4[]'
[10]
[11]   args←(obj ⎕WG'Handle') LB_SETTABSTOPS (⍴,stops)(,stops)
[12]   sink←SetTabStops args
[13]
[14]   obj ⎕WS'Items'I
     ∇
```
