# <span>ActiveXContainer</span> <span>Object</span>

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

**Application**

Parents: [ActiveXControl](../objects/activexcontrol.md)

Children: [ActiveXControl](../objects/activexcontrol.md)

Properties: [BCol](../properties/bcol.md), [ChildList](../properties/childlist.md), [Data](../properties/data.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [FCol](../properties/fcol.md), [FontObj](../properties/fontobj.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [PropList](../properties/proplist.md), [Type](../properties/type.md)

Methods: [Detach](../methodorevents/detach.md), [OLEQueryInterface](../methodorevents/olequeryinterface.md)

Events: [AmbientChanged](../methodorevents/ambientchanged.md), [Close](../methodorevents/close.md), [Create](../methodorevents/create.md)
