# <span>ProgressBar</span> <span>Object</span>



[Parents](../parentlists/progressbar.md), [Children](../childlists/progressbar.md), [Properties](../proplists/progressbar.md), [Methods](../methodlists/progressbar.md), [Events](../eventlists/progressbar.md)



**Purpose:** The ProgressBar object is used to indicate the progress of a lengthy operation.

**Description**


The ProgressBar object is a window that an application can use to indicate the progress of a lengthy operation. The appearance of the bar in the ProgressBar is determined by the [ProgressStyle](../properties/progressstyle.md) property.



If ProgressStyle is `Normal` or `Smooth`, the  size of the bar, intended to indicate the amount of progress, is determined using the [Thumb](../properties/thumb.md) property in relation to its [Limits](../properties/limits.md) property, and/or using the [ProgressStep](../methodorevents/progressstep.md) method. This can be updated as appropriate in the application logic or by using a [Timer](timer.md).


The range of a ProgressBar is specified by the [Limits](../properties/limits.md) property. This is a 2-element integer vector defining its minimum and maximum values. The position of the filled rectangle is specified by the Thumb property. You can update the ProgressBar by using `⎕WS` to set the value of the [Thumb](../properties/thumb.md) directly, or by using the [ProgressStep](../methodorevents/progressstep.md) method. The latter causes the [Thumb](../properties/thumb.md) to be updated by the value of the [Step](../properties/step.md) property.


If you attempt to set the [Thumb](../properties/thumb.md) to a value greater than its maximum value (using either method) the behaviour depends upon the value of the [Wrap](../properties/wrap.md) property which is Boolean and has a default value of 1. If [Wrap](../properties/wrap.md) is 1, the value obtained when you set the Thumb property is given by the expression:
```apl
      LIMITS[1]+(1+LIMITS[2]-LIMITS[1])|THUMB-LIMITS[1]

```


where `THUMB` is the value to which you set the Thumb property and `LIMITS` is the value of the [Limits](../properties/limits.md) property. This causes the highlighted rectangle to begin filling again from the left.


If ProgressStyle is `Marquee`, the size of the bar is fixed and its position  changes with time according to the value of the [Interval](../properties/interval.md) property. The values of [Thumb](../properties/thumb.md), [Limits](../properties/limits.md), [Wrap](../properties/wrap.md) and [Step](../properties/step.md) are irrelevant.


