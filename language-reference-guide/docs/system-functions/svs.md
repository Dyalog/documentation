---
search:
  boost: 2
---

# <span>Query Shared Variable State</span> `R←⎕SVS Y`{{key}}

This function returns the [state vectors](#state-vector) of shared variables, which tell whether you and your partner know the current value of each.

!!! Legacy "Legacy"
    Shared variables are available only under Microsoft Windows, where they communicate through [Dynamic Data Exchange (DDE)](../../interface-guide/dde/introduction.md). `⎕SVS` is retained for backwards compatibility purposes. [COM](../../interface-guide/ole-client/introduction.md) has largely superseded DDE, and Dyalog Ltd recommends COM for new applications.

<h2 class="example">Examples</h2>

```apl
      ⎕SVS 'X'
0 1 0 1
      ⎕SVS ↑'X SALES' 'Y' 'JUNK'
0 0 1 1
1 0 1 0
0 0 0 0
```

## Right Argument

`Y` is a character scalar, vector, or matrix of names of shared variables. A vector holds one name, which can be followed by one or more blanks and the variable's external name, also called its surrogate. A matrix holds one name, and optionally its external name, in each row. A scalar is a one-character name.

## Result

If `Y` names one shared variable, `R` is its state vector, a 4-item Boolean vector. If `Y` is a matrix, `R` is a Boolean matrix with the state vector of the variable in each row of `Y`.

## State Vector

A shared variable is in one of these states:

|State vector|Meaning|
|------------|-------|
|`0 0 1 1`|You and your partner both know the current value, and neither has set the variable since|
|`1 0 1 0`|You have set the variable, and your partner has not used it yet|
|`0 1 0 1`|Your partner has set the variable, and you have not used it yet|
|`0 0 0 0`|The variable is not shared with a partner, because no partner has accepted the offer to share it, or because the name is not that of a shared variable|

When a variable is first coupled, its state vector is `1 0 1 0` in the server and `0 1 0 1` in the client. This means that the server has set the variable, and that the client has not used it yet.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVS SVS
</div>
