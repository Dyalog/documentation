# <span>DockChildren</span> <span>Property</span>

**Applies To:** [CoolBar](../objects/coolbar.md), [Form](../objects/form.md), [SubForm](../objects/subform.md)

**Description**

The DockChildren property specifies the names of client objects that may be docked in a host object.

DockChildren may be a single ref or simple character scalar or vector, or a vector of refs or character vectors. Each item represents an object that may be docked. Notice that if you use a name, you must specify the simple name of the object, excluding any part of its full pathname that refers to a parent; that is, the specified names must not contain any leading pathname information.

If the name of, or ref to, a [dockable](dockable.md) object occurs in the DockChildren property, the host object will generate DockMove events when the client is dragged over it, and will generate a DockAccept event when a docking operation takes place.

If the name of, or ref to, the client object is not present in its DockChildren property, the object will not respond in any way as the client is dragged over it.

The following example shows the creation of 3 dockable forms, all of which are dockable in a host form called h1.

The first, `c1`, is a totally independent Form. When docked in `h1`, it will become a SubForm `h1.c1`. When undocked, it will revert to an independent Form `c1`.

The second, `c2`, is created initially as a child of `h1` and will therefore be displayed above it in the window stacking order. When docked it will become a SubForm `h1.c2`. When undocked, it will revert back to a dependent Form `h1.c2`. In all cases, it appears on top of `h1`.

The third, `c3`, is created initially as a child of another Form, `h2`. When docked (in `h1`) it will become a SubForm `h1.c3`. When undocked, it will become a dependent Form `h1.c3`, and will therefore appear above `h1` in the stacking order.
```apl

      'h1'⎕WC'Form' 'Host1' 
      'h2'⎕WC'Form' 'Host2' 
			
      'c1' ⎕WC 'Form' 'Client 1' ('Dockable' 'Always')
      'h1.c2' ⎕WC 'Form' 'Client 2' ('Dockable' 'Always')
      'h2.c3' ⎕WC 'Form' 'Client 3' ('Dockable' 'Always')

      h1.DockChildren←'c1' 'c2' 'c3'
```
