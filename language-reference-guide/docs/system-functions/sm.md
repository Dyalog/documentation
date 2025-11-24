---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SM SM
</div>






<h1 class="heading"><span class="name">Screen Map</span> <span class="command">⎕SM</span></h1>



`⎕SM` is a system variable that defines a character-based user interface (as opposed to a graphical user interface).  In versions of Dyalog APL that support asynchronous terminals, `⎕SM` defines a **form** that is displayed on the **USER SCREEN**.  The implementation of `⎕SM` in "window" environments is compatible with these versions.  In Dyalog APL/X, `⎕SM` occupies its own separate window on the display, but is otherwise equivalent.  In versions of Dyalog APL with GUI support, `⎕SM` either occupies its own separate window (as in Dyalog APL/X) or, if it exists, uses the window assigned to the SM object.  This allows `⎕SM` to be used in a GUI application in conjunction with other GUI components.


`⎕SM` has workspace scope.


In general `⎕SM` is a nested matrix containing between 3 and 13 columns.  Each row of `⎕SM` represents a **field**; each column a **field attribute**.



The columns have the following meanings:


|Column|Description                 |Default|
|------|----------------------------|-------|
|1     |Field Contents              |N/A    |
|2     |Field Position - Top Row    |N/A    |
|3     |Field Position - Left Column|N/A    |
|4     |Window Size - Rows          |0      |
|5     |Window Size - Columns       |0      |
|6     |Field Type                  |0      |
|7     |Behaviour                   |0      |
|8     |Video Attributes            |0      |
|9     |Active Video Attributes     |`¯` 1  |
|10    |Home Element - Row          |1      |
|11    |Home Element - Column       |1      |
|12    |Scrolling Group - Vertical  |0      |
|13    |Scrolling Group - Horizontal|0      |


With the exception of columns 1 and 8, all elements in `⎕SM` are integer scalar values.



Elements in column 1 (Field Contents) may be:

- A numeric scalar
- A numeric vector
- A 1-column numeric matrix
- A character scalar
- A character vector
- A character matrix (rank 2)
- A nested matrix defining a sub-form whose structure and contents must conform to that defined for `⎕SM` as a whole.  This definition is recursive.  Note however that a sub-form must be a matrix - a vector is not allowed.




Elements in column 8 (Video Attributes) may be:

- An integer scalar that specifies the appearance of the entire field.
- An integer array of the same shape as the field contents.  Each element specifies the appearance of the corresponding element in the field contents.


## Screen Management (Async Terminals)


Dyalog APL for UNIX systems on tty devices (async terminals or on terminal emulators) manages two screens; the SESSION screen and the USER screen.  If the SESSION screen is current, an assignment to `⎕SM` causes the display to switch to the USER screen and show the form defined by `⎕SM`.


Note that Ride does not directly support `⎕SM`, although it is possible to display `⎕SM` in the tty session to which a Ride client is connected.


If the USER screen is current, any change in the value of `⎕SM` is immediately reflected by a corresponding change in the appearance of the display.  However, an assignment to `⎕SM` that leaves its value unchanged has no effect.


Dyalog APL automatically switches to the SESSION screen for default output, if it enters immediate input mode (6-space prompt), or through use of `⎕` or `⍞`.  This means that typing
```apl
      ⎕SM ← expression
```


in the APL session will cause the screen to switch first to the USER screen, display the form defined by `⎕SM`, and then switch back to the SESSION screen to issue the 6-space prompt.  This normally happens so quickly that all the user sees is a flash on the screen.To retain the USER screen in view it is necessary to issue a call to `⎕SR` or for APL to continue processing. For example:

```apl
      ⎕SM ← expression  ⋄  ⎕SR 1
```


or
```apl
      ⎕SM ← expression  ⋄  ⎕DL 5
```


## Screen Management (Window Versions)


In Dyalog APL/X, and optionally in Dyalog APL/W, `⎕SM` is displayed in a separate **USER WINDOW** on the screen.  In an end-user application this may be the only Dyalog APL window.  However, during development, there will be a SESSION window, and perhaps EDIT and TRACE windows too.


The USER Window will only accept input during execution of `⎕SR`.  It is otherwise "output-only".  Furthermore, during the execution of `⎕SR` it is the only active window, and the SESSION, EDIT and TRACE Windows will not respond to user input.

## Screen Management (GUI Versions)


In versions of Dyalog APL that provide GUI support, there is a special SM object that defines the position and size of the window to be associated with `⎕SM`.  This allows character-mode applications developed for previous versions of Dyalog APL to be migrated to and integrated with GUI environments without the need for a total re-write.

## Effect of Localisation


Like all system variables (with the exception of `⎕TRAP`) `⎕SM` is subject to "pass-through localisation".  This means that a localised `⎕SM` assumes its value from the calling environment.  The localisation of `⎕SM` does not, of itself therefore, affect the appearance of the display.  However, reassignment of a localised `⎕SM` causes the new form to overlay rather than replace whatever forms are defined further down the stack.  The localisation of `⎕SM` thus provides a simple method of defining pop-up forms, help messages, etc.



The user may edit the form defined by `⎕SM` using the system function `⎕SR`.  Under the control of `⎕SR` the user may change the following elements in `⎕SM` which may afterwards be referenced to obtain the new values.


|---------|-------------------------------------------------|
|Column 1 |Field Contents                                   |
|Column 10|Home Element - Row (by scrolling vertically)     |
|Column 11|Home Element - Column (by scrolling horizontally)|



