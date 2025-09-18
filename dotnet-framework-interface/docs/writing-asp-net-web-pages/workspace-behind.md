<h1 class="heading"><span class="name"> Workspace Behind</span></h1>

The previous section discussed how APL logic can be separated from page layout, by placing it in a separate APLScript file which is referred to from the `.aspx` web page. It is also possible to have the code reside in a separate *workspace*. This allows you to develop web pages using a traditional workspace approach, and it is probably the quickest way to give an HTML front-end to an existing Dyalog APL application.

In the previous example, you saw that the `fruit.apl` file defined a new class called `FruitSelection` that inherits from `System.Web.UI.Page`. This class contains a `Page_Load` function that (by virtue of its name) overrides the `Page_Load` method of the underlying base class and will be called every time the web page is loaded or posted back. The `Page_Load` function takes whatever action is required; for example, initialisation. The class also contained a callback function to perform some action when the user pressed a button.

A similar technique is employed when the code behind the web page is implemented in a separate workspace. The workspace should contain a class that inherits from `System.Web.UI.Page`. This class may contain a `Page_Load` function that will be invoked every time the corresponding web page is loaded, and as many callback functions as are required to provide the application logic. The workspace is hooked up to one or more web pages by the `Inherits="<classname>"` and  `src="<workspace>"` declarations in the Page directive statement that appears at the beginning of the web page script.

The `ACTFNS` subdirectory in `samples\asp.ne`t contains some examples of Dyalog APL systems that have been converted to run as Web applications using this technique.

Dyalog is grateful to David Hughes who provided the original workspaces and advised on their conversion.

The two workspaces are named `ACTFNS.DWS` and `PROJ.DWS`. The original code used the Dyalog APL GUI to display an input Form, collect and validate the user's input, and calculate and display the results. The original logic supported field level validation and results were immediately recalculated whenever any field was changed. With some exceptions, this has been changed so that the user must press a button to tell the system to recalculate the results. This approach is more appropriate in an Internet application, especially when connection speed is low. Apart from this change, the applications run more-or-less as originally designed.

![](../img/actuarial-diagram.png)

The diagram above illustrates the structure of the web application and the various files involved. The starting page, `actfns.htm`, simply provides a menu of choices which link to various `.aspx` web pages. These pages in turn are linked to one of the two workspaces via the `src=""` declaration

![](../img/actfns-1.png)

The `actfns.htm` start page offers 3 application choices

![](../img/actfns-2.png)

The result of choosing *Tabulate single life insurance and annuity values*

When you choose the first option, the system loads `sla_tab.aspx`. This defines the screen layout in terms of ASP.NET controls, including the `DataGrid` control for tabulating the results. The `sla_tab.aspx` script contains the declarations `Inherits="actuarial" src="actfns.dws"`, so ASP.NET loads the `actuarial` class from this workspace (via a call to Dyalog APL). When the page is loaded, it generates a `Page_Load` event, which in turn calls its `Page_Load` method. This populates the ASP controls with data, and the resulting web page is displayed. The mechanism is described below.

For further details, see the `sla_tab.aspx` script and `ACTFNS.DWS` workspace.

## Converting an Existing Workspace

The steps involved in converting the workspaces were as follows:

1. Replace the Dyalog APL GUI with the equivalent HTML Forms, which are defined in one or more separate `.aspx` web pages. To retain consistency, it is helpful to give the ASP controls the same names as the original GUI controls, which they are replacing.
2. Attach the names of APL callback functions to the appropriate ASP controls; essentially, any controls that will be involved in a postback operation, such as the Submit button. 
3. Starting with a `CLEAR WS`, create a `Class` that represents a .NET class based upon `System.Web.UI.Page`. For example, in converting the ACTFNS workspace, we started by creating the class:
    ```apl
          )ED ○actuarial
    ```

4. then defining `⎕USING` as follows:
    ```apl
    :Using System                      
    :Using System.Web.UI,system.web.dll
    :Using System.Web.UI.WebControls      
    :Using System.Web.UI.HtmlControls     
    :Using System.Data,system.data.dll 
    ```
    The name you choose for this class will replace `classname` in the `Inherits="classname"` declaration in the `.aspx` web page(s) that call it.

5. Create a namespace, change into it, and copy the workspace to be converted; in this case, the starting point was a workspace named `DH_ACTFNS`:
    ```apl
          )NS actuarial_utils
          )CS actuarial_utils
    #.actuarial_utils
          )COPY DH_ACTFNS
    DH_ACTFNS saved ...
    ```

