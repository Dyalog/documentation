<h1 class="heading"><span class="name">Using Windows Forms</span></h1>

<code class="language-nonAPL">System.Windows.Forms</code> is a .NET namespace that provides a set of classes for creating the GUI for Microsoft Windows applications.

As an alternative to the built-in Dyalog GUI, Windows Forms has been superseded by [Windows Presentation Foundation](windows-presentation-foundation/index.md). This page is included to support existing Dyalog applications that make use of Windows Forms.

## Creating GUI Objects

GUI objects are represented by .NET classes in the <code class="language-nonAPL">System.Windows.Forms</code> .NET namespace. In general, these classes correspond closely to the GUI objects provided by Dyalog, which are themselves based on the Windows API.

For example, to create a form containing a button and an edit field, you would create instances of the <code class="language-nonAPL">Form</code>, <code class="language-nonAPL">Button</code>, and <code class="language-nonAPL">TextBox</code> classes.

## Object Hierarchy

The most striking difference between the <code class="language-nonAPL">Windows.Forms</code> GUI and the Dyalog GUI is that in <code class="language-nonAPL">Windows.Forms</code> the container hierarchy represented by forms, group boxes, and controls is not represented by an object hierarchy. Instead, objects that represent GUI controls are created stand-alone (that is, without a parent) and then associated with a container, such as a <code class="language-nonAPL">Form</code>, by calling the Add method of the parent’s Controls collection.

<code class="language-nonAPL">Windows.Forms</code> objects are associated with APL symbols that are namespace references, but <code class="language-nonAPL">Windows.Forms</code> objects do not have implicit names.

# Positioning and Sizing Forms and Controls

The position of a form or a control is specified by its <code class="language-nonAPL">Location</code> property, which is measured relative to the top left corner of the client area of its container.

<code class="language-nonAPL">Location</code> has a data type of <code class="language-nonAPL">System.Drawing.Point</code>. To set <code class="language-nonAPL">Location</code>, you must first create an object of type <code class="language-nonAPL">System.Drawing.Point</code> and then assign that object to Location.

Similarly, the size of an object is determined by its <code class="language-nonAPL">Size</code> property, which has a data type of <code class="language-nonAPL">System.Drawing.Size</code>. For this, you must create a <code class="language-nonAPL">System.Drawing.Size</code> object before assigning it to the <code class="language-nonAPL">Size</code> property of the control or form.

Objects also have <code class="language-nonAPL">Top</code>(Y) and <code class="language-nonAPL">Left</code>(X) properties that can be specified or referenced  independently. These accept simple numeric values.

The position of a <code class="language-nonAPL">Form</code> can instead be determined by its <code class="language-nonAPL">DesktopLocation</code> property, which is specified relative to the taskbar. Another alternative is to set the <code class="language-nonAPL">StartPosition</code> property whose default setting is <code class="language-nonAPL">WindowsDefaultLocation</code>, which represents a computed best location.

# Modal Dialog Boxes

Dialog Boxes are displayed modally to prevent the user from performing tasks outside of the dialog box.

To create a modal dialog box, you create a <code class="language-nonAPL">Form</code>, set its <code class="language-nonAPL">BorderStyle</code> property to <code class="language-nonAPL">FixedDialog</code>, set its <code class="language-nonAPL">ControlBox</code>, <code class="language-nonAPL">MinimizeBox</code>, and <code class="language-nonAPL">MaximizeBox</code> properties to false, and display it using <code class="language-nonAPL">ShowDialog</code>.

A modal dialog box has a <code class="language-nonAPL">DialogResult</code> property that is set when the <code class="language-nonAPL">Form</code> is closed or when the user presses **OK** or **Cancel**. The value of this property is returned by the <code class="language-nonAPL">ShowDialog</code> method, so the simplest way to handle user actions is to check the result of <code class="language-nonAPL">ShowDialog</code> and proceed accordingly.

The examples in this section can be found in the **[DYALOG]\Samples\winforms\WINFORMS.dws** workspace.

