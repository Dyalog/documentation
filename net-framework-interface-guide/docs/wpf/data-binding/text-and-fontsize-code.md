<h1 class="heading"><span class="name">Example 3</span></h1>

This example uses APL code to both build the user-interface (instead of using XAML) and handle the data binding. In this case both the Text and the FontSize properties are bound to APL variables. The function is shown below:
```apl
     ∇ TextFontSize(txt size);⎕USING;win;sink
[1]    ⎕USING←'System'
[2]    ⎕USING,←,⊂'System.Windows.Controls,WPF/PresentationFramework.dll'
[3]    ⎕USING,←⊂'System.Windows.Controls.Primitives,WPF/PresentationFramework.dll'
[4]    ⎕USING,←⊂'System.Windows,WPF/PresentationFramework.dll'
[5]    ⎕USING,←⊂'System.Windows,WPF/PresentationCore.dll'
[6]
[7]   ⍝ Create a Window, DockPanel and TextBox
[8]    win←⎕NEW Window
[9]    win.SizeToContent←SizeToContent.WidthAndHeight
[10]   win.Title←'Data Binding (Text and FontSize)'
[11]   win.txtBox←⎕NEW TextBox
[12]   win.txtBox.Width←350
[13]   win.Content←win.txtBox
[14]
[15]  ⍝ Define data binding from variable "txtSource"
[16]  ⍝ to the Text property of TextBox win.txtBox
[17]   ⎕EX'txtSource'
[18]   txtSource←txt
[19]   win.txtbinding←⎕NEW Data.Binding(⊂'txtSource')
[20]   win.txtbinding.Source←2015⌶'txtSource'
[21]   win.txtbinding.Mode←Data.BindingMode.TwoWay
[22]   win.txtbinding.UpdateSourceTrigger←Data.UpdateSourceTrigger.PropertyChanged
[23]   sink←win.txtBox.SetBinding TextBox.TextProperty win.txtbinding
[24]
[25]  ⍝ Define data binding from variable "sizeSource"
[26]  ⍝ to the FontSize property of TextBox win.txtBox
[27]   ⎕EX'sizeSource'
[28]   sizeSource←size
[29]   win.fntbinding←⎕NEW Data.Binding(⊂'sizeSource')
[30]   win.fntbinding.Source←Int32(2015⌶)'sizeSource'
[31]   win.fntbinding.Mode←Data.BindingMode.OneWay
[32]   sink←win.txtBox.SetBinding TextBox.FontSizeProperty win.fntbinding
[33]
[34]   win.Show
     ∇

```

Apart from the code that creates the controls, the only material difference between this and the previous examples is the way that the bindings are handled.

In code (as opposed to using XAML) this is done using explicit Binding objects[^1] The code for binding the Text property to the `txtSource` variable is as follows:
```apl
[19]   win.txtbinding←⎕NEW Data.Binding(⊂'txtSource')
[20]   win.txtbinding.Source←2015⌶'txtSource'
[21]   win.txtbinding.Mode←Data.BindingMode.TwoWay
[22]   win.txtbinding.UpdateSourceTrigger←Data.UpdateSourceTrigger.PropertyChanged
[23]   sink←win.txtBox.SetBinding TextBox.TextProperty win.txtbinding
```

Line [19] creates a Binding object, passing the constructor  the name of the APL variable `txtSource` as the Path to the binding value.
```apl
[19]   win.txtbinding←⎕NEW Data.Binding(⊂'txtSource')
```

Line [20] creates a Binding Source object using `2015⌶` as before, but this time assigns it to the Source property of the Binding object.
```apl
[20]   win.txtbinding.Source←2015⌶'txtSource'
```

Line [21] sets the Mode property of the Binding object to TwoWay (a field of the BindingMode Type). As in Example 1, this specifies two-way binding.
```apl
[21]   win.txtbinding.Mode←Data.BindingMode.TwoWay
```

Line [22] sets the UpdateSourceTrigger property of the Binding object to PropertyChanged (a field of the UpdateSourceTrigger Type). This causes the value in the Binding Source (in this case `txtSource`) to be changed whenever the property (in this case the Text property) of the TextBox changes. This will occur on every keystroke.
```apl

[22]   win.txtbinding.UpdateSourceTrigger←Data.UpdateSourceTrigger.PropertyChanged
```

(Note that the three types Binding, BindingMode and UpdateSourceTrigger are located in System.Windows.Data)

The code that establishes the binding between the `sizeSource` variable and the FontSize property is very similar.

```apl
[29]   win.fntbinding←⎕NEW Data.Binding(⊂'sizeSource')
[30]   win.fntbinding.Source←Int32(2015⌶)'sizeSource'
[31]   win.fntbinding.Mode←Data.BindingMode.OneWay
[32]   sink←win.txtBox.SetBinding
                TextBox.FontSizeProperty win.fntbinding
```

Note however that (as in Example 2) the left-argument to `(2015⌶)` specifies that the exported data type of the `sizeSource` variable is to be Int32.

## Testing the Data Binding
```apl
      )LOAD wpfintro
      )CS DataBinding.TextFontSizeCode
```
```apl
      TextFontSize 'Hello World' 30
```

![](../../img/data-binding-text-fontsize-1.png)
```apl
      txtSource sizeSource←(⌽txtSource) 18
```

![](../../img/data-binding-text-fontsize-2.png)

As in previous examples, when the user changes the text, the new text appears in `txtSource`.

![](../../img/data-binding-text-fontsize-3.png)
```apl
      txtSource
Learn to play the bouzouki!

```

!!! note
    It is perhaps worth mentioning that if you want to bind two properties *of the same object* to two APL variables, it has to be done by writing code as shown in this example, using two separate Binding Source objects. This is because using XAML you may only associate a single Binding Source to an object.

    However, this minor restriction is easily surmounted by using an APL namespace as a Binding Source as illustrated in the next Example.

[^1]: Binding objects are implicit in all binding operations, but are created declaratively when using XAML.
