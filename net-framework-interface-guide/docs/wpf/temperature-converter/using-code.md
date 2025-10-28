<h1 class="heading"><span class="name">Using Code</span></h1>

The functions for this example are provided in the workspace `WPFIntro.dws` in the namespace `WPF.UsingCode`. To run the example:
```apl
      )LOAD wpfintro
      WPF.UsingCode.TempConverter
```

The following function `TempConverter` performs *exactly* the same task of defining and manipulating the user-interface for the Temperature Converter example using XAML which was discussed previously.

The callback functions it uses are identical.
```apl
     ∇ TempConverter;⎕USING;win;dp;mnu;mnuFahrenheit;mnuCentigrade;gr;tn;rd1;rd2;rd3;rc1;rc2;rc3;l1;l2;txtFahrenheit;txtCentigrade;btnF2C;btnC2F;btnQuit;sink;mnuScale;scrTemp
[1]
[2]    ⎕USING←,⊂'System.Windows.Controls,WPF/PresentationFramework.dll'
[3]    ⎕USING,←⊂'System.Windows.Controls.Primitives,WPF/PresentationFramework.dll'
[4]    ⎕USING,←⊂'System.Windows,WPF/PresentationFramework.dll'
[5]    ⎕USING,←⊂'System.Windows,WPF/PresentationCore.dll'
[6]
[7]    win←⎕NEW Window
[8]    win.SizeToContent←SizeToContent.WidthAndHeight
[9]    win.Title←'WPF Temperature Converter'
[10]
[11]   dp←⎕NEW DockPanel
[12]   dp.LastChildFill←0
[13]
[14]   mnu←⎕NEW Menu
[15]
[16]   mnuScale←⎕NEW MenuItem
[17]   mnuScale.Header←'_Scale'
[18]   sink←mnu.Items.Add mnuScale
[19]
[20]   mnuFahrenheit←⎕NEW MenuItem
[21]   mnuFahrenheit.Header←'Fahrenheit'
[22]   mnuFahrenheit.IsCheckable←1
[23]   mnuFahrenheit.IsChecked←1
[24]   mnuFahrenheit.onClick←'SET_F'
[25]   sink←mnuScale.Items.Add mnuFahrenheit
[26]
[27]   mnuCentigrade←⎕NEW MenuItem
[28]   mnuCentigrade.Header←'_Centigrade'
[29]   mnuCentigrade.IsCheckable←1
[30]   mnuCentigrade.IsChecked←0
[31]   mnuCentigrade.onClick←'SET_C'
[32]   sink←mnuScale.Items.Add mnuCentigrade
[33]
[34]   sink←dp.Children.Add mnu
[35]   dp.SetDock mnu Dock.Top
[36]
[37]   gr←⎕NEW Grid
[38]   gr.Width←230
[39]   gr.Margin←⎕NEW Thickness(40 10 10 10)
[40]
[41]   rd1←⎕NEW RowDefinition
[42]   rd1.Height←GridLength.Auto
[43]   rd2←⎕NEW RowDefinition
[44]   rd2.Height←GridLength.Auto
[45]   rd3←⎕NEW RowDefinition
[46]   rd3.Height←GridLength.Auto
[47]   gr.RowDefinitions.Add¨rd1 rd2 rd3
[48]
[49]   rc1←⎕NEW ColumnDefinition
[50]   rc1.Width←GridLength.Auto
[51]   rc2←⎕NEW ColumnDefinition
[52]   rc2.Width←⎕NEW GridLength 80
[53]   rc3←⎕NEW ColumnDefinition
[54]   rc3.Width←⎕NEW GridLength 60
[55]   gr.ColumnDefinitions.Add¨rc1 rc2 rc3
[56]
[57]   l1←⎕NEW Label
[58]   l1.Content←'Fahrenheit'
[59]   sink←gr.Children.Add l1
[60]   gr.SetRow l1 0
[61]   gr.SetColumn l1 0
[62]
[63]   l2←⎕NEW Label
[64]   l2.Content←'Centigrade'
[65]   sink←gr.Children.Add l2
[66]   gr.SetRow l2 1
[67]   gr.SetColumn l2 0
[68]
[69]   txtFahrenheit←⎕NEW TextBox
[70]   txtFahrenheit.Margin←⎕NEW Thickness 5
[71]   sink←gr.Children.Add txtFahrenheit
[72]   gr.SetRow txtFahrenheit 0
[73]   gr.SetColumn txtFahrenheit 1
[74]
[75]   txtCentigrade←⎕NEW TextBox
[76]   txtCentigrade.Margin←⎕NEW Thickness 5
[77]   sink←gr.Children.Add txtCentigrade
[78]   gr.SetRow txtCentigrade 1
[79]   gr.SetColumn txtCentigrade 1
[80]
[81]   btnF2C←⎕NEW Button
[82]   btnF2C.Content←'F>C'
[83]   btnF2C.Margin←⎕NEW Thickness 5
[84]   btnF2C.onClick←'f2c'
[85]   sink←gr.Children.Add btnF2C
[86]   gr.SetRow btnF2C 0
[87]   gr.SetColumn btnF2C 2
[88]
[89]   btnC2F←⎕NEW Button
[90]   btnC2F.Content←'C>F'
[91]   btnC2F.Margin←⎕NEW Thickness 5
[92]   btnC2F.onClick←'c2f'
[93]   sink←gr.Children.Add btnC2F
[94]   gr.SetRow btnC2F 1
[95]   gr.SetColumn btnC2F 2
[96]
[97]   btnQuit←⎕NEW Button
[98]   btnQuit.Content←'Quit'
[99]   btnQuit.Margin←⎕NEW Thickness 5
[100]  btnQuit.onClick←'Quit'
[101]  sink←gr.Children.Add btnQuit
[102]  gr.SetRow btnQuit 2
[103]  gr.SetColumn btnQuit 1
[104]
[105]  sink←dp.Children.Add gr
[106]
[107]  scrTemp←⎕NEW ScrollBar
[108]  scrTemp.Width←20
[109]  scrTemp.Orientation←Orientation.Vertical
[110]  scrTemp.Minimum←1
[111]  scrTemp.Maximum←213
[112]  scrTemp.onScroll←'F2C'
[113]
[114]  sink←dp.Children.Add scrTemp
[115]  dp.SetDock scrTemp Dock.Right
[116]
[117]  win.Content←dp
[118]
[119]  sink←win.ShowDialog
     ∇

```