<h4 class="example">Example 1</h4>

This example illustrates a simple modal dialog box.

Function `EG1` illustrates how to create and use a simple modal dialog box. Much of the function is self-explanatory, but some points are noteworthy:

- Lines `[1-2]` set `⎕USING` to include the .NET namespaces <code class="language-nonAPL">System.Windows.Forms</code> and <code class="language-nonAPL">System.Drawing</code>.

- Lines `[6,8,9]` create a `Form` and two `Button` objects. As yet, they are unconnected. The constructor for both classes is defined to take no arguments, so the `⎕NEW` system function is only called with a class argument.

- Lines `[14]` shows how the `Location` property is set by first creating a new `Point` object with a specific pair of (`x` and `y`) values.

- Lines `[18]` computes the values for the `Point` object for `button2.Location`, from the values of the `Left`, `Height`, and `Top<` properties of `button1`; thus positioning `button2` relative to `button1`.

```apl
     ∇ EG1;form1;button1;button2;true;false;⎕USING;Z
[1]    ⎕USING←,⊂'System.Windows.Forms, System.Windows.Forms.dll'
[2]    ⎕USING,←⊂'System.Drawing,System.Drawing.dll'
[3]    true false←1 0
[4]
[5]    ⍝ Create a new instance of the form.
[6]    form1←⎕NEW Form
[7]    ⍝ Create two buttons to use as the accept and cancel btns
[8]    button1←⎕NEW Button
[9]    button2←⎕NEW Button
[10]
[11]   ⍝ Set the text of button1 to "OK".
[12]   button1.Text←'OK'
[13]   ⍝ Set the position of the button on the form.
[14]   button1.Location←⎕NEW Point,⊂10 10
[15]   ⍝ Set the text of button2 to "Cancel".
[16]   button2.Text←'Cancel'
[17]   ⍝ Set the position of the button relative to button1.
[18]   button2.Location←⎕NEW Point, ⊂button1.Left button1. (Height+Top+10)
[19]
```

- Lines `[21,23]` sets the `DialogResult` property of `button1` and `button2` to `DialogResult.OK` and `DialogResult.Cancel` respectively. `DialogResult` is an enumeration with a predefined set of member values.

- Similarly, lines `[32]` defines the `BorderStyle` property of the form using the <code class="language-nonAPL">FormBorderStyle</code> enumeration.

- Lines `[38 40]` defines the `AcceptButton` and `CancelButton` properties of the `Form` to `button1` and `button2` respectively. These have the same effect as the Dyalog GUI _Default_ and _Cancel_ properties.

- Lines `[42]` sets the `StartPosition` of the Form to be centre screen. This is specified using an enumeration; <code class="language-nonAPL">FormStartPosition</code>.

```apl
[20]   ⍝ Make button1's dialog result OK.
[21]   button1.DialogResult←DialogResult.OK
[22]   ⍝ Make button2's dialog result Cancel.
[23]   button2.DialogResult←DialogResult.Cancel
[24]
[25]
[26]   ⍝ Set the title bar text of the form.
[27]   form1.Text←'My Dialog Box'
[28]   ⍝ Display a help button on the form.
[29]   form1.HelpButton←true
[30]
[31]   ⍝ Define border style of form to that of a dialog box.
[32]   form1.BorderStyle←FormBorderStyle.FixedDialog
[33]   ⍝ Set MaximizeBox to false to remove the maximize box.
[34]   form1.MaximizeBox←false
[35]   ⍝ Set MinimizeBox to false to remove the minimize box.
[36]   form1.MinimizeBox←false
[37]   ⍝ Set the accept button of the form to button1.
[38]   form1.AcceptButton←button1
[39]   ⍝ Set the cancel button of the form to button2.
[40]   form1.CancelButton←button2
[41]   ⍝ Set start position of the form to centre of the screen.
[42]   form1.StartPosition←FormStartPosition.CenterScreen
[43]

```

