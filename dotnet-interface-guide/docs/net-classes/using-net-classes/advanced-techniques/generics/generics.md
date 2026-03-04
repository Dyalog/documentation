# Generics

The .NET interface supports creating concrete versions of generic classes, instantiating them, and calling generic methods. This is done by calling `43⌶` with a right argument of `632` (for more information on `43⌶`, see the Dyalog APL Language Reference Guide). Note that this I-beam will be replaced with something that is better integrated into the language in a future Dyalog version.

A generic class is a class that has type parameters, which must be given values to create a concrete version of the class. Similarly, a generic method has type parameters that must be specified before the method can be called.

The result of `43⌶632` is a monadic operator, which is used to apply the type arguments of generic classes or methods.

See also:

- [Section ](creating-a-concrete-version-of-a-generic-class.md)

- [Section ](calling-a-generic-method.md)

- [Section ](calling-a-niladic-generic-method.md)
