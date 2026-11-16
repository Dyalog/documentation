---
search:
  exclude: true
---

# <span>Export Type</span> `⎕EXPORT`

`⎕EXPORT` deals with the export type of functions and operators, which determines whether the [`⎕PATH`](path.md) mechanism finds them.

!!! Legacy "Legacy"
    `⎕EXPORT` is retained for backwards compatibility purposes. Dyalog Ltd recommends referring to a function or operator in another namespace by its full (absolute or relative) namespace path instead.

## Query Export Type

[Monadic `⎕EXPORT`](export-monadic.md) reports the export types:

```apl
      utils.⎕EXPORT 'Average' 'Sum'
1 0
```

## Set Export Type

[Dyadic `⎕EXPORT`](export-dyadic.md) sets the export types:

```apl
      0 utils.⎕EXPORT 'Sum'
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕EXPORT EXPORT
</div>
