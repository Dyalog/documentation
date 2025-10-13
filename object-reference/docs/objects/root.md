<h1 class="heading"><span class="name">Root</span> <span class="right">Object</span></h1>

[Children](../childlists/root.md), [Properties](../proplists/root.md), [Methods](../methodlists/root.md), [Events](../eventlists/root.md)

**Purpose:** This is an invisible "system" object that acts as the parent of all other objects.

**Description**

There is a single Root object called `'.'` which is always present. It cannot be created using [`⎕WC`](../../../language-reference-guide/system-functions/wc) nor can it be destroyed.

The [Caption](../properties/caption.md) and [IconObj](../properties/iconobj.md) properties of `'.'` are used to identify a Dyalog APL/W application as distinct from the APL Session. The [Caption](../properties/caption.md) property specifies the application name that is displayed when you cycle through running applications using Alt+Tab and by the Windows Task List. The [IconObj](../properties/iconobj.md) property specifies the name of an [Icon](icon.md) object that is displayed alongside the application name in the box displayed by Alt+Tab. For these to take effect, your application must have at least one visible and active [Form](form.md).

For the Root object, the value of [Posn](../properties/posn.md) is (0,0). The value of [Size](../properties/size.md) is either (100,100) if [Coord](../properties/coord.md) is `'Prop'`, or the size of the screen in pixels if [Coord](../properties/coord.md) is `'Pixel'`. [XRange](../properties/xrange.md) and [YRange](../properties/yrange.md) both have the value (0,100). The [DevCaps](../properties/devcaps.md) property reports the physical size of the screen in terms of both pixels and millimetres. It also reports the number of colours available.

The [FontList](../properties/fontlist.md) property provides a list of all the character fonts that are available. The [PrintList](../properties/printlist.md) property provides a list of all the installed printers. These properties are *read-only* and may not be changed using [`⎕WS`](../../../language-reference-guide/system-functions/ws)

As the default value of [Coord](../properties/coord.md) is `'Inherit'` for all other objects, the value of [Coord](../properties/coord.md) for `'.'` defines the default co-ordinate system. It may be either `'Prop'` (the default) or `'Pixel'`. `'Inherit'` and `'User'` are not allowed.

The [CursorObj](../properties/cursorobj.md) property is used to define a cursor for the application as a whole. Its default value is an empty character vector. If it is set to any value other than `''` or 0, the selected cursor overrides the [CursorObj](../properties/cursorobj.md) values for all other objects. If you want to indicate that the application is "busy", you can therefore set the [CursorObj](../properties/cursorobj.md) property on `'.'` to an hourglass for the duration of the operation. For example:
```apl
      '.' ⎕WS 'CursorObj' 1  ⍝ Set cursor to an hourglass
```

[lengthy process...]
```apl
      '.' ⎕WS 'CursorObj' 0  ⍝ Reset cursor
```

The [Yield](../properties/yield.md) property specifies how frequently APL yields to Windows during the execution of code. Its default value is 200 milliseconds.

The [EdgeStyle](../properties/edgestyle.md) property is used to determine whether or not objects may have 3-dimensional effects. Setting [EdgeStyle](../properties/edgestyle.md) to `'None'` disables 3-dimensional effects on all [Form](form.md)s and controls. Setting [EdgeStyle](../properties/edgestyle.md) to any other value enables 3-dimensional effects for these objects.

The [ExitApp](../methodorevents/exitapp.md) and [ExitWindows](../methodorevents/exitwindows.md) events can be used to prevent the user closing your application from the Windows Task List or by terminating Windows.

The expression `⎕EX '.'` deletes all objects owned by the current thread **except** the Root object itself. In addition, if this expression is executed by thread 0, it resets all the properties of `'.'` to their default values.

## Exposing Root members

The Properties, Methods and Events of the Root object are always accessible using the system functions `⎕WS`, `⎕WG` and `⎕NQ` but may also be optionally accessed directly as if they were global variables or functions in the workspace.

For example, if Root members are exposed, the following expression will set the application cursor (GUI) to an hourglass:
```apl
      CursorObj←1
```

There are a number of elements that control whether or not Root members are exposed.

1. The fundamental mechanism is a flag that is saved in every workspace. If this flag is set, the members of the Root object are exposed; if not, they are not exposed.
2. This flag may be changed dynamically using the *Options/Object Syntax/Expose Root Properties* menu item on the Session or using `2401⌶`.  If the workspace is subsequently saved, the current value of the flag is saved with it.
3. The value of the flag in a `CLEAR WS` is determined by the **PropertyExposeRoot** parameter. Under Windows, this parameter is associated with the *Expose properties of Root* checkbox on the *Object Syntax* Tab of the *Configuration* dialog box. When you change the value of this checkbox and close the *Configuration* dialog by clicking *OK*, the value of the **PropertyExposeRoot** parameter is immediately updated in the user's section of the Registry. However, the value of the flag *in the current workspace* is not changed. The **PropertyExposeRoot** parameter only defines the value of the flag in a `CLEAR WS`, so if you subsequently type `)CLEAR`, the current value of the parameter in the Registry determines whether or not Root members are exposed and sets the flag in the workspace accordingly.

For further information, see [The Options Menu](../../../windows-ui-guide/session-menubar), [ PropertyExposeRoot](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters), and [Expose Root Properties](../../../language-reference-guide/primitive-operators/i-beam/expose-root-properties).

## Notes

1. When Root members are exposed, the first reference or assignment to a member, associates that name (with a nameclass of `¯2.6` or `¯3.6`) with that member. If, having referenced a member in this way, you subsequently hide Root members using `(2401⌶0)`, that name remains connected to that member and the member remains exposed. This association may however be removed by erasing the name.
2. If Root members are not exposed, you are free to define an APL object with the same name as one of the members. If you subsequently expose Root members using `(2401⌶1)`, the name remains associated with the APL object and not with a member of Root. If you then erase the name and re-reference or re-assign it, the name will be associated with the corresponding member.


