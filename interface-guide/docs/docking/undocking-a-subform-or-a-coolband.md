# Undocking a SubForm or a CoolBand

When a SubForm or a CoolBand is undocked, it becomes a Form.

The object may either become a Form that is a child of Root, or a Form that remains the child of the Form from where it was undocked. Such an object will always appear *on top of* its parent, even when undocked.

This behaviour is controlled by the UndocksToRoot Property.

Note that a Form or a CoolBand object may be undocked if its Dockable property is set to `'Always'`; the DockChildren property does not apply to the Root object.

The Root object does not provide DockMove events, but the docked object will generate a DockRequest event when the user releases the mouse button over the desktop. This may be used to disable or modify the operation.
