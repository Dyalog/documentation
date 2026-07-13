# <span>Create</span> <span>Event 34</span>

[**Applies To**](../methodoreventapplies/create.md)

**Description**


If enabled, this event is reported *after* an object has been created.
You may not nullify or modify the event with a 0-returning callback, nor may you
generate the event using `⎕NQ`, or call it
as a method.


The event message reported as the result of `⎕DQ`,
or supplied as the right argument to your callback function, is a 3-element
vector as follows :


|-----|------|------------------------------------------------------------------------------------|
|`[1]`|Object|ref or character vector                                                             |
|`[2]`|Event |`'Create'` or 34                                                                    |
|`[3]`|Flag  |1 = object was created by `⎕WC` 0 = object was created by `)LOAD` , `)COPY` or `⎕OR`|


This event also applies to the Session object `⎕SE` and may be used to fire a start-up function (in the `⎕SE` namespace) when APL initialises.



