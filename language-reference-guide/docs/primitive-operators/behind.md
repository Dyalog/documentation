<div style="display: none;">
  ⍛
</div>

<h1 class="heading"><span class="name">Behind</span> <span class="command">{R}←{X}f⍛gY</span></h1>

!!! Info "Information"
    The `⍛` glyph is not available in Classic Edition, and the _behind_ operator is instead represented by `⎕U235B`.

`f` can be any monadic function that returns a result; the result must be suitable as the left argument to the function `g`.

`g` can be any dyadic function; it does not need to return a result.

`Y` can be any array that is suitable as the right argument to the function `g`.
If `X` is omitted, `Y` must also be suitable as the right argument to the function `f`.

`X` can be any array that is suitable as the right argument to the function `f`.

The derived function is equivalent to either `(f Y) g Y` or `(f X) g Y`, depending on whether `X` is specified or not.

The _behind_ operator allows functions to be *glued* together to build up more complex functions. For further information, see [Function Composition](./operator-syntax.md).

<h2 class="example">Examples: Monadic Application of Derived Function</h2>

Are numbers in a sequence identical to the first number in that sequence?
```apl
      ⊃⍛= 2 7 1 8 2 8 1 8 2 8
1 0 0 0 1 0 0 0 1 0 
```

Are the characters within each vector unique?
```apl
      ∪⍛≡¨ 'Hello' 'Helo'
0 1
```

Where in a Boolean mask does it match its reverse?
```apl
      ⌽⍛∧ 0 1 1 1 1 0 0 0 0
0 0 0 0 1 0 0 0 0
```

Prefix a vector with its final element:
```apl
      ⊢/⍛,'XYZ'
ZXYZ
```

Identify where the odd numbers are located within a vector, and add 1 to them:
```apl
      2∘| 3 1 4 1 5 9     ⍝ create mask of odd numbers
1 1 0 1 1 1
      2∘|⍛+ 3 1 4 1 5 9   ⍝ add one to the odd numbers
4 2 4 2 6 10
```

Identify the numbers in a vector greater than 3, and filter to return only those numbers:
```apl
      3∘< 2 7 1 8 2 8     ⍝ create mask
0 1 0 1 0 1
      3∘<⍛/ 2 7 1 8 2 8   ⍝ apply filter
7 8 8
```

Identify the integers in a vector of numbers, and filter to return only the integers:
```apl
      ⌊⍛= 1 3.2 ¯5 0 ¯3.2 8.1     ⍝ create mask
1 0 1 1 0 0
      ⌊⍛=⍛/ 1 3.2 ¯5 0 ¯3.2 8.1   ⍝ apply filter
1 ¯5 0
```

Identify the palindromes, and filter to return only the palindromes:
```apl
      ⌽⍛≡¨ 'racecar' 'racer' 'hanna' 'asa'   ⍝ create mask
1 0 0 1
      ⌽⍛≡¨⍛/ 'racecar' 'racer' 'hanna' 'asa' ⍝ apply filter
‘racecar’ ‘asa’
```

Find the mean value of a vector of numbers, identify the individual numbers in the vector that are greater than the mean value, and filter to retun only those numbers:
```apl
      (+⌿÷≢) 3 1 4 1 5 9 2 6       ⍝ calculate mean value
3.875
      (+⌿÷≢)⍛< 3 1 4 1 5 9 2 6     ⍝ create mask
0 0 1 0 1 1 0 1
      (+⌿÷≢)⍛<⍛/ 3 1 4 1 5 9 2 6   ⍝ apply filter
4 5 9 6
```

<h2 class="example">Examples: Dyadic Application of Derived Function</h2>

Some functions require their left arguments to be enclosed to achieve the desired result. Without _behind_, the left argument needs to be parenthesised to enclose the left argument. With _behind_, a new function can be derived that achieves the required enclosure by including `⊂⍛` before the main function. For example:

Does the left argument exist within the right argument?
```apl
      (⊂'dog') ∊ 'cat' 'dog' 'bird'    ⍝ without behind
1
      'dog' ⊂⍛∊ 'cat' 'dog' 'bird'     ⍝ with behind
1
```

Select elements using the index function:
```apl
      1 4 1 13 ⊂⍛⌷ ⎕A
ADAM
```

Write a vector of vectors to a file:
```apl
      'abc' 'def' ⊂⍛⎕NPUT 'myfile.txt'
```
<br />
You can compose functions to achieve useful functionality. For example:

Evaluate x²+2 for multiple values of x: 
```apl
      (⍪5 10)⊥ 1 0 2              ⍝ without behind
      5 10 ⍪⍛⊥ 1 0 2              ⍝ with behind
27 102

```

Convert numbers to text as they are catenated:
```apl
      'there are ',2⍕⍛,' things'
there are 2 things
```

Reshape an array to conform to the shape of another array:
```apl
      'abc' ⍴⍛⍴ 'z'
zzz
```
<br />
Some functionality does not exist as a primitive but can easily be composed using _behind_. For example:

Identify the first occurrence of an element starting from the end of the source:
```apl
      'abracadabra' ⌽⍛⍳ 'ab'
1 3
```

Construct a Boolean mask from a length and the indices of the `1`s (inverse of monadic `⍸`):
```apl
      10 ⍳⍛∊ 1 3 5
1 0 1 0 1 0 0 0 0 0
```

Filter to return elements that correspond to `0` in a Boolean mask – the opposite of _reduce_ (`/`), which returns elements that correspond to `1` in a Boolean mask.:
```apl
      0 1 0 1 1 0 ~⍛/ 'Dyalog'
Dag
```

Take elements from both ends of the source:
```apl
      3 (↑⍪-⍛↑) ⎕A
ABCXYZ
```

Sort a vector by values in another vector:
```apl
      30 40 20 ⊂⍤⍋⍛⌷ 'Abe' 'Bea' 'Carl'
Carl Abe Bea
```

Split a vector with a function that can be applied either monadically (in which case it uses the initial character as separator) or dyadically (in which case it uses the left argument as separator):

```apl
      ]Boxing on
      Split←⊃⍛≠⊆⊢
      Text←',I S,EAT ING,RATES'
      Split Text     ⍝ Split at occurences of first element
┌───┬───────┬─────┐
│I S│EAT ING│RATES│
└───┴───────┴─────┘
      ' 'SPLIT TEXT  ⍝ Split at occurences of left argument
┌──┬─────┬─────────┐
│,I│S,EAT│ING,RATES│
└──┴─────┴─────────┘
```
