# <span>ActiveXContainer</span> <span>Object</span>

[Parents](../parentlists/activexcontainer.md), [Properties](../proplists/activexcontainer.md), [Methods](../methodlists/activexcontainer.md), [Events](../eventlists/activexcontainer.md)

**Purpose:** The ActiveXContainer object represents the application that is currently hosting an instance of an ActiveXControl object.

**Description**

An ActiveXContainer is used to represent the host application that is hosting an [ActiveXControl](activexcontrol.md) object, and provides access to its ambient properties such as font, and colour.

An ActiveXContainer object is created using the [Container](../properties/container.md) property of the [ActiveXControl](activexcontrol.md) object.

For example, the following expression, executed within an [ActiveXControl](activexcontrol.md) instance creates an ActiveXContainer named `'CONT'`
```apl
      'CONT' ⎕NS ⎕WG'Container'
```

The ambient properties of the host application are reported by the [FontObj](../properties/fontobj.md), [BCol](../properties/fcol.md) and [FCol](../properties/bcol.md) properties which are all read-only.

The ActiveXContainer object supports the [AmbientChanged](../methodorevents/ambientchanged.md) event which is reported when any of the ambient properties change. This event allows the ActiveXContainer to react to such changes.
