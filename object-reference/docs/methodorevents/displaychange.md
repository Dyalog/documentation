# <span>DisplayChange</span> <span>Event 137</span>

**Applies To:** [Root](../objects/root.md)

**Description**

If enabled, this event is reported when the user changes the screen resolution or number of colours. The event is reported for information only; you cannot prevent the change from occurring.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 5-element vector as follows :

|-----|-----------------|--------------------------------------------|
|`[1]`|Object           |ref or character vector                     |
|`[2]`|Event            |`'DisplayChange'` or 137                    |
|`[3]`|Height           |Integer. Number of pixels in the y-direction|
|`[4]`|Width            |Integer. Number of pixels in the x-direction|
|`[5]`|Number of colours|Integer.                                    |
