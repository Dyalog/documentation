# Drawing Lines

To draw a line you use the Poly object. The following example draws a line in a Form from the point (y=10, x=5) to the point (y=90, x=60) :
```apl
      'F'      ⎕WC 'Form' 'Drawing Lines' ('Size' 25 50)
      'F.Line' ⎕WC 'Poly' ((10 90)(5 60))
```

![](../img/drawing-lines-1.png)

In the previous example, the points are specified as a 2-element nested vector containing y-coordinates and x-coordinates respectively. You can also use a 2-column matrix. For example:
```apl
      'F.Line'⎕WC'Poly'(4 2⍴90 5 5 50 90 95 90 5)
```

![](../img/drawing-lines-2.png)

Notice that because the second example **replaced** the object `F.Line`, the original line drawn in the first example has been erased.

In common with the position and size of other GUI objects, y-coordinates precede x-coordinates. Graphical software typically uses (x,y) rather than (y,x) but the latter is consistent with the order in which coordinates are specified and reported for all other objects and events. The Dyalog APL GUI support allows you to freely mix graphical objects with other GUI components (for example, you can use the graphical Text object in place of a Label) and this (y,x) consistency serves to avoid confusion.

When a graphical object in a screen object is erased its parent is restored to the appearance that it had before that graphical object was created. Thus:
```apl
      'F.Line' ⎕WC 'Poly' (2 2⍴10 5 50 10)
      ⎕EX 'F.Line'
```

first draws a line and then removes it. The following expression clears all graphical objects (and any other non-graphical ones too) from a parent object `'F'`:
```apl
      ⎕EX ⎕WN'F'
```

Similarly, objects automatically disappear when a function in which they are localised exits.

Erasing graphical objects that have been drawn on a Printer has no effect. Once drawn they cannot be undrawn.
