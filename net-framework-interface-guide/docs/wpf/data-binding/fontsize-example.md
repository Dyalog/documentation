<h1 class="heading"><span class="name">Example 2</span></h1>

This example illustrates the use of the optional left argument to `2015⌶` to specify the data type used to export the value of the bound variable.

![](../../img/data-binding-text-xaml-1.png)

## The XAML

The XAML shown below,  describes the same Window containing a TextBox as before.
```xml
<Window
 xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
 xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
 Name="Temp"
 Title="Data Binding (FontSize)"
 SizeToContent="WidthandHeight">
     <TextBox Name="txt" Text="Hello World" Width="300"
      Margin="5"
      FontSize="{Binding sizeSource,Mode=OneWay}"/>
</Window>

```

This time, the data binding expression is:
```xml
      FontSize="{Binding sizeSource,Mode=OneWay}"/>
```

This specifies that the FontSize property of the TextBox is bound to a value in the Binding Source (which has yet to be defined) whose path is `sizeSource`. The binding mode is set to `OneWay` which means that the FontSize property depends on the data value but not vice versa. Were the FontSize to change for any external reason (which is admittedly unlikely in the case of FontSize), it would not alter the value in `sizeSource` to which it is bound.

## The APL Code

The function `FontSize` is almost identical to the function `Text` which is described in Example 1.
```apl
     ∇ FontSize size;⎕USING;win
[1]    ⎕USING←'System'
[2]    ⎕USING,←⊂'System.Windows.Controls,WPF/PresentationFramework.dll'
[3]    win←LoadXAML XAML
[4]    win.txtBox←win.FindName⊂'txt'
[5]
[6]    ⎕EX'sizeSource'
[7]    sizeSource←size
[8]    win.txtBox.DataContext←Int32(2015⌶)'sizeSource'
[9]
[10]   win.Show
     ∇

```

The key difference is in `FontSize[8]`. Here the left argument of `(2015⌶)` is `Int32`. This means that the exported Type of the variable `sizeSource` will be Int32. This Type (a 32-bit integer) is required by the FontSize property of a TextBox; no other Type will do. If this were omitted, APL would export the value of the variable using a Type dependent on its internal format (most likely Int16) and the binding would fail.
```apl

[8]    win.txtBox.DataContext←Int32(2015⌶)'sizeSource'
```

## Testing the Data Binding
```apl
      )LOAD wpfintro
      )CS DataBinding.FontSize
```
```apl
      FontSize 12
```

![](../../img/data-binding-fontsize-xaml-1.png)
```apl
      sizeSource
12
      sizeSource←30
```

![](../../img/data-binding-fontsize-xaml-2.png)
