---
search:
  boost: 2
---

<!-- Hidden search keywords -->
<div style="display: none;">
  2015⌶
</div>






<h1 class="heading"><span class="name">Create Data Binding Source</span> <span class="command">R←{X}2015⌶Y</span></h1>



!!! note
    **.NET Framework only**


Creates an object that may be used as a data source for WPF data binding. For more information on the concepts of WPF data binding, see [Microsoft Developer Network's Data Binding Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/data/).

This function connects a *Binding Target* to a *Binding Source*. In WPF a Binding Target is a particular property of a user interface object; for example, the Text property of a TextBox object. A Binding Source is  a *Path* to a value in a data object (which may contain other values). The value of the Binding Source determines the value of the Binding Target. If two-way binding is in place, a change in a user-interface component causes the bound data value to change accordingly. In the example of the TextBox, the value in the Binding Source changes as the user types into the TextBox.



`Y` is a character vector containing one of the following:

- the name of a variable
- the name of a  namespace containing one or more variables
- the name of a variable containing a vector of refs to namespaces, each of which contains one or more variables.


If the name specified by `Y` doesn't exist or represents neither a variable nor a namespace,  the function reports `DOMAIN ERROR`. Currently, no further validation of the structure and contents of `Y` is performed, but nothing other than the examples described herein is supported.


If the optional left argument `X` is given and `Y` is a variable other than a ref, `X` specifies the binding type for that variable. If `Y` specifies one or more namespaces, `X` specifies the names and binding types of each of the variables which are to be bound, contained in the namespaces specified by  `Y`.


The structure of `X` depends upon the structure of `Y` and is discussed later in this topic.


If `X` is omitted, all of the variables specified by `Y` are bound with default binding types.


Here the term *bind variable* refers to any variable specified by `X` and `Y` to be bound, and the term *binding type* means the .NET data type to which the value of the bind variable is converted before it is passed to the .NET interface.


`2015⌶` creates a Binding Source object `R`. This is a .NET object which contains *Path*(s) to one or more bind variables. This object may then be assigned to a property of a WPF object or passed a s as a parameter to a WPF method that requires a Binding Source.

## Bind Variables and Bind Types


A bind variable should be of rank 2 or less. Higher rank arrays are not supported.


If not specified by `X`, the  binding type of a bind variable is derived from its content  at the time `2015⌶` is executed. The binding type is then stored with the variable in the workspace. There is no mechanism to change a variable's binding type without erasing the variable and re-executing `2015⌶`. If you change the type or rank of a bind  variable while it is bound (for example from a variable to a namespace), the behaviour of the system is unpredictable.


The default binding type is derived as follow:


If the bind variable is a simple scalar number the default binding type is System.Object. At the point when the value of the variable is passed to the .NET interface this will be cast to a numeric type such as  System.Int16, System.Int32, System.Int64, or System.Double, depending upon the internal representation of the data. The .NET property to which it is bound will typically only accept a single Type (for example System.Int32), so to avoid unpredictable behaviour,  it is recommended that the left argument `X` be used to specify the binding type for numeric data.


If the bind variable is a character scalar or vector, the default binding type is also System.Object, but at the point  when the value of the variable is passed to the .NET interface it will always be passed as System.String, which is suitable for binding to any property that accepts a System.String, such as the Text property of a TextBox.


If the bind variable is a vector other than a simple character vector, such as a vector of character vectors,  a simple numeric vector, or a vector of .NET objects, the bind type will be a collection. This is suitable for binding to any property that  represents a collection (list) of items, for example the ItemsSource property of a ListBox.


If the bind variable is a matrix, the default binding type is System.Object.


All the examples that follow assume `⎕USING←'System'`.


## Binding Single Variables


In this case, `Y` specifies the name of a variable which is one of the following:

- character vector (or scalar)
- numeric scalar
- scalar .NET object (not currently supported)
- vector of character vectors
- numeric vector
- vector of .NET objects
- matrix



`X` (if specified) defines the binding type for the bind variable named by `Y` and is a single .NET Type.


Note that in the following examples, the reason for expunging the name first is discussed in the section headed Rebinding a Variable.

## Binding a Character Vector


This example illustrates how to bind a variable which contains a character vector.
```apl
      ⎕EX'txtSource'
      txtSource←HELLO WORLD'
      bindsource←2015⌶'txtSource'
```


In this example, the binding type of the variable `txtSource` will be System.String, suitable for binding to any property that accepts a String, such as the Text property of a `TextBox`.

## Binding a Numeric Scalar


This example illustrates how to bind a variable which contains a numeric scalar value.
```apl
      ⎕EX'sizeSource'
      sizeSource←36
      bindSource←Int32(2015⌶)'sizeSource'
```


In this example, the left argument `Int32` specifies that the binding type for the variable sizeSource is to be System.Int32. This means that whenever APL passes the value of `sizeSource` to the control, it will first be cast to an Int32. This makes it suitable, for example, for binding to the FontSize property of a TextBox.



A number of controls have a Value property which must be expressed as a System.Double. The next example shows how to create a Binding Source for such a variable.
```apl
      ⎕EX'valSource'
      valSource←42
      bindSource←Double(2015⌶)'valSource'
```


### Binding a  Scalar .NET Object


This is currently not supported.

## Binding a Vector of Character Vectors


WPF data binding provides the means to bind controls that display lists of items, such as the ListBox, ListView, and TreeView controls, to collections of data. These controls are all based upon the ItemsControl class. To bind an ItemsControl to a collection object, you use its ItemsSource property.


This example illustrates how to bind a variable which contains a vector of character vectors.
```apl
      ⎕EX'itemsSource'
      itemsSource←'beer' 'wine' 'water'
      bindsource←2015⌶'itemsSource'
```


In this example, the binding type of the variable `itemsSource` will be System.Collection, suitable for binding to the ItemSource property of an ItemsControl.

### Binding a Numeric Vector


By default, a numeric vector is bound in the same way as a vector of character vectors, that is, as a System.Collection, suitable for binding to the ItemSource property of an ItemsControl.
```apl
      ⎕EX'yearsSource'
      yearsSource←2000+⍳20
      bindSource←2015⌶'yearsSource'
```



In principle, a numeric vector may alternatively be bound to a WPF property that requires a 1-dimensional numeric array, by specifying the appropriate data type (for example, Int32, Double) for the array as the left argument. For example:
```apl
      ⎕EX'arraySource'
      arraySource←42 24
      bindSource←Int32 (2015⌶)'arraySource'
```



### Binding a Vector of .NET Objects


A vector of .NET objects is bound in the same way as a vector of character vectors, that is, as a System.Collection, suitable for binding to the ItemSource property of an ItemsControl.
```apl
      ↑Easter
2015 4 12
2016 5  1
2017 4 16
2018 4  8
2019 4 28
2020 4 19
2021 5  2
2022 4 24
2023 4 16
2024 5  5
      dt←{⎕NEW DateTime ⍵}¨Easter
      bindSource←2015⌶'dt'

```



Note that, as a specific optimisation for binding DateTime data, it is not necessary to create `DateTime` objects in the workspace. Instead, the data may be represented by 7-element integer vectors (`⎕TS` format) or character strings that can be parsed by the DateTime.Parse(String) method.  However, in both cases it is necessary to explicitly specify the binding type to force the data to be converted to `DateTime`, as illustrated by the following examples:
```apl
      TSEaster←7↑¨Easter
      bindSource←DateTime (2015⌶) 'TSEaster'

```
```apl
      CharEaster←'2015/4/12' '2016/5/1' '2017/4/16'
      bindSource←DateTime (2015⌶) 'CharEaster'

```

#### Binding a Matrix


If the bind variable is a matrix, it is bound in a similar way to a vector of namespaces and is discussed below.

### Rebinding a Variable


As mentioned earlier, when a variable is bound its binding type is stored with it in the workspace. If you subsequently attempt to rebind the variable there is no mechanism in place to alter the binding type. If the current binding type (whether specified by the left argument `X`, or by being the default) differs from the saved one, the function will generate a `DOMAIN ERROR`.
```apl
      num←42
      bs←2015⌶'num'

      bs←'Int32'(2015⌶)'num'
DOMAIN ERROR: You cannot redefine the binding types
      bs←'Int32'(2015⌶)'num'
     ∧

```


In this example, perhaps the programmer realised after binding `num` (with a default binding type of System.Object) that the binding type should really be System.Int32, and simply was trying to correct the error. To avoid this problem, it is recommended that you expunge the name before using it.
```apl
      ⎕EX 'num'
      num←42
      bs←2015⌶'num'⍝ (default) binding type System.Object
      
      ⎕EX 'num'
      num←42
      bs←Int32(2015⌶)'num'
```

#### Binding A Namespace


In this case, `Y` specifies the name of a namespace that contains one or more variables. By default, each variable is bound using its default binding type as described above. Objects other than variables are ignored.


If it is required to specify the binding type of any of the variables, or if certain variables are to be excluded, the left argument is a 2-column matrix. The first column contains the names of the variables to be bound, and the second column their binding types.

<h4 class="example">Example</h4>


The following code snippet binds a namespace containing two variables named `txtSource` and `sizeSource`. In this case, the name of each variable may be specified as the Path for a WPF property that requires a String or an Int32. For example, if bindSource were assigned to the DataContext property of a TextBox, its Text property could be bound to `txtSource` and its FontSize property to `sizeSource`.
```apl
      src←⎕NS''
      src.txtSource←'Hello World'
      src.sizeSource←36
      options←2 2⍴'txtSource'String'sizeSource'Int32
      bindSource←options(2015⌶)'src'
```

#### Binding a Vector of Namespaces


In this case, `Y` specifies the name of a variable that contains a vector of refs to namespaces. In this case, the result `R` is of type Dyalog.Data.DataBoundCollectionHandler which is suitable for binding to a WPF property that requires  an IEnumerable implementation, such as the  ItemsSource property of the DataGrid.


Each namespace in `Y` represents one of a collection of  instances of an object, which exports a particular set of properties for binding purposes. For example, `Y` could specify a wine database where each namespace represents a different wine, and each namespace contains the same set of variables that contain the name, price (and so forth) of each wine.

<h4 class="example">Example</h4>
```apl
 winelist←⎕NS¨(⍴Wines)⍴⊂''
 winelist.Name←Wines
 winelist.Price←0.01×10000+?(⍴Wines)⍴10000
 
 bindSource←2015⌶'winelist'
```

#### Binding a Matrix


Binding a matrix is like binding a vector of namespaces. Each row of `Y` represents one of a collection of  instances of an object, which exports a particular set of properties for binding purposes. Each column of  `Y` represents one of these properties.


Every row in the datasource will be of the same type (which might not be the case with an array of namespaces), and so the collection is a collection of specific things. The *specific thing* is a .NET type that is created dynamically and has a unique name.


Unlike variables in namespaces, the columns of an APL matrix do not have names which can be exported as properties, so this information must be provided in the left argument to `(2015⌶)` which also specifies their data types. If the left argument is omitted, the default names are `Column1`, `Column2`, ... and so forth and the default data type is `System.Object`.


So if the right argument  of `(2015⌶)``Y` is the name of a matrix, the left argument `X` is a matrix with as many rows as there are columns in `Y`. `X[;1]` contains the names by which each of the columns of `Y` will be exported as a property, and `X[;2]` their data types.


Values in the matrix may be scalar numbers, character scalars or vectors, or nested vectors, but each column in the matrix must be uniform.


The result `R` is a specific type that is created dynamically and assigned a unique name of the form Dyalog.Data.DyalogCollectionNotifyHandler`1[Dyalog.Data.DataBoundRow_nnnnnnnn]. This is suitable for binding to a WPF property that requires  an IEnumerable implementation, such as the  ItemsSource property of the DataGrid.


<h4 class="example">Example</h4>


`mat` is a matrix of numbers and is bound with default property/column names `Column1`, `Column2`, ... `Column10` and the default data type of `System.Object`.

```apl
      mat←?20 10⍴100
      bindSource←2015⌶'mat'


```

<h4 class="example">Example</h4>



`winelist` is a matrix whose first column contains a list of wines, and whose second column their prices. The left argument is a matrix. Its first column specifies the property names by which the columns will be exported (`'Name'` and `'Price'`) and its second column, their data types (`System.Object`)
```apl
 winelist←Wines,[1.5]0.01×10000+?(⍴Wines)⍴10000
 info←(⍪'Name' 'Price'),⊂Object

 bindSource←info(2015⌶)'winelist'
 
```



<h4 class="example">Example</h4>


`emp` is a 3-column matrix which contains names,  numbers and  addresses. Each address is made up of two character vectors containing street and town
```apl
      emp
┌───────────────────┬──────────────────┬────────────────────┐
│John Smith         │Mary White        │T.W. Penk           │
├───────────────────┼──────────────────┼────────────────────┤
│1                  │2                 │3                   │
├───────────────────┼──────────────────┼────────────────────┤
│┌─────────┬───────┐│┌──────────┬─────┐│┌──────────┬───────┐│
││2 East Rd│Headley│││42 High St│Alton│││23 West St│Farnham││
│└─────────┴───────┘│└──────────┴─────┘│└──────────┴───────┘│
└───────────────────┴──────────────────┴────────────────────┘
      schema
┌───────┬────────────────────────┐
│Name   │(System.Object)         │
├───────┼────────────────────────┤
│Number │(System.Object)         │
├───────┼────────────────────────┤
│Address│┌──────┬───────────────┐│
│       ││Street│(System.Object)││
│       │├──────┼───────────────┤│
│       ││Town  │(System.Object)││
│       │└──────┴───────────────┘│
└───────┴────────────────────────┘

      bindSource←schema(2015⌶)'emp'
```


#### Notification Events


The object `R` generates notification events when the value(s) of the Binding Source are updated as the contents of the Binding Target are changed by the user. These events are generated after the data has changed and there is no mechanism to prevent the change from occurring.


There are two types of event; ElementChanged and CellsChanged. The CellsChanged event applies only to a data bound matrix; the ElementChanged event applies to all other types of binding.


The event message  supplied as the right argument to your callback function, is a 2-element vector as follows :


|-----|---------|---|
|`[1]`|Object   |ref|
|`[2]`|EventArgs|ref|


EventArgs is an instance of the internal class `Dyalog.Data.ElementChangedEventArgs` or `Dyalog.Data.CellsChangedEventArgs` whose fields are described below:



`Dyalog.Data.ElementChangedEventArgs` fields


|---|---|
|`Indices`|An indication of which member has changed. Typically this will either be `¯1` to indicate that the indices are unavailable or a scalar value indicating (origin 0), which element of an array has been modified or added.|
|`Name`|The name of the variable that has been modified. This is especially useful when the datasource corresponds to a namespace.|
|`Path`|A path used to locate the variable that has been modified. This is especially useful when the datasource corresponds to a deeply nested namespace, where the value changed is an element of an array inside a namespace which is itself an element of an array within the datasource.|




`Dyalog.Data.CellsChangedEventArgs` fields


|------------|-----------------------------------------------------------------------------------------------------------------------|
|`Path`      |Identifies the cell or row that was changed. See below.                                                                |
|`SourceName`|The name of the matrix that was specified as the right argument to `2015⌶` .                                           |
|`Reason`    |A character vector that describes what in the matrix has changed is `'RowDeleted'` , `'CellChanged'` or `'RowInserted'`|
|`Value`     |The new value in the cell or `⎕NULL`                                                                                   |



If Reason is `'CellChanged'`, Path is the row and column number (in origin 0) of the cell that was changed and Value is its new value.


If Reason is `'RowDeleted'` or `'RowInserted'`, Path is the number of the row that has been added or removed (in origin 0) and Value is `⎕NULL`.
