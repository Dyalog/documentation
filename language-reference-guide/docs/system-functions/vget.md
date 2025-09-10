<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕VGET VGET
</div>

<h1 class="heading"><span class="name">Value Get</span> <span class="command">R←{X}⎕VGET Y</span></h1>

`⎕VGET` enables values to be read for names in a source namespace or source namespaces. Optionally, a fallback value can be used if the name requested is undefined.

`Y` specifies the names. It must be one of the following:

* a matrix of names or a matrix of names and a value vector – see [Case 1: Name Matrix](#case-1-name-matrix).
* a vector of names or name-value pairs – see [Case 2: Vector of Names](#case-2-vector-of-names).
* a vector of nameclasses – see [Case 3: Nameclasses](#case-3-nameclasses).

All specified names must be either undefined, or have an array value in the source namespace(s). If `Y` specifies a matrix or a vector of names, fallback values to use in cases where a name has no value can also be specified to prevent a `VALUE ERROR` from being generated.

If specified, `X` must be an array that identifies one or more source namespaces. This means that `X` must be one of:

* a simple character scalar or vector identifying the name of a namespace.
* a reference to a namespace.
* an array in which each item is one of the above. If `X` refers to multiple namespaces, then `⎕VGET` processes each item of `X` in ravel order, using the entire right argument `Y`; this is equivalent to  `X ⎕VGET¨⊂Y`.

When `X` is an empty array, the prototype of the empty result `R` depends on the fallback values, if specified. If the prototype of `X` is an instance of a class that can be instantiated, such as an instance of a class with a niladic or no constructors, then a new instance of the class is made and the prototype of the result is determined by the values found within the new instance.

The namespace(s) referenced must already exist, or a `VALUE ERROR` is generated.  

If `X` is not specified, the source namespace is the current namespace.

The result `R` depends on the format of `Y`.

See also [`⎕VSET`](vset.md).

## Case 1: Name Matrix

Names are specified as rows in a character matrix.
`Y` must be either:

* a character matrix, where each row is a name.
* a two element vector, where the first item is a character matrix of names and the second item is a specification of fallback values.

The fallback values must one of the following:

* a vector with as many elements as there are names in the matrix.
* a scalar value that is the fallback value for all names.


The result `R` is a vector of the values from the corresponding names or fallback values.

<h3 class="example">Examples</h3>

Multiple names without fallback:

```apl
      (name1 name2 name3 longer_name)←(1 2 3) () 'APL' 42
      names←↑'name1' 'name2' 'name3' 'longer_name'
      names
name1
name2
name3
longer_name
      ⎕VGET names
 1 2 3  #.[Namespace]  APL  42
```

Multiple names with different fallback for each name:

```apl
      name2←100
      names←↑'name1' 'name2' 'name3'
      names
name1
name2
name3
      defaults←1 2 3
      ⎕VGET names defaults
1 100 3
```

Multiple names with the same fallback for all of them:

```apl
      persons←(
        (name: 'Jack' ⋄ age: 36)
        (name: 'Peter' ⋄ email: 'peter@example.com')
        (phone: 12345678 ⋄ email: 'susan@example.com')
      )
      persons
 #.[Namespace]  #.[Namespace]  #.[Namespace]
      names←↑'name' 'age' 'email' 'phone'
      names
name
age
email
phone

      ⍝ Lookup information about each person, with a default for missing data
      ↑persons ⎕VGET names (⊂'<no data>')
 Jack              36  <no data>          <no data>
 Peter      <no data>  peter@example.com  <no data>
 <no data>  <no data>  susan@example.com   12345678
```

## Case 2: Vector of Names

Names are specified as character vectors or scalars. `Y` must be one of the following:

* a single name: `R` is the value of that name in the source namespace.
* a single enclosed name: `R` is also the value of the name, but enclosed.
* a single enclosed name-value pair, which is a two-element vector consisting of a character vector name and a fallback value for that name: `R` is the value of the name, or the fallback value in case the name has no value.
* a nested vector where each item is either a name, or a name value pair: `R` is a vector with the same length as `Y`, with the values from the corresponding names, or fallback values.

<h3 class="example">Examples</h3>

Single name:
```apl
      (ns1 ns2)←()()
      (ns1 ns2).name1←'ABC' 'DEF'

      ns1 ⎕VGET 'name1'
ABC
      ns1 'ns2' ⎕VGET 'name1'
 ABC  DEF
```

Single name enclosed:
```apl
      name1←'APL'
      ⎕VGET ⊂'name1'
 APL
      ≢⍴⎕VGET ⊂'name1'
0
```

Multiple names without fallback:
```apl
      (name1 name2 name3)←(1 2 3) () 'APL'

      ⎕VGET 'name1' 'name2' 'name3'
 1 2 3  #.[Namespace]  APL
```

Single name with fallback:
```apl
      ns←()
      ns ⎕VGET ⊂'name1' 'default'
default
```

Multiple names with fallback for some:
```apl
      (name1 name2)←'APL' 123
      ⎕VGET ('name1' 1) 'name2' ('name3' 3)
 APL  123 3
      ⎕EX'name1'
      ⎕VGET ('name1' 1) 'name2' ('name3' 3)
1 123 3
```

Multiple names with different fallback for each of them:
```apl
      name2←100
      ⎕VGET ('name1' 1) ('name2' 2) ('name3' 3)
1 100 3
```

See [Case 1: Name Matrix](#case-1-name-matrix) for an example of multiple names with the same fallback value for all of them.

## Case 3: Nameclasses

`Y` must be a numeric scalar or vector, where each item is a nameclass (see [Name Classification](nc.md)).

If any of the numbers in `Y` are negative, the result `R` is a vector of name-value pairs, one for each existing name in the source namespace with a nameclass from `Y`. Otherwise, `R` is a 2-element nested vector, where the first element is a character matrix of names and the second element is a vector of values. In both cases, `R` is suitable as an argument for [`⎕VGET`](vget.md) and [`⎕VSET`](vset.md).

[`⎕NC`](nc.md) always reports the names of fields in a class as having nameclass `2` (`2.2` with the sub-class), even when the name has no value (might expect `0`) or the field is a namespace reference (might expect `9`). [`⎕VGET`](vget.md) with a right argument of `2` will only include fields that have values that are not references, while a right argument of `9` will include fields that are references. With a right argument of `2.2`, [`⎕VGET`](vget.md) will return all fields that are not undefined.

<h3 class="example">Examples</h3>
Name value pairs:

```apl
      ns←()
      ns.ns1←⎕SE
      ns.ns2←#
      ns.a1←1 2 3
      ns.a2←'APL'
      ns ⎕VGET ¯2
  a1  1 2 3    a2  APL
      ns ⎕VGET ¯2 ¯9
  a1  1 2 3    a2  APL    ns1  ⎕SE    ns2  #
      ↑⎕SE ⎕VGET ¯8
 onClose            0
 onCreate            Dyalog.Callbacks.SECreate
 onFontOK           0
 onFontCancel       0
 onWorkspaceLoaded   Dyalog.Callbacks.WSLoaded
 onSessionPrint     0
 onSessionTrace     0

      ÷0
DOMAIN ERROR: Divide by zero
      ÷0
      ∧
      ↑⎕DMX ⎕VGET ¯2
 Category                                             General
 DM                          DOMAIN ERROR        ÷0        ∧
 EM                                              DOMAIN ERROR
 EN                                                        11
 ENX                                                        1
 HelpURL           https://help.dyalog.com/dmx/20.0/General/1
 InternalLocation                              scalm.cpp  356
 Message                                       Divide by zero
 OSError                                               0 0
 Vendor                                                Dyalog
```

Name matrix and value vector:

```apl
      ]box on
Was OFF
      (name1 name2 name3)←'APL' (1 2 3) ⎕SE
      ⎕VGET 2 9
┌─────┬─────────────────┐
│name1│┌───┬─────┬─────┐│
│name2││APL│1 2 3│ ⎕SE ││
│name3│└───┴─────┴─────┘│
└─────┴─────────────────┘
```
