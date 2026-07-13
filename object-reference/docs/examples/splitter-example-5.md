---
search:
  exclude: true
---

# <span>Splitter</span> <span>Example 5</span>


```apl
'F'⎕WC'Form' 'Combining Horizontal and Vertical Splitters'
'F.E1'⎕WC'Edit'(20 6⍴'Edit 1')('Style' 'Multi')
'F.E2'⎕WC'Edit'(10 6⍴'Edit 2')('Style' 'Multi')
'F.E3'⎕WC'Edit'(10 6⍴'Edit 3')('Style' 'Multi')
'F.E4'⎕WC'Edit'(5 6⍴'Edit 4')('Style' 'Multi')
'F.E5'⎕WC'Edit'(5 6⍴'Edit 5')('Style' 'Multi')

'F.S1'⎕WC'Splitter' 'F.E1'('Style' 'Vert')
'F.S2'⎕WC'Splitter' 'F.E2'('Style' 'Horz')
'F.S3'⎕WC'Splitter' 'F.E3'('Style' 'Vert')
'F.S4'⎕WC'Splitter' 'F.E4' 'F.E5'('Style' 'Horz')
```


![](../img/split5.gif)