6. Modify the code as appropriate, inserting a `Page_Load` function and whatever callback functions that are required.
7. Make sure the class 'actuarial' has an *:Include actuarial_utils* statement

### The Page_Load function

The `Page_Load` function must be declared as :*Access Public*. `Page_Load` must be spelled correctly as it is this name that causes the function to supersede the base class `Page_Load` method of the same name.

For example, the Page_Load function of the `actuarial` class in ACTFNS.DWS is shown below:
```apl
∇ Page_Load;INT;AGE;DUR;TERM;TAB_DURS;MPC1;INT1;INT2;
            INTY;RUN_OPTION;OPT
  :Access public
  :Signature Page_Load
 ⍝ Overrides Page_Load method of Page class
 ⍝ Called when Page is loaded or re-loaded after postback
 ⍝ Initialise fields and calculate on initial load only
  :If 0=IsPostBack
      RUN_OPTION←GET_RUN_OPTION
      :Select RUN_OPTION
      :Case 1
          EINT.Text←⍕INT←3.25
          EAGE.Text←⍕AGE←30
          EDUR.Text←⍕DUR←0
          ETRM.Text←⍕TERM←10
          TA.Checked←TAB_DURS←1
          CHANGE_TABLES ⍬
      :Case 2
          CPLAN.Items.Clear
          :For OPT :In ↓⊃OPTSPLAN
          CPLAN.Items.Add{82∊⎕DR 1⍴⍵:⊂⍵ ⋄ ⍵}DETRAIL OPT
          :EndFor
          EMPC1.Text←⍕MPC1←100
          EINT1.Text←⍕INT1←3.25
          EINT2.Text←⍕INT2←3.25
          EINTY.Text←⍕INTY←99
          EAGE.Text←⍕AGE←30
          EDUR.Text←⍕DUR←0
          ETRM.Text←'N/A'
          CHANGE_TABLES ⍬
      :EndSelect
  :EndIf
∇
```
If exported correctly, `Page_Load` will be called every time the calling web page is loaded. This occurs when the page is loaded for the first time, and whenever the page is submitted back to the web server by the browser (postback). A postback will occur whenever a callback function is involved, and potentially at other times.

The `Page_Load` function may determine whether it is being invoked by a first time load, or by a postback, from the value of the `IsPostBack` property. This is a property that it inherits from its base class `System.Web.UI.Page`.

The `Page_Load` example shown above uses this property to control the initialisation of the controls in the calling web page. The names `EINT`, `EAGE`, `EDUR` and so forth refer to names of controls in the calling web page. When `Page_Load` is executed, the `actuarial` object is associated with the web page itself, and so the names of all its controls are visible as sub-objects within it.

Note that the `actuarial` class is used by two different web pages, and the function `GET_RUN_OPTION` function determines which of these are involved. (It does so by detecting the presence or otherwise of a particular control on the page).

### Callback functions

The actuarial class in ACTFNS.DWS provides four callback functions named `CALC_FSLTAB_RESULTS`, `CALC_FSL_RESULTS,` `CHANGE_TABLES` and `CHANGE_TABLE_FORMAT`. The first two of these functions are attached as callbacks to the *Calculate* button in each of two separate web pages `sla_tab.aspx` and `sla_disp.aspx`. For example, the statement that defines the button in `sla_tab.aspx` is:
```xml
<asp:Button id=Button1 runat="server" Text="Calculate" onClick="CALC_FSLTAB_RESULTS"></asp:Button>
```

The third callback, `CHANGE_TABLES`, is called by `sla_tab.aspx` when the user selects a different set of Mortality Tables from the three provided. `CHANGE_TABLE_FORMAT` is called when the user clicks either of the two radio buttons that select how the output is to be displayed.

Like the `Page_Load` function, callback functions must be declared as being *Public* methods. This is done using the :*Access* statement.

In addition, and this is **essential**, APL callback functions must be declared to have the correct signature expected of .NET callback functions. This means that they must be monadic, and their argument must be declared to be a 2-element nested array containing two .NET objects; the object that generated the event, and an object that represents the arguments to the event.

Specifically, these parameters must be of type `System.Object` and `System.EventArgs` respectively. However, as our `⎕USING` contains System, it is not necessary to include the `System` prefix.

