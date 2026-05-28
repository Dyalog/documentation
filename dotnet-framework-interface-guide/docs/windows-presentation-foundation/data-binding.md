<h1 class="heading"><span class="name">Data Binding</span></h1>

This section provides some simple examples of WPF data binding using Dyalog. Each example builds upon the previous ones, so it is advisable to work through them in order.

The example code used in throughout section is included in the **[DYALOG]\ws\wpfintro.dws** workspace.

## Example 1: Text

This example illustrates data binding using XAML to specify the user interface coupled with an APL function to drive it and handle the data binding.

### The XAML

The XAML shown below describes a <code class="language-nonAPL">Window</code> containing a <code class="language-nonAPL">TextBox</code>.
```xml
<Window
 xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
 xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
 Name="Temp"
 Title="Data Binding (Text)"
 SizeToContent="WidthandHeight">
     <TextBox Name="txt" Width="300" Margin="5"
     Text="{Binding txtSource,Mode=TwoWay,UpdateSourceTrigger=PropertyChanged}"/>
</Window>
```

The data binding expression
```xml
     Text="{Binding txtSource,Mode=TwoWay,UpdateSourceTrigger=PropertyChanged}"/>

```

specifies that the <code class="language-nonAPL">Text</code> property of the <code class="language-nonAPL">TextBox</code> is bound to a value in the <code class="language-nonAPL">Binding Source</code> (which has yet to be defined) whose path is <code class="language-nonAPL">txtSource</code>. The binding mode is set to <code class="language-nonAPL">TwoWay</code>, which means that any change in the <code class="language-nonAPL">TextBox</code> will be reflected in a new value in the <code class="language-nonAPL">Binding Source</code>, and any change in the <code class="language-nonAPL">Binding Source</code> will be reflected in the <code class="language-nonAPL">TextBox</code>. The value in the <code class="language-nonAPL">Binding Source</code> will be updated when the property (in this case the <code class="language-nonAPL">Text</code> property) changes.

### The APL Code

The function `Text` that generates this example is shown below. The argument `txt` is the text to be displayed initially in the TextBox. The variable `XAML_Text` contains the [XAML that describes the user interface](#the-xaml).
```apl
     ∇ Text txt;⎕USING;str;xml;win
[1]    ⎕USING←,⊂'System.Windows.Controls,WPF/PresentationFramework.dll'
[2]    win←LoadXAML XAML
[3]    win.txtBox←win.FindName⊂'txt'
[4]
[5]    ⎕EX'txtSource'
[6]    txtSource←txt
[7]    win.txtBox.DataContext←2015⌶'txtSource'
[8]
[9]    win.Show
     ∇

```

The utility function `LoadXAML` incorporates the 3 lines of code `[5-7]` used to create a WPF window from XAML that were coded in-line in the [Temperature Converter Tutorial](temperature-converter-tutorial.md):
```apl
     ∇ win←LoadXAML xaml;⎕USING;str;xml
[1]    ⎕USING←'System.IO'
[2]    ⎕USING,←⊂'System.Windows.Markup'
[3]    ⎕USING,←⊂'System.Xml,system.xml.dll'
[4]    ⎕USING←,⊂'System.Windows.Controls,WPF/PresentationFramework.dll'
[5]    str←⎕NEW StringReader(⊂xaml)
[6]    xml←⎕NEW XmlTextReader str
[7]    win←XamlReader.Load xml
     ∇

```

`Text[1]` defines the .NET search path needed to access the WPF controls:
```apl

[1]    ⎕USING←,⊂'System.Windows.Controls,WPF/PresentationFramework.dll'
```

`Text[2-3]` uses the utility function `LoadXAML` to load a WPF user-interface from the XAML and then uses the `FindName` method to obtain a reference to the object named `txt`:
```apl

[2]    win←LoadXAML XAML
[3]    win.txtBox←win.FindName⊂'txt'
```

`Text[5-6]` initialise a new global variable called `txtSource` to the value of the argument. When using a global variable as a data binding source, it is generally advisable to establish a new variable by first expunging it. This is because its binding type (the exported type of the data bound variable) is stored in the workspace along with its value, and the binding type (were it to be incorrect) cannot be changed once it has been established:
```apl

[5]   ⎕EX'txtSource'
[6]   txtSource←txt
```

`Text[7]`creates a Binding Source object using `2015⌶` and assigns it to the `DataContext` property of the TextBox object. As it is a character vector, the exported Type for the bound variable `txtSource` is <code class="language-nonAPL">System.String</code>, which is appropriate for the Text property of a TextBox:
```apl

[7]    win.txtBox.DataContext←2015⌶'txtSource'
```

`Text[9]` displays the Window:
```apl

[9]   win.Show
```

Although the APL local variable `win` goes out of scope when the function terminates, the Window remains visible until the user has closed it.

### Testing the Data Binding

The following expressions can be used to explore the effect of data binding:
```apl
      )LOAD wpfintro
      )CS DataBinding.Text
#.DataBinding.Text

```

```apl
      Text 'Hello World'
```

![](../../img/s-data-binding-eg1-1.png)

```apl
      txtSource←⌽txtSource
```

![](../../img/s-data-binding-eg1-2.png)

Typing into the TextBox changes the value of the bound variable:

![](../../img/s-data-binding-eg1-3.png)
```apl
      txtSource
What is in txtSource now?

```

## Example 2: Fontsize

## Example 3: Text and Fontsize – Code

## Example 4: Text and Fontsize – XAML

## Example 5: Filtered List

## Example 6: .NET Object

## Example 6a: .NET Onbject using TS Format

## Example 7: Datagrid

## Example 8: Datagrid Matrix