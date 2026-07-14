# <span>Label</span> <span>Object</span>

[Parents](../parentlists/label.md), [Children](../childlists/label.md), [Properties](../proplists/label.md), [Methods](../methodlists/label.md), [Events](../eventlists/label.md)

**Purpose:** Displays static text.

**Description**

This object displays a text label, a number, a date or a time value.

If [FieldType](../properties/fieldtype.md) is empty, the Label displays the text defined by its [Caption](../properties/caption.md) property. If the [Caption](../properties/caption.md) property contains one or more linefeed characters (`⎕UCS 10`) the Label becomes a multi-line Label which is top-left justified and automatically wraps on white-space characters (such as space and tab) to fit in the width provided.

If [FieldType](../properties/fieldtype.md) is `'Numeric'`, `'LongNumeric'`, `'Currency'`, `'Date'`, `'LongDate'`, or `'Time'` the Label converts and formats the number defined by its [Value](../properties/value.md) property and displays this instead. See [FieldType](../properties/fieldtype.md) property for details.

The [Border](../properties/border.md) property determines whether or not the label has a border. A value of 0 means no border (the default). A value of 1 means that a 1-pixel border is drawn around the label.

By default, the value of the [EdgeStyle](../properties/edgestyle.md) property for a Label is `'None'` and the value of [BCol](../properties/bcol.md) is 0 which is normally white, or grey if the parent object has a 3-dimensional appearance. You can change its appearance by setting [EdgeStyle](../properties/edgestyle.md) and/or [BCol](../properties/bcol.md) to different values.