For example, the statements for the function `CALC_FSLTAB_RESULTS` is shown below:
```apl
:Access Public
:Signature CALC_FSLTAB_RESULTS Object obj, EventArgs ev
```

### Validation functions

In a Dyalog APL web page application, there are basically two approaches to validation. You can handle it entirely yourself or you can exploit the various validation controls that come with ASP.NET. The sample application uses the latter approach by way of illustration. For example:
```xml
<asp:TextBox id=EINT runat="server"></asp:TextBox>
<asp:RequiredFieldValidator id="RFVINT"
     ControlToValidate="EINT"
     ErrorMessage="Interest Rate must be a number
                   between 0 and 20"
     Text="*"
     runat="server"/></td>

```

These ASP.NET statements associate a `RequiredFieldValidator` named *RFVINT* with the *EINT* field, the field used to enter *Interest Rate*. If the user leaves this field blank, the system will automatically generate the specified error message. The page defines a separate `ValidationSummary` control as follows:
```xml
<asp:ValidationSummary id="Summary1" 
    HeaderText="Please enter a value in the following fields"
    Font-Size="smaller"
    ShowSummary="false"
    ShowMessageBox="true"
    EnableClientScript="true"
    runat="server"/>
```

The `ValidationSummary` control collects error messages from all the other validation controls on the page, and displays them together. In this case, a pop-up message box is used. One advantage of this approach is that this type of validation can be carried out client-side by local JavaScript that is generated automatically on the server and incorporated in the HTML that is sent to the browser.

Logical field validation for this page is carried out on the server by APL functions that are attached to `CustomValidator` controls. For example:

```xml
<asp:CustomValidator id="CustomValidator_INT" 
     OnServerValidate="VALIDATE_INT"
     ControlToValidate="EINT"
     Display="Dynamic"                 
     ErrorMessage="Interest Rate must be a number between 0 and 20"
     runat="server"/>
```

These ASP.NET statements associate a `CustomValidator` control named *CustomValidator_INT* with the *Interest Rate* field *EINT*. The statement `OnServerValidate="VALIDATE_INT"` specifies that `VALIDATE_INT` is the validation function for the *CustomValidator_INT* object.

The `VALIDATE_INT` function and its .NET Properties page are shown below.
```apl
     ∇ VALIDATE_INT MSG;source;args
[1]   ⍝ Validates Interest Rate
[2]    :Access Public
[3]    :Signature VALIDATE_INT Object source,
                  ServerValidateEventArgs args
[4]    source args←MSG
[5]    :Trap 0
[6]        INT←Convert.ToDouble args.Value
[7]    :Else
[8]        args.IsValid←0
[9]        :Return
[10]   :EndTrap
[11]   args.IsValid←(0≤INT)^20≥INT
     ∇
```

To make the `VALIDATE_INT` function available to the calling web page, it is exported as a method. Its *calling signature*, namely that it takes two parameters of type `System.Object` and `System.Web.UI.WebControls.ServerValidateEventArgs` respectively, identifies it as a validation function. All these factors are essential in making it recognizable and callable.

`VALIDATE_INT[4]` assigns its (2-element) argument to `source` and `args` respectively. Both are namespace references to .NET objects. `source` is the object that fired the event (*CustomValidator_INT*). `args` is an object that represents the event. Its `Value` property returns the text in the control being validated, in this case the control named *EINT1*.

`VALIDATE_INT[6]` converts the text in the EINT control to a number, using the `ToDouble` method of the `System.Convert` class. You could of course use `⎕VFI`, but the `Convert` methods automatically cater for National Language numerical formats. This statement is executed within a `:Trap` control structure because the method will generate a .NET exception if the data in the field is not a valid number.

`VALIDATE_INT[8 11]` set the `IsValid` property of the `ServerValidateEventArgs` object `args` to 0 or 1 accordingly. This also sets the `IsValid` property of the validation control represented by `source`. The system will automatically display the error message associated with any validation control whose `IsValid` property is 0. Furthermore, the page itself has an `IsValid` property, which is the logical-and of all the `IsValid` properties of all the validation controls on the page. This is used later by the calculation function `CALC_FSLTAB_VALUES`.

In this case, the validation function stores the numeric value of the control in a variable `INT`, which will subsequently be used by the calculation functions.

