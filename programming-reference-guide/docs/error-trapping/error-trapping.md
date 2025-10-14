<h1 class="heading"><span class="name">Error Trapping Concepts</span></h1>

The purpose of this section is to show some of the ways in which the ideas of error trapping can be used to great effect to change the flow of control in a system.

First, we must have an idea of what is meant by error trapping. We are all used to entering some duff APL code, and seeing a (sometimes) rather obscure, esoteric error message echoed back:
```apl
         10÷0
   DOMAIN ERROR
         10÷0
        ^
```

This message is ideal for the APL programmer, but not so for the end user. We need a way to bypass the default action of APL, so that we can take an action of our own, thereby offering the end user a more meaningful message.

Every error message reported by Dyalog APL has a corresponding error number (for a list of error codes and message, see `⎕TRAP`, Language Reference). Many of these error numbers plus messages are common across all versions of APL. We can see that the code for `DOMAIN ERROR` is 11, whilst `LENGTH ERROR` has code 5.

Dyalog APL provides two distinct but related mechanisms for the trapping and control of errors. The first is based on the control structure `:Trap ... :EndTrap`, and the second, on the system variable `⎕TRAP`. The control structure is easier to administer and so is recommended for normal use, while the system variable provides slightly finer control and may be necessary for specialist applications.

## Last Error number and Diagnostic Message

Dyalog APL keeps a note of the last error that occurred, and provides this information through system functions: `⎕EN`, `⎕EM` and `⎕DM`.
```apl
         10÷0
   DOMAIN ERROR
         10÷0
        ^
```

Error Number for last occurring error:
```apl
         ⎕EN
   11
```

Error Message associated with code 11:
```apl
         ⎕EM 11
   DOMAIN ERROR
```

`⎕DM` (Diagnostic Message) is a 3 element nested vector containing error message, expression and caret:
```apl
         ⎕DM
    DOMAIN ERROR         10÷0        ^
```

Use function `DISPLAY` to show structure:
```apl

         DISPLAY ⎕DM
   ┌→─────────────────────────────────────┐
   │ ┌→───────────┐ ┌→─────────┐ ┌→─────┐ │
   │ │DOMAIN ERROR│ │      10÷0│ │     ∧│ │
   │ └────────────┘ └──────────┘ └──────┘ │
   └∊─────────────────────────────────────┘
```

Mix (`↑`) of this vector produces a matrix that displays the same as the error message produced by APL:
```apl
         ↑⎕DM
    DOMAIN ERROR
         10÷0
        ^
```

## Error Trapping Control Structure

You can embed a number of lines of code in a `:Trap` control structure within a defined function.
```apl
   [1]   ...
   [2]   :Trap 0
   [3]       ...
   [4]       ...
   [5]   :EndTrap
   [6]   ...
```

Now, whenever *any* error occurs in one of the enclosed lines, or in a function called from one of the lines, processing stops immediately and control is transferred to the line following the `:EndTrap`. The 0 argument to `:Trap`, in this case represents any error. To trap only specific errors, you could use a vector of error numbers:
```apl
   [2]   :Trap 11 2 3
```

Notice that in this case, no extra lines are executed after an error. Control is passed to line `[6]` either when an error has occurred, *or* if all the lines have been executed without error. If you want to execute some code *only* after an error, you could re-code the example like this:
```apl
 
   [1]   ...
   [2]   :Trap 0
   [3]       ...
   [4]       ...
   [5]   :Else
   [6]       ...
   [7]       ...
   [8]   :EndTrap
   [9]   ...
```

Now, if an error occurs in lines `[3-4]`, (or in a function called from those lines), control will be passed immediately to the line following the `:Else` statement. On the other hand, if all the lines between `:Trap` and `:Else` complete successfully, control will pass out of the control structure to (in this case) line `[9]`.

The final refinement is that specific error cases can be accommodated using `:Case[List]` constructs in the same manner as the `:Select` control structure.
```apl
   [1]   :Trap 17+⍳21            ⍝ Component file errors.
   [2]       tie←name ⎕FTIE 0    ⍝ Try to tie file
   [3]       'OK'
   [4]   :Case 22
   [5]       'Can''t find ',name
   [6]   :CaseList 25+⍳13
   [7]       'Resource Problem'
   [8]   :Else
   [9]       'Unexpected Problem'
   [10]  :EndTrap
```

Note that `:Trap` can be used in conjunction with `⎕SIGNAL` described below.

Traps can be nested. In the following example, code in the inner trap structure attempts to tie a component file, and if unsuccessful, tries to create one. In either case, the tie number is then passed to function `ProcessFile`. If an error other than 22 (`FILE NAME ERROR`) occurs in the inner trap structure, or an error occurs in function `ProcessFile` (or any of its called function), control passes to line immediately to line `[9]`.
```apl
   [1]   :Trap 0
   [2]       :Trap 22
   [3]           tie←name ⎕FTIE 0
   [4]       :Else
   [5]           tie←name ⎕FCREATE 0
   [6]       :EndTrap
   [7]       ProcessFile tie 
   [8]   :Else
   [9]       'Unexpected Error'
   [10]  :EndTrap
```

## Trap System Variable: `⎕TRAP`

The second way of trapping errors is to use the system variable: `⎕TRAP`.

`⎕TRAP`, can be assigned a nested vector of **trap specifications**. Each trap specification is itself a nested vector, of length 3, with each element defined as:

|---------------------|---------------------------------------------------------------------------------------|
|list of error numbers|The error numbers we are interested in.                                                |
|action code          |Either `'E'` (Execute) or `'C'` (Cut Back). There are others, but they are seldom used.|
|action to be taken   |APL expression, usually a branch statement or a call to an APL function.               |

So a single trap specification may be set up as:
```apl
         ⎕TRAP←5 'E' 'ACTION1'
```

and a multiple trap specification as:
```apl
         ⎕TRAP←(5 'E' 'ACTION1')((1 2 3) 'C' 'ACTION2')
```

The action code `E` tells APL that you want your action to be taken in the function in which the error occurred, whereas the code `C` indicates that you want your action to be taken in the function where the `⎕TRAP` was *localised*. If necessary, APL must first travel back up the state indicator (cut-back) until it reaches that function.
