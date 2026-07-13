# <span>HintObj</span> <span>Property</span>

[**Applies To**](../propertyapplies/hintobj.md)

**Description**


The HintObj property is a character vector or ref that specifies the name of, or a ref to, an object in which the "help" message defined by the [Hint](hint.md) property is to be displayed. This message is displayed when the user positions the mouse pointer over the object. The [Hint](hint.md) is displayed by automatically setting the [Caption](caption.md) or [Text](text.md) property of the object named by HintObj.


The following types of object can therefore be used to display Hints: [Button](../objects/button.md), [Edit](../objects/edit.md), [Combo](../objects/combo.md), [Group](../objects/group.md), [Form](../objects/form.md), [Label](../objects/label.md), [Menu](../objects/menu.md), [MenuItem](../objects/menuitem.md), [StatusField](../objects/statusfield.md), [SubForm](../objects/subform.md) and [Text](../objects/text.md). For a [StatusField](../objects/statusfield.md) that has both [Caption](caption.md) and [Text](text.md) properties, the text property is used for displaying hints.


When the user moves the mouse pointer away from the object, the [Caption](caption.md) or [Text](text.md) property of the object specified by HintObj is reset to an empty vector.


Note that if HintObj is empty, its value is inherited from its parent. Thus setting HintObj on a [Form](../objects/form.md) defines the default location for displaying [Hint](hint.md)s for all the controls in that [Form](../objects/form.md). Setting HintObj on [Root](../objects/root.md) defines the default location for hints for the entire application.



