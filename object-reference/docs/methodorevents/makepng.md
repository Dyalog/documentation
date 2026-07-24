# <span>MakePNG</span> <span>Method 260</span>

**Description**

This method is used to generate a PNG (Portable Network Graphics) representation of a picture from a Bitmap object suitable for display by a Web browser.

The MakePNG method is niladic.

The result is an integer vector containing the encoded PNG image.

**Example:**
```apl
      ⍴PNG←BM.MakePNG
4930
```

**Application**

Objects: [Bitmap](../objects/bitmap.md)
