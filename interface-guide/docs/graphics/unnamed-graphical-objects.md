# Unnamed Graphical Objects

When using the seven graphical output objects, you can optionally omit the final part of the name. For example, the following expression is valid:
```apl
      'F.' ⎕WC 'Poly' (2 2⍴10 5 50 10)
```

When you create a **named** object, all of the properties pertaining to that object are stored internally in your workspace. A polyline consisting of a large number of points thus takes up a significant amount of memory. However, this is necessary because the APL interpreter needs the information in order to redraw the object when another window is placed over it and then moved away again (exposure) or when the user resizes the Form in which it is displayed.

When you create an **unnamed** graphical object, the object is drawn, but its properties are **not** remembered internally, thus conserving workspace. This has two consequences. Firstly, you cannot subsequently modify or query the object's properties; you must name an object if you are ever going to refer to it again. Secondly, the object cannot automatically be redrawn (by APL) when it is exposed or resized. Instead, you must control this yourself using the Expose event.

Unnamed graphical objects are useful in the following circumstances:

- For output to a Printer.
- When you are very short of workspace.
- When you are sure that the window you are drawing in will not need to be redrawn, for example, when you are working "full-screen".
- For drawing in a Bitmap or a Metafile.
- For creating bitmaps in an ImageList
