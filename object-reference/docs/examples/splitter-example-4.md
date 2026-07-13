---
search:
  exclude: true
---

# <span>Splitter</span> <span>Example 4</span>


```apl
'F'⎕WC'Form' 'Multiple Splitters: non-hierarchical'('Size' 25 50)
'F.E1'⎕WC'Edit'(10 6⍴'Edit 1')('Style' 'Multi')
'F.E2'⎕WC'Edit'(10 6⍴'Edit 2')('Style' 'Multi')
'F.E3'⎕WC'Edit'(10 6⍴'Edit 3')('Style' 'Multi')
'F.S1'⎕WC'Splitter' 'F.E1'
'F.S2'⎕WC'Splitter' 'F.E2' 'F.E3'
```


![](../img/split4.gif)


![](../img/split4a.gif)


After dragging the first Splitter to the left.


