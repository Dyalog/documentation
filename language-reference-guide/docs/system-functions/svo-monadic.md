---
search:
  boost: 2
---

# <span>Query Shared Variable Degree of Coupling</span> `R←⎕SVO Y`{{key}}

This function returns the [degree of coupling](#result) of shared variables, which tells whether a partner has accepted the offer to share them. [Dyadic `⎕SVO`](svo-dyadic.md) offers to share a variable.

!!! Legacy "Legacy"
    Shared variables are available only under Microsoft Windows, where they communicate through [Dynamic Data Exchange (DDE)](../../interface-guide/dde/introduction.md). `⎕SVO` is retained for backwards compatibility purposes. [COM](../../interface-guide/ole-client/introduction.md) has largely superseded DDE, and Dyalog Ltd recommends COM for new applications.

<h2 class="example">Examples</h2>

```apl
      ⎕SVO 'X'
2
      ⎕SVO ↑'X SALES' 'Y' 'JUNK'
2 1 0
```

## Right Argument

`Y` is a character scalar, vector, or matrix of names of shared variables. A vector holds one name, which can be followed by one or more blanks and the variable's external name, also called its surrogate. A matrix holds one name, and optionally its external name, in each row. A scalar is a one-character name.

## Result

`R` is a numeric vector with the degree of coupling of each name in `Y`:

|Degree|Meaning|
|------|-------|
|`2`|The variable is coupled, through a warm or hot DDE link, with a shared variable in another APL workspace or with a DDE item in another application|
|`1`|The variable has been offered, but is not coupled|
|`0`|The name is not that of a shared variable|

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVO SVO
</div>
