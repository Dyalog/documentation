

# <span>PropertyGet Function</span> `R←Get {ipa}`

The name of the PropertyGet function must be `Get`, but is case-independent. For example, `get`, `Get`, `gEt` and `GET` are all valid names for the PropertyGet function.

The PropertyGet function must be result returning. For a Simple Property, it may be monadic or niladic. For a Numbered or Keyed Property it must be monadic.

The result `R` may be any array. However, for a Keyed Property, `R` must conform to the rank and shape specified by `ipa.Indexers` or be scalar.

If monadic, `ipa` is an instance of the internal class [PropertyArguments](propertyarguments-class.md).

In all cases, `ipa.Name` contains the name of the Property being referenced and `NewValue` is undefined (`VALUE ERROR`).

If the Property is *Simple*, `ipa.Indexers` is undefined (`VALUE ERROR`).

If the Property is *Numbered*, `ipa.Indexers` is an integer vector of the same length as the rank of the property (as implied by the result of the `Shape` function) that identifies a single element of the Property whose value is to be obtained. In this case, `R` must be scalar.

If the Property is Keyed, `ipa.IndexersSpecified` is a Boolean vector with the same length as the rank of the property  (as implied by the result of the `Shape` function). A value of 1 means that an indexing array for the corresponding dimension of the Property was specified, while a value of 0 means that the corresponding dimension was elided. `ipa.Indexers` is a vector of the same length  containing the arrays that were specified within the square brackets in the reference expression. Specifically, `ipa.Indexers` will contain one fewer elements than, the number of semi-colon (;) separators. If any index was elided, the corresponding element of `ipa.Indexers` is `⎕NULL`.

!!! note
    It is not possible to predict the number of times that a PropertyGet, PropertySet or PropertyShape function will be called by a particular APL expression, as this depends upon how that expression is implemented internally. You should therefore not rely on the number of times that a Get, Set or Shape function is called, and none should have any side effects on any other APL object
