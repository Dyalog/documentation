# Example Traps

## Dividing by Zero

Let's try setting a `⎕TRAP` on `DOMAIN ERROR`:
```apl
         MSG←'''Please give a non-zero right arg'''
         ⎕TRAP←11 'E' MSG
```

When we enter:
```apl
         10÷0
```

APL executes the expression, and notes that it causes an error number 11. Before issuing the standard error, it scans its `⎕TRAP` table, to see if you were interested enough in that error to set a trap; you were, so APL executes the action specified by you:
```apl
         10÷0
   Please give non-zero right arg
```

Let's reset our `⎕TRAP`:
```apl
         ⎕TRAP←0⍴⎕TRAP        ⍝ No traps now set
```

and write a defined function to take the place of the primitive function `÷`:
```apl
       ∇ R←A DIV B
   [1]   R←A÷B
   [2] ∇
```

Then run it:
```apl
         10 DIV 0
   DOMAIN ERROR
         DIV[1] R←A÷B
                ^
```

Let's edit our function, and include a localised `⎕TRAP`:
```apl
       ∇ R←A DIV B;⎕TRAP
   [1] ⍝ Set the trap
   [2]   ⎕TRAP←11 'E' '→ERR1'
   [3] ⍝ Do the work; if it results in error 11,
   [4] ⍝ execute the trap
   [5]   R←A÷B
   [6] ⍝ All OK if we got to here, so exit
   [7]   →0
   [8] ⍝ Will get here only if error 11 occurred
   [9] ERR1:'Please give a non-zero right arg'
       ∇
```

Running the function with good and bad arguments has the desired effect:
```apl
         10 DIV 2
   5
```
```apl
         10 DIV 0
   Please give a non-zero right arg
```

`⎕TRAP` is a variable like any other, and since it is localised in `DIV`, it is only effective in `DIV` and any other functions that may be called by `DIV`. So
```apl
        10÷0
   DOMAIN ERROR
        10÷0
       ^
```

still gives an error, since there is no trap set in the global environment.

## Other Errors

What happens to our function if we run it with other duff arguments:
```apl
         1 2 3 DIV 4 5
   LENGTH ERROR
   DIV [4] R←A÷B
            ^
```

Here is an error that we have taken no account of.

Change `DIV` to take this new error into account:
```apl
       ∇ R←A DIV B;⎕TRAP
  [1]  ⍝ Set the trap
  [2]    ⎕TRAP←(11 'E' '→ERR1')(5 'E' '→ERR2')
  [3]  ⍝ Do the work; if it results in error 11,
  [4]  ⍝ execute the trap
  [5]    R←A ÷ B
  [6]  ⍝ All OK if we got to here, so exit
  [7]    →0
  [8]  ⍝ Will get here only if error 11 occurred
  [9]  ERR1:'Please give a non-zero right arg'⋄→0
  [10] ⍝ Will get here only if error 5 occurred
  [11] ERR2:'Arguments must be same length'
       ∇
```
```apl
         )RESET
```
```apl
         1 2 3 DIV 4 5
   Arguments must be the same length
```

But here's yet another problem that we didn't think of:
```apl
        (2 3⍴⍳6) DIV (2 3 4⍴⍳24)
   RANK ERROR
   DIV [4] R←A÷B
            ^
```

## Global Traps

Often when we are writing a system, we can't think of everything that may go wrong ahead of time; so we need a way of catching "everything else that I may not have thought of". The error number used for "everything else" is zero:
```apl
         )RESET
```

Set a global trap:
```apl
         ⎕TRAP ← 0 'E' ' ''Invalid arguments'' '
```

And run the function:
```apl
         (2 3⍴⍳6) DIV (2 3 4⍴⍳24)
   Invalid arguments
```

