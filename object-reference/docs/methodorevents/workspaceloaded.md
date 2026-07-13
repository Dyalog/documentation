---
search:
  exclude: true
---

# <span>WorkspaceLoaded</span> <span>Event 525</span>



**Applies To:** [Session](../../../windows-ui-guide/the-session-object/session-object)

**Description**


If enabled, this event is reported when a workspace is loaded or on a `clear ws`. You may not nullify or modify the event with a 0-returning callback, nor may you generate the event using `⎕NQ`, or call it as a method.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 2-element vector as follows :


|-----|------|--------------------------|
|`[1]`|Object|ref or character vector   |
|`[2]`|Event |`'WorkspaceLoaded'` or 525|


This event is fired immediately after a workspace has been loaded and before the execution of `⎕LX`.


The callback function you attach should be defined in `⎕SE`.



