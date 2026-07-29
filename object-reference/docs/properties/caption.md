# <span>Caption</span> <span>Property</span>

**Description**

The Caption property is a character vector specifying fixed text associated with the object. For example, Caption defines the label on a [Button](../objects/button.md), the title of a [Form](../objects/form.md), [SubForm](../objects/subform.md) or [MsgBox](../objects/msgbox.md), the heading in a [Group](../objects/group.md), and the text of a [Menu](../objects/menu.md) or a [MenuItem](../objects/menuitem.md).

For the [Root](../objects/root.md) object, Caption specifies the text displayed when Alt+Tab is used to switch to the Dyalog APL/W application. It may be used in conjunction with the [IconObj](iconobj.md) property which specifies the name of an [Icon](../objects/icon.md) object to be displayed alongside this text.

Its default value is an empty vector.

For a [Button](../objects/button.md) or [Label](../objects/label.md), if the Caption property  contains one or more linefeed characters (`⎕UCS 10`) the text is top-left justified or, for a [Button](../objects/button.md) with [Style](style.md)`'Push'`, centre-justifed ;  and automatically wraps on white-space characters (such as space and tab) to fit in the width provided.

For controls that support this feature, a single ampersand (&) is used to designate that the following character (if present) is an access key or an accelerator key and that character is underlined. The ampersand is not itself displayed. To negate this feature and cause an ampersand to be displayed, it is necessary to specify "&&".

**Application**

Objects: [BrowseBox](../objects/browsebox.md), [Button](../objects/button.md), [ColorButton](../objects/colorbutton.md), [CoolBand](../objects/coolband.md), [FileBox](../objects/filebox.md), [Form](../objects/form.md), [Group](../objects/group.md), [HTMLRenderer](../objects/htmlrenderer.md), [Label](../objects/label.md), [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md), [MsgBox](../objects/msgbox.md), [PropertyPage](../objects/propertypage.md), [PropertySheet](../objects/propertysheet.md), [Root](../objects/root.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md), [TabBtn](../objects/tabbtn.md), [TabButton](../objects/tabbutton.md), [ToolButton](../objects/toolbutton.md)
