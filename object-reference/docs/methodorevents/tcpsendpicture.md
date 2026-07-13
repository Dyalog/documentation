# <span>TCPSendPicture</span> <span>Method 380</span>

**Applies To:** [TCPSocket](../objects/tcpsocket.md)

**Description**

This method is used to transmit a picture represented by a [Bitmap](../objects/bitmap.md) object to a TCP/IP socket. The picture may be transmitted in GIF or in PNG format.

The argument to TCPSendPicture is a 1 or 2-element array as follows:

|-----|--------------|------------------------------------|
|`[1]`|Bitmap name   |character vector                    |
|`[2]`|Picture format|character vector, `'GIF'` or `'PNG'`|

If *Picture format* is omitted, the default is GIF format.

Note that the [Style](../properties/style.md) of the [TCPSocket](../objects/tcpsocket.md) object must be set to `'Raw'` before you execute the TCPSendPicture method.

The (shy) result of the method is an integer that reports the number of bytes that were transmitted.

<h2 class="example">Example</h2>
```apl
      S1.TCPSendPicture 'BM' 'PNG'        
4930
```

!!! note
    Although PNG is recognised as the latest graphics standard for displaying pictures, not all Web browsers support it.

See also: [MakeGIF](./makegif.md), [MakePNG](./makepng.md)
