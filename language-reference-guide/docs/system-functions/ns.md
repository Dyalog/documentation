




<h1 class="heading"><span class="name">Namespace</span> <span class="command">{R}←{X}⎕NS Y</span></h1>

The `⎕NS` system function makes it possible to create namespaces, copy elements from one namespace to another, and clone namespaces.

`Y` is one of the following:

* a character array that represents a list of names of objects to be copied into a namespace.
* a ref to a namespace.
* an array produced by the [`⎕OR`](or.md) of a namespace.

If specified, `X` must be an array that identifies one or more namespaces. This means `X` must be one of:

* a simple character scalar or vector identifying the name of a namespace.
* a reference to a namespace.
* an array where each item is one of the above. If `X` refers to multiple namespaces, then `⎕NS` processes each item of `X` in ravel order, using the entire argument `Y`; this is equivalent to `X ⎕NS¨⊂Y`. If `X` is empty, no action is taken.

The result `R` is shy when the system function is invoked dyadically, otherwise its contents are determined by the value of `Y`.

## Case 1

In the first case, `Y` must be a simple character scalar, vector, matrix or a nested vector of character vectors identifying zero or more workspace objects to be copied into the namespace `X`.  The identifiers in `X` and `Y` may be simple names or compound names separated by `'.'` and including the names of the special namespaces `'#'`, `'##'` and `'⎕SE'`.


The namespace `X` is created if it doesn't already exist.  If the name is already in use for an object other than a namespace, APL issues a `DOMAIN ERROR`.


If `X` is omitted, an unnamed namespace is created.


The objects identified in the list `Y` are copied into the namespace `X`.


If `X` is specified, the result `R` is the full name (starting with `#.` or `⎕SE.`) of the namespace `X`. If `X` is omitted, the result `R` is a namespace reference, or *ref*, to an unnamed namespace.


<h2 class="example">Examples</h2>
```apl
      +'X'⎕NS''               ⍝ Create namespace X.
#.X
      ⊢'X'⎕NS'VEC' 'UTIL.DISP'⍝ Copy VEC and DISP to X.
#.X
      )CS X                   ⍝ Change to namespace X.
#.X
      ⊢'Y'⎕NS'#.MAT' '##.VEC' ⍝ Create #.X.Y &copy in
#.X.Y
      ⊢'#.UTIL'⎕NS'Y.MAT'     ⍝ Copy MAT from Y to UTIL #.UTIL.
#.UTIL
      ⊢'#'⎕NS'Y'              ⍝ Copy namespace Y to root.
#

```
```apl
      ⊢''⎕NS'#.MAT'           ⍝ Copy MAT to current space.
#.X
      ⊢''⎕NS''                ⍝ Display current space.
#.X
      ⊢'Z'⎕NS ⎕OR'Y'          ⍝ Create nspace from ⎕OR.
#.X.Z
```
```apl
      NONAME←⎕NS ''           ⍝ Create unnamed nspace
      NONAME
#.[Namespace]
```
```apl
      DATA←⎕NS¨3⍴⊂''         ⍝ Create 3-element vector of
                             ⍝ distinct unnamed nspaces
      DATA
 #.[Namespace]  #.[Namespace]  #.[Namespace]
```

## Case 2


The second case is where `Y` is a ref to a namespace or the `⎕OR` of a namespace.


If `Y` is a ref to or a `⎕OR` of a *GUI* object, `X` must be a valid parent for the GUI object represented by `Y`, or the operation will fail with a `DOMAIN ERROR`.


Otherwise, the result of the operation depends upon the existence of `X`.

- If `X` does not currently exist (name class is 0), `X` is created as a complete copy (clone) of the original namespace represented by `Y`. If `Y` is a ref to or the `⎕OR` of a GUI object or of a namespace containing GUI objects, the corresponding GUI components of `Y` will be instantiated in `X`.
- If `X` is the name of an existing namespace (name class 9), the contents of `Y`, including any GUI components, are merged into `X`. Any items in `X` with corresponding names in `Y` (names with the same path in both `Y` and `X`) will be replaced by the names in `Y`, unless they have a conflicting name class in which case the existing items in `X` will remain unchanged. However, all GUI spaces in `X` will be stripped of their GUI components prior to the merge operation.

`Y` can also be a vector of namespaces, in which case each item of `Y` is processed as explained above, in ravel order. The effect is that the contents of all the namespaces are merged into the target namespace.

<h3 class="example">Examples</h3>
```apl
      original←⎕NS⍬
      original.(A B C)←1 2 3
      cloned←⎕NS original		⍝ cloning a namespace
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

      show ⎕NS defaults jack		⍝ merge defaults and jack
{
  "age": "<no age>",
  "email": "jack@example.com",
  "name": "Jack",
  "phone": "<no phone>"
}
      show ⎕NS defaults person	⍝ merge defaults and person
{
  "age": 42,
  "email": "<no email>",
  "name": "<no name>",
  "phone": 12345678
}

```
## Variant Option: Trigger

The `Trigger` variant option specifies whether any [triggers](../../programming-reference-guide/triggers/triggers) should be run for the modified variables in the target namespace that have triggers attached.
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
