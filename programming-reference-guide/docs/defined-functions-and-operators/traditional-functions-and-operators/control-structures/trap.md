

# <span>Trap Statement</span> `:Trap ecode`

[Formal Definition](trap-statement-definition.md){: .noprint }

`:Trap` is an error trapping mechanism that can be used in conjunction with, or as an alternative to, the `⎕TRAP` system variable. It is equivalent to APL2's `⎕EA`, except that the code to be executed is not restricted to a single expression and is not contained within quotes (and so is slightly more efficient).

`ecode` is an integer scalar or vector containing the list of event codes which are to be *handled* during execution of the segment of code between the `:Trap` and `:End[Trap]` statements. Note that event codes 0 and 1000 are wild cards that means *any* event code in a given range. See [APL Error Messages](../../../error-messages/apl-errors.md).

## Operation

The segment of code immediately following the `:Trap` keyword is executed. On completion of this segment, if no error occurs, control passes to the code following `:End[Trap]`.

If an error occurs which is not specified by `ecode`, it is processed by outer `:Trap`s,   `⎕TRAP`s, or by the default system processing in the normal fashion.

If an error occurs, whose event code matches `ecode:`

- If the error occurred within a sub-function, the system cuts the state indicator back to the function containing the `:Trap` keyword. In this respect, `:Trap` behaves like `⎕TRAP` with a `'C'` qualifier.
- If the `:Trap` segment contains a `:Case[List] ecode` statement whose `ecode` matches the event code of the error that has occurred, execution continues from the statement following that `:Case[List] ecode`.
- Otherwise, if the `:Trap` segment contains a `:Else` statement, execution continues from the first statement following the `:Else` statement. 
- Otherwise, execution continues from the first statement following the `:End[Trap]` and no error processing occurs.

Note that the error trapping is in effect **only** during execution of the initial code segment. When a trapped error occurs, further error trapping is immediately disabled (or surrendered to outer level `:Trap`s or `⎕TRAP`s). In particular, the error trap is no longer in effect during processing of `:Case[List]`'s argument or in the code following the `:Case[List]` or `:Else` statement. This avoids the situation sometimes encountered with `⎕TRAP` where an infinite "trap loop" occurs.

Note that the statement  `:Trap ⍬` results in no errors being trapped.

<h2 class="example">Examples</h2>
```apl
     ∇ lx
[1]    :Trap 1000        ⍝ Cutback and exit on interrupt
[2]        Main ...
[3]    :EndTrap
     ∇

     ∇ ftie←Fcreate file        ⍝ Create null component file
[1]    :Trap 22                 ⍝ Trap FILE NAME ERROR
[2]        ftie←file ⎕FCREATE 0 ⍝ Try to create file.
[3]    :Else
[4]        ftie←file ⎕FTIE 0    ⍝ Tie the file.
[5]        file ⎕FERASE ftie    ⍝ Drop the file.
[6]        file ⎕FCREATE ftie   ⍝ Create new file.
[7]    :EndTrap
     ∇

 
     ∇ lx ⍝ Distinguish various cases
[1]    :Trap 0 1000 
[2]        Main ... 
[3]    :Case 1002 
[4]        'Interrupted ...' 
[5]    :CaseList 1 10 72 76 
[6]        'Not enough resources' 
[7]    :CaseList 17+⍳20 
[8]        'File System Problem' 
[9]    :Else 
[10]       'Unexpected Error' 
[11]   :EndTrap 
     ∇
```

Note that `:Trap`s can be nested:
```apl
     ∇ ntie←Ntie file                    ⍝ Tie native file
[1]    :Trap 22                          ⍝ Trap FILE NAME ERROR
[2]        ntie←file ⎕NTIE 0             ⍝ Try to tie file
[3]    :Else
[4]        :Trap 22                      ⍝ Trap FILE NAME ERROR
[5]            ntie←(file,'.txt')⎕NTIE 0 ⍝ Try with .txt extn
[6]        :Else
[7]            ntie←file ⎕NCREATE 0      ⍝ Create null file.
[8]        :EndTrap
[9]    :EndTrap
     ∇

```
