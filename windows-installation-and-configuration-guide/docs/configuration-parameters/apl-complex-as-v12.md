# APL_COMPLEX_AS_V12

Support for Complex Numbers means that some functions produce different results from older Versions of Dyalog APL. If **APL_COMPLEX_AS_V12** is set to 1 the behaviour of code developed using Version 12.1 or earlier will be unchanged; in particular:

- Power (`*` ) and logarithm (`⍟` ) do not produce Complex Numbers as results from non-complex arguments.
- `⎕VFI` will not honour "J" or "j" as part of a number.
- `¯4○Y` will be evaluated as `(¯1+Y*2)*0.5` , which is positive for negative real arguments.

If **APL_COMPLEX_AS_V12** is set to any other value or is not set at all then code developed using version 12.1 or earlier may now generate Complex Numbers.

In addition, if **APL_COMPLEX_AS_V12** is set to 1, objects containing complex numbers cannot be transferred to or from component files, TCP/IP (CONGA), or auxiliary processors and may not be used as an argument to Serialise/Deserialise Array (`220⌶` ). Instead, a `DOMAIN ERROR` will be issued.

Note that this feature is provided to simplify the transition of older code to currently supported Versions of Dyalog APL. It does not prevent the generation and use of Complex Numbers using newer features (such as explicitly specifying a Complex Number literal), and the intention is that it will be removed in a future release of Dyalog APL.
