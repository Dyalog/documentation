# <span>FontObj</span> <span>Property</span>

[**Applies To**](../propertyapplies/fontobj.md)

**Description**

The FontObj property associates a font with an object. It specifies either the name of or a ref to a [Font](../objects/font.md) object

If unspecified, the default value for FontObj is an empty character vector. For most objects, this setting implies that the font used in the object is **inherited** from its parent object. However, [CoolBar](../objects/coolbar.md), [Menu](../objects/menu.md), [MenuBar](../objects/menubar.md), [StatusBar](../objects/statusbar.md), [TipField](../objects/tipfield.md), [ToolBar](../objects/toolbar.md), and [ToolControl](../objects/toolcontrol.md) objects do not inherit their font.

Note that the default value of FontObj for [Root](../objects/root.md) is also an empty character vector and that this implies the Windows default GUI font, which is a Windows user preference setting.

Note however that it is not currently possible to specify the font for [Menu](../objects/menu.md) and [MenuItem](../objects/menuitem.md) objects which are the direct descendants of a [MenuBar](../objects/menubar.md). Nor is it possible to specify the font used for the [Caption](caption.md) in a [Form](../objects/form.md).
