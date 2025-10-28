<h1 class="heading"><span class="name">Prerequisites</span></h1>

The Dyalog version {{ version_majmin }} .NET Framework interface requires version 4.0 or greater of Microsoft .NET Framework. It does *not* operate with earlier versions of the .NET Framework. In addition:

- .NET Framework version 4.5 is needed for full Data Binding support (including support for the `INotifyCollectionChanged` interface, which is used by Dyalog to notify a data consumer when the contents of a variable, that is data bound as a list of items, changes).
- IIS needs to be installed before installing Dyalog APL in order to access the examples in the `Samples/asp.net` sub-directory – if IIS and ASP.NET are not present, the `asp.net` sub-directory will not be installed during the Dyalog installation.

Note that .NET Framework is specific to Microsoft Windows; the cross-platform .NET is also supported (see below).
