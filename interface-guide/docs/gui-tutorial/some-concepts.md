# Some Concepts

## Objects

Objects are GUI components such as Forms, Buttons and Scrollbars. You create objects using the system function `⎕WC`. Its left argument is a name for the object; its right argument specifies the object type and various properties. Objects are created in a hierarchy.

## Properties

Properties specify the appearance and behaviour of an object. For example, the Caption property specifies the text that appears on a Button or the title that appears in the title bar on a Form. When you create an object with `⎕WC`, its right argument specifies its properties. You can also set properties using `⎕WS`. This lets you dynamically alter the appearance and behaviour of an object as required.

## Events

Events are things that happen in objects as a result (usually) of some action by the user. For example, when the user clicks a MenuItem, it generates a Select event. Similarly, when the user focuses on an object, it generates a GotFocus event.

## Callback Functions

Callback Functions are APL functions that you can associate with a particular event in a particular object. Interaction with the user is controlled by the system function `⎕DQ`. This function performs all of the routine tasks involved in driving the GUI interface. However, its main role is to invoke your callback functions for you as and when events occur.

That's enough theory for now ... let's see how it all works in practice.
