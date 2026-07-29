# Shared Variable Principles

Shared Variables are part of the APL standard, although strictly speaking as an optional facility. They provide a comprehensive mechanism for communicating between two APL workspaces, or between APL and a co-operating non-APL application. Despite some conflicts between Shared Variable concepts and DDE, this standard APL mechanism has overriding advantages as the basis for a DDE interface. The main benefit is that Shared Variables provide a **general** basis for developing communications using a variety of protocols, of which DDE is but a single example. Dyalog APL communications are not therefore designed for and limited to DDE, but can be extended to other protocols which are appropriate in different environments.

Most mainframe APL users will already be familiar with Shared Variables and will need no introduction to their concepts. New APL users, or those whose experience has been only of PC-based interpreters, may find the following introduction helpful.

## Introduction

It is easiest to consider Shared Variables between two APL workspaces. A Shared Variable is simply a variable that is common to and visible in two workspaces. Once a variable is shared, its value is the same in both workspaces. Communication is achieved by one workspace assigning a new value to the variable and then the other workspace referencing it. Although there is no explicit **send** or **receive**, it is perhaps easier to think of things in this way. When you assign a value to a shared variable, you are in effect transmitting it to your partner. When you reference a shared variable, you are in fact receiving it from your partner.

This discussion of shared variables will refer to the terms **set** and **use**. The term **set** means to assign a (new) value to a variable, that is, its name appears to the left of an assignment arrow. The term **use** means to refer to the value of a variable, that is, its name appears to the right of an assignment arrow.

## Sharing a Variable

Variables are shared using the system function `⎕SVO`. This is a dyadic function whose right argument specifies the name (or a matrix of names) of the variable, and whose left argument identifies the partner with whom the variable is to be shared. In mainframe APL, you identify the partner by its processor id. For example, the following statement means that you offer to share the variable `X` with processor 123.
```apl
      123 ⎕SVO 'X'
```

A single `⎕SVO` by one workspace is not however sufficient to make a connection. It is necessary that **both** partners make an offer to share the variable. Thus if you are process 345, your partner must complete the coupling by making an equivalent shared variable offer. For example:
```apl
      345 ⎕SVO 'X'
```

The coupling process is symmetrical and there is no specific order in which offers must be made. However, there is a concept known as the *degree of coupling* which is returned as the result of `⎕SVO`. The degree of coupling is simply a count of the number of processes which currently have the variable "on offer". When the first process offers to share the variable, its `⎕SVO` will return 1. When the second follows suit, its `⎕SVO` returns 2. The first process can tell when coupling is complete by calling `⎕SVO` monadically at a later point, as illustrated below.

|Process 345   |Process 123   |
|--------------|--------------|
|`123 ⎕SVO 'X'`|&nbsp;        |
|`1`           |&nbsp;        |
|&nbsp;        |`345 ⎕SVO 'X'`|
|&nbsp;        |`2`           |
|`⎕SVO 'X'`    |&nbsp;        |
|`2`           |&nbsp;        |

In this example, both partners specified exactly whom they wished to share with. These are termed **specific offers**. It is also possible to make a **general offer**, which means that you offer to share a particular variable with **anyone**. Coupling can be established by any other processor that offers to share the same variable with you, but notice that the other processor must make a **specific offer** to couple with your general one. The rule is in fact, that sharing may be established by matching a specific offer with another specific offer, or by matching a specific offer with a general offer. Two general offers cannot establish a connection.

## The State Vector

One of the interesting things about Shared Variables, is that both APL workspaces are equal partners. Either of them is allowed to change the value of a shared variable, thus communication is two way. In any communication of this sort, it is essential to have a mechanism to keep things in step. If not, it is possible for one partner to miss something or to receive the same message twice. In some applications this doesn't matter. For example, if one APL workspace is simply monitoring the current value of a particular currency, it does not matter that a second workspace doesn't see all of the fluctuations as they occur. It is important only that the latest value can be referenced when it is needed. Contrast this with a trading application in which the trading workspace registers each transaction with a second workspace which monitors and stores the transactions on a database. Clearly in this case it is essential that each and every transaction is properly communicated and recorded.

Synchronisation is provided by two system functions, `⎕SVS` and `⎕SVC`. `⎕SVS` reports the current value of a shared variable's **State Vector**. This provides information concerning the state of the variable from each partner's point of view. The second function, `⎕SVC`, allows you and your partner to specify interlocking that enforces the level of synchronisation required by your application.

