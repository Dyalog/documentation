<h1 class="heading"><span class="name">Positioning and Sizing Forms and Controls</span></h1>

The position of a form or a control is specified by its `Location` property, which is measured relative to the top left corner of the client area of its container.

`Location` has a data type of `System.Drawing.Point`. To set `Location`, you must first create an object of type `System.Drawing.Point` then assign that object to `Location`.

Similarly, the size of an object is determined by its `Size` property, which has a data type of `System.Drawing.Size`. This time, you must create a `System.Drawing.Size` object before assigning it to the `Size` property of the control or form.

Objects also have `Top(Y)` and `Left(X)` properties that may be specified or referenced  independently. These accept simple numeric values.

The position of a `Form` may instead be determined by its `DeskTopLocation` property, which is specified relative to the taskbar. Another alternative is to set the `StartPosition` property whose default setting is `WindowsDefaultLocation`, which represents a computed best location.
