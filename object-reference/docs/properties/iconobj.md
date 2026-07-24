# <span>IconObj</span> <span>Property</span>

**Description**

This property is used to specify a *large* and *small* icon for a [Form](../objects/form.md) or [SubForm](../objects/subform.md), or for the [Root](../objects/root.md) object which represents your application as a whole. Its value is either a single ref or character scalar or vector containing the name of, or ref to, an Icon object, or a 2-element vector of character vectors or refs that specifies 2 [Icon](../objects/icon.md) objects.

If empty (the default value), the standard "Dyalog APL GUI" icon is used.

The large and small icons are supplied to the Operating System which uses them as and when is appropriate. Normally, the large icon is of size 32x32 and the small icon is 16x16. If you specify an icon of a different size, the Operating System will scale it as appropriate.

The icon associated with a [Form](../objects/form.md) is displayed when the [Form](../objects/form.md) is minimised. The icon associated with `'.'` is displayed when the user presses Alt+Tab to toggle between applications. In both cases, the text shown underneath or alongside the icon is defined by the [Caption](caption.md) property.

**Application**

Objects: [Form](../objects/form.md), [HTMLRenderer](../objects/htmlrenderer.md), [MDIClient](../objects/mdiclient.md), [Root](../objects/root.md), [SubForm](../objects/subform.md), [SysTrayItem](../objects/systrayitem.md), [TabBar](../objects/tabbar.md), [ToolBar](../objects/toolbar.md)
