# <span>DDE</span> <span>Event 50</span>

**Description**

If enabled, a DDE event is generated whenever a DDE message is received by Dyalog APL. This will occur whenever a server notifies APL that the value of a shared variable has changed, and whenever a client application requests data from APL. If you have several shared variables, you can determine which of them has changed or whose value has been requested using `⎕SVS`.

This event **only** applies to the [Root](../objects/root.md) object ".", so to enable it you must execute one of the following statements :
```apl
      '.' ⎕WS 'Event' 50 1
      '.' ⎕WS 'Event' 50 fn
      '.' ⎕WS 'Event' 50 fn larg
```

The first statement would cause [`⎕DQ`](../../../language-reference-guide/system-functions/dq) to terminate on receipt of a DDE event. The second would cause it to call "`fn`" each time. The third would do likewise but the value in "`larg`" would be supplied as its left argument.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function is a 2-element vector as follows :

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'DDE'` or 50          |

!!! note
    Due to the nature of DDE "conversations" messages may be received when in fact no change in the value of any shared variables has occurred. Your application code must therefore be prepared to cater for this situation.

**Application**

Objects: [Root](../objects/root.md)
