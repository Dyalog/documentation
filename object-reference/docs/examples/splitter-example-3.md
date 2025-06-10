---
search:
  exclude: true
---

<h1 class="heading"><span class="name">Splitter</span> <span class="right">Example 3</span></h1>


```apl
'F'⎕WC'Form' 'Multiple Splitters: hierarchical using SubForms'('Size' 25 50)
'F.E1'⎕WC'Edit'(10 6⍴'Edit 1')('Style' 'Multi')
'F.SF1'⎕WC'SubForm'('EdgeStyle' 'Default')
'F.S1'⎕WC'Splitter' 'F.E1' 'F.SF1'
'F.SF1.E1'⎕WC'Edit'(10 6⍴'Edit 2')('Style' 'Multi')
'F.SF1.E2'⎕WC'Edit'(10 6⍴'Edit 3')('Style' 'Multi')
'F.SF1.S1'⎕WC'Splitter' 'F.SF1.E1' 'F.SF1.E2'
```


![](../img/split3.gif)


![](../img/split3a.gif)


After dragging the first Splitter to the left.


