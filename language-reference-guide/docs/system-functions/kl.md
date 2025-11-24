---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕KL KL
</div>






<h1 class="heading"><span class="name">Key Label</span> <span class="command">R←⎕KL Y</span></h1>



`Y` is a simple character vector or a vector of character vectors containing Input Codes for Keyboard Shortcuts. In the Classic Edition, keystrokes are associated with Keyboard Shortcuts by the Input Translate Table.


`R` is a simple character vector or a vector of character vectors containing the labels associated with the codes.  If `Y` specifies codes that are not defined, the corresponding elements of `R` are the codes in `Y`.


`⎕KL` provides the information required to build device-independent help messages into applications, particularly full-screen applications using `⎕SM` and `⎕SR`.

<h2 class="example">Examples</h2>
```apl
      ⎕KL 'RC'
Right
 
      ⎕KL 'ER' 'EP' 'QT' 'F1' 'F13'
  Enter  Esc  Shift+Esc  F1  Shift+F1
```



