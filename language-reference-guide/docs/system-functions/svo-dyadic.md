---
search:
  boost: 2
---

# <span>Offer Shared Variable</span> `R←X ⎕SVO Y`{{key}}

This function offers to share variables with another APL workspace or another application, and returns their [degree of coupling](#result). [Monadic `⎕SVO`](svo-monadic.md) returns the degree of coupling without making an offer.

!!! Legacy "Legacy"
    Shared variables are available only under Microsoft Windows, where they communicate through [Dynamic Data Exchange (DDE)](../../interface-guide/dde/introduction.md). `⎕SVO` is retained for backwards compatibility purposes. [COM](../../interface-guide/ole-client/introduction.md) has largely superseded DDE, and Dyalog Ltd recommends COM for new applications.

<h2 class="example">Examples</h2>

A general offer shares `X` with any client:

```apl
      'DDE:' ⎕SVO 'X'
1
      'DDE:' ⎕SVO 'X SALES_92'
1
      'DDE:' ⎕SVO ↑'X SALES_92' 'COSTS_92'
1 1
```

A specific offer shares `X` with another APL workspace, or with a range of cells in Microsoft Excel:

```apl
      'DDE:DYALOG|SERV_WS' ⎕SVO 'X'
2
      'DDE:EXCEL|SHEET1' ⎕SVO 'DATA R1C1:R10C12'
2
```

## Left Argument

`X` identifies the partner, as a character vector of the form `'DDE:application|topic'`, where `DDE` is the protocol, `application` is the DDE server application, and `topic` is the topic of the conversation. If `Y` names several variables, `X` can be a matrix with the partner for the corresponding row of `Y` in each row.

A specific offer names the application and topic, and makes the workspace a DDE client. A general offer, `'DDE:'` on its own, makes the workspace a DDE server, which any client can share the variable with. The application and topic of a general offer are `dyalog` and the value of [`⎕WSID`](wsid.md).

## Right Argument

`Y` is a character scalar, vector, or matrix of the variables to share. A vector holds one name, which can be followed by one or more blanks and the variable's external name, also called its surrogate. A matrix holds one name, and optionally its external name, in each row. A scalar is a one-character name.

The name is the name of the variable in the workspace. It must be a valid APL name, and either undefined or the name of a variable. The external name is the name with which the partner shares the variable, and can contain any characters. If the partner is another application, the external name is the DDE item of that application. If the external name is omitted, the name is used instead.

Instead of an external name, `'⍎'` makes the variable [execute commands](#executing-commands) in the partner.

## Result

`R` is a numeric vector with the degree of coupling of each name in `Y`:

|Degree|Meaning|
|------|-------|
|`2`|The variable is coupled, through a warm or hot DDE link, with a shared variable in another APL workspace or with a DDE item in another application|
|`1`|The variable has been offered, but is not coupled|
|`0`|The name is not that of a shared variable|

## Executing Commands

When `'⍎'` is the external name of a variable, assigning a character vector to the variable sends the vector to the partner as a `DDE_EXECUTE` message. The variable then becomes `1` or `0`, according to whether the partner acknowledges the message positively or negatively. Most applications require each command in a `DDE_EXECUTE` message to be enclosed in square brackets (`[]`). The documentation of the partner application describes the commands that it accepts.

```apl
      'DDE:EXCEL|SYSTEM' ⎕SVO 'X ⍎'
2
      X←'[OPEN("c:\mydir\mysheet.xls")]'
      X
1
      X←'[SELECT("R1C1:R5C10")]'
      X
1
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVO SVO
</div>
