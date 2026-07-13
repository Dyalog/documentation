# APL Line Editor

The APL Line Editor described herein is included for completeness and for adherence to the ISO APL standard.  Dyalog recommends the use of the more powerful Editor and Tracer in preference to the APL Line Editor. Full details of these facilities can be found in the UI Guides for your version of Dyalog APL, as well as in the descriptions of `⎕ED` and `)ED` which appear in the *Dyalog APL Language Reference Guide.*

Using the APL Line Editor, functions and operators are defined by entering Definition Mode.  This mode is opened and closed by the Del symbol, `∇`.  Within this mode, all evaluation of input is deferred.  The standard APL line editor (described below) is used to create and edit operations within definition mode.

Operations may also be defined using the system function `⎕FX` (implicit in a `⎕ED` fix) which acts upon the canonical (character), vector, nested or object representation form of an operation. (See [Fix Definition ](../../../../language-reference-guide/system-functions/fx) for details.)

Functions may also be created dynamically or by function assignment.

The line editor recognises three forms for the opening request.

## Creating Defined Operation

The opening `∇` symbol is followed by the header line of a defined operation.  Redundant blanks in the request are permitted except within names.  If acceptable, the editor prompts for the first statement of the operation body with the line-number 1 enclosed in brackets.  On successful completion of editing, the defined operation becomes the active definition in the workspace.

<h3 class="example">Example</h3>
```apl
      ∇R←FOO
[1]  R←10
[2]  ∇
 
      FOO
10
```

The given operation name must not have an active referent in the workspace, otherwise the system reports `defn error` and the system editor is not invoked:
```apl
      )VARS
SALES  X  Y
 
      ∇R←SALES Y
defn error
```

The header line of the operation must be syntactically correct, otherwise the system reports `defn error` and the system editor is not invoked:
```apl
      ∇R←A B C D:G
defn error
```

## Listing Defined Operation

The `∇` symbol followed by the name of a defined operation and then by a closing `∇`, causes the display of the named operation.  Omitting the function name causes the suspended operation (that is, the one at the top of the state indicator) to be displayed and opened for editing.

<h4 class="example">Example</h4>
```apl
      ∇FOO∇
     ∇ R←FOO
[1]    R←10
     ∇
 
      )SI
#.FOO[1] *
 
     ∇
     ∇ R←FOO
[1]    R←10
[2]
```

## Editing Active Defined Operation

Definition mode is entered by typing `∇` followed optionally by a name and editing directive.

The `∇` symbol on its own causes the suspended operation (that is,  the one at the top of the state indicator) to be displayed.  The editor then prompts for a statement or editing directive with a line-number one greater than the highest line-number in the function.  If the state indicator is empty, the system reports `defn error` and definition mode is not entered.

The `∇` symbol followed by the name of an active defined operation causes the display of the named operation.  The editor then prompts for input as described above.  If the name given is not the name of an active referent in the workspace, the opening request is taken to be the creation of a new operation as described in paragraph 1.  If the name refers to a pendent operation, the editor issues the message `warning pendent operation` prior to displaying the operation.  If the name refers to a locked operation, the system reports defn error and definition mode is not entered.

The `∇` symbol followed by the name of an active defined operation and an editing directive causes the operation to be opened for editing and the editing directive actioned.  If the editing directive is invalid, it is ignored by the editor which then prompts with a line-number one greater than the highest line-number in the operation.  If the name refers to a pendent operation, the editor issues the message  `warning pendent operation` prior to actioning the editing directive.  If the name refers to a locked operation, the system reports `defn error` and definition mode is not entered.

On successful completion of editing, the defined operation becomes the active definition in the workspace which may replace an existing version of the function.  Monitors, and stop and trace vectors are removed.

<h2 class="example">Example</h2>
```apl
      ∇FOO[2]
[2]  R←R*2
[3]  ∇
```

## Editing Directives

Editing directives, summarised in Figure 2(iv) are permitted as the first non-blank characters either after the operation name on opening definition mode for an active defined function, or after a line-number prompt.

|Syntax |Description                                                                                                     |
|-------|----------------------------------------------------------------------------------------------------------------|
|`∇`    |Closes definition mode                                                                                          |
|`[⎕]`  |Displays the entire operation                                                                                   |
|`[⎕n]` |Displays the operation starting at line n                                                                       |
|`[n⎕]` |Displays only line n                                                                                            |
|`[∆n]` |Deletes line n                                                                                                  |
|`[n∆m]`|Deletes m lines starting at line n                                                                              |
|`[n]`  |Prompts for input at line n                                                                                     |
|`[n]s` |Replaces or inserts a statement at line n                                                                       |
|`[n⎕m]`|Edits line n placing the cursor at character position m where an Edit Control Symbol performs a specific action.|

## Line Numbers

Line numbers are associated with lines in the operation.  Initially, numbers are assigned as consecutive integers, beginning with `[0]` for the header line.  The number associated with an operation line remains the same for the duration of the definition mode unless altered by editing directives.  Additional lines may be inserted by decimal numbering.  Up to three places of decimal are permitted.  On closing definition mode, operation lines are re-numbered as consecutive integers.

The editor always prompts with a line number.  The response may be a statement line or an editing directive.  A statement line replaces the existing line (if there is one) or becomes an additional line in the operation:
```apl
      ∇R←A PLUS B
[1]  R←A+B
[2]
```

## Position

