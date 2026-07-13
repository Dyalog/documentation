---
search:
  exclude: true
---

# <span>Format</span> <span>Event 821</span>



**Applies To:** [Editor](../../../windows-ui-guide/the-session-object/session-object)

**Description**


If enabled, this event is reported when the user attempts to format an object in the Editor window.


If the callback function returns 0, the contents of the Edit window are not reformatted.


You may not generate the event using `⎕NQ`, or call it as a method.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 6-element vector as follows :


|-----|--------|----------------------------------------------------------------------------------------------------|
|`[1]`|Object  |ref to the Editor object                                                                            |
|`[2]`|Event   |`'Format'` or 821                                                                                   |
|`[3]`|Contents|the contents of the Edit window, as a vector of character vectors                                   |
|`[4]`|Space   |ref to the namespace in which the object will be fixed                                              |
|`[5]`|Old Name|a character vector containing the original name of the object when it was opened by the Editor      |
|`[6]`|New Name|a character vector containing the new name of the object. This is empty if the object is a variable.|



