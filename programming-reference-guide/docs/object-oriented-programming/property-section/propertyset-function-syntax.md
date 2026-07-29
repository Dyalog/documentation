

# <span>PropertySet Function</span> `Set ipa`

The name of the PropertySet function must be `Set`, but is case-independent. For example, `set`, `Set`, `sEt` and `SET` are all valid names for the PropertySet function.

The PropertySet function must be monadic and may not return a result.

`ipa` is an instance of the internal class [PropertyArguments](propertyarguments-class.md).

In all cases, `ipa.Name` contains the name of the Property being referenced and `NewValue` contains the new value(s) for the element(s) of the Property being assigned.

If the Property is *Simple*, `ipa.Indexers` is undefined (`VALUE ERROR`).

If the Property is *Numbered*, `ipa.Indexers` is an integer vector of the same length as the rank of the property (as implied by the result of the `Shape` function) that identifies a single element of the Property whose value is to be set.

If the Property is Keyed, `ipa.IndexersSpecified` is a Boolean vector with the same length as the rank of the property  (as implied by the result of the `Shape` function). A value of 1 means that an indexing array for the corresponding dimension of the Property was specified, while a value of 0 means that the corresponding dimension was elided.`ipa.Indexers` is a vector containing the arrays that were specified within the square brackets in the assignment expression. Specifically, `ipa.Indexers` will contain one fewer elements than, the number of semi-colon (;) separators. If any index was elided, the corresponding element of `ipa.Indexers` is `⎕NULL`. However, if the Keyed Property is being assigned in its entirety, without square-bracket indexing, `ipa.Indexers` is undefined (`VALUE ERROR`).

!!! note
    It is not possible to predict the number of times that a  PropertyGet, PropertySet or PropertyShape function will be called by a particular APL expression, as this depends upon how that expression is implemented internally. You should therefore not rely on the number of times that a Get, Set or Shape function is called, and none should have any side effects on any other APL object
