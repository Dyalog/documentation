# InitFullScriptSusp

When the Editor is used to edit a script (such as a Class or Namespace) that is **suspended**, this controls whether fixing the script and exiting the Editor re-fixes just the functions in the script, or re-executes the whole script (re-initialising any fields or variables defined within it). It determines the action associated with the `<EP>` (Esc) key; the other action remains available on the Editor File menu (and can be assigned to `<S1>` in the Keyboard Shortcuts tab).

Valid values are:

- `Only Functions` : only the functions in the script are re-fixed
- `Everything` : the whole script is re-executed

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->

Related parameters: [InitFullScriptNormal](initfullscriptnormal.md).

See also the [Trace/Edit tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab) of the Windows Configuration Dialog.
