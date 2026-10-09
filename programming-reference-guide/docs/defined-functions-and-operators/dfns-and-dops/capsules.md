# Capsules

A _capsule_ is a dfn or dop that is not directly contained in another dfn or dop. It can be named, like a dfn that is defined on its own, or anonymous, like a dfn that is written in a line of a tradfn, in the session, or in a string executed by [_execute_ (`⍎`)](../../../language-reference-guide/primitive-functions/execute.md). Every dfn and dop written inside a capsule belongs to that capsule, including one that is given a local name, as described in [Lexical Name Scope](static-name-scope.md). An operand that is written outside a dop is a capsule of its own.

In the following, `f` and `g` are separate capsules, while `h` is a single capsule that contains the local dfn `i`:

```apl
f←{1+g ⍵}
g←{⎕SIGNAL 11}

h←{
    i←{⎕SIGNAL 11}
    1+i ⍵
}
```

## Line Numbers

The lines of a capsule are numbered through the whole capsule, starting with 0 for the line that contains its opening brace. An error message names the capsule, while the state indicator names the dfn in which the error occurred, both using the capsule's line numbers. In this tradfn, the capsule `outer` contains the dfn `inner`:

```apl
      ⎕VR 'T5'
     ∇ T5;outer
[1]    outer←{
[2]        inner←{
[3]            ÷0
[4]        }
[5]        1+inner ⍬
[6]    }
[7]    1+outer ⍬
     ∇
      T5
DOMAIN ERROR: Divide by zero
outer[2] ÷0
         ∧
      )SI
#.inner[2]*
#.outer[4]
#.T5[7]
```

## Signalling Events

[`⎕SIGNAL`](../../../language-reference-guide/system-functions/signal.md) cuts the state indicator back to exit the capsule that contains the line that invoked it, so the event is reported where that capsule was called. Using the functions defined above, `g` is exited, and the event is reported in `f`, whereas `h` is exited as a whole, because `i` is part of it:

```apl
      f 1
DOMAIN ERROR
f[0] f←{1+g ⍵}
          ∧
      h 1
DOMAIN ERROR
      h 1
      ∧
```

When the capsule is called from a tradfn, the event is therefore reported in the tradfn, where a [`:Trap`](../traditional-functions-and-operators/control-structures/trap.md) control structure or [`⎕TRAP`](../../../language-reference-guide/system-functions/trap.md) can trap it.

## Cutting a Capsule from the Stack

When execution is suspended in a capsule, the **&lt;CA&gt;** (Cut Capsule) action removes the capsule from the state indicator. This leaves execution suspended at the point where the capsule was called, in the state just before it was entered, so that the call can be traced or executed again. In `T5` above, **&lt;CA&gt;** removes both `inner` and `outer`, leaving `T5` suspended on line 7.

**&lt;CA&gt;** has no keystroke by default. You can assign one on the [Keyboard Shortcuts tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog.md#keyboard-shortcuts-tab) of the Configuration dialog box, or invoke the action from the session by sending the key press to the session object with [`⎕NQ`](../../../language-reference-guide/system-functions/nq.md):

```apl
      2 ⎕NQ ⎕SE 'KeyPress' 'CA'
```

The other ways of clearing the state indicator do not respect capsules:

- [_Abort_ (`→`)](../../../language-reference-guide/other-syntax/abort.md) clears the most recently suspended statement and all of its pendent statements, which in `T5` means `inner`, `outer`, and `T5` itself.
- [`)RESET n`](../../../language-reference-guide/system-commands/reset.md) removes the top `n` levels of the state indicator, whatever functions they belong to, and leaves execution suspended at the level below them. In `T5`, `)RESET 1` removes only `inner`, leaving `outer` suspended on line 4, while `)RESET 2` has the same effect as **&lt;CA&gt;**.

## Error-Guards

Capsules do not limit [error-guards](error-guards.md). An error-guard applies to errors in all of the functions that are called while it is in effect, including dfns in other capsules and tradfns:

```apl
gg←{
    11::'caught'
    1+hh ⍵
}
hh←{
    ÷⍵
}
```

```apl
      gg 0
caught
```
