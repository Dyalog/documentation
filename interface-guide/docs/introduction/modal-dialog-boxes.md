# Modal Dialog Boxes

Up to now, it has been assumed that your user has constant access to all of the interface features and controls that you have provided. The user is in charge; your application merely responds to his requests.

Although this is generally considered desirable, there are times when a particular operation must be allowed to complete before anything else can be done. For example, an unexpected error may occur and the user must decide upon the next course of action (for example,  Continue, Restart, Quit). In these situations, a *modal* dialog box is required. A modal dialog box is one to which the user must respond before the application will continue. While the modal dialog box is in operation, interaction with all other objects is inhibited.

A modal dialog box is simply achieved by calling `⎕DQ` with just the name of the corresponding Form in its argument. This can be done from within a callback function or indeed from any point in an application. To make the local `⎕DQ` terminate, you may specify an action code of 1 for an event. Alternatively, if you wish to make exclusive use of callback functions to process events, you can cause the `⎕DQ` to terminate by erasing the Form from a callback function.

For example, suppose that you want the user to close the dialog box by clicking an "OK" button. You would specify the Event property for the Button as:
```apl
      ('Event' 'Select' 'EXIT')
```

... and the function `EXIT` is simply...
```apl
     ∇ EXIT Msg;BTN;Form
[1]   ⍝ Terminate modal ⎕DQ by erasing Form
[2]    OBJ←⍕⊃Msg
[3]    Form←(¯1+OBJ⍳'.')↑OBJ ⍝ Get Form name
[4]    ⎕EX Form
     ∇
```

Note that this function is fairly general, as it gets the name of the Form from the name of the object that generated the event.

## The MsgBox and FileBox Objects

The MsgBox and FileBox objects are standard MS-Windows dialog boxes and are strictly modal. The following discussion refers to the way a MsgBox is used, but applies equally to a FileBox.

The MsgBox is a pop-up modal dialog box with a title bar (defined by the Caption property), an icon (defined by the Style property), some text (defined by the Text property) and up to three buttons (defined by the Btns property).

The MsgBox does not appear on the screen when you create it with `⎕WC`. Instead, it pops up ONLY when you call `⎕DQ` with the name of the MsgBox as its sole right argument. Furthermore, the MsgBox automatically pops down when the user clicks on any one of its buttons; you don't actually have to enable any events to achieve this. For example:
```apl
      'ERR' ⎕WC 'MsgBox' 'Input Error' '' 'Error'
```

creates an invisible MsgBox with the title (Caption) `'Input Error'`, no text, and a Style of `'Error'`. This gives it a "Stop sign" icon. When you want to issue an error message to your user, you simply call a function (let's call it `ERRMSG`) which is defined as follows:
```apl
     ∇ ERRMSG Msg
[1]   ⍝ Displays 'ERR' message box
[2]    ERR.Text←Msg ⍝ Put Msg in box
[3]   ⎕DQ 'ERR'
     ∇
```

Note that `⎕DQ` will terminate automatically when the user clicks one of the buttons in the MsgBox object.

In this case we were not interested in the particular button that the user pressed. If you are interested in this information, you can enable special events associated with these buttons. For details, see the description of the MsgBox and FileBox objects in the Object Reference.
