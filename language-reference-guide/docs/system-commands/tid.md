




<h1 class="heading"><span class="name">Thread Identity</span> <span class="command">)TID {tid}</span></h1>



`)TID` associates the Session window with the specified thread so that expressions that you subsequently execute in the Session are executed in the context of that thread.


If you attempt to `)TID` to a thread that is paused or running, that thread will, if possible, be interrupted by a strong interrupt. If the thread is in a state which it would be inappropriate to interrupt (for example, if the thread is executing an external function), the system reports:
```
      Can't switch, this thread is n
```


If no thread number is given, `)TID` reports the number of the current thread.


<h2 class="example">Examples</h2>
```apl
      ⍝ State indicator
      )SI
·   #.print[1]
&3
·   ·   #.sub_calc[2]*
·   &2
·   #.calc[1]
&1
 
      ⍝ Current thread
      )TID
is 2
 
      ⍝ Switch suspension to thread 3
      )TID 3
was 2
 
      ⍝ State indicator
      )SI
·   #.print[1]*
&3
·   ·   #.sub_calc[2]
·   &2
·   calc[1]
&1
 
      ⍝ Attempt to switch to pendent thread 1
      )TID 1
Can't switch, this thread is 3
```


