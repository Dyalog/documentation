<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕LC LC
</div>

<h1 class="heading"><span class="name">Line Count</span> <span class="command">R←⎕LC</span></h1>

This is a simple vector of line numbers drawn from the state indicator. The most recently activated line is shown first. If a value corresponds to a defined function in the state indicator, it represents the current line number where the function is either suspended or pendent.

The value of `⎕LC` changes immediately upon completion of the most recently activated line, or upon completion of execution within `⍎` or `⎕`.  If a `⎕STOP` control is set, `⎕LC` identifies the line on which the stop control is effected. In the case where a stop control is set on line 0 of a defined function, the first entry in `⎕LC` is 0 when the control is effected.

The value of `⎕LC` in a clear workspace is the null vector.

<h2 class="example">Examples</h2>
```apl
      )SI
#.TASK1[5]*
⍎
#.BEGIN[3]
 
      ⎕LC
5 3
```
```apl

      →⎕LC
      ⎕LC
 
      ⍴⎕LC
0
```
