# <span>MaskCol</span> <span>Property</span>



**Applies To:** [Bitmap](../objects/bitmap.md), [Form](../objects/form.md)

**Description**


Specifies the transparent colour for a Bitmap or Form.


MaskCol may be an integer scalar or a 3-element integer vector.


If MaskCol is 0 (the default), no transparent colour is defined.


If MaskCol is a negative scalar, it specifies a standard Windows colour. See BCol for details.


Otherwise, MaskCol is a 3-element vector of integers in the range 0-255 that specifies the transparent colour in terms of RGB values (the intensity of the red, green and blue components of colour).


For a Bitmap, if MaskCol is non-zero, any pixels specified with the same colour will instead be displayed in whatever colour is underneath the Bitmap. This achieves similar behaviour to that of an Icon.


For a Form, if MaskCol is non-zero, any of the contents of the Form that are specified to be the same colour as MaskCol will be transparent. For example, if MaskCol is 255 0 0 (red), any red items contained in the Form will instead be transparent areas, displaying whatever is behind them on the screen. Mouse events generated over such transparent areas will be passed to any other windows behind them, and will not be reported on the Form itself.


