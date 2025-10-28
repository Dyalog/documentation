<h1 class="heading"><span class="name">Syncfusion Libraries</span></h1>

Dyalog does not include the [Syncfusion](https://www.syncfusion.com/) library of WPF controls. A separate licence is required from Syncfusion to use these in application development and to distribute them with run-time applications.

!!! note "Note"
    From Dyalog v20.0 onwards, you must not use the Syncfusion libraries that were distributed with previous versions of Dyalog.


## Requirements

To use the Syncfusion libraries you must be using Microsoft .NET Version 4.6.

In addition, to use the controls contained in these assemblies it is necessary to perform one or both of the following steps.

## Using XAML

If using XAML, the XAML must include the appropriate `xmlns` statements that specify where the Syncfusion controls are to be found. For example:
```xml
xmlns:syncfusion="clr-namespace:Syncfusion.Windows.Gauge;
                  assembly=Syncfusion.Gauge.WPF"
```

The above statement defines the prefix `syncfusion` to mean the specified Syncfusion namespace and assembly that contains the various Gauge controls. When the prefix `syncfusion` is subsequently used in front of a control in the XAML, the system knows where to find it. For example:
```apl
<syncfusion:CircularGauge Name="fahrenheit" Margin="10">
```

## ⎕USING

In common with all .NET types, when a Syncfusion control is loaded using XAML or using `⎕NEW` it is essential that the current value of `⎕USING` identifies the .NET namespace and assembly in which the control will be found. For example:
```apl
       ⎕USING,←⊂'Syncfusion.Windows.Gauge,YOUR_INSTALL_PATH/Syncfusion.Gauge.WPF.dll'
```

This statement tells APL to search the .NET namespace named *Syncfusion.Windows.Gauge*, which is located in the assembly file whose path depends on your specific Syncfusion installation.
