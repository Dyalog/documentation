---
search:
  boost: 2
---

# <span>Set Value in Namespace</span> `{R}←X ⎕VSET Y`{{key}}

`⎕VSET` enables values to be set for names in a target namespace or target namespaces.

`Y` specifies the names and the values to set for them. It must be one of the following:

* a nested vector or scalar, where each element is a name-value pair. The name must be a simple character vector.
* a two-element nested array, where the first element is a matrix of names and the second element is a vector or scalar of value(s). If multiple names are specified and the value is a scalar, the same value is used for all names.

All names must have nameclass 0, 2, 8 or 9 in the target namespace(s). For more information on nameclasses, see [`⎕NC`](nc.md).

`X` must be an array that references one or more namespaces. This means that `X` must be one of:

* a simple character scalar or vector identifying the name of a namespace.
* a reference to a namespace.
* an array in which each item is one of the above. If `X` refers to multiple namespaces, then `⎕VSET` processes each item of `X` in ravel order, using the entire right argument `Y`; this is equivalent to `X ⎕VSET¨⊂Y`.

The namespace(s) referenced must already exist, or a `VALUE ERROR` is generated.

The result `R` is a shy reference to the target namespace(s).

See also [`⎕VGET`](vget-monadic.md).

## Examples

Name value pairs:

```apl
      name1
123
      name2
1 2  hello

      (ns1 ns2 ns3)←()()()
      ns1 'ns2' ns3 ⎕VSET ('X1' 'X value') ('Y1' 'Y value')
      (ns1 ns2 ns3).(X1 Y1)
  X value  Y value    X value  Y value    X value  Y value
```

## Variant Option: Trigger

The `Trigger` variant option specifies whether any [triggers](../../../programming-reference-guide/triggers/triggers) should be run for the modified variables in the target namespace that have triggers attached.
The value must be a Boolean scalar. The default is `1`, meaning that triggers are run.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕VSET VSET
</div>
