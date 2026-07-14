# <span>Translate</span> <span>Property</span>

[**Applies To**](../propertyapplies/translate.md)

**Description**

This property specifies whether or not character data is to be translated.

Translate applies to the Classic Edition only. In the Unicode Edition,
			its value is ignored.

Translate is a character vector whose values may be `'Inherit'`,
`'Translate'`, `'ANSI'` or `'None'`.

A value of `'Translate'` means that all
character property values and event parameters are translated to and from `⎕AV` using the current output translation table (WIN.DOT).

`'None'` means that character data is
passed between APL and the object with no translation.

If you set the value of the Translate property to `'ANSI'`,
APL does not attempt to resolve characters as they are typed by the user via the
Input Translate Table. Using Translate `'ANSI'` in combination with the appropriate value of [CharSet](charset.md) and the corresponding National Language keyboard will permit users to enter
strings in non-western languages.

`'Inherit'` means that the object
inherits its translation from its parent.

The default value for the Root and Printer objects is `'Translate'`,
and for most other objects it is `'Inherit'`.
