




# <span>For Statement</span> `:For var :In[Each] aexp`



[Formal Definition](for-statement-definition.md){: .noprint }

## Single Control Variable


The `:For` loop is used to execute a block of code for a series of values of a particular control variable.  For example, the following would execute lines `[2-3]` successively for values of `I` from 3 to 5 inclusive:
```apl
[1]   :For I :In 3 4 5
[2]       expr1 I
[3]       expr2 I
[4]   :EndFor
```



The way a `:For` loop operates is as follows.  On encountering the `:For`, the expression to the right of `:In` is evaluated and the result stored.  This is the *control array*.  The *control variable*, named to the right of the `:For`, is then assigned the first value in the control array, and the code between `:For` and `:EndFor` is executed.  On encountering the `:EndFor`, the control variable is assigned the next value of the control array and execution of the code is performed again, starting at the first line after the `:For`.  This process is repeated for each value in the control array.


Note that if the control array is empty, the code in the `:For` structure is not executed.  Note too that the control array may be any rank and shape, but that its elements are assigned to the control variable in ravel order.


The control array may contain any type of data.  For example, the following code resizes (and compacts) all your component files
```apl
[1]   :For FILE :In (↓⎕FLIB '')~¨' '
[2]       FILE ⎕FTIE 1
[3]       ⎕FRESIZE 1
[4]       ⎕FUNTIE 1
[5]   :EndFor
```


You may also nest `:For` loops.  For example, the following expression finds the timestamp of the most recently updated component in all your component files.
```apl
[1]   TS←0
[2]   :For FILE :In (↓⎕FLIB '')~¨' '
[3]       FILE ⎕FTIE 1
[4]       START END←2⍴⎕FSIZE 1
[5]       :For COMP :In (START-1)↓⍳END-1
[6]           TS⌈←¯1↑⎕FREAD FILE COMP
[7]       :EndFor
[8]       ⎕FUNTIE 1
[9]   :EndFor
```

## Multiple Control Variables


The `:For` control structure can also take multiple variables. This has the effect of doing a strand assignment each time around the loop.


For example `:For a b c :in (1 2 3)(4 5 6)`, sets `a b c←1 2 3`, first time around the loop and `a b c←4 5 6`, the second time.


Another example is `:For i j :In ⍳⍴Matrix`, which sets `i` and `j` to each row and column index of `Matrix`.


## :InEach Control Word
```apl
      :For var ... :InEach value ...
```


In a `:For` control structure, the keyword `:InEach` is an alternative to `:In`.


For a single control variable, the effect of the keywords is identical but for multiple control variables the values vector is inverted.



The distinction is best illustrated by the following equivalent examples:
```apl
      :For a b c :In (1 2 3)(3 4 5)(5 6 7)(7 8 9)
          ⎕←a b c
      :EndFor
 
      :For a b c :InEach (1 3 5 7)(2 4 6 8)(3 5 7 9)
           ⎕←a b c
      :EndFor
```


In each case, the output from the loop is:
```apl
1 2 3
3 4 5
5 6 7
7 8 9
```


Notice that in the second case, the number of items in the values vector is the same as the number of control variables. A more typical example might be.
```apl
      :For a b c :InEach avec bvec cvec
          ...
      :EndFor
```


Here, each time around the loop, control variable `a` is set to the next item of `avec`, `b` to the next item of `bvec` and `c` to the next item of `cvec`.


