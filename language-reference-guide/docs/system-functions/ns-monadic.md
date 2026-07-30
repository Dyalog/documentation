---
search:
  boost: 2
---

# <span>Create/Clone Namespace</span> `{R}←⎕NS Y`{{key}}

The `⎕NS` system function makes it possible to create namespaces, copy elements from one namespace to another, and clone namespaces.

`Y` is one of the following:

* an vector of zero or more objects to be copied.
* an array containing references to, and/or [`⎕OR`](or.md)s of, one or more namespaces.

The result `R` is shy when the system function is invoked dyadically, otherwise its contents are determined by the value of `Y`.

## Usage

`⎕NS` is used to create or populate one or more namespaces based on either a list of members to be copied into the target namespace(s), or a list of objects to be merged into the target namespace(s).

### Case 1: Create or Populate Namespace from Member List

`Y` must be a simple character scalar, vector, matrix, or a nested vector of character vectors identifying zero or more workspace objects to be copied into the new namespace. The identifiers in `Y` can be simple names or compound names separated by `'.'` and including the names of the special namespaces `'#'`, `'##'` and `'⎕SE'`.

The objects identified in the list `Y` are copied into the new namespace.

The result `R` is a namespace reference to an unnamed namespace.

<h4 class="example">Examples</h4>

```apl
      ⎕←'X'⎕NS''                 ⍝ Create namespace X
#.X
      ⎕←'X'⎕NS'VEC' 'UTIL.DISP'  ⍝ Copy VEC and DISP to X
#.X
      )CS X                      ⍝ Change to namespace X
#.X
      ⎕←'Y'⎕NS'#.MAT' '##.VEC'   ⍝ Create #.X.Y and copy in
#.X.Y
      ⎕←'#.UTIL'⎕NS'Y.MAT'       ⍝ Copy MAT from Y to UTIL #.UTIL
#.UTIL
      ⎕←'#'⎕NS'Y'                ⍝ Copy namespace Y to root
#
```

```apl
      ⎕←''⎕NS'#.MAT'           ⍝ Copy MAT to current space
#.X
      ⎕←''⎕NS''                ⍝ Display current space
#.X
```

```apl
      NONAME←⎕NS ''           ⍝ Create unnamed namespace
      NONAME
#.[Namespace]
```

```apl
      DATA←⎕NS¨3⍴⊂''         ⍝ Create 3-element vector of
                             ⍝ distinct unnamed nspaces
      DATA
 #.[Namespace]  #.[Namespace]  #.[Namespace]
      'one' 'two' ⎕NS 'DATA'
      one.⎕NL ¯2
 DATA
```

## Case 2: Create or Populate Namespace from Object List

`Y` is one or more references to, or `⎕OR`s of, namespaces.

A new namespace is created as a complete copy (clone) of the original namespace represented by `Y`.

`Y` can also be a vector of namespaces, in which case each item of `Y` is processed as explained above, in ravel order. The effect is that the contents of all the namespaces are merged into the target namespace.

<h4 class="example">Examples</h4>

```apl
      original←⎕NS⍬
      original.(A B C)←1 2 3
      'new' ⎕NS ⎕OR'original'  ⍝ cloning a namespace from ⎕OR
      new.A
1
      cloned←⎕NS original  ⍝ cloning a namespace from reference
      cloned.D←4

      original.⎕NL ¯2
 A  B  C
      cloned.⎕NL ¯2
 A  B  C  D
```

```apl
      defaults←(
        name: '<no name>'
        age: '<no age>'
        phone: '<no phone>'
        email: '<no email>'
      )
      jack←(name: 'Jack' ⋄ email: 'jack@example.com')
      person←(age: 42 ⋄ phone: 12345678)
      show←⎕JSON⍠'Compact' 0

      show ⎕NS defaults jack  ⍝ merge defaults and jack
{
  "age": "<no age>",
  "email": "jack@example.com",
  "name": "Jack",
  "phone": "<no phone>"
}
      show ⎕NS defaults person  ⍝ merge defaults and person
{
  "age": 42,
  "email": "<no email>",
  "name": "<no name>",
  "phone": 12345678
}

```
### Variant Option: Trigger

The `Trigger` variant option specifies whether any [triggers](../../../programming-reference-guide/triggers/triggers) should be run for the modified variables in the target namespace that have triggers attached.
The value must be a Boolean scalar. The default is 0, meaning that triggers are not run.

<h4 class="example">Example</h4>

```apl
      ⎕VR 'trigger'
     ∇trigger arg
[1]   :Implements Trigger X,Y
[2]   ⎕←'Running trigger for: ',arg.Name
     ∇

      newValues←(Y: 1 ⋄ Z: 2)

      ⍝ ⎕NS without running triggers
      ⎕THIS ⎕NS newValues
      ⎕THIS ⎕NS⍠'Trigger' 0⊢newValues

      ⍝ ⎕NS running triggers
      ⎕THIS ⎕NS⍠'Trigger' 1⊢newValues
Running trigger for: Y
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NS NS
</div>