When the page is posted back to the server, ASP.NET executes its own built-in validation controls and then calls the functions associated with the `CustomValidator` controls, in the order they are defined on the page. In addition to the `VALIDATE_INT` function, there are eight other custom validation functions. Three of these, which validate the *Initial Age*, *Endowment Term* and *Initial Duration* fields, are listed below. Note that all of the `VALIDATE_xxx` functions have the same .NET signature as `VALIDATE_INT`.
```apl
     ∇ VALIDATE_AGE MSG;source;args
[1]    ⍝ Validates Age
[2]    :Access Public
[3]    :Signature VALIDATE_AGE Object source,
                  ServerValidateEventArgs args
[4]    source args←MSG
[5]    :Trap 0
[6]        AGE←Convert.ToInt32 args.Value
[7]    :Else
[8]        args.IsValid←0
[9]        :Return
[10]   :EndTrap
[11]   args.IsValid←(10≤AGE)^80≥AGE
     ∇
```

`VALIDATE_AGE` is similar to `VALIDATE_INT`, except that, because it expects an integer value, it uses the `ToInt32` method instead of the `ToDouble` method.

`VALIDATE_TERM`, which validates the *Endowment Term* field`,` is slightly more interesting because there are two levels of checking involved. The first check that the user has entered an integer number, is performed by lines `[`10-15] in the same way as in the previous examples, using the `ToInt32` method of the `System.Convert` class within a `:Trap` control structure. However, validation of the *Endowment Term* field depends upon the value of another field, namely *Initial Age*.

Not only must the user enter an integer, but also its value must be between 10 and (90-`AGE`) where `AGE` is the value in the *Initial Age* field. However, if the user has entered an incorrect value in the *Initial Age* field, this, the second level of validation cannot be performed.
```apl
    
     ∇ VALIDATE_TERM MSG;source;args
[1]    ⍝ Validates Endowment Term
[2]    :Access Public
[3]    :Signature VALIDATE_TERM Object source,
                  ServerValidateEventArgs args
[4]    source args←MSG
[5]    :If ^/(RFVAGE CustomValidator_AGE).IsValid
[6]          source.ErrorMessage←'Endowment Term must
             be an integer between 10 and ',(⍕90-AGE),
             ' (90-Age)'
[7]    :Else
[8]        source.ErrorMessage←'Endowment Term must
           be an integer between 10 and (90-Age)'
[9]     :EndIf
[10]    :Trap 0
[11]       TERM←Convert.ToInt32 args.Value
[12]   :Else
[13]       args.IsValid←0
[14]       :Return
[15]   :EndTrap
[16]   :If ^/(RFVAGE CustomValidator_AGE).IsValid
[17]       args.IsValid←(TERM≥10)^TERM≤90-AGE
[18]   :EndIf
     ∇
```

At this stage it is worth reviewing the sequence of events that occurs when a user action in the browser causes a *postback* to the server.

1. The page, including all the contents of its fields, is sent back to the ASP.NET server using an http POST command.
2. The postback causes the creation of a new instance of the page; which is represented by a new clone of the `actuarial` namespace.
3. The creation of a new page instance raises the `Page_Load` event which in turn invokes the `Page_Load` method associated with the Page class, or an override method is one is specified. In this case, it calls our `Page_Load` function in the newly cloned instance of the `actuarial` namespace. The `Page_Load` function typically deals with initialisation, such as opening a component file or establishing a connection to a data source. In this case, it does nothing on a postback.
4. Because the *Calculate* button was pressed (see *Forcing Validation*), each of the `CustomValidator` controls on the page raises an `OnServerValidate` event, which in turn calls the associated function in the current instance of the page. These events occur in the order the controls are defined within the page. Note that built-in validation controls, including any `RequiredFieldValidator` controls, are invoked first, potentially in the browser prior to the postback.
5. Because the *Calculate* button was pressed  (see *Forcing Validation*), each of the `CustomValidator` controls on the page raises an `OnServerValidate` event, which in turn calls the associated function in the current instance of the page. These events occur in the order the controls are defined within the page. Note that built-in validation controls, including any `RequiredFieldValidator` controls, are invoked first, potentially in the browser prior to the postback.
6. The control that caused the postback raises an appropriate event, which in turn fires the associated callback function.
7. After all the control events have been raised and processed the `Page_UnLoad` event is raised and the associated function (if any) is invoked. This function is a good place to implement termination code, such as closing a component file or data source.
8. The instance of the page is destroyed. Any global variables in the namespace that were defined by the Page_Load function, the validation functions and the callback function are lost because the clone of the `actuarial` namespace disappears.

