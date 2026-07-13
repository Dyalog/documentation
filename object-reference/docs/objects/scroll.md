# <span>Scroll</span> <span>Object</span>



[Parents](../parentlists/scroll.md), [Children](../childlists/scroll.md), [Properties](../proplists/scroll.md), [Methods](../methodlists/scroll.md), [Events](../eventlists/scroll.md)



**Purpose:** Provides a vertical or horizontal scrollbar.

**Description**


The Scroll object provides a vertical or horizontal scrollbar that can be used as a "free-standing" object or can be "attached" to the side of its parent.



An "attached" scrollbar is one that extends along one edge of a [Form](form.md), [SubForm](subform.md) or [Group](group.md) and has a standard width or height. When the [Form](form.md) or [Group](group.md) is resized, a vertical attached scrollbar is resized vertically but remains the same width and stays fixed to the side of its parent. Similarly, a horizontal attached scrollbar is resized horizontally but remains the same height.


For most purposes, the use of the Scroll object to provide attached scrollbars in a [Form](form.md) has been superseded by the provision of scrollbars as a **property** of a [Form](form.md).


A "free-standing" scrollbar is typically used as a "scale" for selecting a numeric value from a range and may appear and behave rather differently from a standard attached scrollbar. Firstly, a free-standing scrollbar will normally be positioned at an arbitrary position within its parent [Form](form.md) or [Group](group.md) and be associated with other objects such as [Label](label.md)s and [Edit](edit.md) fields. Secondly, when its parent [Form](form.md) or [Group](group.md) is resized, it is probably desirable that the scrollbar reacts in the same way as the other child objects, so that the overall appearance of the layout is maintained.


The [Align](../properties/align.md) property determines whether or not a scrollbar is attached, and if so, to which side of the parent [Group](group.md) or [Form](form.md) it is fixed. The direction of the scrollbar is determined by the [VScroll](../properties/vscroll.md) and [HScroll](../properties/hscroll.md) properties, which are mutually exclusive. The position and size of the scrollbar are determined by [Posn](../properties/posn.md) and [Size](../properties/size.md).


To obtain an "attached" scrollbar, it is sufficient for most purposes to specify only the [Align](../properties/align.md) property. If so, the direction of the scrollbar and its position and size (which are otherwise defined by [VScroll](../properties/vscroll.md), [HScroll](../properties/hscroll.md), [Posn](../properties/posn.md) and [Size](../properties/size.md)) are determined automatically for you.


To obtain a "free-standing" scrollbar, it is recommended for most purposes that you set [Align](../properties/align.md) to `'None'` and define the orientation, position and size of the scrollbar explicitly using [VScroll](../properties/vscroll.md) or [HScroll](../properties/hscroll.md), [Posn](../properties/posn.md) and [Size](../properties/size.md).


[VScroll](../properties/vscroll.md) and [HScroll](../properties/hscroll.md) may only be set when the object is created and may not subsequently be changed.


If you do attach a "free-standing" scrollbar to a particular side of its parent using [Align](../properties/align.md), it will maintain its physical position (in pixels) relative to the side to which it is attached, and its dimension in that direction will remain fixed.


The [Align](../properties/align.md) property is a character vector containing `'Top'`, `'Bottom'`, `'Right'`, `'Left'` or `'None'`. If you specify [Align ](../properties/align.md)`'Right'` you get a vertical scrollbar attached to the right-hand edge of the parent [Form](form.md) or [Group](group.md). [Align ](../properties/align.md)`'Left'` also produces a vertical scrollbar, but one that is attached to the left-hand edge. [Align ](../properties/align.md)`'Top'` and `'Bottom'` each produce horizontal scrollbars, attached  to the top and bottom edges of the [Form](form.md) or [Group respectively](group.md).


Note that the default value of [Align](../properties/align.md) is `'Right'` unless [HScroll](../properties/hscroll.md) is set to `¯1` in which case it is `'Bottom'`. It must therefore be explicitly set to `'None'` if you want a non-attached "free-standing" scrollbar.


[VScroll](../properties/vscroll.md) and [HScroll](../properties/hscroll.md) are used to specify the orientation of the scrollbar explicitly, usually in conjunction with [Align](../properties/align.md) set to `'None'`. [VScroll](../properties/vscroll.md) or [HScroll](../properties/hscroll.md) may be specified when the object is created by [`⎕WC`](../../../language-reference-guide/system-functions/wc), but cannot be changed using [`⎕WS`](../../../language-reference-guide/system-functions/ws). The two properties are mutually exclusive. Each of them may be set to 0 or `¯1`, where `¯1` means "true" and 0 means "false". Thus ([VScroll](../properties/vscroll.md)`¯1`) defines a vertical scrollbar, while ([HScroll](../properties/hscroll.md)`¯1`) specifies a horizontal one. Setting either property to `¯1` automatically causes the other to be set to 0. If you try to set both to `¯1`, [VScroll](../properties/vscroll.md) takes precedence and [HScroll](../properties/hscroll.md) is reset to 0.


[Note: the reason for using two properties where one would be sufficient is to allow for the possible future implementation of scrolling groups as provided by `⎕SM`/`⎕SR`.]


Scrolling is controlled by the [Thumb](../properties/thumb.md), [Range](../properties/range.md) and [Step](../properties/step.md) properties.


[Thumb](../properties/thumb.md) sets and reports the current position of the "thumb" as an integer in the range 1 to the value of the [Range](../properties/range.md) property.


[Step](../properties/step.md) determines the size of changes reported when the user clicks a scroll arrow (small change) or clicks on the body of the scrollbar (large change). [Step](../properties/step.md) is a 2-element numeric vector whose first element specifies the value of the "small change" and whose second element specifies the value of the "large change". The [PageSize](../properties/pagesize.md) property specifies the sizes of the thumb in the scrollbar.

## Examples of Attached Scrollbars
```apl
      'F' ⎕WC 'Form' 'Default Scroll Bar'
      'F.SCR' ⎕WC 'Scroll'

      'F' ⎕WC 'Form' 'Default Horizontal Scroll Bar'
      'F.SCR' ⎕WC 'Scroll' ('HScroll' ¯1)
```

## Examples of Free-Standing Scrollbars
```apl
      'F' ⎕WC 'Form' 'Non-Default Scroll Bar'
      'F.SCR' ⎕WC 'Scroll' (5 45)(90 10)
                  ('Align' 'None')('VScroll' ¯1)

      'F' ⎕WC 'Form' 'Horizontal Scroll Bars'
      'F.SC1' ⎕WC 'Scroll' (15 15)(15 70)
                  ('Align' 'None')('HScroll' ¯1)
      'F.SC2' ⎕WC 'Scroll' (40 40)(20 20)
                  ('Align' 'None')('HScroll' ¯1)
      'F.SC3' ⎕WC 'Scroll' (85 5)(10 90)
                  ('Align' 'None')('HScroll' ¯1)
```


