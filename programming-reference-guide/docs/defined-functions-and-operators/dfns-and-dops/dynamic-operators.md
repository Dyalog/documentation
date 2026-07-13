# Dops

The operator equivalent of a dfn is distinguished by the presence of  either of the compound symbols `⍺⍺` or `⍵⍵` anywhere in its definition.

The syntax of a dop is:

- monadic – `⍺ (⍺⍺ op) ⍵`
- dyadic –  `⍺ (⍺⍺ op ⍵⍵) ⍵` 

where `⍺⍺` and `⍵⍵` are the left and right operands (functions or arrays) respectively, and `⍺` and `⍵` are the arguments of the derived function.

<h2 class="example">Example</h2>

The following monadic `each` operator applies its function operand only to unique elements of its argument. It then distributes the result to match the original argument. This can deliver a performance improvement over the primitive each (`¨`) operator if the operand function is costly and the argument contains a significant number of duplicate elements. Note however, that if the operand function causes side effects, the operation of dop and primitive versions will be different.
```apl
      each←{              ⍝ Fast each:                           
          shp←⍴⍵          ⍝ Shape and ...                        
          vec←,⍵          ⍝ ... ravel of arg.                    
          nub←∪vec        ⍝ Vector of unique elements.           
          res←⍺⍺¨nub      ⍝ Result for unique elts.              
          idx←nub⍳vec     ⍝ Indices of arg in nub ...
          shp⍴idx⊃¨⊂res   ⍝ ... distribute result.
      }
```

The dyadic `else` operator applies its left (else right) operand to its right argument depending on its left argument.
```apl
      else←{
          ⍺: ⍺⍺ ⍵     ⍝ True: apply Left operand
             ⍵⍵ ⍵     ⍝ Else,  ..   Right   ..
      }
      0 1 ⌈else⌊¨ 2.5     ⍝ Try both false and true.
2 3
```
