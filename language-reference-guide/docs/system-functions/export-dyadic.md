---
search:
  boost: 2
---

# <span>Set Export Type</span> `{R}←X ⎕EXPORT Y`{{key}}

This function sets the export type of functions and operators, which determines whether the [`⎕PATH`](path.md) mechanism finds them. [Monadic `⎕EXPORT`](export-monadic.md) reports the export type, and describes the [export types](export-monadic.md#export-types).

!!! Legacy "Legacy"
    `⎕EXPORT` is retained for backwards compatibility purposes. Dyalog Ltd recommends referring to a function or operator in another namespace by its full (absolute or relative) namespace path instead.

<h2 class="example">Example</h2>

In the namespace `utils`, the function `Average` calls the function `Sum`. Setting the export type of `Sum` to `0` makes `⎕PATH` find `Average` but not `Sum`:

```apl
      'utils'⎕NS''
      utils.⎕FX 'r←Average y' 'r←(Sum y)÷≢y'
      utils.⎕FX 'r←Sum y' 'r←+/y'
      0 utils.⎕EXPORT ⊂'Sum'
      ⎕PATH←'utils'
      Average 1 2 3 4
2.5
      Sum 1 2 3 4
VALUE ERROR: Undefined name: Sum
      Sum 1 2 3 4
      ∧
```

## Left Argument

`X` is an integer scalar or vector of [export types](export-monadic.md#export-types), `0` or `1`, with one item per name in `Y`. A scalar or 1-item vector applies to every name.

## Right Argument

`Y` contains the names of functions and operators, in any of the forms that [monadic `⎕EXPORT`](export-monadic.md#right-argument) accepts.

## Result

`R` is an integer vector of the export types that were set, with one item per name in `Y`, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕EXPORT EXPORT
</div>
