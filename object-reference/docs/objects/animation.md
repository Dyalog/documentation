# <span>Animation</span> <span>Object</span>



[Parents](../parentlists/animation.md), [Children](../childlists/animation.md), [Properties](../proplists/animation.md), [Methods](../methodlists/animation.md), [Events](../eventlists/animation.md)



**Purpose:** The Animation object displays simple animations from basic .AVI files or resources.

**Description**


The Animation object displays simple animations from basic .AVI files or resources.



The Animation object can only play AVI files or resources that have no sound and can only display uncompressed AVI files or .AVI files that have been compressed using Run-Length Encoding (RLE).


For more sophisticated animations, you may use the Windows Media Player (OCX).


To display an AVI file, you must first use the [AnimOpen](../methodorevents/animopen.md) method to open it. If the [AutoPlay](../properties/autoplay.md) property is set to 1, the animation will play immediately. Otherwise, only the first frame will be displayed.


The [Align](../properties/align.md) property may be `'None'` or `'Centre'` (`'Center'`). If [Align](../properties/align.md) is `'None'`, the Animation window is automatically resized to fit the AVI being played. If [Align](../properties/align.md) is `'Centre'`, the AVI is centred in the Animation window. If the window is too small, the AVI is clipped.


The [AnimPlay](../methodorevents/animplay.md) method may be used to play the animation and allows you to specify the start, number of frames, and repeat count.


The [AnimStop](../methodorevents/animstop.md) method causes the animation to stop.


The [AnimClose](../methodorevents/animclose.md) method closes the current AVI file and resets the contents of the object's window to its background colour.


The [AnimStarted](../methodorevents/animstarted.md) and [AnimStopped](../methodorevents/animstopped.md) events are reported when the animation starts and stops respectively.


