# <span>MDIMenu</span> <span>Property</span>

**Applies To:** [MenuBar](../objects/menubar.md)

**Description**

This property specifies the name of, or ref to, the [Menu](../objects/menu.md) object that is nominated as the "Window" menu in an MDI application. If such a menu is defined, the [Caption](caption.md)s of all the child [Form](../objects/form.md)s are automatically added to it below any other [Menu](../objects/menu.md) or [MenuItem](../objects/menuitem.md) objects that the application has created directly. This list is separated from the preceding items by a separator. The entry for the currently active [SubForm](../objects/subform.md) is checked and the user may switch between [SubForm](../objects/subform.md)s by selecting from this list.

Note that the additional separator and the items representing the list of child forms are not Dyalog APL/W objects and may not be accessed by the application. If you prefer to maintain your own "window list" you should not use this property.
