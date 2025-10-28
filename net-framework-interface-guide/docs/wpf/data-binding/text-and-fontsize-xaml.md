<h1 class="heading"><span class="name">Example 4</span></h1>

This example uses XAML to specify the user-interface and the main components of the data binding.

## The XAML

The XAML is much the same as in Example 1 and 2 except that it connects two properties Text and FontSize of the same TextBox to two Paths *txtSource* and *sizeSource*.
```xml
<Window
 xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
 xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
 Name="Temp"
 Title="Data Binding (Text and FontSize)"
 SizeToContent="WidthandHeight">
     <TextBox Name="txt" Width="350" Margin="5"
      Text="{Binding txtSource,Mode=TwoWay,
             UpdateSourceTrigger=PropertyChanged}"
      FontSize="{Binding sizeSource,Mode=OneWay}"/>
</Window>
```

## The APL Code

The function `TextFontSize` is shown below.
```apl
     ∇ TextFontSize(txt size);⎕USING;str;xml;win;options
[1]    ⎕USING←'System'
[2]    ⎕USING,←⊂'System.Windows,WPF/PresentationFramework.dll'
[3]
[4]    win←LoadXAML XAML
[5]
[6]    src←⎕NS''
[7]    src.(txtSource sizeSource)←txt size
[8]    options←2 2⍴'txtSource'String'sizeSource'Int32
[9]
[10]   win.DataContext←options(2015⌶)'src'
[11]
[12]   win.Show
     ∇
```

Lines [6-7] create a new namespace src containing two variables `txtSource` and `sizeSource` which are initialised to the arguments of the function.
```apl

[6]    src←⎕NS''
[7]    src.(txtSource sizeSource)←txt size
```

Line [8] creates a local variable named options which will be used as the left argument of  `2015⌶)`. It is a 2-column matrix. The first column is a list of the names of the variables which are to be exported by the namespace when used as a Binding Source. The second column specifies their data types.
```apl

[8]    options←2 2⍴'txtSource'String'sizeSource'Int32
```

Line [10] creates a Binding Source object from the namespace `src` and a left argument `options` and assigns it to the DataContext property of the Window `win`.
```apl

[10]   win.DataContext←options(2015⌶)'src'
```

An alternative would be to assign it to the DataContext property of the TextBox object, but this would require one further line of code to identify it. The reason this works is that the DataContext property of a TextBox (and many other controls) is inherited from its parent Window. This feature allows a single Binding Source namespace to be used to specify data bindings between its component variables and any number of properties of any number of controls in the same Window.

As shown before, the left argument of `2015⌶)` is optional. Without it, the namespace would export all its variables using default binding types. In this case, because the binding type of `sizeSource` must be specified as Int32, it is necessary to use a left argument, which means specifying all the variables involved.

## Testing the Data Binding
```apl
      )LOAD wpfintro
      )CS DataBinding.TextFontSizeXAML
```
```apl
      DB_Text_FontSize_XAML'Hello World' 30
```

![](../../img/data-binding-text-fontsize-1.png)
```apl
      src.(txtSource sizeSource←(⌽txtSource) 18)
```

![](../../img/data-binding-text-fontsize-2.png)

As in previous examples, when the user changes the text, the new text appears in `txtSource`.

![](../../img/data-binding-text-fontsize-3.png)
```apl
      src.txtSource
Learn to play the bouzouki!
```
