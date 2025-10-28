<h1 class="heading"><span class="name">Modal Dialog Boxes</span></h1>

Dialog Boxes are displayed modally to prevent the user from performing tasks outside of the dialog box.

To create a modal dialog box, you create a `Form`, set its `BorderStyle` property to `FixedDialog`, set its `ControlBox`, `MinimizeBox` and `MaximizeBox` properties to false, and display it using `ShowDialog`.

A modal dialog box has a `DialogResult` property that is set when the `Form` is closed, or when the user presses OK or Cancel. The value of this property is returned by the `ShowDialog` method, so the simplest way to handle user actions is to check the result of `ShowDialog` and proceed accordingly. Example 1 illustrates a simple modal dialog box.

<h2 class="example">Example 1</h2>

Function `EG1` illustrates how to create and use a simple modal dialog box. Much of the function is self-explanatory, but the following points are noteworthy.

`EG1[1-2]` set `⎕USING` to include the .NET Namespaces `System.Windows.Forms` and `System.Drawing`.

`EG1[6,8,9]` create a `Form` and two `Button` objects. As yet, they are unconnected. The constructor for both classes is defined to take no arguments, so the `⎕NEW` system function is only called with a class argument.

`EG1[14]` shows how the `Location` property is set by first creating a new `Point` object with a specific pair of (x and y) values.

`EG1[18]` computes the values for the `Point` object for `button2.Location`, from the values of the `Left`, `Height` and `Top` properties of `button1`; thus positioning `button2` relative to `button1`.
```apl
     ∇ EG1;form1;button1;button2;true;false;⎕USING;Z
[1]    ⎕USING←,⊂'System.Windows.Forms,
                 System.Windows.Forms.dll'
[2]    ⎕USING,←⊂'System.Drawing,System.Drawing.dll'
[3]    true false←1 0
[4]
[5]    ⍝ Create a new instance of the form.
[6]    form1←⎕NEW Form
[7]    ⍝ Create two buttons to use as the accept and cancel btns
[8]    button1←⎕NEW Button
[9]    button2←⎕NEW Button
[10]
[11]   ⍝ Set the text of button1 to "OK".
[12]   button1.Text←'OK'
[13]   ⍝ Set the position of the button on the form.
[14]   button1.Location←⎕NEW Point,⊂10 10
[15]   ⍝ Set the text of button2 to "Cancel".
[16]   button2.Text←'Cancel'
[17]   ⍝ Set the position of the button relative to button1.
[18]   button2.Location←⎕NEW Point,
                   ⊂button1.Left button1.(Height+Top+10)
[19]
```

`EG1[21,23]` sets the `DialogResult` property of `button1` and `button2` to `DialogResult.OK` and `DialogResult.Cancel` respectively. Note that `DialogResult` is an enumeration with a predefined set of member values.

Similarly, `EG1[32]` defines the `BorderStyle` property of the form using the `FormBorderStyle` enumeration.

`EG1[38 40]` defines the `AcceptButton` and `CancelButton` properties of the Form to `button1` and `button2` respectively. These have the same effect as the Dyalog GUI Default and Cancel properties.

`EG1[42]` sets the `StartPosition` of the Form to be centre screen. Once again this is specified using an enumeration; `FormStartPosition`.
```apl
[20]  ⍝ Make button1's dialog result OK.
[21]   button1.DialogResult←DialogResult.OK
[22]  ⍝ Make button2's dialog result Cancel.
[23]   button2.DialogResult←DialogResult.Cancel
[24]
[25]
[26]   ⍝ Set the title bar text of the form.
[27]   form1.Text←'My Dialog Box'
[28]   ⍝ Display a help button on the form.
[29]   form1.HelpButton←true
[30]
[31]   ⍝ Define the border style of the form to that of a
                                               dialog box.
[32]   form1.BorderStyle←FormBorderStyle.FixedDialog
[33]   ⍝ Set the MaximizeBox to false to remove the
                                             maximize box.
[34]   form1.MaximizeBox←false
[35]   ⍝ Set the MinimizeBox to false to remove the
                                             minimize box.
[36]   form1.MinimizeBox←false
[37]   ⍝ Set the accept button of the form to button1.
[38]   form1.AcceptButton←button1
[39]   ⍝ Set the cancel button of the form to button2.
[40]   form1.CancelButton←button2
[41]   ⍝ Set the start position of the form to the centre
                                            of the screen.
[42]   form1.StartPosition←FormStartPosition.CenterScreen
[43]
 
```

