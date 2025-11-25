---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ 
</div>






<h1 class="heading"><span class="name">Evaluated Input/Output</span> <span class="command">⎕</span></h1>



`⎕` is a variable which communicates between the user's terminal and APL.  Its behaviour depends on whether it is being assigned or referenced.


When `⎕` is assigned an array, the array is displayed at the terminal in exactly the same form as is direct output (see [Programmer's Guide: "Display of Arrays"](../../../programming-reference-guide/introduction/arrays/display-of-arrays)).


<h2 class="example">Example</h2>
```apl
      ⎕←2+⍳5
3 4 5 6 7
 
      ⎕←2 4⍴'WINEMART'
WINE
MART
```


When `⎕` is referenced, a prompt (`⎕:`) is displayed at the terminal, and input is requested.  The response is evaluated and an array is returned if the result is valid.  If an error occurs in the evaluation, the error is reported as normal (unless trapped by a `⎕TRAP` definition) and the prompt (`⎕:`) is again displayed for input.  An EOF interrupt reports `INPUT INTERRUPT` and the prompt (`⎕:`) is again displayed for input.  A soft interrupt is ignored and a hard interrupt reports `INTERRUPT` and the prompt (`⎕:`) is redisplayed for input.

<h2 class="example">Examples</h2>
```apl
      10×⎕+2
⎕:
      ⍳3
30 40 50
 
      2+⎕
⎕:
      X
VALUE ERROR
      X
     ^
⎕:
      2+⍳3
5 6 7
```



A system command may be entered.  The system command is effected and the prompt is displayed again (unless the system command changes the environment):
```apl
      ⍴3,⎕
⎕:
      )WSID
WS/MYWORK
⎕:
      )SI
⎕
⎕:
      )CLEAR
CLEAR WS
```




If the response to a `⎕:` prompt is an abort statement (`→`), the execution will be aborted:
```apl
      1 2 3 = ⎕
⎕:
      →
```



A trap definition on interrupt events set for the system variable `⎕TRAP` in the range 1000-1008 has no effect whilst awaiting input in response to a `⎕:` prompt.

<h2 class="example">Example</h2>
```apl
      ⎕TRAP←(11 'C' '''ERROR''')(1000 'C' '''STOP''')
 
      2+⎕
⎕:
      (Interrupt Signal)
INTERRUPT
⎕:
      'C'+2
ERROR
```


A time limit set in system variable `⎕RTL` has no effect whilst awaiting input in response to a `⎕:` prompt.


