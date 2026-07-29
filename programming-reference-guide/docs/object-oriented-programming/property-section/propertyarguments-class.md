# PropertyArguments Class

Where appropriate, APL supplies the PropertyGet and PropertySet functions with an argument that is an instance of the internal class `PropertyArguments`.

`PropertyArguments` has just 3 read-only Fields which are as follows:

|-------------------|-----------------------------------------------------------------------------------------------------------------------|
|`Name`             |The name of the property. This is useful when one function is handling several properties.                             |
|`NewValue`         |Array containing the new value for the Property or for selected element(s) of the property as specified by `Indexers` .|
|`IndexersSpecified`|A Boolean vector that identifies which dimensions of the Property are to be referenced or assigned.                    |
|`Indexers`         |A vector that identifies the elements of the Property that are to be referenced or assigned.                           |
