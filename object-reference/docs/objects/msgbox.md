# <span>MsgBox</span> <span>Object</span>



[Parents](../parentlists/msgbox.md), [Children](../childlists/msgbox.md), [Properties](../proplists/msgbox.md), [Methods](../methodlists/msgbox.md), [Events](../eventlists/msgbox.md)



**Purpose:** Provides a "modal" dialog box for displaying messages, errors, warnings and other information. The dialog box has a title, one or more lines of text, and up to three buttons.

**Description**


The [Caption](../properties/caption.md) property determines the text displayed in the object's title bar.



The [Text](../properties/text.md) property determines the text to be displayed as the message.


The [Style](../properties/style.md) property determines the type of icon which is displayed. This is a character vector with one of the following values:


|---------|------------------------|
|`'Msg'`  |no icon (the default)   |
|`'Info'` |information message icon|
|`'Query'`|query (question) icon   |
|`'Warn'` |warning icon            |
|`'Error'`|critical error icon     |


The [Btns](../properties/btns.md) property determines the set of buttons to be displayed. It is a simple vector (one button) or a matrix with up to 3 rows, or a vector of up to 3 character vectors specifying the captions for up to 3 buttons. MS-Windows restricts you to a fixed set of button captions which are described below. However, the property has been designed more generally to be useful under different GUIs and perhaps later revisions of Windows. The buttons are arranged along the bottom of the dialog box in the order specified.


The [Btns](../properties/btns.md) property may specify one of six sets of buttons as follows:

- `'OK'`

- `'OK'    'CANCEL'`

- `'RETRY' 'CANCEL'`

- `'YES'   'NO'`

- `'YES'   'NO'    'CANCEL'`

- `'ABORT'  'RETRY' 'IGNORE'`



If any other combination is specified, [`⎕WC`](../../../language-reference-guide/system-functions/wc) and [`⎕WS`](../../../language-reference-guide/system-functions/ws) will report a `DOMAIN ERROR`. The names of the buttons are however case-insensitive, so the system will accept `'ok'`, `'Ok'`, `'oK'` or `'OK'`. If [Btns](../properties/btns.md) is not specified, it assumes a default according to [Style](../properties/style.md) as follows:


|Style                    |Btns           |
|-------------------------|---------------|
|`'Msg'` **or** `'Info'`  |`'OK'`         |
|`'Warn'` **or** `'Error'`|`'OK' 'CANCEL'`|
|`'Query'`                |`'YES' 'NO'`   |


The [Default](../properties/default.md) property may be used to determine which of the buttons is the "default" button, that is, the one which initially has the focus and is "selected" when the user presses the Enter key. It has the value 1, 2 or 3. If [Default](../properties/default.md) is not specified, the first button is the "default" button. Note that if the user switches focus to another button and presses Enter, this action selects the button with the focus.


Like a pop-up (floating) [Menu](menu.md), the MsgBox object is unusual in that it is strictly modal. It is created by [`⎕WC`](../../../language-reference-guide/system-functions/wc) in the normal way, but at that stage is invisible and inactive. It is activated ONLY when [`⎕DQ`](../../../language-reference-guide/system-functions/dq) is called with the name of the MsgBox as the argument. When this is done, the MsgBox object pops up and is activated. Because there is no other object specified in the argument to [`⎕DQ`](../../../language-reference-guide/system-functions/dq), all other objects are de-activated. The only thing that the user can do (within the APL application) is to press one of the buttons in the MsgBox. When this happens, the MsgBox automatically pops down, the callback function (if any) is fired, and then [`⎕DQ`](../../../language-reference-guide/system-functions/dq) terminates.


Notice that the position and size of the MsgBox are determined by Windows and are fixed, although the MsgBox may be moved by the user after it has been displayed.


The MsgBox object generates one of three events; [MsgBtn1](../methodorevents/msgbtn1.md) (61), [MsgBtn2](../methodorevents/msgbtn2.md) (62), or [MsgBtn3](../methodorevents/msgbtn3.md) (63) depending upon which button is pressed.
```apl
   Caption←'Default MsgBox' ⋄ Text←'Hello World'
   'Msg' ⎕WC 'MsgBox' Caption Text ⋄ ⎕DQ 'Msg'
      
   Caption←'Information MsgBox' ⋄ Text←'Update Completed'
   'Msg' ⎕WC 'MsgBox' Caption Text 'Info' ⋄ ⎕DQ 'Msg'
      
   Caption←'Query MsgBox' ⋄ Text←'Save Changes'
   'Msg' ⎕WC 'MsgBox' Caption Text 'Query' ⋄ ⎕DQ 'Msg'
      
   Caption←'Warning MsgBox'
   Text←'Calculations will take 10 minutes'
   'Msg' ⎕WC 'MsgBox' Caption Text 'Warn' ⋄ ⎕DQ 'Msg'
      
   Caption←'Error MsgBox'
   Text←'Data out of range'
   'Msg' ⎕WC 'MsgBox' Caption Text 'Error' ⋄ ⎕DQ 'Msg'


   Caption←'Custom MsgBox'
   Text←⊂'You can have a multi-line'
   Text,←⊂'message if you want one'
   B←'ABORT' 'RETRY' 'IGNORE'
   'Msg' ⎕WC 'MsgBox' Caption Text 'Info' B ⋄ ⎕DQ 'Msg'
```


