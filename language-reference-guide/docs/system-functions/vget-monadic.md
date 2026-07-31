---
search:
  boost: 2
---

# <span>Get Value from Current Namespace</span> `R←⎕VGET Y`{{key}}

`⎕VGET` enables values to be read for names in a source namespace or source namespaces. Optionally, a fallback value can be used if the name requested is undefined.

`Y` specifies the names. It must be one of the following:

* a matrix of names or a matrix of names and a value vector – see [Case 1: Name Matrix](#case-1-name-matrix).
* a vector of names or name-value pairs – see [Case 2: Vector of Names](#case-2-vector-of-names).
* a vector of nameclasses – see [Case 3: Nameclasses](#case-3-nameclasses).

All specified names must be either undefined, or have an array value in the source namespace(s). If `Y` specifies a matrix or a vector of names, fallback values to use in cases where a name has no value can also be specified to prevent a `VALUE ERROR` from being generated.

The source namespace is the current namespace.

The result `R` depends on the format of `Y`.

See also [`⎕VSET`](vset-monadic.md).

## Case 1: Name Matrix

Names are specified as rows in a character matrix.
`Y` must be either:

* a character matrix, where each row is a name.
* a two element vector, where the first item is a character matrix of names and the second item is a specification of fallback values.

The fallback values must be one of the following:

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

Multiple names with a different fallback for each name:

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

## Case 2: Vector of Names

Names are specified as character vectors or scalars. `Y` must be one of the following:

* a single name: `R` is the value of that name in the source namespace.
* a single enclosed name: `R` is also the value of the name, but enclosed.
* a single enclosed name-value pair, which is a two-element vector consisting of a character vector name and a fallback value for that name: `R` is the value of the name, or the fallback value in case the name has no value.
* a nested vector where each item is either a name, or a name value pair: `R` is a vector with the same length as `Y`, with the values from the corresponding names, or fallback values.

<h3 class="example">Examples</h3>

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

Multiple names with fallback for some:
```apl
      (name1 name2)←'APL' 123
      ⎕VGET ('name1' 1) 'name2' ('name3' 3)
 APL  123 3
      ⎕EX'name1'
      ⎕VGET ('name1' 1) 'name2' ('name3' 3)
1 123 3
```

Multiple names with a different fallback for each of them:
```apl
      name2←100
      ⎕VGET ('name1' 1) ('name2' 2) ('name3' 3)
1 100 3
```

See [Case 1: Name Matrix](#case-1-name-matrix) for an example of multiple names with the same fallback value for all of them.

## Case 3: Nameclasses

`Y` must be a numeric scalar or vector, where each item is a nameclass (see [Name Classification](nc.md)).

If any of the numbers in `Y` are negative, the result `R` is a vector of name-value pairs, one for each existing name in the source namespace with a nameclass from `Y`. Otherwise, `R` is a 2-element nested vector, where the first element is a character matrix of names and the second element is a vector of values. In both cases, `R` is suitable as an argument for [`⎕VGET`](vget-monadic.md) and [`⎕VSET`](vset-monadic.md).

[`⎕NC`](nc.md) always reports the names of fields in a class as having nameclass `2` (`2.2` with the sub-class), even when the name has no value (might expect `0`) or the field is a namespace reference (might expect `9`). [`⎕VGET`](vget-monadic.md) with a right argument of `2` will only include fields that have values that are not references, while a right argument of `9` will include fields that are references. With a right argument of `2.2`, [`⎕VGET`](vget-monadic.md) will return all fields that are not undefined.

<h3 class="example">Examples</h3>
Name matrix and value vector:

```apl
      ]Boxing on
Was OFF
      (name1 name2 name3)←'APL' (1 2 3) ⎕SE
      ⎕VGET 2 9
┌─────┬─────────────────┐
│name1│┌───┬─────┬─────┐│
│name2││APL│1 2 3│ ⎕SE ││
│name3│└───┴─────┴─────┘│
└─────┴─────────────────┘
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕VGET VGET
</div>
