# <span>Start</span> <span>Property</span>

**Applies To:** [Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md)

**Description**

This property specifies one or more start-angles for an arc, pie-slice, or chord of a circle or ellipse. It may be used in conjunction with [End](end.md) which specifies end angles. Angles are measured counter-clockwise from the x-axis at the centre of the object.

If a single arc is being drawn, Start is a single number that specifies the start angle of the arc in radians `(0 ⍎> ○2)`. If multiple arcs are being drawn, Start is either a single number as before (the start angle for several concentric arcs) or a numeric vector with one element per arc.

If [End](end.md) is not specified, the default value of Start is 0. Otherwise, the default value of Start is `(0,¯1↓+\End)`.