This means that within the life of the cloned instance of the actuarial namespace, the system runs our `Page_Load` function followed by `VALIDATE_INT`, followed by `VALIDATE_AGE`, `VALIDATE_TERM`, `VALIDATE_DUR` etc. and finally by `CALC_FSLTAB_RESULTS`. These functions take their input from the values passed in their arguments (as in the case of the `VALIDATE_xxx` functions) or from the properties of any of the controls on the Page. They perform output by modifying these properties, or by invoking standard methods on the Page.

Notice that, if successful, the `VALIDATE_INT` function set up a global variable (strictly speaking, only global within the current instance of the actuarial namespace) called `INT` that contains the value in the *Interest Rate* field. Similarly, `VALIDATE_AGE` defines a variable called `AGE`. These variables are subsequently available for use by the calculation function.

This technique, of having each validation function define a variable for its associated field, saves repeating the conversion work in the calculation routine `CALC_FSLTAB_RESULTS` that will be called when the validation is complete. It also saves repeating the conversion work in a validation routine that needs to know the value of a previously validated field.

Returning to the explanation of `VALIDATE_TERM`, line [16] checks to see that both the `RequiredFieldValidator` and `CustomValidator` controls for the *Initial Age* field register that the value in the field is valid, before attempting to perform the second stage of the validation which depends upon `AGE`. Note that `AGE` must exist (and be a reasonable value) if `CustomValidator_AGE.IsValid` is true. Notice too that it is insufficient just to check the `CustomValidator` control, because its validation function will not be invoked (and the control will register that the field is valid) if the field is empty.

Line [5] uses similar logic to set up an appropriate error message, which is assigned to the `ErrorMessage` property of the corresponding `CustomValidator` control, represented by `source`.

`VALIDATE_DUR`, which validates the *Initial Duration* field, uses similar logic to check that the value in the *Endowment Term* field is correct and that `TERM`, on which it depends, is therefore defined. In addition, in line [8] it refers to the `Checked` property of the `RadioButton` controls named `TA` and `TB` respectively.

```apl
    ∇ VALIDATE_DUR MSG;source;args;DT
[1]    ⍝ Validates Initial Duration
[2]    :Access Public
[3]    :Signature VALIDATE_DUR Object source,
                  ServerValidateEventArgs args
[4]    source args←MSG
[5]    :If 2=GET_RUN_OPTION
[6]       DT←1
[7]   :Else
[8]      DT←+/10 1×(TA TB).Checked
[9]   :EndIf
[10]  :If ^/(RFVTRM CustomValidator_TERM).IsValid

[11]     source.ErrorMessage←'Initial Duration must be an
         integer between 0 and ',(⍕TERM-DT),
         ' (TERM-',(⍕DT),')'
[12]  :Else
[13]     source.ErrorMessage←'Initial Duration must be an
            integer between 0 and (Term-',(⍕DT),')'
[14]  :EndIf
[15]  :Trap 0
[16]     DUR←Convert.ToInt32 args.Value
[17]  :Else
[18]     args.IsValid←0
[19]     :Return
[20]  :EndTrap
[21]  :If ^/(RFVTRM CustomValidator_TERM).IsValid
[22]     args.IsValid←(0≤DUR)^DUR≤TERM-DT
[23]  :EndIf
     ∇
```

### Forcing Validation

Validation controls are automatically invoked when the user activates a Button control, but not when other postbacks occur. For example, when the user selects a different Mortality Table (represented by a `RadioButtonList` control), the page calls the `CHANGE_TABLES` function.
```xml
<asp:RadioButtonList id=MT runat="server"
     RepeatDirection="Vertical" RepeatRows="3"  tabIndex=1
     onSelectedIndexChanged="CHANGE_TABLES" 
     AutoPostBack="true">
<asp:ListItem Value="UK Assured Lives">
     Selected="True">UK Assured Lives</asp:ListItem>
<asp:ListItem Value="UK Immediate Annuitant">
     UK Immediate Annuitant</asp:ListItem>
<asp:ListItem Value="UK Pension Annuitant">
     UK Pension Annuitant</asp:ListItem>
</asp:RadioButtonList>

```

