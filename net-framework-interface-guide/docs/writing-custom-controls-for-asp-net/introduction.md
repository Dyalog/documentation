<h1 class="heading"><span class="name">Introduction</span></h1>

The previous chapter showed how you can build ASP.NET Web Pages by combining APL code with the Web Controls provided in the .NET Namespace `System.Web.UI.WebControls`. These controls are in fact just ordinary .NET classes. In particular, they are extensible components that can be used to develop more complex controls that encapsulate additional functionality.

This chapter describes how you can go about building custom server-side controls, for deployment in ASP.NET Web Pages.

A custom control is simply a .NET class that inherits from the `Control` class in the .NET Namespace `System.Web.UI`, or inherits from a higher class that is itself based upon the `Control` class. Like any other .NET class, a custom control is implemented in an assembly, physically as a DLL file. This chapter explores three different ways to implement a custom control.

The `Control` class provides a `Render` method whose job is to generate the HTML that defines appearance of the control. The first example, the `SimpleCtl` control, overrides the `Render` method to display a simple string "Hello World" in the browser.

The `TemperatureConverterCtl1` control is an example of a compositional control, that is, one that is composed of other standard controls packaged with special functionality. The `TemperatureConverterCtl2` control, uses the basic approach of the `SimpleCtl` control, but provides the same functionality as `TemperatureConverterCtl1`. The `TemperatureConverterCtl3` control illustrates how to generate events for the hosting page to catch and process.

These examples, which are based upon a series of articles called *Advanced ASP.NET Server-Side Controls* by George Shepherd that appeared in the *msdn magazine* (October 2000, January 2001 and March 2001 issues), are implemented as Dyalog classes in a namespace called `DyalogSamples` in the workspace `samples\asp.net\temp\bin\temp.dws.` The corresponding .NET Assembly `samples\asp.net\temp\bin\temp.dll` was generated from this workspace.
```
      )LOAD "C:\Program Files (x86)\Dyalog\Dyalog APL 15.0 Unicode\Samples\asp.net\temp\bin\temp.dws"
```
```apl
C:\Program Files (x86)\Dyalog\Dyalog APL 15.0 Unicode\Samples\asp.net\temp\bin\temp.dws saved Tue Nov 22 15:04:11 2016
```
```
      )OBS
DyalogSamples
      )CS DyalogSamples
#.DyalogSamples
      )CLASSES
SimpleCtl       TemperatureConverterCtl1        TemperatureConverterCtl2        TemperatureConverterCtl3
```
