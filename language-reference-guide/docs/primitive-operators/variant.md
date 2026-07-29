---
search:
  boost: 2
---

# <span>Variant</span> `{R}←{X}(f⍠B)Y`{{key}}

!!! note "Classic Edition"
    The symbol `⍠` is not available in Classic Edition, and the Variant operator is instead represented by `⎕U2360`. Note too that `⍠` and `⎕OPT` are synonymous though only the latter is available in the Classic Edition.

The Variant operator `⍠` specifies the value of an *option* to be used by its left operand function `f`. An *option* is a named property of a function whose value in some way affects the operation of that function.

For example, the Search and Replace operators include options named `IC` and `Mode` which respectively determine whether or not *case* is ignored and in what manner the input document is processed.

One of the set of options may be designated as the *Principal option* whose value may be set using a short-cut form of syntax as described below. For example, the Principal option for the Search and Replace operators is `IC`.

For the operand function with right argument `Y` and optional left argument `X`, the right operand `B` specifies the values of one or more options that are applicable to that function. If `B` is empty, function `f` is called with default options. Otherwise, `B` may be a scalar, a 2-element vector, or a vector of 2-element vectors which specifies values for one or more options as follows:

- If `B` is a 2-element vector and the first element is a character vector, it specifies an option name in the first element and the option value (which may be any suitable array) in the second element.
- If `B` is a vector of 2-element vectors, each item of B is interpreted as above.
- If `B` is a scalar (a rank-0 array of any depth), it specifies the value of the Principal option,

Option names and their values must be appropriate for the left operand function, otherwise `DOMAIN ERROR` (error code 11) will be reported.

<h2 class="example">Example</h2>
```apl

       tn←'Dick'(⎕FCREATE⍠'Z' 1)0
```

The following illustrations and examples apply to functions derived from the Search and Replace operators.

## Examples of operand `B`

The following expression sets the IC option to `1`, the Mode option to `'D'` and the EOL option to `'LF'`.
```apl
      ⍠('Mode' 'D')('IC' 1)('EOL' 'LF')
```

The following expression sets just the EOL option to 'CR'.
```apl
      ⍠'EOL' 'CR'
```

The following expression sets just the Principal option (which for the Search and Replace operators is IC) to 1.
```apl
      ⍠ 1
```

The order in which options are specified is typically irrelevant but if the same option is specified more than once, the rightmost one dominates. The following expression sets the option IC to 1:
```apl
      ⍠('IC' 0) ('IC' 1)
```

The Variant operator generates a derived function `f⍠B` and may be assigned to a name. The derived function is effectively function `f` bound with the option values specified by `B`.

The derived function may itself be used as a left operand to Variant to produce a second derived function whose options are further modified by the second application of the operator. The following sets the same options as the first example above:
```apl
      ⍠'Mode' 'D'⍠'IC' 1⍠'EOL' 'LF'
```

When the same option is specified more than once in this way, the outermost (rightmost) one dominates. The following expression also sets the option `IC` to 1:
```apl
      ⍠'IC' 0⍠'IC' 1
```

## Further Examples

The following derived function returns the location of the word `'variant'` within its right argument using default values for all the options.
```apl
      f1 ← 'variant' ⎕S 0
      f1 'The variant Variant operator'
4
```

It may be modified to perform a case-insensitive search:
```apl
      (f1 ⍠ 1) 'The variant Variant operator'
4 12
```

This modified function may be named:
```apl
      f2 ← f1 ⍠ 1
      f2 'The variant Variant operator'
4 12
```

The modified function may itself be modified, in this case to revert to a case sensitive search:
```apl
      f3 ← f2 ⍠ 0
      f3 'The variant Variant operator'
4
```

This is equivalent to:
```apl
      (f1 ⍠ 1 ⍠ 0) 'The variant Variant operator'
4
```

## Redundancy

A function that has been modified by Variant may be used in a context where the option or options that have been modified are not relevant. This is illustrated by the following example.

`JSON` is a character matrix that specifies 2 objects `a` and `b`.
```apl
      JSON
{                    
"a": "The answer is",
"b" : 42             
}      ⍴JSON
4 21
```

It can be imported to a matrix `mat` ...
```apl
            
      ⊢mat←(⎕JSON⍠('Format' 'M'))JSON
┌─┬─┬─────────────┬─┐
│0│ │             │1│
├─┼─┼─────────────┼─┤
│1│a│The answer is│4│
├─┼─┼─────────────┼─┤
│1│b│42           │3│
└─┴─┴─────────────┴─┘
```

This result may be exported
```apl
      1(⎕JSON⍠('Format' 'M')) mat
{"a":"The answer is","b":42}
```

The ('Compact' 0) variant option delivers a more readable result:
```apl

      1(⎕JSON⍠('Format' 'M')('Compact' 0)) mat
{                      
  "a": "The answer is",
  "b": 42              
}
```

A modified version of `⎕JSON` ...
```apl
                      
      myJSON←(⎕JSON⍠('Format' 'M')('Compact' 0))
      myJSON
┌─────┬─┬────────────────────────┐
│⎕JSON│⍠│┌──────────┬───────────┐│
│     │ ││┌──────┬─┐│┌───────┬─┐││
│     │ │││Format│M│││Compact│0│││
│     │ ││└──────┴─┘│└───────┴─┘││
│     │ │└──────────┴───────────┘│
└─────┴─┴────────────────────────┘
```

... may be used both to import and export, despite the fact that the Compact option applies only to JSON export. In the context of JSON import it is redundant and ignored.
```apl
       ⊢mat← myJSON JSON
┌─┬─┬─────────────┬─┐
│0│ │             │1│
├─┼─┼─────────────┼─┤
│1│a│The answer is│4│
├─┼─┼─────────────┼─┤
│1│b│42           │3│
└─┴─┴─────────────┴─┘
      1 myJSON mat
{                      
  "a": "The answer is",
  "b": 42              
}                      
```

## Variant and .NET

The Variant operator may also be used in conjunction with .NET classes; it can used to cast an array into a specific .NET data type, and to specify which constructor should be used when creating a new instance of a .NET class which has overloaded constructors. For further information, see [Advanced Techniques](../../../dotnet-framework-interface-guide/dotnet-classes/advanced-techniques).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⍠
  variant
</div>
