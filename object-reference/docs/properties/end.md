# <span>End</span> <span>Property</span>



**Applies To:** [Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md)

**Description**


This property specifies one or more end-angles for an arc, pie-slice, or chord of a circle or ellipse. It may be used in conjunction with [Start](start.md) which specifies start angles. Angles are measured counter-clockwise from the x-axis at the centre of the object.


If a single arc is being drawn, End is a single number that specifies the end angle of the arc in radians `(0 ⍎> ○2)`. If multiple arcs are being drawn, End is either a single number as before (the end angle for several concentric arcs) or a numeric vector with one element per arc.


If [Start](start.md) is not specified, the default value of End is `○2`. Otherwise, the default value of End is `((¯1↓+\Start),○2)`.



