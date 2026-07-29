# <span>AmbientChanged</span> <span>Event 533</span>

**Description**

If enabled, this event is reported when any of the ambient properties change in an application hosting an [ActiveXControl](../objects/activexcontrol.md) object. The new values of the ambient properties are available from the [FontObj](../properties/fontobj.md), [BCol](../properties/fcol.md) and [FCol](../properties/bcol.md) properties of the [ActiveXContainer](../objects/activexcontainer.md).

This event is reported for information alone. You may not disable or nullify the event by setting the action code for the event to `¯1` or by returning 0 from a callback function.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 4-element vector as follows :

|-----|-------------|-------------------------|
|`[1]`|Object       |ref or character vector  |
|`[2]`|Event        |`'AmbientChanged'` or 533|
|`[3]`|Property code|integer                  |
|`[4]`|Description  |character vector         |

For properties supported by Dyalog APL, Property code and Description may be one of the following:

|Property code|Description             |Meaning         |
|-------------|------------------------|----------------|
|`¯701`       |DISPID_AMBIENT_BACKCOLOR|BCol has changed|
|`¯703`       |DISPID_AMBIENT_FORECOLOR|FCol has changed|
|`¯705`       |DISPID_AMBIENT_FONT     |Font has changed|
|`¯1`         |DISPID_AMBIENT_UNKNOWN  |Unknown         |

Note that other ambient properties may be reported, although these have no corresponding Dyalog APL property.

**Application**

Objects: [ActiveXContainer](../objects/activexcontainer.md), [ActiveXControl](../objects/activexcontrol.md)