Although this approach appears at first sight to be considerably more verbose than  using XAML (a 120-line function compared with a 21-line function and a 44-line block of XAML) each line of code performs only one very simple task, and no attempt has been made to write utility functions to perform the same task for similar controls, as might be done in a real application.

As before, let us examine the code line-by-line.

`TempConverter[2-5]` define `⎕USING` so that the appropriate .NET assemblies are on the search-path. Note that the ScrollBar control is in `System.Windows.Controls.Primitives` and not `System.Windows.Controls` like the others.
```apl

[2]    ⎕USING←,⊂'System.Windows.Controls,WPF/PresentationFramework.dll'
[3]    ⎕USING,←⊂'System.Windows.Controls.Primitives,WPF/PresentationFramework.dll'
[4]    ⎕USING,←⊂'System.Windows,WPF/PresentationFramework.dll'
[5]    ⎕USING,←⊂'System.Windows,WPF/PresentationCore.dll'
```

`TempConverter[8-9]` creates a Window and sets its SizeToContent and Title properties as in the XAML example. Notice however that whereas using XAML the string  `SizeToContent="WidthandHeight"` is sufficient, when using code it is necessary to get the *Type* right. In this case, the SizeToContent property must be set to a specific member (in this case WidthAndHeight) of the System.Windows.SizeToContent enumeration. Other members of this Type are Width, Height and Manual (the default).
```apl
[7]    win←⎕NEW Window
[8]    win.SizeToContent←SizeToContent.WidthAndHeight
[9]    win.Title←'WPF Temperature Converter'
```

`TempConverter[11-12]` create a DockPanel control and set its LastChildFill property to 0. In this case the APL value 0 is used instead of the string "False" in XAML.
```apl

[11]   dp←⎕NEW DockPanel
[12]   dp.LastChildFill←0
```

`TempConverter[14]` creates a Menu control.
```apl

[14]   mnu←⎕NEW Menu
```

`TempConverter[16-18]` create a MenuItem control with the caption *Scale*, and then add the control to the Items collection of the main Menu using its Add method. This illustrates one significant difference between using XAML and code. In XAML, the parent/child relationships between controls are defined by the structure and order of the XML. Using code, child controls must be explicitly added to the appropriate list of child controls managed by the parent.
```apl
[16]   mnuScale←⎕NEW MenuItem
[17]   mnuScale.Header←'_Scale'
[18]   sink←mnu.Items.Add mnuScale
```

`TempConverter[20-25]` create a MenuItem control labelled *Fahrenheit*. The IsCheckable and IsChecked properties are set to 1, which is equivalent to "True" in XAML. The callback function `SET_F` is assigned to the Click event exactly as in the XAML version of this example. The last line in this section makes the *Fahrenheit* MenuItem a child of the *Scale* MenuItem.
```apl

[20]   mnuFahrenheit←⎕NEW MenuItem
[21]   mnuFahrenheit.Header←'Fahrenheit'
[22]   mnuFahrenheit.IsCheckable←1
[23]   mnuFahrenheit.IsChecked←1
[24]   mnuFahrenheit.onClick←'SET_F'
[25]   sink←mnuScale.Items.Add mnuFahrenheit
```

The code used to create the *Centigrade* MenuItem is more or less the same.

