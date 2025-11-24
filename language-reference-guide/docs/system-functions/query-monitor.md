---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕MONITOR MONITOR
</div>






<h1 class="heading"><span class="name">Query Monitor</span> <span class="command">R←⎕MONITOR Y</span></h1>



`Y` must be a simple character scalar or vector which is taken to be the name of a visible defined function or operator.


Note that `⎕MONITOR` does not apply to  dfns or dops.


`R` is a simple non-negative integer matrix of 5 columns with one row for each line in the function or operator `Y` which has the monitor set, giving:


|--------|-------------------------------------|
|Column 1|Line number                          |
|Column 2|Number of times the line was executed|
|Column 3|CPU time in milliseconds             |
|Column 4|Elapsed time in milliseconds         |
|Column 5|Reserved                             |


The value of `0` in column one indicates that the monitor is set on the function or operator as a whole. `R` will be empty for dfns and dops.


<h2 class="example">Example</h2>
```apl
      ∇ FOO
[1]   A←?25 25⍴100
[2]   B←⌹A
[3]   C←⌹B
[4]   R1←⌊0.5+A+.×B
[5]   R2←A=C
      ∇
 
      (0,⍳5) ⎕MONITOR 'FOO' ⍝ Set monitor
 
      FOO                   ⍝ Run function
 
      ⎕MONITOR 'FOO'        ⍝ Monitor query
0 1 1418 1000 0
1 1   83    0 0
2 1  400    0 0
3 1  397    0 0
4 1  467 1000 0
5 1  100    0 0
```


