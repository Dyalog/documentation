# <span>UndocksToRoot</span> <span>Property</span>



**Applies To:** [CoolBand](../objects/coolband.md), [Form](../objects/form.md), [SubForm](../objects/subform.md), [ToolControl](../objects/toolcontrol.md)

**Description**


Specifies the parent adopted by an object when its Type changes to a Form as a result of an undocking operation.


UndocksToRoot is a single number with the value 0 or 1.


If UndocksToRoot is 1, the object becomes a Form that is a child of Root and therefore becomes completely independent of the Form in which it was previously docked.


If UndocksToRoot is 0, the object becomes a Form that is a child of the Form in which it was previously docked and is therefore always displayed on top of it. This setting is appropriate for a dockable toolbar.


The default value of UndocksToRoot is 1 if the object was originally created as a child of Root; otherwise it is 0.



