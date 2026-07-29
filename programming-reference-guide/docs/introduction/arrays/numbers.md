# Numbers

Dyalog APL supports both real numbers and complex numbers.

## Real Numbers

Numbers are entered or displayed using conventional decimal notation (for example, 299792.458) or using a scaled form for example, 2.999792458E5).

On entry, a decimal point is optional if there is no fractional part.  On output, a number with no fractional part (an integer) is displayed without a decimal point.

The scaled form consists of:

1. an integer or decimal number called the mantissa,
2. the letter `E` or `e`,
3. an integer called the scale, or exponent.

The scale specifies the power of 10 by which the mantissa is to be multiplied.

<h3 class="example">Example</h3>
```apl
      12 23.24 23.0 2.145E2
12 23.24 23 214.5
```

Negative numbers are preceded by the high minus (`¯`) symbol, not to be confused with the minus (`-`) function.  In scaled form, both the mantissa and the scale may be negative.

<h3 class="example">Example</h3>
```apl
      ¯22 2.145E¯2 ¯10.25
¯22 0.02145 ¯10.25
```

## Complex Numbers

Complex numbers use the J notation introduced in IBM APL2 and are written as `aJb` or `ajb` `(`without spaces) where the real and imaginary parts `a` and `b` are written as described above. The capital `J` is always used to display a value.

<h4 class="example">Examples</h4>
```apl
      2+¯1*.5
2J1
      .3j.5
0.3J0.5
	1.2E5J¯4E¯4
120000J¯0.0004
```

## Zilde

The empty vector (`⍳0`) may be represented by the numeric constant `⍬` called ZILDE.
