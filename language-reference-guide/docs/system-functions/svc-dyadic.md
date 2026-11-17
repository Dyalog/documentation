---
search:
  boost: 2
---

# <span>Set Shared Variable Access Control</span> `R←X ⎕SVC Y`{{key}}

This function sets your [access control vectors](#access-control) of shared variables, and returns the resulting effective access control vectors. [Monadic `⎕SVC`](svc-monadic.md) returns them without changing them.

!!! Legacy "Legacy"
    Shared variables are available only under Microsoft Windows, where they communicate through [Dynamic Data Exchange (DDE)](../../interface-guide/dde/introduction.md). `⎕SVC` is retained for backwards compatibility purposes. [COM](../../interface-guide/ole-client/introduction.md) has largely superseded DDE, and Dyalog Ltd recommends COM for new applications.

<h2 class="example">Examples</h2>

```apl
      1 0 0 1 ⎕SVC 'X'
1 0 0 1
      1 ⎕SVC 'X EXTNAME'
1 1 1 1
```

A matrix sets a different access control vector for each name:

```apl
      ac←[1 0 0 1
          0 1 1 0]
      ac ⎕SVC ↑'ONE' 'TWO'
1 1 1 1
0 1 1 0
```

## Left Argument

`X` is a Boolean scalar, vector, or matrix. A 4-item vector is the access control vector for every name in `Y`, and a 4-column matrix has the access control vector for the corresponding row of `Y` in each row. A scalar or a 1-item vector stands for a 4-item vector with that value in each item.

## Right Argument

`Y` is a character scalar, vector, or matrix of names of shared variables. A vector holds one name, which can be followed by one or more blanks and the variable's external name, also called its surrogate. A matrix holds one name, and optionally its external name, in each row. A scalar is a one-character name.

## Result

If `Y` names one shared variable, `R` is its new effective access control vector, a 4-item Boolean vector, whatever the shape of `X`. If `Y` is a matrix, `R` is a Boolean matrix with the new effective access control vector of the variable in each row of `Y`. A name that is not that of a shared variable, or that has the wrong external name, gives `0 0 0 0`.

## Access Control

Access control vectors control the order in which you and your partner can set a shared variable (assign a new value to it) and use it (refer to its value). Each item of an access control vector that is `1` imposes a restriction:

|Item|Restriction when `1`|
|----|--------------------|
|1|You cannot set a new value until your partner has used or set the variable|
|2|Your partner cannot set a new value until you have used or set the variable|
|3|You cannot use the value until your partner has set the variable|
|4|Your partner cannot use the value until you have set the variable|

A set or use that the access control does not allow waits until it is allowed. Therefore, an application that uses access control inappropriately can hang.

You and your partner each set an access control vector. Your partner's restrictions on its partner are restrictions on you, and the other way round. Therefore, your effective access control vector is `mine∨partner[2 1 4 3]`, where `mine` is your access control vector and `partner` is your partner's. This means that you cannot clear a restriction that your partner has set. For example, when your partner sets `1 0 0 1`, your effective access control vector includes `0 1 1 0`. Your partner's access control vector is normally `0 0 0 0`. However, a non-APL client application that establishes a hot DDE link has the access control vector `1 0 0 1`, which stops either partner from setting the variable twice without an intervening use or set by the other. To stop the application from setting a value twice, APL delays its acknowledgement of the DDE message that contains the second value until the workspace uses the variable. Therefore, an application that waits for the acknowledgement hangs until then, and an application that does not wait carries on.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVC SVC
</div>
