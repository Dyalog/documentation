# <span>ValidIfEmpty</span> <span>Property</span>

**Applies To:** [ButtonEdit](../objects/buttonedit.md), [Edit](../objects/edit.md), [Spinner](../objects/spinner.md)

**Description**

This property applies to an [Edit](../objects/edit.md) object with [Style](style.md) Single and specifies whether or not an empty field is considered to be valid. It also applies to a [Spinner](../objects/spinner.md). Its value is either 0 (an empty field is not valid) or 1 (an empty field is valid. If the [FieldType](fieldtype.md) is Numeric, LongNumeric, Currency, Date or Time, the default value for ValidIfEmpty is 0. Otherwise, its default value is 1.

If ValidIfEmpty is 0 and the user attempts to *leave* the [Edit](../objects/edit.md) object by shifting the input focus to another control, or by selecting a [Button](../objects/button.md) or [MenuItem](../objects/menuitem.md), the [Edit](../objects/edit.md) object will generate a [BadValue](../methodorevents/badvalue.md) event. The [Text](text.md) property will reflect the appearance of the field and be empty, but the [Value](value.md) property will not be changed.

If ValidIfEmpty is 1 and the [FieldType](fieldtype.md) is Numeric, LongNumeric, Currency, date or Time, the [Value](value.md) property will be set to `⍬` when the user clears the field and leaves it.
