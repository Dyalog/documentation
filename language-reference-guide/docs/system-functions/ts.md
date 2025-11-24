---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕TS TS
</div>






<h1 class="heading"><span class="name">Timestamp</span> <span class="command">R←⎕TS</span></h1>



This is a seven element vector which identifies the clock time set on the particular installation as follows:


|--------|-----------|
|`⎕TS[1]`|Year       |
|`⎕TS[2]`|Month      |
|`⎕TS[3]`|Day        |
|`⎕TS[4]`|Hour       |
|`⎕TS[5]`|Minute     |
|`⎕TS[6]`|Second     |
|`⎕TS[7]`|Millisecond|


<h2 class="example">Example</h2>
```apl
      ⎕TS
1989 7 11 10 42 59 123
```


Note that on some systems, where time is maintained only to the nearest second, a zero is returned for the seventh (millisecond) field.


