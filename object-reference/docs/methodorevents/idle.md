# <span>Idle</span> <span>Event 130</span>

**Applies To:** [Root](../objects/root.md)

**Description**

If enabled, this event is generated whenever APL looks to see if there is an event on the queue and finds it empty. Its purpose is to allow an application to perform some background processing when the user is not doing anything. It is unwise to use this event directly from the Session as it will occur repeatedly and may lock you out.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function is a 2-element vector as follows:

|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'Idle'` or 130        |