`EG1[45 46]` associate the buttons with the Form. The `Controls` property of the `Form` returns an object of type `Form.ControlCollection`. This class has an `Add` method that is used to add a control to the collection of controls that are owned by the `Form`.

`EG1[50]` calls the `ShowDialog` method (with no argument; hence the `⍬`). The result is an object of type `Form.DialogResult`, which is an enumeration.

`EG1[52]` compares the result returned by `ShowDialog` with the enumeration member `DialogResult.OK` (note that the primitive function = has been extended to compare objects).
```apl
[44]   ⍝ Add button1 to the form.
[45]   form1.Controls.Add button1
[46]   ⍝ Add button2 to the form.
[47]   form1.Controls.Add button2
[48]
[49]   ⍝ Display the form as a modal dialog box.
[50]   Z←form1.ShowDialog ⍬
[51]   ⍝ Determine if the OK button was clicked on the
                                              dialog box.
[52]   :If Z=DialogResult.OK
[53]      ⍝ Display a message box saying that the OK
                                      button was clicked.
[54]       Z←MessageBox.Show⊂'The OK button on the form
                                             was clicked.'
[55]   :Else
[56]      ⍝ Display a message box saying that the Cancel
                                      button was clicked.
[57]       Z←MessageBox.Show⊂'The Cancel button on the
                                        form was clicked.'
[58]   :EndIf
     ∇
```

!!! warning
    The use of modal forms in .NET can lead to problematic situations while debugging. As the control is passed to .NET the APL interpreter cannot regain control in the event of an unforeseen error. It is advisable to change the code to something like the following until the code is fully tested:
     ```apl
     [52]   form1.Visible←1
     [53]   :While form1.Visible ⋄ :endwhile
     ```

<h2 class="example">Example 2</h2>

Functions `EG2` and `EG2A` illustrate how the Each operator (`¨`) and the extended namespace reference syntax in Dyalog may be used to produce more succinct, and no less readable, code.
```apl
     ∇ EG2;form1;label1;textBox1;true;false;⎕USING;Z
[1]    ⎕USING←,⊂'System.Windows.Forms,
                 System.Windows.Forms.dll'
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
[19]   ⍝ Add the TextBox control to the form's control
          collection.
[20]   form1.Controls.Add textBox1
[21]   ⍝ Add the Label control to the form's control
          collection.
[22]   form1.Controls.Add label1
[23]
[24]   ⍝ Display the form as a modal dialog box.
[25]   Z←form1.ShowDialog ⍬
     ∇
```

`EG2A[7]` takes advantage of the fact that .NET classes are namespaces, so the expression `Form TextBox Label`  is a vector of namespace refs, and the expression `⎕NEW¨Form TextBox Label`  runs the `⎕NEW` system function on each of them.

Similarly, `EG2A[10 11 12]` combine the use of extended namespace reference and the *Each* operator to set the `Text`, `Location` and `Size` properties in several objects together.

```apl
     
     ∇ EG2A;form1;label1;textBox1;true;false;⎕USING;Z
[1]    ⍝ Compact version of EG2 taking advantage of ref
          syntax and ¨
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
[14]   ⍝ Add the Label and TextBox controls to the form's
          control collection.
[15]   form1.Controls.AddRange⊂label1 textBox1
[16]
[17]   ⍝ Display the form as a modal dialog box.
[18]   Z←form1.ShowDialog ⍬
     ∇
```
