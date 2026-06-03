<h1 class="heading"><span class="name">Writing Custom Controls for ASP.NET</span></h1>

[Writing ASP.NET Web Pages](../writing-aspnet-webpages/index.md) showed how you can build ASP.NET web pages by combining APL code with the web controls provided in the .NET namespace <code class="language-nonAPL">System.Web.UI.WebControls</code>. These controls are just ordinary .NET classes. In particular, they are extensible components that can be used to develop more complex controls that encapsulate additional functionality.

This chapter describes how you can build custom server-side controls for deployment in ASP.NET web pages.

A custom control is a .NET class that either inherits from the <code class="language-nonAPL">Control</code> class in the .NET namespace <code class="language-nonAPL">System.Web.UI</code> or inherits from a higher class that is itself based upon the <code class="language-nonAPL">Control</code> class. Like any other .NET class, a custom control is implemented in an assembly, physically as a DLL file. This chapter uses examples to explore different ways to implement a custom control:

- The <code class="language-nonAPL">Control</code> class provides a <code class="language-nonAPL">Render</code> method whose job is to generate the HTML that defines appearance of the control. The first example, the `SimpleCtl` control, overrides the <code class="language-nonAPL">Render</code> method to display a simple string "Hello World" in the browser (see [Example: The SimpleCtl Control](example-the-simplectl-control.md)).

- The `TemperatureConverterCtl1` control is an example of a compositional control, that is, one that is composed of other standard controls packaged with special functionality (see [Example: The TemperatureConverterCtl1 Control](example-the-temperatureconverterctl1-control.md)).

- The `TemperatureConverterCtl2` control uses the basic approach of the `SimpleCtl` control, but provides the same functionality as `TemperatureConverterCtl1` (see [Example: The TemperatureConverterCtl2 Control](example-the-temperatureconverterctl2-control.md)).

- The `TemperatureConverterCtl3` control illustrates how to generate events for the hosting page to catch and process (see [Example: The TemperatureConverterCtl3 Control](example-the-temperatureconverterctl3-control.md)).

These examples, which are based on a series of articles called _Advanced ASP.NET Server-Side Controls_ by George Shepherd that appeared in the msdn magazine (October 2000, January 2001 and March 2001 issues), are implemented as Dyalog classes in a namespace called `DyalogSamples` in the workspace **[DYALOG]\Samples\asp.net\temp\bin\temp.dws**. The corresponding .NET assembly **[DYALOG]\Samples\asp.net\temp\bin\temp.dll**) was generated from this workspace.
```apl
      )LOAD "C:\Program Files\Dyalog\Dyalog APL-64 18.2 Unicode\Samples\asp.net\temp\bin\temp.dws"
C:\Program Files\Dyalog\Dyalog APL-64 18.2 Unicode\Samples\asp.net\temp\bin\temp.dws saved Tue Mar  8 13:20:48 2022

      )OBS
DyalogSamples

      )CS DyalogSamples
#.DyalogSamples

      )CLASSES
SimpleCtl       TemperatureConverterCtl1        TemperatureConverterCtl2        TemperatureConverterCtl3

```
