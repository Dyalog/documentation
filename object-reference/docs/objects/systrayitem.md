# <span>SysTrayItem</span> <span>Object</span>

**Purpose:** The SysTrayItem object represents an item that you can create in the Windows System Tray.

**Description**

The SysTrayItem object appears as an icon in the Windows System Tray and allows the user to interact with your application even if it is minimised or has no other visible presence.

Interaction is provided through a pop-up menu that is displayed when the user clicks on the SysTrayItem. The SysTrayItem does not support mouse or keyboard events directly.

The IconObj property specifies the name of an Icon object used to display the SysTrayItem. If not specified, the default is the standard Dyalog APL icon.

The Popup property specifies the name of a Menu object (which may be a child of the SysTrayItem). The Menu object is displayed automatically when the user clicks on the SysTrayItem icon. The Menu should contain one or more MenuItem objects with suitable callback functions attached.

Unlike other popup menus, the SysTrayItem menu is not activated by an explicit (modal) `⎕DQ` but is posted automatically for you. The MenuItem callbacks will be executed by the current `⎕DQ`, with the exception of modal `⎕DQ`s on MsgBox, FileBox, Locator and other popup Menu objects. For example, if your application is in a modal `⎕DQ` on a Form, that `⎕DQ` will react to and action events on the SysTrayItem menu, even though it is not explicitly included in the list of objects being `⎕DQ`'ed.

The Tip property specifies a character string to be displayed when the user hovers the mouse over the SysTrayItem. This is displayed using the user's current setting for Tip text and it is not possible to change this appearance.

**Application**

Parents: [Form](../objects/form.md), [Root](../objects/root.md)

Children: [Icon](../objects/icon.md), [Menu](../objects/menu.md), [Timer](../objects/timer.md)

Properties: [ChildList](../properties/childlist.md), [Data](../properties/data.md), [Event](../properties/event.md), [EventList](../properties/eventlist.md), [IconObj](../properties/iconobj.md), [KeepOnClose](../properties/keeponclose.md), [MethodList](../properties/methodlist.md), [Popup](../properties/popup.md), [PropList](../properties/proplist.md), [Tip](../properties/tip.md), [Translate](../properties/translate.md), [Type](../properties/type.md)

Methods: [Detach](../methodorevents/detach.md), [ShowBalloonTip](../methodorevents/showballoontip.md), [Wait](../methodorevents/wait.md)

Events: [BalloonHide](../methodorevents/balloonhide.md), [BalloonShow](../methodorevents/balloonshow.md), [BalloonTimeout](../methodorevents/balloontimeout.md), [BalloonUserClick](../methodorevents/balloonuserclick.md), [Close](../methodorevents/close.md), [Create](../methodorevents/create.md), [MouseDblClick](../methodorevents/mousedblclick.md), [MouseDown](../methodorevents/mousedown.md), [MouseMove](../methodorevents/mousemove.md), [MouseUp](../methodorevents/mouseup.md)
