# Introduction

Dyalog APL supports dockable Forms, SubForms, CoolBands and ToolControls.

If an object is dockable, the user may drag it to a different position within the same container, drag it out of its current container and drop it onto a different container, or drop it onto the desktop as a free-floating window. An undocked object can subsequently be redocked in its original container or in another.

For example, a SubForm can be dragged from one Form and docked into another. Or a CoolBand can be dragged out of its CoolBar and turned into a top-level Form on the desktop.

With the exception of ToolControls, when a dockable object is docked or undocked, the full Name and Type of the object change according to the following table.

|&nbsp;              |Parent Object                                                    ||||
|--------------------|---------------|------------------|--------------------|------------|
|**Dockable Object** |Form<br/>`F1`      |SubForm<br/>`F1.S1`   |CoolBar<br/>`F1.CB1`    |Root<br/>`(.)`  |
|Form<br/>`F2`           |SubForm<br/>`F1.F2`|SubForm<br/>`F1.S1.F2`|CoolForm<br/>`F1.CB1.F2`|Form<br/>`F2`   |
|Form<br/>`F1.F2`        |SubForm<br/>`F1.F2`|SubForm<br/>`F1.S1.F2`|CoolForm<br/>`F1.CB1.F2`|Form<br/>`F1.F2`|
|SubForm<br/>`F2.S2`     |SubForm<br/>`F1.F2`|SubForm<br/>`F1.S1.F2`|CoolForm<br/>`F1.CB1.F2`|Form<br/>`S2`   |
|CoolForm<br/>`F2.CB2.C2`|SubForm<br/>`F1.C2`|SubForm<br/>`F1.S1.C2`|CoolForm<br/>`F1.CB1.C2`|Form<br/>`C2`   |

For example, a top-level Form `F2` when docked in another top-level Form `F1`, becomes a SubForm named `F2.F1`.

Similarly, a CoolBand named `F2.CB2.C2` when dragged from its CoolBar `F2.CB2` and dropped over the desktop, becomes a top-level Form named `C2`.

Notice how the node name of the object remains the same, but its full pathname changes as it is moved from one parent object to another.

When an object changes Type in this way, the values of all its properties for its original Type are remembered, and these are automatically restored when the object reverts back to its original Type. Since an object can change Type between Form, SubForm, and CoolBand, it follows that there are effectively 3 different sets of properties associated with the object. However, only one set of properties (the set associated with the object's current Type) is visible and accessible (to the programmer) at any one time.
