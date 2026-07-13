# <span>ArcMode</span> <span>Property</span>

**Applies To:** [Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md)

**Description**

This property determines how arcs are drawn. Its value is 0, 1 or 2.

|---|---------------------------------------------------------------------------------------------------|
|0  |only the arc is drawn                                                                              |
|1  |arcs define "arc segments", with a single straight line joining the two ends of the arc together   |
|2  |arcs define "pie segments", with lines drawn from the start and end points of the arc to the centre|

Note that the segments defined by ArcMode 1 and 2 may be filled (by setting [FStyle](fstyle.md)).
