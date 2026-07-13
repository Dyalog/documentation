# <span>ColSorted</span> <span>Method 174</span>

**Applies To:** [Grid](../objects/grid.md)

**Description**

This method is used to specify that an image is to be displayed in a [Grid](../objects/grid.md) column title to indicate the column has been sorted.

The argument to ColSorted is a 2-element array as follows:

|-----|-------------|----------------------------------------------------|
|`[1]`|Column number|Integer.                                            |
|`[2]`|Sorted state |Integer. -1 = Sorted Down 0 = Unsorted 1 = Sorted Up|

The column title for the appropriate column is redrawn to include the appropriate image.

If you wish to use your own images, you may specify them using the [ColSortImages](../properties/colsortimages.md) property.

```apl
      'F'⎕WC'Form' 'Grid: ColSorted Method'
      'F.G'⎕WC'Grid'('Posn' 0 0)(100 100)
      F.G.Values←(COUNTRIES,POPULATION,[1.5]AREA)
      F.G.ColTitles←'Country' 'Population' 'Area'
      F.G.TitleWidth←0
```

![](../img/colsorted0.png)

```apl
      F.G.Values←(Values[⍋Values[;2];])
      F.G.ColSorted 2 1
```

![](../img/colsorted1.png)

```apl
      F.G.(Values←Values[⍒↑Values[;1];])
      F.G.ColSorted 2 0
      F.G.ColSorted 1 ¯1

```

![](../img/colsorted2.png)
