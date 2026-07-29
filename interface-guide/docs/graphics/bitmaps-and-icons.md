# Bitmaps and Icons

Bitmaps and icons are implemented as separate objects that you can create and destroy. Once you have created such an object you can reference it as many times as you wish. For example, you can use the same bitmap in several Buttons or associate the same icon with several Forms.

The Bitmap and Icon objects can be created in one of two ways. They are either loaded from an existing file or they are defined from APL arrays.

The files concerned must be in the appropriate Windows format for the object (.BMP or .ICO files) which can be edited by a standard Windows utility such as Paintbrush. The following example creates a Bitmap object from the CARS.BMP bitmap file which is supplied in the WS sub-directory:
```apl
      ROOT←2 ⎕NQ'.' 'GetEnvironment' 'dyalog'
      'CARS' ⎕WC 'Bitmap' (ROOT,'\WS\CARS')
```

Then you can use the Bitmap to fill the background of a Form by:
```apl
      'F1' ⎕WC 'Form' ('Picture' CARS 1)('Size' 25 50)
```

![](../img/cars.png)

The "1" in the expression specifies that the Bitmap is to be used to "tile" the background of the Form. The result is shown in the illustration below. You can also position the Bitmap in the top-left (0) or centre (3) of the Form, or even have the Bitmap scaled automatically (2) to fit exactly in the Form. These settings are useful for displaying pictures. You can explore these facilities using the `BMVIEW` function in the UTIL workspace.

Instead of creating Bitmap and Icon objects from file, you can define them using APL arrays. These arrays specify the individual pixels that make up the picture or shape of the object in question.

There are two ways to define a Bitmap object from APL arrays. The first method, which is limited to colour palettes of 16 or 256 colours is to supply two arrays; one containing the colour indices for every pixel in the bitmap, and one containing the colour map. The colour map specifies the colours (in terms of their red, green and blue components) corresponding to the indices in the first array. For example, the following expressions create a 32 x 32 Bitmap from the arrays `PIX` and `CM`:
```apl
      ⍴PIX  ⍝ colour index (in CM) of each pixel
32 32
      ⍴CM   ⍝ 16-row matrix of RGB values
16 3
      'BM' ⎕WC 'Bitmap' ('Bits' PIX)('CMap' CM)
```

The reason that this method is restricted to 256 colours is that the CMap array containing the colour map is, of necessity, the same size as the colour palette. Even for a relatively modest 16-bit colour palette, the size of the array would be 65536 x 3.

The second method, which applies to all sizes of colour palette, is to use a single array that represents each pixel by a number that is an encoding of the red, green and blue components. The formula used to calculate each pixel value is:
```apl
      256⊥RED GREEN BLUE
```

where `RED`, `GREEN` and `BLUE` are integers in the range 0-255.

Thus the example above can be achieved using a single array `CBITS` as follows:
```apl
      CBITS←(256⊥⍉CMAP)[⎕IO+PIX]
      'BM' ⎕WC 'Bitmap' ('CBits' CBITS)
```

While it is possible to define bitmaps by creating appropriate APL arrays, it is likely that you will load them from file. For example:
```apl
      'BM' ⎕WC 'Bitmap' (ROOT,'\WS\CARS')
      PIX CM ← 'BM' ⎕WG 'Bits' 'CMap'
```
