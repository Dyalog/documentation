---
search:
  exclude: true
---

<h1 class="heading"><span class="name">SessionTrace</span> <span class="right">Event 527</span></h1>



**Applies To:** [Session](../../../windows-ui-guide/the-session-object/session-object)



**Applies To:** [Session](../../../windows-ui-guide/the-session-object/session-object)

|[Session](../../../windows-ui-guide/the-session-object/session-object)|&nbsp;|&nbsp;|||

**Description**


If enabled, this event is reported when an expression is executed with trace control. See [Set Trace ](../../../language-reference-guide/system-functions/set-trace). Error messages and output from system commands do not generate this event.




The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :


|-----|-----------|--------------------------------|
|`[1]`|Object     |ref or character vector         |
|`[2]`|Event      |`'SessionTrace'` or 527         |
|`[3]`|Function   |Character vector ( `''` if none)|
|`[4]`|Line number|Numeric scalar ( `0` if none)   |



The attachment of a callback function intercepts and annuls the normal display of function name, line numbers and any value.


Note that this event may be extended in future; in particular the number of elements in the event message may be increased. You should therefore allow for such extensions in any code which refers to SessionTrace.


When the event is generated, the left argument of the callback function contains the result value of the expression, if any. The callback function may display this or any other value, using default output or by assignment to `⎕`. If so, this output will be processed normally, without generating any SessionTrace or [SessionPrint](sessionprint.md) events. If the callback fails to explicitly display anything, nothing will appear in the Session.


If the expression has no value, then the callback function will be called monadically. It is therefore required that the callback function is ambivalent (can be called both monadically and dyadically).

<h2 class="example">Example</h2>
```apl
      )CS ⎕SE
⎕SE
     ∇ {VAL}TimeStamp EV
[1]    ⍞←⎕TS(2↑2↓EV)
[2]    :If 0≠⎕NC'VAL'
[3]        ⍞←VAL
[4]    :EndIf
[5]    ⍞←⎕UCS 13
     ∇
     )CS
#
      '⎕SE'⎕WS'Event' 'SessionTrace' '⎕SE.TimeStamp'
```
```apl
     ∇ Foo
[1]     ⍝ just a comment
[2]    global←⎕A
     ∇

      1 2 ⎕TRACE'Foo'
      Foo
 2020 7 3 14 2 37 762   Foo  1 
 2020 7 3 14 2 37 763   Foo  2 ABCDEFGHIJKLMNOPQRSTUVWXYZ

```


The result (if any) of the callback function is ignored.


You may not disable the event (by setting its action to `¯1`), nor generate the event using `⎕NQ`, nor call it as a method.


