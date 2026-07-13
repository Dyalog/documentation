---
search:
  boost: 2
---

<div style="display: none;">
  →
</div>


# <span>Branch</span> `→Y`{{key}}

`Y` may be a scalar or vector which, if not empty, has a simple numeric scalar as its first element.  The function has no explicit result.  It is used to modify the normal sequence of execution of expressions or to resume execution after a statement has been interrupted. Branch is not in the function domain of operators.


The following distinct usages of the branch function occur:


|&nbsp; |Entered in a Statement in a Defined Function|Entered in Immediate Execution Mode                                           |
|-------|--------------------------------------------|------------------------------------------------------------------------------|
|`→LINE`|Continue with the specific line             |Restart execution at the specific line of the most recently suspended function|
|`→⍳0`  |Continue with the next expression           |No effect                                                                     |



In a defined function, if `Y` is non-empty then the first element in `Y` specifies a statement line in the defined function to be executed next.  If the line does not exist, then execution of the function is terminated.  For this purpose, line 0 does not exist.  (Note that statement line numbers are independent of the index origin `⎕IO`).


If `Y` is empty, the branch function has no effect.  The next expression is executed on the same line, if any, or on the next line if not.  If there is no following line, the function is terminated.


The `:GoTo` statement may be used in place of Branch in a defined function.

<h2 class="example">Example</h2>
```apl
     ∇ TEST
[1]    1
[2]    →4
[3]    3
[4]    4
     ∇
 
      TEST
1
4
```


In general it is better to branch to a LABEL than to a line number.  A label occurs in a statement followed by a colon and is assigned the value of the statement line number when the function is defined.

<h2 class="example">Example</h2>
```apl
     ∇ TEST
[1]    1
[2]    →FOUR
[3]    3
[4]   FOUR:4
     ∇

```



The previous examples illustrate unconditional branching. There are numerous APL idioms which result in conditional branching. Some popular idioms are identified in the following table:


|Branch Expression     |Comment                                                                                                                   |
|----------------------|--------------------------------------------------------------------------------------------------------------------------|
|`→TEST/L1`            |Branches to label `L1` if `TEST` results in 1 but not if `TEST` results in 0.                                             |
|`→TEST⍴L1`            |Similar to above.                                                                                                         |
|`→TEST↑L1`            |Similar to above.                                                                                                         |
|`→L1⍴⍨TEST`           |Similar to above.                                                                                                         |
|`→L1⌈⍳TEST`           |Similar to above but only if `⎕IO←→1` .                                                                                   |
|`→L1×⍳TEST`           |Similar to above but only if `⎕IO←→1` .                                                                                   |
|`→(L1,L2,L3)[N]`      |Unconditional branch to a selected label.                                                                                 |
|`→(T1,T2,T3)/L1,L2,L3`|Branches to the first selected label dependent on tests `T1` , `T2` , `T3` . If all tests result in 0, there is no branch.|
|`→N⌽L1,L2,L3`         |Unconditional branch to the first label after rotation.                                                                   |




A branch expression may occur within a statement including `⋄` separators:
```apl
[5]   →NEXT⍴⍨TEST ⋄ A←A+1 ⋄ →END
[6]  NEXT:
```


In this example, the expressions `'A←A+1'` and `'→END'` are executed only if `TEST` returns the value 1.  Otherwise control branches to label `NEXT`.



In immediate execution mode, the branch function permits execution to be continued within the most recently suspended function, if any, in the state indicator.  If the state indicator is empty, or if the argument `Y` is the empty vector, the branch expression has no effect.  If a statement line is specified which does not exist, the function is terminated.  Otherwise, execution is restarted from the beginning of the specified statement line in the most recently suspended function.

<h2 class="example">Example</h2>
```apl
     ∇ F
[1]   1
[2]   2
[3]   3
     ∇
 
      2 ⎕STOP'F'
      F
1
 
F[2]
      )SI
#.F[2]*
      →2
2
3
```



The system constant `⎕LC` returns a vector of the line numbers of statement lines in the state indicator, starting with that in the most recently suspended function.  It is convenient to restart execution in a suspended state by the expression:
```apl
      →⎕LC
```



