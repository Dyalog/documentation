# Fields

A Field behaves just like an APL variable.

To get the value of a Field, you reference its name; to set the value of a Field, you assign to its name. Conceptually, the Field value is stored *in* the Field. However, Fields differ from variables in that they possess characteristics that control their accessibility.

A Field may be declared anywhere in a Class script by a `:Field` statement. This specifies:

- the name of the Field
- whether the Field is Public or Private
- whether the Field is Instance or Shared
- whether or not the Field is ReadOnly
- the .NET type for the Field when the Class is exported as a .NET Assembly.
- optionally, an initial value for the Field.

Note that [Triggers](../../../triggers/triggers.md) may be associated with Fields. See [Trigger Fields](trigger-fields.md) for details.
