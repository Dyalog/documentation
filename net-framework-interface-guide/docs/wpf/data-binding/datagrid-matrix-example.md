<h1 class="heading"><span class="name">Example 8</span></h1>

This example illustrates data binding using a matrix and is practically identical to Example 7 except that it uses a matrix instead of a vector of namespaces.

Each row in the WPF DataGrid control is represented by an object, and each column as a property of that object. Each row in the DataGrid is bound to an object in the data source, and each column in the data grid is bound to a property of the data object.

![](../../img/data-binding-datagrid1.png)

## The XAML

The XAML shown below,  describes a Window containing a DockPanel, inside which is a DataGrid. The XAML is identical to the XAML in Example 7, except for the window caption.
```xml
 <Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="DataGrid Matrix Example" Height="500"
    SizeToContent="Width"
    Topmost="true">
    <DockPanel>
        <DataGrid Name="DG1" ItemsSource="{Binding}"
                  AutoGenerateColumns="False" >
            <DataGrid.Columns>
                <DataGridTextColumn Header="Wine"
                 Binding="{Binding Name}"/>
                <DataGridTextColumn Header="Price"
                 Binding="{Binding Price, StringFormat=C}" />
            </DataGrid.Columns>
        </DataGrid>
    </DockPanel>
 </Window>

```

The phrase `ItemsSource="{Binding}"` states that the content of the DataGrid is bound to a data source, which in this case will be inherited from the DataContext property of the parent Window.

`Binding="{Binding Name}"` specifies that the contents of the first column are bound to a Path named *Name* in the data source.

Similarly, `Binding="{Binding Price, StringFormat=C}"` specifies that the Path for the second column is *Price* (the phrase `StringFormat=C` merely specifies the default currency format).

## The APL Code

The function `Grid` is shown below.
```apl
     ∇ Grid;⎕USING;MySource;win;info
[1]    ⎕USING←'System'
[2]    ⎕EX'winelist'
[3]    winelist←Wines,[1.5]0.01×10000+?(⍴Wines)⍴10000
[4]    win←LoadXAML XAML
[5]    info←(⍪'Name' 'Price'),⊂Object
[6]    win.DataContext←info(2015⌶)'winelist'
[7]    win.Show
     ∇

```

As in Example 7, the global variable `Wines` contains a vector of character vectors, each of which is the name of a wine.

`Grid[2-4`] creates a  matrix `winelist`, whose first column contains the names of the wines, and whose second column their (randomly generated) prices. As this is a global variable, the variable is expunged before being used in order to remove any previous data binding information that was associated with it.

`Grid[5]`creates the left argument for `(2015⌶)` which defines the names and data types of the properties which the columns of the matrix `winelist` will be exposed as. In this case, the names of the paths are `Name` and `Price`, and their data types are both `System.Object`. So the first column will be exposed as `Name` and the second as `Price`, matching the path names specified in the XAML:
```apl
            <DataGridTextColumn Header="Wine"
            Binding="{Binding Name}"/>
            <DataGridTextColumn Header="Price"
            Binding="{Binding Price, StringFormat=C}" />
```

## Testing the Data Binding
```apl

      )LOAD wpfintro
      )CS DataBinding.DataGridMatrix
      Grid
```

![](../../img/data-binding-datagrid1.png)

Let's round the prices to the nearest $5.
```apl
 winelist[;2]←5×⌊0.5+winelist[;2]÷5
```

![](../../img/data-binding-datagrid2.png)
## Using Code

The same result can be achieved using code instead of XAML as illustrated by the function `GridCodeNoFmt`. The function is so-named because this code is insufficient to display the second column in currency format.
```apl
     ∇ GridCodeNoFmt;⎕USING;MySource;win;info;fmt
[1]    ⎕USING←'System'
[2]    ⎕USING,←,⊂'System.Windows.Controls,WPF/PresentationFramework.dll'
[3]    ⎕USING,←⊂'System.Windows.Controls.Primitives,WPF/PresentationFramework.dll'
[4]    ⎕USING,←⊂'System.Windows,WPF/PresentationFramework.dll'
[5]    ⎕USING,←⊂'System.Windows,WPF/PresentationCore.dll'
[6]
[7]    ⎕EX'winelist'
[8]    winelist←Wines,[1.5]0.01×10000+?(⍴Wines)⍴10000
[9]    win←⎕NEW Window
[10]   win.Title←'DataGrid Matrix (Code)'
[11]   win.grid←⎕NEW DataGrid
[12]   info←(⍪'Name' 'Price'),⊂Object
[13]   win.grid.ItemsSource←info(2015⌶)'winelist'
[14]   win.grid.Height←500
[15]   win.Content←win.grid
[16]   win.SizeToContent←SizeToContent.WidthAndHeight
[17]   win.Show
     ∇

```

This is because by default the DataGrid generates its columns automatically with default formatting.

![](../../img/data-binding-datagrid3.png)

In order to apply special formatting to one or more columns, it is necessary to set the AutoGenerateColumns property to 0, and to generate the columns programmatically as is shown in the second version of the function, `GridCode`.

```apl
     ∇ GridCode;⎕USING;MySource;win;info;fmt
[1]    ⎕USING←'System'
[2]    ⎕USING,←,⊂'System.Windows.Controls,WPF/PresentationFramework.dll'
[3]    ⎕USING,←⊂'System.Windows.Controls.Primitives,WPF/PresentationFramework.dll'
[4]    ⎕USING,←⊂'System.Windows,WPF/PresentationFramework.dll'
[5]    ⎕USING,←⊂'System.Windows,WPF/PresentationCore.dll'
[6]
[7]    ⎕EX'winelist'
[8]    winelist←Wines,[1.5]0.01×10000+?(⍴Wines)⍴10000
[9]    win←⎕NEW Window
[10]   win.Title←'DataGrid Matrix (Code with Formatting)'
[11]   win.grid←⎕NEW DataGrid
[12]   info←(⍪'Name' 'Price'),⊂Object
[13]   win.grid.ItemsSource←info(2015⌶)'winelist'
[14]   win.grid.Height←500
[15]   win.grid.AutoGenerateColumns←0
[16]   win.Content←win.grid
[17]   win.SizeToContent←SizeToContent.WidthAndHeight
[18]   ⍝ Add columns and set format
[19]   win.grid.Columns.Add¨'' 'C'{
[20]       col←⎕NEW DataGridTextColumn
[21]       col.Header←⍵
[22]       col.Binding←⎕NEW Data.Binding(⊂⍵)
[23]       col.Binding.StringFormat←,⍺
[24]       col
[25]   }¨'Name' 'Price'
[26]
[27]   win.Show
     ∇
```

In this version of the function, lines `[19-25]` create the two columns `Name` and `Price`, applying currency format to the `Price` column.

![](../../img/data-binding-datagrid4.png)
