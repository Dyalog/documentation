<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SAVE SAVE
</div>

<h1 class="heading"><span class="name">Save Workspace</span> <span class="command">{R}←{X}⎕SAVE Y</span></h1>

`Y` must be a simple character scalar or vector that identifies a  full or relative path name to the file in which the workspace will be written.

Unless the path specified by `Y` is a full pathname, it is taken to be relative to the current working directory which may be obtained by the expression: `⊃1 ⎕NPARTS ''`.

See [Programmer's Guide: "Workspaces"](../../../programming-reference-guide/introduction/workspaces) for the rules for specifying a workspace name.

The active workspace is saved with the  file name specified by  `Y`, whether or not a workspace file of that name already exists.

A `DOMAIN ERROR` is reported if the name in `Y` :

- is not a valid workspace name
- is not a valid  file name
- refers to an unauthorised directory
- specifies an existing file that does not already contain a Dyalog workspace or session file

The shy result `R` is a simple Boolean scalar 1. However, when the  workspace is subsequently loaded using `⎕LOAD` and execution restarts, the result is 0, as described below.

The optional left argument `X` is either 0 or 1. If `X` is omitted or 1, the saved version of the workspace has execution suspended at the point of exit from the `⎕SAVE` function.  If the saved workspace is subsequently loaded by `⎕LOAD`, execution is resumed, and the value 0 is returned if the result is used or assigned, or otherwise the result is suppressed. In this case, the latent expression value (`⎕LX`) is ignored.

If `X` is 0, the workspace is saved without any state indicator in effect. The effect is the same as if you first executed `)RESET` and then `)SAVE`. In this case, when the workspace is subsequently loaded, the value of the latent expression (`⎕LX`) is honoured if applicable.

As is the case for `)SAVE` (see [Save Workspace](../system-commands/save.md)), monadic `⎕SAVE` will fail and issue `DOMAIN ERROR` if any threads (other than the root thread 0) are running or if there are any Edit or Trace windows open. However, neither of these restrictions apply if the left argument `X` is 0.

Note that the values of all system variables (including `⎕SM`) and all GUI objects are saved.

<h2 class="example">Example</h2>
```apl
      (⊃'SAVED' 'ACTIVE' [⎕IO+⎕SAVE'TEMP']),' WS'
ACTIVE WS
      ⎕LOAD 'TEMP'
SAVED WS
```


Additional operations may be performed before saving the workspace. For further information, see [Set Workspace Save Options](../primitive-operators/i-beam/set-workspace-save-options.md).


