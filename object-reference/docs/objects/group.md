# <span>Group</span> <span>Object</span>



[Parents](../parentlists/group.md), [Children](../childlists/group.md), [Properties](../proplists/group.md), [Methods](../methodlists/group.md), [Events](../eventlists/group.md)



**Purpose:** This object is used to group a related set of controls together         visually, and to impose "radio-button" behaviour.

**Description**


A Group is displayed as an empty box with a border around it whose appearance
is defined by the [EdgeStyle](../properties/edgestyle.md) property. The
[Caption](../properties/caption.md) property defines a string of text
that is displayed in the top left border. The default value is an empty vector.



A Group will be resized if its parent [Form](form.md) or
Group is resized. It can also be resized directly by the user if its [Sizeable](../properties/sizeable.md) property is set to 1. By default, when a Group is resized, it automatically
adjusts the size and position of its children to maintain the same proportions
within it as before. The resizing of a Group and its children can be controlled
using the [AutoConf](../properties/autoconf.md) property or by enabling
the [Configure](../methodorevents/configure.md) event (31).