- Lines `[45 46]` associate the buttons with the `Form`. The `Controls` property of the `Form` returns an object of type `Form.ControlCollection`. This class has an `Add` method that is used to add a control to the collection of controls that are owned by the `Form`.

- Lines `[50]` calls the `ShowDialog` method (with no argument, hence the `⍬`). The result is an object of type <code class="language-nonAPL">Form.DialogResult</code>, which is an enumeration.

- Lines `[52]` compares the result returned by `ShowDialog` with the enumeration member `DialogResult.OK` (the primitive function `=` has been extended to compare objects).

```apl
[44]   ⍝ Add button1 to the form.
[45]   form1.Controls.Add button1
[46]   ⍝ Add button2 to the form.
[47]   form1.Controls.Add button2
[48]
[49]   ⍝ Display the form as a modal dialog box.
[50]   Z←form1.ShowDialog ⍬
[51]   ⍝ Determine if the OK button was clicked on the dialog box.
[52]   :If Z=DialogResult.OK
[53]      ⍝ Display a message box saying that the OK button was clicked.
[54]       Z←MessageBox.Show⊂'The OK button on the form was clicked.'
[55]   :Else
[56]      ⍝ Display a message box saying that the Cancel button was clicked.
[57]       Z←MessageBox.Show⊂'The Cancel button on the form was clicked.'
[58]   :EndIf
     ∇
```

!!! Warning "Warning"
    The use of modal forms in .NET can lead to problematic situations while debugging. As the control is passed to .NET the APL interpreter cannot regain control in the event of an unforeseen error. Dyalog Ltd recommends changing the code to something like the following until the code is fully tested:	
	```apl
    [52]   form1.Visible←1
    [53]   :While form1.Visible ⋄ :endwhile
    ```

<h4 class="example">Example 2</h4>

Functions `EG2` and `EG2A` illustrate how the _each_ operator (`¨`) and the extended namespace reference syntax in Dyalog can be used to produce more succinct, and no less readable, code:
```apl
     ∇ EG2;form1;label1;textBox1;true;false;⎕USING;Z
[1]    ⎕USING←,⊂'System.Windows.Forms, System.Windows.Forms.dll'
[2]    ⎕USING,←⊂'System.Drawing,System.Drawing.dll'
[3]    true false←1 0
[4]
[5]    ⍝ Create a new instance of the form.
[6]    form1←⎕NEW Form
[7]
[8]    textBox1←⎕NEW TextBox
[9]    label1←⎕NEW Label
[10]
[11]   ⍝ Initialize the controls and their bounds.
[12]   label1.Text←'First Name'
[13]   label1.Location←⎕NEW Point (48 48)
[14]   label1.Size←⎕NEW Size (104 16)
[15]   textBox1.Text←''
[16]   textBox1.Location←⎕NEW Point (48 64)
[17]   textBox1.Size←⎕NEW Size (104 16)
[18]
[19]   ⍝ Add TextBox control to the form's control collection.
[20]   form1.Controls.Add textBox1
[21]   ⍝ Add Label control to the form's control collection.
[22]   form1.Controls.Add label1
[23]
[24]   ⍝ Display the form as a modal dialog box.
[25]   Z←form1.ShowDialog ⍬
     ∇
```

In `EG2A` (an "improved" version of `EG2`), line `[7]` takes advantage of the fact that .NET classes are namespaces, so the expression `Form TextBox Label`  is a vector of namespace references, and the expression `⎕NEW¨Form TextBox Label` runs the `⎕NEW` system function on each of them. Similarly, lines `[10 11 12]` combine the use of extended namespace reference and the _each_ operator to set the `Text`, `Location`, and `Size` properties in several objects together:
```apl
     ∇ EG2A;form1;label1;textBox1;true;false;⎕USING;Z
[1]    ⍝ Compact version of EG2 taking advantage of ref syntax and ¨
[2]    ⎕USING←'System.Windows.Forms,System.Windows.Forms.dll'
[3]    ⎕USING,←⊂'System.Drawing,System.Drawing.dll'
[4]    true false←1 0
[5]
[6]    ⍝ Create a new instance of the form, TextBox and Label.
[7]    (form1 textBox1 label1)←⎕NEW¨Form TextBox Label
[8]
[9]    ⍝ Initialize the controls and their bounds.
[10]   (label1 textBox1).Text←'First Name' ''
[11]   (label1 textBox1).Location←⎕NEW¨Point,¨⊂¨(48 48)(48 64)
[12]   (label1 textBox1).Size←⎕NEW¨Size,¨⊂¨(104 16)(104 16)
[13]
[14]   ⍝ Add Label and TextBox controls to the form's control collection.
[15]   form1.Controls.AddRange⊂label1 textBox1
[16]
[17]   ⍝ Display the form as a modal dialog box.
[18]   Z←form1.ShowDialog ⍬
     ∇
```

