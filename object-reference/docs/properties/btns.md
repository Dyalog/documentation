# <span>Btns</span> <span>Property</span>

**Description**

The Btns property determines the set of buttons to be displayed in a [MsgBox](../objects/msgbox.md). It is a simple vector (one button) or a matrix with up to 3 rows, or a vector of up to 3 character vectors specifying the captions for up to 3 buttons. The buttons are arranged along the bottom of the dialog box in the order specified.

Under Windows, there are restrictions on these buttons. However the property has been designed more generally to be useful under different GUIs and perhaps later revisions of Windows.

Under Windows, the Btns property may specify one of **six** sets of buttons as follows.

- `'OK'`

- `'OK'    'CANCEL'`

- `'RETRY' 'CANCEL'`

- `'YES'   'NO'`

- `'YES'   'NO'    'CANCEL'`

- `'ABORT  'RETRY' 'IGNORE'`

If any other combination is specified, [`⎕WC`](../../../language-reference-guide/system-functions/wc) and [`⎕WS`](../../../language-reference-guide/system-functions/ws) will report a `DOMAIN ERROR`. The names of the buttons are however case-insensitive, so the system will accept `'ok'`, `'Ok'`, `'oK'` or `'OK'`.

If the Btns property is not specified, it assumes a default according to [Style](style.md) as follows :

|Style                |Btns           |
|---------------------|---------------|
|`'Msg'` or `'Info'`  |`'OK'`         |
|`'Warn'` or `'Error'`|`'OK' 'CANCEL'`|
|`'Query'`            |`'YES' 'NO'`   |

If [Style](style.md) is not specified, Btns defaults to `'OK'`.

**Application**

Objects: [MsgBox](../objects/msgbox.md)
