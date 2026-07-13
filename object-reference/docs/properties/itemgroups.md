# <span>ItemGroups</span> <span>Property</span>

**Applies To:** [ListView](../objects/listview.md)

**Description**

This property specifies item groupings for a [ListView](../objects/listview.md) object.

!!! note
    This feature only applies if [Native Look and Feel](../miscellaneous/windows-xp-look-and-feel.md) is enabled.

ItemGroups is a nested scalar or nested vector each of whose elements specifies a grouping. Each grouping is a 5-element vector as follows:

|-----|-----------------|-------------------------------------------------------------------------------------------------------|
|`[1]`|Group caption    |character vector                                                                                       |
|`[2]`|Item index       |Vector of indices to the Items property that specifies which Items are in this grouping.               |
|`[3]`|Caption alignment|an integer: 1 = left aligned caption (the default) 2 = centre aligned caption 4 = right-aligned caption|
|`[4]`|State            |Integer (not yet implemented)                                                                          |
|`[5]`|Footer text      |character vector (not yet implemented)                                                                 |

Note that State and Footer text are not yet implemented by Windows.

For example, the following expressions executed in the WTUTOR95 workspace will result in the display shown below.
```apl
      'F'⎕WC'Form' 'ListView Object'
      II←⍳⍴COUNTRIES
      'F.L'⎕WC'ListView'COUNTRIES(0 0)(100 100)
                       ('ImageList' 'F.I1')
                       ('ImageIndex' (⍳⍴COUNTRIES))
      'F.I1'⎕WC'ImageList'('Size' 32 32)
      (⊂'F.I1.')⎕WC¨(⊂'Icon' ''),¨↓⍉↑FLAGBITS FLAGCMAP FLAGMASK
      GROUPS←⊂'Europe'(11 4 5 6 7 8 9)
      GROUPS,←⊂'Americas'(12 3 2)
      GROUPS,←⊂'Rest of the World'(1 10)
      F.L.ItemGroups←GROUPS
```

![](../img/lvsg1.gif)

You can control the appearance of the groupings using the [ItemGroupMetrics](itemgroupmetrics.md) property.
