# <span>MetafileObj</span> <span>Property</span>

**Description**

This property is used to copy graphical data to and from the Windows clipboard using the Windows Metafile format.

When you set the MetafileObj property of a [Clipboard](../objects/clipboard.md) object to the name of the [Metafile](../objects/metafile.md) object using [`⎕WS`](../../../language-reference-guide/system-functions/ws) its contents are copied to the Windows clipboard in Windows Metafile format.

To import a picture that has been stored in the Windows clipboard in Metafile format you use [`⎕WG`](../../../language-reference-guide/system-functions/wg). This returns a nested array whose elements correspond to the graphical components of the picture. Each of the elements of the array may be used as the arguments of [`⎕WC`](../../../language-reference-guide/system-functions/wc) to draw the corresponding component of the picture. For example, if the picture stored in C:\MSOFFICE\CLIPART\BIRD.WMF is copied to the Windows clipboard, it may be imported into Dyalog APL/W as follows :
```apl
      BIRD ← 'CL' ⎕WG 'MetafileObj'
      ⍴BIRD
4
```

Each of the items in `BIRD` is a 2-element vector. The first element is a "dummy" object name which you may use or ignore as you wish. The second element is an array that defines a graphical object and is suitable as the right argument of [`⎕WC`](../../../language-reference-guide/system-functions/wc). For example :
```apl
      2⊃4⊃BIRD
POLY  191 397   FSTYLE  0   FILLCOL  0 0 0    ...

190 402
187 406
182 409
176 410
172 409
168 406
165 402
164 397
165 391
168 387
172 384
176 383
182 384
187 387
190 391
191 397
189 395
191 397
```

From this array, you can rebuild the imported picture component by component, either as a [Metafile](../objects/metafile.md) object or directly onto a [Form](../objects/form.md), [Static](../objects/static.md) or another object. The following example draws the picture in a [Form](../objects/form.md) using the dummy names supplied.
```apl
      'TEST' ⎕WC 'FORM' ('Coord' 'User')
      'TEST' ⎕WS ('YRange' 0 1024)('XRange' 0 2048)
      TEST.⎕WC/¨BIRD
```

Notice that the co-ordinates of each of the graphical components are typically integers in a co-ordinate system that extends from 0 to 1024 in the y-direction and 0 to 2048 in the x-direction. The simplest way to draw the picture is therefore to set up the same co-ordinate system on a [Form](../objects/form.md) as in the example above.

**Application**

Objects: [Clipboard](../objects/clipboard.md)
