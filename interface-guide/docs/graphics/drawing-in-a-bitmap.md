# Drawing in a Bitmap

A bitmap is an invisible resource (in effect, an area of memory) that is only displayed on the screen when it is referenced by another object. Any of the seven graphical objects (Circle, Ellipse, Image, Marker, Poly, Text and Rect) can be drawn in a bitmap (represented by a Bitmap object), using exactly the same `⎕WC` syntax as if you were drawing in a Form, Static or Printer. However, drawing in a Bitmap is, like drawing on a Printer, an operation that cannot be "undone".

This facility allows you to construct a picture using lines, circles, text etc. and then later display it or save it as a bitmap.
