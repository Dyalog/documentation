# <span>PropertyPage</span> <span>Object</span>



[Parents](../parentlists/propertypage.md), [Children](../childlists/propertypage.md), [Properties](../proplists/propertypage.md), [Methods](../methodlists/propertypage.md), [Events](../eventlists/propertypage.md)



**Purpose:** The PropertyPage object represents a single page in a PropertySheet.

**Description**


The PropertyPage object represents a single page within a [PropertySheet](propertysheet.md).



The Posn and Size properties are read-only properties determined by the parent [PropertySheet](propertysheet.md) and may not be changed using `⎕WC` or `⎕WS`.


The [HasHelp](../properties/hashelp.md) property is either 1 (the default) or 0. If the parent [PropertySheet](propertysheet.md) has a "Help" button (determined by its own [HasHelp](../properties/hashelp.md) property) this property determines whether or not the Help button is active when the PropertyPage is the current page. If the [HasHelp](../properties/hashelp.md) property of a PropertyPage is 0, the Help button on the parent [PropertySheet](propertysheet.md) will be temporarily disabled when that PropertyPage is displayed.


The PropertyPage object generates a [PageActivate](../methodorevents/pageactivate.md) event when it becomes the current page and a [PageDeactivate](../methodorevents/pagedeactivate.md) event when another page is selected. These events may not be disabled by a callback function.


If the user presses the Cancel button, the current PropertyPage generates a [PageCancel](../methodorevents/pagecancel.md) event. This is followed by a Close event which is reported by the parent PropertySheet.


Other properties and behaviour depend upon the Style of the parent PropertySheet which may be `'Standard'` or `'Wizard'`

## Standard Behaviour


![](../img/ps1.gif)


In a *Standard* PropertySheet, the Caption property of each PropertyPage specifies the text that is written in its tab.


PropertyPage objects owned by a Standard [PropertySheet](propertysheet.md) generate [PageCancel](../methodorevents/pagecancel.md), [PageApply](../methodorevents/pageapply.md) and [PageHelp](../methodorevents/pagehelp.md) events. These events are all caused by the user  pressing the corresponding button in the parent [PropertySheet](propertysheet.md).


Conventionally, the Apply button is initially inactive. When the user changes an item on any of the PropertyPages, the Apply button immediately becomes active. When the user clicks the Apply button, the application responds (normally by changing the appropriate properties) and then the Apply button becomes inactive once again. This process is controlled as follows.


The Changed property is a Boolean value that determines whether or not a PropertyPage is marked as having been in any way altered. The Apply button is active if the value of the Changed property for *any* of the PropertyPages is 1, and is inactive otherwise


Initially, the value of the Changed property for all of the PropertyPages is 0 and the Apply button is therefore inactive. If the user alters a control on a PropertyPage, by, for example typing into an Edit object or changing the State of a Radio Button, the PropertyPage immediately generates a [PageChanged](../methodorevents/pagechanged.md) event with the parameter 1. The default processing for this event is to set the Changed property of the PropertySheet (to 1). This in turn activates the "Apply" button. If you return 0 from a callback on the [PageChanged](../methodorevents/pagechanged.md) event, the Changed property remains 0 and the Apply button remains inactive.


When the user clicks the Apply button, each of the PropertyPages whose Changed flag is currently set to 1 generates a [PageApply](../methodorevents/pageapply.md) event. The default processing for this event is to generate a [PageChanged](../methodorevents/pagechanged.md) event with the parameter 0. This is turn resets the Changed property of the PropertyPage to 0. Once all of the Changed flags have been reset, the Apply button becomes inactive. If you return 0 from a callback on any of  the [PageChanged](../methodorevents/pagechanged.md) events, the Changed property for the corresponding PropertyPage remains 1 and the Apply button remains active.


You may control the value of the Changed property using `⎕WS` or by calling [PageChanged](../methodorevents/pagechanged.md) as a method. In all cases, the Apply button is active if the value of Changed on any PropertyPage is 1, and inactive otherwise.

## Wizard Behaviour


![](../img/ps2.gif)


If the PropertyPage is owned by a *Wizard* [PropertySheet](propertysheet.md), its Caption property specifies the text that appears in the title bar of the [PropertySheet](propertysheet.md) window when the PropertyPage is the current page. Note that a Wizard [PropertySheet](propertysheet.md) ignores its own Caption property.


There are effectively 3 page changing buttons on a Wizard [PropertySheet](propertysheet.md), named Back, Next and Finish. The Next and Finish buttons actually occupy the same position and are mutually exclusive. The captions on the buttons are language-dependent.


Conventionally, the buttons change according to which of the PropertyPages is currently displayed. If the first one is displayed, the Next button is active but the Back button is inactive. When a middle page is displayed, both the Next and Back buttons are active. When the last page is displayed, the caption on the Next button changes to Finish. However, in some applications, the Back button may be disabled to prevent the user returning to a previous page.


When the user clicks the Back or Next button, the PropertyPage generates a [PageBack](../methodorevents/pageback.md) or [PageNext](../methodorevents/pagenext.md) event followed by a [PageDeactivate](../methodorevents/pagedeactivate.md) event. The new PropertyPage then generates a [PageActivate](../methodorevents/pageactivate.md) event. These are followed by a [SetWizard](../methodorevents/setwizard.md) event which is generated by the parent PropertySheet and actually controls the state of the buttons. When the user clicks the Finish button, the PropertyPage generates a [PageFinish](../methodorevents/pagefinish.md) event alone. All of these events reported by the PropertyPage are reported for information only. Returning 0 from a callback function has no effect. You may however control the buttons using the [SetWizard](../methodorevents/setwizard.md) event.


