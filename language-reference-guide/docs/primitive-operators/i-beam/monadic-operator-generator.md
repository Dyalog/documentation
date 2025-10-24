
<!-- Hidden search keywords -->
<div style="display: none;">
  43⌶
</div>

<h1 class="heading"><span class="name">Monadic Operator Generator</span> <span class="command">R←43⌶Y</span></h1>

Returns a monadic operator, with functionality determined by the value of `Y`.

`Y` is a scalar integer. Possible values for `Y` are shown in the table below. If an undefined value is specified, a `DOMAIN ERROR` is generated.

`R` is a monadic operator with functionality determined by the value of `Y`.
As `R` is a monadic operator, Dyalog Ltd recommends that the evaluation of this I-Beam is either parenthesised or named.

| `Y` | Returned Operator | Notes |
|---|---                |---|
|632|[Generics Operator](#632-generics-operator)| Requires .NET. |


!!! warning
	The set of supported values for `Y` might change, with existing values being withdrawn as well as new ones being added. This means that saving the resulting operator in a workspace and attempting to run it in a later release might result in a `DOMAIN ERROR` if support has been withdrawn.


### 632 - Generics Operator
The generics operator can create concrete versions of generic classes and execute generic methods. For more information, see the *.NET Interface Guide*.

<h3 class="example">Example</h3>

```apl
      ⎕USING←''

      ⍝ I-Beam call is parenthesised
      IntList←System.Collections.Generic.List (43⌶632) System.Int32

      ⍝ Result of I-Beam call is named
      GenOp←43⌶632
      CharList←System.Collections.Generic.List GenOp System.Char
```
