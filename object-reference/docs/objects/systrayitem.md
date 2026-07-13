# <span>SysTrayItem</span> <span>Object</span>



[Parents](../parentlists/systrayitem.md), [Children](../childlists/systrayitem.md), [Properties](../proplists/systrayitem.md), [Methods](../methodlists/systrayitem.md), [Events](../eventlists/systrayitem.md)



**Purpose:** The SysTrayItem object represents an item that you can create in the Windows System Tray.

**Description**


The SysTrayItem object appears as an icon in the Windows System Tray and allows the user to interact with your application even if it is minimised or has no other visible presence.



Interaction is provided through a pop-up menu that is displayed when the user clicks on the SysTrayItem. The SysTrayItem does not support mouse or keyboard events directly.


The IconObj property specifies the name of an Icon object used to display the SysTrayItem. If not specified, the default is the standard Dyalog APL icon.


The Popup property specifies the name of a Menu object (which may be a child of the SysTrayItem). The Menu object is displayed automatically when the user clicks on the SysTrayItem icon. The Menu should contain one or more MenuItem objects with suitable callback functions attached.


Unlike other popup menus, the SysTrayItem menu is not activated by an explicit (modal) `⎕DQ` but is posted automatically for you. The MenuItem callbacks will be executed by the current `⎕DQ`, with the exception of modal `⎕DQ`s on MsgBox, FileBox, Locator and other popup Menu objects. For example, if your application is in a modal `⎕DQ` on a Form, that `⎕DQ` will react to and action events on the SysTrayItem menu, even though it is not explicitly included in the list of objects being `⎕DQ`'ed.


The Tip property specifies a character string to be displayed when the user hovers the mouse over the SysTrayItem. This is displayed using the user's current setting for Tip text and it is not possible to change this appearance.