In this case, when APL executed line 4 of our function `DIV`, it encountered an error number 4 (`RANK ERROR`). It searched the local trap table, found nothing relating to error 4, so searched further up the stack to see if the error was mentioned anywhere else. It found an entry with an associated Execute code, so executed the appropriate action AT THE POINT THAT THE ERROR OCCURRED. Let's see what's in the stack:
```apl
         )SI
   DIV[4]*
```
```apl
         ↑⎕DM
   RANK ERROR
   DIV[4] R←A÷B
           ^
```

So although our action has been taken, execution has stopped where it normally would after a `RANK ERRO`R.

## Dangers

We must be careful when we set global traps; let's call the non-existent function BUG whenever we get an unexpected error:
```apl
         )RESET
         ⎕TRAP ← 0 'E' 'BUG'
         (2 3⍴⍳6) DIV (2 3 4⍴⍳24)
```

Nothing happens, since APL traps a `RANK ERROR` on line 4 of `DIV`, so executes the trap statement, which causes a `VALUE ERROR`, which activates the trap action, which causes a `VALUE ERROR`, which .... etc. etc. If we had also chosen to trap on 1000 (ALL INTERRUPTS), then we'd be in trouble!

Let's define a function `BUG`:
```apl
       ∇ BUG
   [1] ⍝ Called whenever there is an unexpected error
   [2]   '*** UNEXPECTED ERROR OCCURRED IN: ',⊃1↓⎕SI
   [3]   '*** PLEASE CALL YOUR SYSTEM ADMINISTRATOR'
   [4]   '*** WORKSPACE SAVED AS BUG.',⊃1↓⎕SI
   [5]   ⍝ Tidy up ... reset ⎕LX, untie files ... etc
   [6]   ⎕SAVE 'BUG.',⊃1↓⎕SI
   [7]   '*** LOGGING YOU OFF THE SYSTEM'
   [8]   ⎕OFF
       ∇
```

Now, whenever we run our system and an unexpected error occurs, our `BUG` function will be called.
```apl
         10 DIV 0
   Please give non-zero right arg
```
```apl
         (2 3⍴⍳6) DIV (2 3 4⍴⍳12)
```
```apl
   *** UNEXPECTED ERROR OCCURRED IN: DIV
   *** PLEASE CALL YOUR SYSTEM ADMINISTRATOR'
   *** WORKSPACE SAVED AS BUG.DIV
   *** LOGGING YOU OFF THE SYSTEM'
```

The system administrator can then load BUG.DIV, look at the SI stack, discover the problem, and fix it.

## Looking out for Specific Problems

In many cases, you can of course achieve the same effect of a trap by using APL code to detect the problem before it happens. Consider the function `TIE∆FILE`, which checks to see if a file already exists before it tries to access it:
```apl
       ∇ R←TIE∆FILE FILE;FILES
   [1]  ⍝ Tie file FILE with next available tie number
   [2]  ⍝
   [3]  ⍝ All files in my directory
   [4]    FILES←⎕FLIB 'mydir'
   [5]  ⍝ Remove trailing blanks
   [6]    FILES←dbr¨↓FILES
   [7]  ⍝ Required file in list?
   [8]    →ERR×⍳~(⊂FILE)∊FILES
   [9]  ⍝ Tie file with next number
   [10]   FILE ⎕FTIE R←1+⌈/0,⎕FNUMS
   [11] ⍝ ... and exit
   [12]    →0
   [13] ⍝ Error message
   [14]  ERR:R←'File does not exist'
       ∇
```

This function executes the same code whether the file name is right or wrong, and it could take a while to get all the file names in your directory. It would be neater, and more efficient to take action ONLY when the file name is wrong:
```apl
       ∇ R←TIE∆FILE FILE;⎕TRAP
   [1] ⍝ Tie file FILE with next available tie number
   [2] ⍝
   [3] ⍝ Set trap
   [4]   ⎕TRAP←22 'E' '→ERR'
   [5] ⍝ Tie file with next number
   [6]   FILE ⎕FTIE R←1+⌈/0,⎕FNUMS
   [7] ⍝ ... and exit if OK
   [8]   →0
   [9] ⍝ Error message
   [10]  ERR:R←'File does not exist'
```

