# Capsules

A _capsule_ is a literal dfn or dop whose definition is not directly contained within another dfn or dop. Every literal dfn and dop that is written inside a capsule belongs to that capsule. An operand dfn belongs to the capsule in which it is written (which could be itself), not to the capsule of the dop to which it is passed.

In the following, `caller` and `callee` are separate capsules, while `container` is a single capsule that contains the local dfn `helper`:

```apl
caller←{1+callee ⍵}
callee←{⎕SIGNAL 11}

container←{
    helper←{⎕SIGNAL 11}
    1+helper ⍵
}
```

## Line Numbers

The lines of a capsule are numbered through the whole capsule, starting with 0 for the line that contains its opening brace. An error message names the capsule, and the state indicator names the dfn in which execution is suspended, both using the capsule's line numbers. The pendent levels of dfns nested in the capsule are named after the capsule. In this tradfn, the capsule `outer` contains the dfn `mid`, which contains the dfn `inner`:

```apl
      ⎕CR 'Main'
 Main;outer
 outer←{           ⍝ capsule line [0]
     mid←{         ⍝ capsule line [1]
         inner←{   ⍝ capsule line [2]
             ÷0    ⍝ capsule line [3]
         }         ⍝ capsule line [4]
         1+inner ⍬ ⍝ capsule line [5]
     }             ⍝ capsule line [6]
     1+mid ⍬       ⍝ capsule line [7]
 }                 ⍝ capsule line [8]
 1+outer ⍬
      Main
DOMAIN ERROR: Divide by zero
outer[3] ÷0    ⍝ capsule line [3]
         ∧
      )SI
#.inner[3]*
#.outer[5]
#.outer[7]
#.Main[10]
```

## Signalling Events

[`⎕SIGNAL`](../../../language-reference-guide/system-functions/signal.md) cuts the state indicator back to exit the capsule that contains the line that invoked it, so the event is reported where that capsule was called. Using the functions defined above, `callee` is exited, and the event is reported in `caller`, whereas `container` is exited as a whole, because `helper` is part of it:

```apl
      caller 1
DOMAIN ERROR
caller[0] caller←{1+callee ⍵}
                    ∧
      container 1
DOMAIN ERROR
      container 1
      ∧
```

This means that when a capsule is called from within a tradfn, the event is reported in the tradfn, where a [`:Trap`](../traditional-functions-and-operators/control-structures/trap.md) control structure or [`⎕TRAP`](../../../language-reference-guide/system-functions/trap.md) can trap it.

## Cutting Back to a Capsule

When execution is suspended in a dfn that is nested in a capsule, the **&lt;CA&gt;** (Cut to capsule) action cuts the state indicator back to the capsule's outermost dfn, leaving it suspended at the line that led to the nested call. When execution is suspended in the capsule's outermost dfn, **&lt;CA&gt;** has no effect. In `Main` above, **&lt;CA&gt;** removes `inner` and `mid`:

```apl
      )SI
#.outer[7]*
#.Main[10]
```


- **&lt;CA&gt;** has no keystroke by default. In Microsoft Windows, you can assign one on the [**Keyboard Shortcuts** tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog.md#keyboard-shortcuts-tab) of the **Configuration** dialog box, or invoke the action from the Session by sending the key press to the session object with [`⎕NQ`](../../../language-reference-guide/system-functions/nq.md):


```apl
      2 ⎕NQ ⎕SE 'KeyPress' 'CA'
```

Other ways of cutting back the state indicator work by level, not by capsule:

- [_Abort_ (`→`)](../../../language-reference-guide/other-syntax/abort.md) clears the most recently suspended statement and all of its pendent statements, which in `Main` means every level, including `Main` itself.
- [`)RESET n`](../../../language-reference-guide/system-commands/reset.md) removes the top `n` levels of the state indicator, irrespective of the functions that they belong to, and leaves execution suspended at the level below them. In `Main`, `)RESET 1` removes only `inner`:

```apl
      )RESET 1
      )SI
#.mid[5]*
#.outer[7]
#.Main[10]
```

## Error-Guards

Capsules do not limit [error-guards](error-guards.md). An error-guard applies to errors in all of the functions that are called while it is in effect, including dfns in other capsules and tradfns:

```apl
guarded←{
    11::'caught'
    1+divide ⍵
}
divide←{
    ÷⍵
}
```

```apl
      guarded 0
caught
```