The editing directive `[n]`, where n is a line number, causes the editor to prompt for input at that line number.  A statement or another editing directive may be entered.  If a statement is entered, the next line number to be prompted is the previous number incremented by a unit of the display form of the last decimal digit.  Trailing zeros are not displayed in the fractional part of a line number:
```apl
[2]   [0.8]
[0.8] ⍝ MONADIC OR DYADIC +
[0.9] ⍝ A ←→ OPTIONAL ARGUMENT
[1]
```

The editing directive `[n]`s, where `n` is a line number and s is a statement, causes the statement to replace the current contents of line `n`, or to insert line n if there is none:
```apl
[1] [0] R←{A} PLUS B
[1]
```

## Delete

The editing directive `[∆n]`, where `n` is a line number, causes the statement line to be deleted.  The form `[n∆m]`, where `n` is a line number and `m` is a positive integer, causes `m` consecutive statement lines starting from line number `n` to be deleted.

## Edit

The editing directive `[n⎕m]`, where `n` is a line number and `m` is an integer number, causes line number `n` to be displayed and the cursor placed beneath the `m`{th} character on a new line for editing.  The response is taken to be edit control symbols selected from:

|---|---|
|`/`|to delete the character immediately above the symbol.|
|1 to 9|to insert from 1 to 9 spaces immediately prior to the character above the digit.|
|A to Z|to insert multiples of 5 spaces immediately prior to the character above the letter, where A = 5, B = 10, C = 15 and so forth.|
|`,`|to insert the text after the comma, including explicitly entered trailing spaces, prior to the character above the comma, and then re-display the line for further editing with the text inserted and any preceding deletions or space insertions also effected.|
|`.`|to insert the text after the comma, including explicitly entered trailing spaces, prior to the character above the comma, and then complete the edit of the line with the text inserted and any preceding deletions or space insertions also effected.|

Invalid edit symbols are ignored.  If there are no valid edit symbols entered, or if there are only deletion or space insertion symbols, the statement line is re-displayed with characters deleted and spaces inserted as specified.  The cursor is placed at the first inserted space position or at the end of the line if none.  Characters may be added to the line which is then interpreted as seen.

The line number may be edited.

<h2 class="example">Examples</h2>
```apl
[1]   [1⎕7]
[1]   R←A+B
     ,→(0=⎕NC'A')⍴1←⎕LC ⋄
[1]   →(0=⎕NC'A')⍴1←⎕LC ⋄ R←A+B
                               .⋄→END
[2]   R←B
[3]   END:
[4]
```

The form `[n⎕0]` causes the line number `n` to be displayed and the cursor to be positioned at the end of the displayed line, omitting the edit phase.

## Display

The editing directive `[⎕]` causes the entire operation to be displayed.  The form `[⎕n]` causes all lines from line number n to be displayed.  The form `[n⎕]` causes only line number `n` to be displayed:
```apl
[4]   [0⎕]
[0]   R←{A} PLUS B
[0]
[0]   [⎕]
[0]   R←{A} PLUS B
[0.1] ⍝ MONADIC OR DYADIC +
[1]   →(0=⎕NC'A')⍴1+⎕LC ⋄ R←A+B ⋄→END
[2]   R←B
[3]   'END:
[4]
```

## Close Definition Mode

The editing directive `∇` causes definition mode to be closed.  The new definition of the operation becomes the active version in the workspace.  If the name in the operation header (which may or may not be the name used to enter definition mode) refers to a pendent operation, the editor issues the message `warning pendent operation` before exiting.  The new definition becomes the active version, but the original one will continue to be referenced until the operation completes or is cleared from the state indicator.

If the name in the operation header is the name of a visible variable or label, the editor reports `defn error` and remains in definition mode.  It is then necessary to edit the header line or quit.

If the header line is changed such that it is syntactically incorrect, the system reports `defn error`, and re-displays the line leaving the cursor beyond the end of the text on the line.  Backspace/linefeed editing may be used to alter or cancel the change:
```apl
[3]   [0⎕]             - display line 0
[0]   R←{A} PLUS B
[0]   R←{A} PLUS B:G;H - put syntax error in line 0
defn error
[0]   R←{A} PLUS B:G;H - line redisplayed
                  ;G;H - backspace/linefeed editing
[1]
```

Local names may be repeated.  However, the line editor reports warning messages as follows:

1. If a name is repeated in the header line, the system reports "warning duplicate name" immediately.
2. If a label has the same name as a name in the header line, the system reports "warning label name present in line 0" on closing definition mode.
3. If a label has the same name as another label, the system reports "warning duplicate label" on closing definition mode.

1. If a name is repeated in the header line, the system reports "warning duplicate name" immediately.
2. If a label has the same name as a name in the header line, the system reports "warning label name present in line 0" on closing definition mode.
3. If a label has the same name as another label, the system reports "warning duplicate label" on closing definition mode.

Improper syntax in expressions within statement lines of the function is not detected by the system editor with the following exceptions:

- If the number of opening parentheses in each entire expression does not equal the number of closing parentheses, the system reports "warning unmatched parentheses", but accepts the line.
- If the number of opening brackets in each entire expression does not equal the number of closing brackets, the system reports "warning unmatched brackets", but accepts the line.

These errors are not detected if they occur in a comment or within quotes.  Other syntactical errors in statement lines will remain undetected until the operation is executed.

<h2 class="example">Example</h2>
```apl
[4]   R←(A[;1)=2)⌿⍎EXP,'×2
warning unmatched parentheses
warning unmatched brackets
[5]
```

Note that there is an imbalance in the number of quotes.  This will result in a `SYNTAX ERROR` when this operation is executed.

## Quit Definition Mode

The user may quit definition mode by typing the INTERRUPT character.  The active version of the operation (if any) remains unchanged.
