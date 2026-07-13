# <span>LWidth</span> <span>Property</span>



**Applies To:** [Circle](../objects/circle.md), [Ellipse](../objects/ellipse.md), [Poly](../objects/poly.md), [Rect](../objects/rect.md)

**Description**


This property determines the width of line used to draw a graphics object. A positive value specifies the line width in pixels. A negative value specifies line width in units of the co-ordinate system defined for the object in the x direction. If the object contains more than one component, LWidth may be a vector.


In versions of Dyalog prior to v13.2 revision 19489, if LWidth specified a line width greater than 1 pixel, a solid line was drawn in the colour specified by the FCol Property, regardless of the value of [LStyle](lstyle.md). From that revision onwards, if the value of LWidth is greater than 1  then the value of LStyle is honoured, but only the FCol of the line is honoured - the BCol is still ignored.



