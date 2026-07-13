# <span>HideComment</span> <span>Event 224</span>



**Applies To:** [Grid](../objects/grid.md)

**Description**


If enabled, a HideComment event is generated just before a comment window is hidden as a result of the user moving the mouse-pointer away from a commented cell.


The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :


|-----|------|-----------------------|
|`[1]`|Object|ref or character vector|
|`[2]`|Event |`'HideComment'` or 224 |
|`[3]`|Row   |integer                |
|`[4]`|Column|integer                |


You may prevent the comment from being hidden by returning 0 as the result of a callback function.


Note that if the comment window relates to a row or column *title*, the value reported in element [3] or [4] of the event message is `¯1`.


Invoked as a method, HideComment is used to hide a comment that has previously been displayed by ShowComment. For example, the following expression hides the comment associated with the cell at row 2, column 1.
```apl
      F.G.HideComment 2 1
```


If HideComment is called with an argument of `⍬`, all comments are hidden.