Each shared variable has a **state vector** which indicates which partner has set a value of which the other is still ignorant, and which partner is aware of the current value. The current state of a shared variable is reported by the monadic system function `⎕SVS`. Its argument is the name of the shared variable. Its result is a 4-element Boolean vector which specifies the current state vector, that is:
```apl
      state ← ⎕SVS name
```

The state vector will have one of the following values:

|---------|---------------------------------------------------------------|
|`0 0 0 0`|The variable is not shared                                     |
|`0 0 1 1`|Both partners know the current value                           |
|`1 0 1 0`|You have set the value, but your partner has yet to use it.    |
|`0 1 0 1`|Your partner has set the variable but you have not yet used it.|

It may not be immediately apparent as to how the information provided by `⎕SVS` can be used. The answer, as we will see later, is that communications generates **events**. That is to say, when your partner sets a shared variable to a new value or references a value that you have set, an event is generated telling you that something has happened. `⎕SVS` is then used to determine what has happened (set or use) and, if you have several variables shared, which one of the variables has in some way changed state. A shared variable state change is thus the trigger that forces some kind of action out of the other process.

## Access Control

`⎕SVS` is not sufficient on its own to synchronise data transfer. For example, what if the two partners both set the shared variable to a different value at **exactly** the same point in time ?  This is the role of `⎕SVC` which actually assures data integrity (if required) by imposing access controls. Its purpose is to synchronise the order in which two applications **set** and **use** the value of a shared variable.

In simple terms, `⎕SVC` allows an application to inhibit its partner from setting a new value before it has read the current one, and/or to inhibit its partner from using a variable again before it has been reset.

`⎕SVC` is a dyadic system function. Its right argument specifies the name of the shared variable; its left argument the access control vector, that is,
```apl
       access ⎕SVC name
```

The access control vector is a 4-element Boolean vector whose elements specify access control as follows:

|-----|-------------------------------------------------------------------------|
|`[1]`|1 means that you cannot set the variable until your partner has used it. |
|`[2]`|1 means that your partner cannot set the variable until you have used it.|
|`[3]`|1 means that you cannot use the variable until your partner has set it.  |
|`[4]`|1 means that your partner cannot use the variable until you have set it. |

In principle, each of the two partners maintains its own copy of the access control vector using `⎕SVC`. Control is actually imposed by the **effective access control vector** which is the result of "ORing" the two individual ones. From your own point of view, the effective access control vector is:
```apl
   (your ⎕SVC)  ∨  (your partner's ⎕SVC)[3 4 1 2]
```

Whenever either of the partners attempts an operation (set or use) on a shared variable, the system consults its effective access control vector. If the vector indicates that the operation is currently permitted, it goes ahead. If however the vector indicates that the operation is currently inhibited, the operation is delayed until the situation changes.

For example, suppose that the effective access control vector is (1 0 0 1). This prevents either partner from setting the shared variable twice in a row, without an intervening use by the other. The purpose of this is to prevent loss of data. Suppose now that one workspace assigns the value 10 to the shared variable (which is called `DATA`), that is:
```apl
      DATA ← 10
```

Then, before the partner has referenced the new value it attempts to execute the statement:
```apl
      DATA ← 20
```

APL will **not** execute the statement. Instead it will wait (indefinitely if required) until the partner has received the first value (10). Only then will the second assignment be executed and processing continued. Effectively one workspace stops and waits for the other to catch up.

Similarly, suppose that the effective access control vector is (0 0 1 1). This means that neither partner can **use** the variable twice in succession without an intervening **set** by the other. This type of control is appropriate where each **set** corresponds to an individual transaction, and you want to prevent transactions from inadvertently being duplicated.

Suppose now that one workspace references the shared variable (which is called `DATA`), that is:
```apl
      TRANSACTION ← DATA
```

Then, soon after, it executes the statement again, but without an intervening **set** by its partner, that is:
```apl
      TRANSACTION ← DATA
```

This time, the reference to `DATA` is inhibited, and the workspace waits (indefinitely if necessary) until the partner has assigned a new value. Only then will the second reference be executed and processing continued. Again, one workspace stops and waits for the other.

The purpose of `⎕SVC` is to synchronise data transfer. It is particularly useful where timing considerations would otherwise cause data loss. However, an incorrect application which makes inappropriate use of `⎕SVC` may hang.

A second type of problem can occur during the development of an application that uses shared variables. If the program is interrupted by an error, an attempt to display the value of a shared variable counts as a "use" and, if inhibited, will hang. In applications that use interlocking, it is recommended that a shared variable is explicitly "used" by making an assignment to a temporary variable which can then be referenced freely.

This is the theory; we will now see how DDE, by its very nature, imposes certain limitations in practice.
