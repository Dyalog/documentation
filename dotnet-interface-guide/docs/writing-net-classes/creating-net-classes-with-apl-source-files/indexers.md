# Indexers

An indexer is a property of a class that enables an instance of that class (an object) to be indexed in the same way as an array, if the host language supports this feature. Languages that support object indexing include C#. Dyalog also allows indexing to be used on objects. This means that you can define an APL class that exports an indexer, and you can use the indexer from C# or Dyalog.

Indexers are defined in the same way as properties, that is, between `:Property Default` and `:EndProperty` statements. There can only be one indexer defined for a class.

The `:Property Default` statement in Dyalog is closely modelled on the indexer feature in C# and employs similar syntax.
If you use `ILDASM` to browse a .NET class containing an indexer, you will see the indexer as the default property of that class, which is how it is implemented.
