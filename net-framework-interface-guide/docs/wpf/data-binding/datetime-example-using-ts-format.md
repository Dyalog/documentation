<h1 class="heading"><span class="name">Example 6a (Casting to DateTime)</span></h1>

This example is similar to Example 6 but illustrates how numeric data in `⎕TS` format can be converted to  DateTime type.

## The XAML

The XAML shown below describes a Window containing a StackPanel, inside which is a ListBox.
```xml
<Window
  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="DateTimes using ⎕TS data"
    SizeToContent="WidthAndHeight" >
    <StackPanel>
         <TextBlock Text="Some High Tides at Portsmouth, England"
          FontSize="18" Margin="5"/>
         <ListBox Name="TideTimes" Height="200"
          Margin="5" />
    </StackPanel>
</Window>
```

## The APL Code

The function `Tides` is shown below.
```apl
     ∇ Tides;⎕USING;win;dt;Highs
[1]    ⎕USING←'System'
[2]    win←LoadXAML XAML_Tides
[3]    win.times←win.FindName⊂'TideTimes'
[4]    Highs←(⊂2016 2 18),¨(7 9)(8 44)(19 47)(21 47)
[5]    Highs,←(⊂2016 2 19),¨(8 17)(10 12)(20 51)(22 51)
[6]    dt←7↑¨Highs
[7]    win.times.ItemsSource←DateTime(2015⌶)'dt'
[8]    sink←win.ShowDialog
     ∇

```

`Tides[3]` uses FindName to obtain a ref to the ListBox (defined in the XAML) named *TideTimes*:
```apl

[3]    win.times←win.FindName⊂'TideTimes'
```

`Tides[4-5]` creates a vector of integer vectors each of which species the time and date of a high tide at Portsmouth. `Tides[6]` extends each to 7-elements, which is required to represent a DateTime object.

Then, `Tides[7]` creates a binding source object from this array and assigns it to the ItemsSource property of the ListBox. Note that the left argument DateTime specifies that the data be cast to that type.
```apl

[7]    win.times.ItemsSource←DateTime(2015⌶)'dt'
```

## Testing the Data Binding
```apl
      )LOAD wpfintro
      DataBinding.NetObjects.Tides
```

![](../../img/tides.png)

`Tides[3]` uses FindName to obtain a ref to the ListBox (defined in the XAML) named *TideTimes*:
```apl

[3]    win.times←win.FindName⊂'TideTimes'
```

`Tides[4-5]` creates a vector of integer vectors each of which species the time and date of a high tide at Portsmouth. `Tides[6]` extends each to 7-elements, which is required to represent a DateTime object.

Then, `Tides[7]` creates a binding source object from this array and assigns it to the ItemsSource property of the ListBox. Note that the left argument DateTime specifies that the data be cast to that type.
```apl

[7]    win.times.ItemsSource←DateTime(2015⌶)'dt'
```

## Testing the Data Binding
```apl
      )LOAD wpfintro
      DataBinding.NetObjects.Tides
```

![](../../img/tides.png)