## Non-Modal Forms

Non-modal forms are displayed using the <code class="language-nonAPL">Run</code> method of the <code class="language-nonAPL">System.Windows.Forms.Application</code> object. This method is designed to be called once, and only once, during the life of an application, which seems problematic for during APL development. Fortunately, in practice the restriction is that <code class="language-nonAPL">Application.Run</code> can only be run once on a single system thread but it can be run successively on different system threads. During development, you can, therefore, test a function that calls <code class="language-nonAPL">Application.Run</code> by running it on a new APL thread using _spawn_ ([`&`](../language-reference-guide/primitive-operators/spawn/)) see [Threading](implementation-details/threading.md) for further details.

There are several examples of non-modal forms in **[DYALOG]\Samples**:

- DataGrid Examples<br />Three functions in the **[DYALOG]\Samples\winforms\WINFORMS.dws** workspace provide examples of non-modal forms. These examples also illustrate the use of the <code class="language-nonAPL">WinForms.DataGrid</code> class.

    - Function `Grid1` is an APL translation of the example given in the help file for the <code class="language-nonAPL">DataGrid</code> class in the .NET SDK Beta1. The original code has been slightly modified to work with the current version of the SDK.

    - Function `Grid2` is an APL translation of the example given in the help file for the <code class="language-nonAPL">DataGrid</code> class in the .NET SDK Beta2.

    - Function `Grid` is an APL translation of the example given in the file:<br />```nonAPL
C:\Program Files\Microsoft.NET\SDK\v1.1\...
QuickStart\winforms\samples\Data\Grid\vb\Grid.vb
```
      This example uses Microsoft SQL Server 2000 to extract sample data from the sample NorthWind database. To run this example, you must have SQL Server running and you must modify function <code class="language-nonAPL">Grid_Load</code> to specify the name of your server.

- GDIPLUS workspace<br />The **[DYALOG]\Samples\winforms\GDIPLUS.dws** workspace contains a sample that demonstrates the use of non-rectangular Forms. It is a direct translation into APL from a C# sample (WinForms-Graphics-GDIPlusShape) that was distributed on the Visual Studio .NET Beta 2 Resource CD.

- tetris workspace<br />The **[DYALOG]\Samples\winforms\tetris.dws** workspace contains a sample that demonstrates the use of graphics. It is a direct translation into APL from a C# sample (WinForms-Graphics-Tetris) that was distributed on the Visual Studio .NET Beta 2 Resource CD.

- webservices workspace<br />The `WFGOLF` function in the **[DYALOG]\Samples\asp.net\webservices\webservices.dws** workspace performs the same task as the `GOLF` function in the same workspace, but it uses <code class="language-nonAPL">Windows.Forms</code> instead of the built-in Dyalog GUI.<br />`WFGOLF` and its callback functions `WFBOOK` and `WFSS` perform exactly the same task, with almost identical dialog box appearance, as `GOLF` and its callbacks `BOOK` and `SS` (described in [Using GolfService from Dyalog](../calling-web-services/#using-golfservice-from-dyalog)).

    !!! Info "Information"
        When you run `WFGOLF` or `GOLF` for the first time, you must supply an argument of `1` to force the creation of the proxy class for the <code class="language-nonAPL">GolfService</code> web service.
