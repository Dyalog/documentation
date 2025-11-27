




<h1 class="heading"><span class="name">With Statement</span> <span class="command">:With obj</span></h1>



[Formal Definition](with-statement-definition.md){: .noprint }



`:With` is a control structure that may be used to simplify a series of references to an object or namespace. `:With` changes into the specified namespace for the duration of the control structure, and is terminated by `:End[With]`. `obj` is either the name of or a reference to a namespace. For example, you could update several properties of a Grid object `F.G` as follows:

```apl
       :With F.G
            Values←4 3⍴0
            RowTitles←'North' 'South' 'East' 'West'
            ColTitles←'Cakes' 'Buns' 'Biscuits'
       :EndWith
```




`:With` is analogous to `⎕CS` in  the following senses:

- The namespace argument to `:With` is interpreted relative to the current space.
- With the exception of those with name class `9`, local names in the containing defined function continue to be visible in the new space. Therefore any names in the new space that match local names in the containing defined function will be invisible.
- Names in the new space must not be localised in the containing defined function.
- Global references from within the `:With` control structure are to names in the new space. 
- Exiting the defined function from within a `:With` control structure causes the space to revert to the one from which the function was called.



On leaving the `:With` control structure, execution reverts to the original namespace. Notice however that the interpreter does not detect branches (`→`) out of the control structure. `:With` control structures can be nested in the normal fashion:
```apl
[1]   :With 'x'           ⍝ Change to #.x
[2]       :With 'y'       ⍝ Change to #.x.y
[3]           :With ⎕SE   ⍝ Change to ⎕SE
[4]               ...     ⍝ ... in ⎕SE
[5]           :EndWith    ⍝ Back to #.x.y
[6]       :EndWith        ⍝ Back to #.x
[7]   :EndWith            ⍝ Back to #
```