A `RadioButtonList` control does not cause validation to occur, so this must be done explicitly. This is easily achieved by calling the `Validate` method of the Page itself as shown in `CHANGE_TABLES[11]` below.
```apl
     ∇ CHANGE_TABLES ARGS;TableNames;TableName;OPTSMORT;
                MORT_OPTION;RUN_OPTION
[1]   :Access public
[2]   :Signature CHANGE_TABLES  Object obj, EventArgs ev
[3]    RUN_OPTION←GET_RUN_OPTION
[4]    MORT_OPTION←1+MT.SelectedIndex
[5]    OPTSMORT←MORT_OPTION⊃OPTSMORT_ASS OPTSMORT_ANNI
                            OPTSMORT_ANNP
[6]    TableNames←⊃OPTSMORT       ⍝ Assured lives/term
                                     assurance tables
[7]    TableNames←↓(2=⎕NC 0 1↓3⊃OPTSMORT)⌿TableNames
[8]    TableNames←TableNames~¨' '
[9]    CMTAB.Items.Clear
[10]   :For TableName :In TableNames
[11]       CMTAB.Items.Add TableName
[12]   :EndFor
[13]   Page.Validate ⍝ Force page validation
[14]   :Select RUN_OPTION
[15]   :Case 1
[16]       CALC_FSLTAB_RESULTS ⍬
[17]   :Case 2
[18]       CALC_FSL_RESULTS ⍬
[19]   :EndSelect
     ∇
```

### Calculating and Displaying Results

The function `CALC_FSLTAB_RESULTS`, which for brevity is only partially shown below, is used by the `sla_tab.aspx` page to calculate and display results.
```apl
    ∇ CALC_FSLTAB_RESULTS ARGS;X;ULT;MORTOPT;QTAB;TABLE;
         TAB_DURS;RUN_OPTION;MORT_OPTION;UNIX;DOS;
         CURRENTDATE;CURRENTTIME;OPTSMORT;TABLES;MSG;data
[1]    :If IsValid ⍝ Is page valid ?
...
[6]        MORT_OPTION←1+MT.SelectedIndex
[7]        OPTSMORT←MORT_OPTION⊃OPTSMORT_ASS
                                OPTSMORT_ANNI
                                OPTSMORT_ANNP
[8]
[9]        TABLES←↓3⊃OPTSMORT
[10]       MORTOPT←(⍴TABLES)⍴0
[11]       MORTOPT[1+CMTAB.SelectedIndex]←1
[12]       TABLE←⊃MORTOPT/TABLES
...
[15]       TAB_DURS←TA.Checked
...
[41]       FSLT←((⍴X)⍴(3 0)(3 0)(3 0)(11 4)(11 6)(12 4)
                (11 6)(8 0))⍕¨X
[42]       FSLT←FSLT~¨' '
[43]       :With data←⎕NEW DataTable
[44]           cols←Columns.Add¨⊂¨##.FSL_HEADER
[45]           {
[46]               row←NewRow ⍬
[47]               row.ItemArray←⍵
[48]               Rows.Add row
[49]           }¨↓##.FSLT
[50]       :EndWith
[51]       fsl.DataSource←⎕NEW DataView data
[52]       fsl.DataBind
[53]       fsl.Visible←1
[54]   :Else
[55]       fsl.Visible←0
[56]   :EndIf
     ∇
```

The results of the calculation are displayed in a DataGrid object named `fsl`. This is defined within the `sla_tab.aspx` page as follows:
```xml
<asp:DataGrid id="fsl" runat="server" Width="700"
     AllowPaging="false" BorderColor="black" CellPadding="3"
     CellSpacing="0" Font-Size="9pt" PageSize="10">
     <ItemStyle HorizontalAlign="right" Width="100">
     </ItemStyle>
     <HeaderStyle HorizontalAlign="center"
     Font-Size="12pt" Font-Bold="true" BackColor="#17748A"
     ForeColor="#FFFFFF"></HeaderStyle>
     </asp:DataGrid>
```

`CALC_FSLTAB_RESULTS[1]` checks to see if the user input is valid. If not, `[55]` hides the `DataGrid` object `fsl` so that no results are displayed in the page. The display of error messages is handled separately, and automatically, by the `ValidationSummary` control on the page.

`CALC_FSLTAB[11 15]` obtain the values of the *CMTAB* (`DropDownList`) and *TA* (`RadioButton`) controls on the page.

`CALC_FSLTAB[43-53]` store the calculated data table `FSLT` in the `DataGrid` `fsl`.
