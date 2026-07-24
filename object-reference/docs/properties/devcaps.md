# <span>DevCaps</span> <span>Property</span>

**Description**

This property reports the device capabilities of the screen or printer. It is a 4-element nested vector as follows:

|-----|-----------------------------------------------------------------------------------------------------------------------------------------------|------|
|`[1]`|Height and Width:2-element numeric vector of device in pixels                                                                                        ||
|`[2]`|Height and Width:2-element numeric vector of device in mm                                                                                            ||
|`[3]`|Number of colours or `¯1`                                                                                                                            ||
|`[4]`|Windows scaling factor as a percentage (100=no scaling). This value is the same as reported in the Display section of the Windows Control Panel|&nbsp;|

This property is useful if you want to make objects of a specific physical size. For example, to draw a 10mm square in a [Form ](../objects/form.md)`'F'`                  at (5,5):
```apl
      Size ← 10× ⊃÷/2↑'.' ⎕WG 'DevCaps'
      'F.R' ⎕WC 'Rect' (5 5) Size ('Coord' 'Pixel')
```

## Notes

- the physical size reported for the screen is typically only a *nominal* size, because, if you use a generic video driver, Windows has no way to tell what size of screen is attached to your computer.
- The number of colours is reported only if the device has a colour depth of no more than 8 bits per pixel. For devices with greater colour depths, `¯1` is returned.
- new elements may be added to DevCaps in future releases.

**Application**

Objects: [Printer](../objects/printer.md), [Root](../objects/root.md)
