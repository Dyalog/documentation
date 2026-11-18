---
search:
  boost: 2
---

# <span>Retract Shared Variable Offer</span> `R←⎕SVR Y`{{key}}

This function ends the sharing of variables, whether a partner has accepted the offer to share them or not. Afterwards, each name is no longer that of a shared variable, and a partner's variable stays offered, with the degree of coupling `1`. Expunging a shared variable with [`⎕EX`](ex.md), or leaving a function in which it is localised, also ends the sharing.

!!! Legacy "Legacy"
    Shared variables are available only under Microsoft Windows, where they communicate through [Dynamic Data Exchange (DDE)](../../interface-guide/dde/introduction.md). `⎕SVR` is retained for backwards compatibility purposes. [COM](../../interface-guide/ole-client/introduction.md) has largely superseded DDE, and Dyalog Ltd recommends COM for new applications.

<h2 class="example">Example</h2>

A workspace with the `⎕WSID` `SERVER` has made a general offer to share a variable with the external name `EXTNAME`:

```apl
      'DDE:DYALOG|SERVER' ⎕SVO 'Y EXTNAME'
2
      ⎕SVR 'Y'
2
      ⎕SVO 'Y'
0
```

## Right Argument

`Y` is a character scalar, vector, or matrix of names of shared variables. A vector holds one name, which can be followed by one or more blanks and the variable's external name, also called its surrogate. A matrix holds one name, and optionally its external name, in each row. A scalar is a one-character name.

## Result

`R` is a numeric vector with the degree of coupling of each name in `Y` before the retraction:

|Degree|Meaning|
|------|-------|
|`2`|The variable is coupled, through a warm or hot DDE link, with a shared variable in another APL workspace or with a DDE item in another application|
|`1`|The variable has been offered, but is not coupled|
|`0`|The name is not that of a shared variable|

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVR SVR
</div>