## Cut-Back versus Execute

Let us consider the effect of using Cut-Back instead of Execute. Consider the system illustrated below, in which the function `REPORT` gives the user the option of 4 reports to be generated:
```apl
             REPORT
                |
 .-------------------------.
 |          |      |       |
REP1      REP2    REP3    REP4
                   |
              .----.----.
              |    |    |
             ...  DIV  ...
```
```apl
       ∇  REPORT;OPTIONS;OPTION;⎕TRAP
   [1]  ⍝ Driver functions for report sub-system. If an
   [2]  ⍝ unexpected error occurs, take action in the
   [3]  ⍝ function where the error occurred
   [4]  ⍝
   [5]  ⍝ Set global trap
   [6]   ⎕TRAP←0 'E' 'BUG'
   [7]  ⍝ Available options
   [8]   OPTIONS←'REP1' 'REP2' 'REP3' 'REP4'
   [9]  ⍝ Ask user to choose
   [10] LOOP:→END×⍳0=⍴OPTION←MENU OPTIONS
   [11] ⍝ Execute relevant function
   [12]  ⍎OPTION
   [13] ⍝ Repeat until EXIT
   [14]  →LOOP
   [15] ⍝ Now end
   [16] END:
```

Suppose the user chooses `REP3`, and an unexpected error occurs in `DIV`. The good news is that the System Administrator gets a snapshot copy of the workspace that he can play about with:
```apl
         )LOAD BUG.DIV  ⍝ Load workspace
   saved ......
```
```apl
         )SI            ⍝ Where did error occur?
   DIV[4]*
   REP3[6]
   ⍎
   REPORT[7]

         ↑⎕DM           ⍝ What happened?
   RANK ERROR
   DIV[4] R←A÷B
           ^
         ∇              ⍝ Edit function on top of stack
   [0]R←A DIV B
   .........
```

The bad news is, our user is locked out of the whole system, even though it may only be `REP3` that has a problem. We can get around this by making use of the CUT-BACK action code.
```apl
      ∇ REPORT;OPTIONS;OPTION;⎕TRAP
   [1] ⍝ Driver functions for report sub-system. If an
   [2] ⍝ unexpected error occurs, cut the stack back
   [3] ⍝ to this function, then take action
   [4] ⍝
   [5] ⍝ Set global trap
   [6]  ⎕TRAP←0 'C' '→ERR'
   [7] ⍝ Available options
   [8]  OPTIONS←'REP1' 'REP2' 'REP3' 'REP4'
   [9] ⍝ Ask user to choose
  [10] LOOP:→END×⍳0=⍴OPTION←MENU OPTIONS
  [11] ⍝ Execute relevant function
  [12]  ⍎OPTION
  [13] ⍝ Repeat until EXIT
  [14]  →LOOP
  [15] ⍝ Tell user ...
  [16] ERR:MESSAGE'Unexpected error in',OPTION
  [17] ⍝ ... what's happening
  [18]  MESSAGE'Removing from list'
  [19] ⍝ Remove option from list
  [20]  OPTIONS←OPTIONS~⊂OPTION
  [21] ⍝ And repeat
  [22]  →LOOP
  [23] ⍝ End
  [24] END:
```

Suppose the user runs this version of `REPORT` and chooses `REP3`. When the unexpected error occurs in `DIV`, APL will check its trap specifications, and see that the relevant trap was set in `REPORT` with a cut-back code. APL therefore **cuts back the stack to the function in which the trap was localised, THEN takes the specified action**. Looking at the SI stack above, we can see that APL must jump out of `DIV`, then `REP3`, then `⍎`, to return to line 7 of `REPORT`; THEN it takes the specified action.