`TempConverter[34-35]` adds the top-level Menu  to the DockPanel. Note that in the case of a DockPanel, the list of its child controls is represented by its Children property. Furthermore, to define how it is docked this is done,  using code, by the SetDock method of the DockPanel. This contrasts with the way this is achieved using XAML (`DockPanel.Dock="Top"`). Note too that the argument to SetDock is not just a simple string as in XAML, but a member of the System.Windows.Controls.Dock enumeration.
```apl

[34]   sink←dp.Children.Add mnu
[35]   dp.SetDock mnu Dock.Top
```

`TempConverter[37-39]` create the Grid control. Its Width property will accept a simple numeric value, but its Margin property must be given an instance of a System.Windows.Thickness structure. In this case, the ThickNess constructor is given a 4-element numeric vector that specifies its Left, Top, Right and Bottom members respectively.
```apl

[37]   gr←⎕NEW Grid
[38]   gr.Width←230
[39]   gr.Margin←⎕NEW Thickness(40 10 10 10)
```

`TempConverter[41-47]` create instances of 3 RowDefinition classes and add them to the RowDefinitions collection of the Grid. Note that whereas in XAML the Height can be specified as a string, using code it is necessary once again to use the correct Type. In this case, Height must be specified by a member of the System.Windows.GridLength structure.
```apl
[41]   rd1←⎕NEW RowDefinition
[42]   rd1.Height←GridLength.Auto
[43]   rd2←⎕NEW RowDefinition
[44]   rd2.Height←GridLength.Auto
[45]   rd3←⎕NEW RowDefinition
[46]   rd3.Height←GridLength.Auto
[47]   gr.RowDefinitions.Add¨rd1 rd2 rd3
```

Similarly, `TempConverter[49-55]` create instances of 3 ColumnDefinition classes and add them to the ColumnDefinitions collection of the Grid. Note that The Width property will not accept a simple numeric value, it must be a member of the GridLength structure. To set the Width to 80, it is  necessary first to create an instance of a GridLength structure giving this value as the argument to its constructor.
```apl
[49]   rc1←⎕NEW ColumnDefinition
[50]   rc1.Width←GridLength.Auto
[51]   rc2←⎕NEW ColumnDefinition
[52]   rc2.Width←⎕NEW GridLength 80
[53]   rc3←⎕NEW ColumnDefinition
[54]   rc3.Width←⎕NEW GridLength 60
[55]   gr.ColumnDefinitions.Add¨rc1 rc2 rc3
```

`TempConverter[57-61]` create a Label control with the caption *Fahrenheit*. To display the Label in a Grid it is necessary to first add it to the Children collection of the Grid, and then set its position in the Grid using its SetRow and SetColumn methods. Similar code is used to create and position the second Label.
```apl
[57]   l1←⎕NEW Label
[58]   l1.Content←'Fahrenheit'
[59]   sink←gr.Children.Add l1
[60]   gr.SetRow l1 0
[61]   gr.SetColumn l1 0
```

`TempConverter[69-73]` create and position a TextBox control, in the same way as the Label controls. Notice that in this case, the constructor for the Thickness structure is given a single value that specifies all four of its Left, Top, Right and Bottom members.
```apl

[69]   txtFahrenheit←⎕NEW TextBox
[70]   txtFahrenheit.Margin←⎕NEW Thickness 5
[71]   sink←gr.Children.Add txtFahrenheit
[72]   gr.SetRow txtFahrenheit 0
[73]   gr.SetColumn txtFahrenheit 1
```

`TempConverter[81-87]` create and position a Button control. The callback function `f2c` is attached to the Click event in the same way as in the XAML version of this example.
```apl

[81]   btnF2C←⎕NEW Button
[82]   btnF2C.Content←'F>C'
[83]   btnF2C.Margin←⎕NEW Thickness 5
[84]   btnF2C.onClick←'f2c'
[85]   sink←gr.Children.Add btnF2C
[86]   gr.SetRow btnF2C 0
[87]   gr.SetColumn btnF2C 2
```

`TempConverter[105]` adds the Grid to the list of Children to be managed by the DockControl.
```apl
[105]  sink←dp.Children.Add gr
```

`TempConverter[107-112]` create a ScrollBar control. Its Width, Minimum and Maximum properties all accept simple numeric values. However, its Orientation property must be set to a member of the System.Windows.Controls.Orientation enumeration.
```apl

[107]  scrTemp←⎕NEW ScrollBar
[108]  scrTemp.Width←20
[109]  scrTemp.Orientation←Orientation.Vertical
[110]  scrTemp.Minimum←1
[111]  scrTemp.Maximum←213
[112]  scrTemp.onScroll←'F2C'
```

`TempConverter[114-115]` add the ScrollBar to the list of Children managed by the DockPanel, and use its SetDock method to cause it to be right-aligned.
```apl
[114]  sink←dp.Children.Add scrTemp
[115]  dp.SetDock scrTemp Dock.Right
```

Finally, the DockPanel is assigned to the Content property of the Window, and the Window displayed as in the XAML version of this example. Note that a Window may contain just one control.
```apl

[117]  win.Content←dp
[118]
[119]  sink←win.ShowDialog
```
