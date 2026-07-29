---
search:
  boost: 2
---

# <span>Value Set</span> `{R}←{X}⎕VSET Y`{{key}}

`⎕VSET` enables values to be set for names in a target namespace or target namespaces.

`Y` specifies the names and the values to set for them. It must be one of the following:

* a nested vector or scalar, where each element is a name-value pair. The name must be a simple character vector.
* a two-element nested array, where the first element is a matrix of names and the second element is a vector or scalar of value(s). If multiple names are specified and the value is a scalar, the same value is used for all names.

All names must have nameclass 0, 2, 8 or 9 in the target namespace(s). For more information on nameclasses, see [`⎕NC`](nc.md).

If specified, `X` must be an array that references one or more namespaces. This means that `X` must be one of:

* a simple character scalar or vector identifying the name of a namespace.
* a reference to a namespace.
* an array in which each item is one of the above. If `X` refers to multiple namespaces, then `⎕VSET` processes each item of `X` in ravel order, using the entire right argument `Y`; this is equivalent to `X ⎕VSET¨⊂Y`.

The namespace(s) referenced must already exist, or a `VALUE ERROR` is generated.

If `X` is not specified, the target namespace is the current namespace.

The result `R` is a shy reference to the target namespace(s).

See also [`⎕VGET`](vget.md).

## Examples

Name value pairs:

```apl
      ⎕VSET ('name1' 123) ('name2' (1 2 'hello'))
      name1
123
      name2
1 2  hello

      (ns1 ns2 ns3)←()()()
      ns1 'ns2' ns3 ⎕VSET ('X1' 'X value') ('Y1' 'Y value')
      (ns1 ns2 ns3).(X1 Y1)
  X value  Y value    X value  Y value    X value  Y value
```

Name matrix and value vector:

```apl
      names←↑'name1' 'name2' 'name3'
      names
name1
name2
name3
      values←1 2 3
      ⎕VSET names values
      name1 name2 name3
1 2 3
```

Single name-value pair:

```apl
      ⎕VSET ⊂'name1' (10 20 30)
      ⎕VSET ,⊂'name2' (40 50 60)
      name1
10 20 30
      name2
40 50 60
```

Multiple names, with a single value:

```apl
      names←↑'name1' 'name2' 'name3'
      value←'APL'

      ⎕VSET names (⊂value)
      name1 name2 name3
 APL  APL  APL
```
## Variant Option: Trigger

The `Trigger` variant option specifies whether any [triggers](../../../programming-reference-guide/triggers/triggers) should be run for the modified variables in the target namespace that have triggers attached.
The value must be a Boolean scalar. The default is `1`, meaning that triggers are run.

<h4 class="example">Example</h4>
```apl
      ⎕VR 'trigger'
     ∇trigger arg
[1]   :Implements Trigger name1,name3
[2]   ⎕←'Running trigger for: ',arg.Name
     ∇

      ⍝ name1 has a trigger, name2 does not
      name1←1
Running trigger for: name1
      name2←2

      ⍝ With the trigger option disabled, triggers are not run
      ⎕VSET⍠'Trigger' 0⊢('name1' 1) ('name2' 2) ('name3' 3)

      ⍝ With the trigger option enabled, triggers are run
      ⎕VSET⍠'Trigger' 1⊢('name1' 1) ('name2' 2) ('name3' 3)
Running trigger for: name1
Running trigger for: name3

      ⍝ Without the trigger option, triggers are run (the default)
      ⎕VSET ('name1' 1) ('name2' 2) ('name3' 3)
Running trigger for: name1
Running trigger for: name3
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕VSET VSET
</div>
