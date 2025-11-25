---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SR SR
</div>


<h1 class="heading"><span class="name">Screen Read</span> <span class="command">R←{X}⎕SR Y</span></h1>

`⎕SR` is a system function that allows the user to edit or otherwise interact with the form defined by `⎕SM`.

In versions of Dyalog APL that support asynchronous terminals, if the current screen is the SESSION screen, `⎕SR` immediately switches to the USER SCREEN and displays the form defined by `⎕SM`.

In Dyalog APL/X, `⎕SR` causes the input cursor to be positioned in the USER window.  During execution of `⎕SR`, only the USER Window defined by `⎕SM` will accept input and respond to the keyboard or mouse.  The SESSION and any EDIT and TRACE Windows that may appear on the display are dormant.

In versions of Dyalog APL with GUI support, a single SM object may be defined.  This object defines the size and position of the `⎕SM` window, and allows `⎕SM` to be used in conjunctions with other GUI components.  In these versions, `⎕SR` acts as a superset of `⎕DQ` (see [Dequeue Events](dq.md)) but additionally controls the character-based user interface defined by `⎕SM`.

`Y` is an integer vector that specifies the fields which the user may visit.  In versions with GUI support, `Y` may additionally contain the names of GUI objects with which the user may also interact.

If specified, `X` may be an enclosed vector of character vectors defining `EXIT_KEYS` or a 2-element nested vector defining `EXIT_KEYS` and the `INITIAL_CONTEXT`.

The result `R` is the `EXIT_CONTEXT`.

Thus the 3 uses of `⎕SR` are:
```apl
     EXIT_CONTEXT←⎕SR FIELDS
 
     EXIT_CONTEXT←(⊂EXIT_KEYS)⎕SR FIELDS
 
     EXIT_CONTEXT←(EXIT_KEYS)(INITIAL_CONTEXT)⎕SR FIELDS
```

## FIELDS

If an element of `Y` is an integer scalar, it specifies a field as the index of a row in `⎕SM` (if `⎕SM` is a vector it is regarded as having 1 row).

If an element of `Y` is an integer vector, it specifies a sub-field.  The first element in `Y` specifies the top-level field as above.  The next element is used to index a row in the form defined by `⊃⎕SM[Y[1];1]` and so forth.

If an element of `Y` is a character scalar or vector, it specifies the name of a top-level GUI object with which the user may also interact.  Such an object must be a "top-level" object, that is, the `Root` object ('`.'`) or a `Form` or pop-up `Menu`.  This feature is implemented ONLY in versions of Dyalog APL with GUI support.

## EXIT_KEYS

Each element of `EXIT_KEYS` is a 2-character code from the Input Translate Table for the keyboard.  If the user presses one of these keys, `⎕SR` will terminate and return a result.

If `EXIT_KEYS` is not specified, it defaults to:
```apl
      'ER' 'EP' 'QT'
```

which (normally) specifies <Enter>, <Esc> and <Shift+Esc>.

## INITIAL_CONTEXT

This is a vector of between 3 and 6 elements with the following meanings and defaults:

|Element|Description                  |Default|
|-------|-----------------------------|-------|
|1      |Initial Field                |N/A    |
|2      |Initial Cursor Position - Row|N/A    |
|3      |Initial Cursor Position - Col|N/A    |
|4      |Initial Keystroke            |`''`   |
|5      |(ignored)                    |N/A    |
|6      |Changed Field Flags          |0      |


Structure of INITIAL_CONTEXT


`INITIAL_CONTEXT[1]` specifies the field in which the cursor is to be placed.  It is an integer scalar or vector, and must be a member of `Y`.  It must not specify a field which has `BUTTON` behaviour (64), as the cursor is not allowed to enter such a field.

`INITIAL_CONTEXT[2 3]` are integer scalars which specify the initial cursor position within the field in terms of row and column numbers.

`INITIAL_CONTEXT[4]` is either empty, or a 2-element character vector specifying the initial keystroke as a code from the Input Translate Table for the keyboard.

`INITIAL_CONTEXT[5]` is ignored.  It is included so that the `EXIT_CONTEXT` result of one call to `⎕SR` can be used as the `INITIAL_CONTEXT` to a subsequent call.

`INITIAL_CONTEXT[6]` is a Boolean scalar or vector the same length as `Y`.  It specifies which of the fields in `Y` has been modified by the user.

## EXIT_CONTEXT

The result `EXIT_CONTEXT` is a 6 or 9-element vector whose first 6 elements have the same structure as the `INITIAL_CONTEXT`.  Elements 7-9 **only** apply to those versions of Dyalog APL that provide mouse support.

|Element|Description                |
|-------|---------------------------|
|1      |Final Field                |
|2      |Final Cursor Position - Row|
|3      |Final Cursor Position - Col|
|4      |Terminating Keystroke      |
|5      |Event Code                 |
|6      |Changed Field Flags        |
|7      |Pointer Field              |
|8      |Pointer Position - Row     |
|9      |Pointer Position - Col     |

Structure of the Result of `⎕SR`

`EXIT_CONTEXT[1]` contains the field in which the cursor was when `⎕SR` terminated due to the user pressing an exit key or due to an event occurring.  It is an integer scalar or vector, and a member of `Y`.

`EXIT_CONTEXT[2 3]` are integer scalars which specify the row and column position of the cursor within the field `EXIT_CONTEXT[1]` when `⎕SR` terminated.

`EXIT_CONTEXT[4]` is a 2-element character vector specifying the last keystroke pressed by the user before `⎕SR` terminated.  Unless `⎕SR` terminated due to an event, `EXIT_CONTEXT[4]` will contain one of the exit keys defined by `X`.  The keystroke is defined in terms of an Input Translate Table code.

`EXIT_CONTEXT[5]` contains the **sum** of the event codes that caused `⎕SR` to terminate.  For example, if the user pressed a mouse button on a `BUTTON` field (event code 64) **and** the current field has `MODIFIED` behaviour (event code 2) `EXIT_CONTEXT[5]` will have the value 66.

`EXIT_CONTEXT[6]` is a Boolean scalar or vector the same length as `Y`.  It specifies which of the fields in `Y` has been modified by the user during **this** `⎕SR`, ORed with `INITIAL_CONTEXT[6]`.  Thus if the `EXIT_CONTEXT` of one call to `⎕SR` is fed back as the `INITIAL_CONTEXT` of the next, `EXIT_CONTEXT[6]` records the fields changed since the start of the process.

## EXIT_CONTEXT (Window Versions)

`⎕SR` returns a 9-element result **ONLY** if it is terminated by the user pressing a mouse button.  In this case:

`EXIT_CONTEXT[7]` contains the field over which the mouse pointer was positioned when the user pressed a button. It is an integer scalar or vector, and a member of `Y`.

`EXIT_CONTEXT[8 9]` are integer scalars which specify the row and column position of the mouse pointer within the field `EXIT_CONTEXT[7]` when `⎕SR` terminated.

!!! note
    This function is disabled and instead generates a `DOMAIN ERROR` if the RIDE_SPAWNED parameter is non-zero. This is designed to prevent it being invoked from a Ride session which does not support this type of user interface. For further details, see the [Ride User Guide](https://dyalog.github.io/ride).


