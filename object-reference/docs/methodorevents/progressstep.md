# <span>ProgressStep</span> <span>Method 250</span>

**Applies To:** [ProgressBar](../objects/progressbar.md)

**Description**

This method is used to increment the thumb in a [ProgressBar](../objects/progressbar.md) object.

The ProgressStep method is niladic.

The ProgressStep method causes the [ProgressBar](../objects/progressbar.md) to attempt to increment its thumb by the value of its [Step](../properties/step.md) property, taking into account the settings of its [Limits](../properties/limits.md) and [Wrap](../properties/wrap.md) properties.

If the values of the [Thumb](../properties/thumb.md), [Step](../properties/step.md) and [Limits](../properties/limits.md) properties are `THUMB`, `STEP` and `LIMITS` respectively, the new value of Thumb (and the corresponding position of the highlighted bar) is:

if Wrap is 0:
```apl
      LIMITS[2]⌊THUMB+STEP
```

if Wrap is 1:
```apl
      LIMITS[1]+(1+LIMITS[2]-LIMITS[1])|THUMB+STEP-LIMITS[1]
```
