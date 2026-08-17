# APL_COMPLEX_AS_V12

!!! Legacy "Legacy"
    This configuration parameter eases the transition of older code to currently supported versions of Dyalog. It is intended to be removed in a future release.

Whether code developed with Version 12.1 or earlier keeps its original behaviour with respect to complex numbers.

Valid values are:

- `1` : Version 12.1 behaviour is retained. Power (`*`) and logarithm (`⍟`) do not produce complex results from non-complex arguments; `⎕VFI` does not honour `J`/`j`; and `¯4○Y` is evaluated as `(¯1+Y*2)*0.5`. In addition, objects containing complex numbers cannot be transferred to or from component files, TCP/IP (Conga), or auxiliary processors, nor used as an argument to Serialise/Deserialise Array (`220⌶`); a `DOMAIN ERROR` is issued instead.
- any other value, or unset : code developed with Version 12.1 or earlier might now generate complex numbers

This does not prevent the generation and use of complex numbers through newer features, such as complex-number literals.
