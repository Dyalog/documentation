# <span>GoTo Statement</span> `:GoTo aexp`

A `:GoTo` statement is a direct alternative to `→` (branch) and causes execution to jump to the line specified by the first element of `aexp`.

The following are equivalent.  See [Branch](../../../../../language-reference-guide/other-syntax/branch) for further details.
```apl
      →Exit
      :GoTo Exit
 
      →(N<I←I+1)/End
      :GoTo (N<I←I+1)/End
 
      →1+⎕LC
      :GoTo 1+⎕LC
 
      →10
      :GoTo 10
```
