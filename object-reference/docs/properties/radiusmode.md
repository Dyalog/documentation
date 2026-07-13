# <span>RadiusMode</span> <span>Property</span>



**Applies To:** [Circle](../objects/circle.md), [Root](../objects/root.md)

**Description**


A perfectly round circle can only be drawn if the diameter is an odd number of pixels. The RadiusMode property specifies whether or not a circle is adjusted by a single pixel, if necessary, so as to appear perfectly round.


If RadiusMode is 1 or `¯1`, and the diameter is an even number of pixels, the circle is actually drawn with a diameter of 1 pixel more or less than specified. If RadiusMode is 0 (the default), no such adjustment is made.


RadiusMode may be set on the Root object to be inherited by all Circle objects.



