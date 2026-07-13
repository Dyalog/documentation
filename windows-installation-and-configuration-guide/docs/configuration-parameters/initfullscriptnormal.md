# InitFullScriptNormal

When using the Editor to edit  a script such as a Class or Namespace you can specify whether, when you Fix the script and Exit  the Editor, just the functions in the script are re-fixed, or whether the whole script is re-executed, thereby re-initialising any Fields or variables defined within.

These two actions always appear in the Editor File menu, but you can specify which is associated with the <EP> (Esc) key by selecting the appropriate option in the drop-downs labelled:

- Exit and save changes (EP) in a suspended class or namespace should fix:
- If not suspended fix:

In both cases, you may select either  *Only Functions* or         *Everything*.

The label for the corresponding items on the Editor File menu (see  Editor (The File Menu, editing a script)) will change according to which behaviour applies. Note that if you specify a keystroke for <S1> in the *Keyboard Shortcuts* tab, this will be associated with the unselected action.

See also [If not ...](../configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab.md).
