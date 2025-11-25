---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SVO SVO
</div>






<h1 class="heading"><span class="name">Shared Variable Offer</span> <span class="command">R←X ⎕SVO Y</span></h1>



This system function offers to share one or more variables with another APL workspace or with another application.  Shared variables are implemented using Dynamic Data Exchange (**DDE**) and may be used to communicate with any other application that supports this protocol.  See *Interface Guide* for further details.


`Y` is a character scalar, vector or matrix.  If it is a vector it contains a name and optionally an external name or surrogate.  The first name is the name used internally in the current workspace.  The external name is the name used to make the connection with the partner and, if specified, must be separated from the internal name by one or more blanks.  If the partner is another application, the external name corresponds to the DDE **item** specified by that application.  If the external name is omitted, the internal name is used instead.  The internal name must be a valid APL name and be either undefined or be the name of a variable.  There are no such restrictions on the content of the external name.



Instead of an external name, `Y` may contain the special symbol `'⍎'` separated from the (internal) name by a blank.  This is used to implement a mechanism for sending `DDE_EXECUTE` messages, and is described at the end of this section.


If `Y` is a scalar, it specifies a single 1-character name.  If `Y` is a matrix, each row of `Y` specifies a name and an optional external name as for the vector case.


The left argument `X` is a character vector or matrix.  If it is a vector, it contains a string that defines the **protocol**, the **application** to which the shared variable is to be connected, and the **topic** of the conversation.  These three components are separated by the characters `':'` and `'|'` respectively.  The protocol is currently always `'DDE'`, but future implementations of Dyalog APL may support additional communications protocols if applicable.  If `Y` specifies more than one name, `X` may be a vector or a matrix with one row per row in `Y`.


If the shared variable offer is a general one (server), `X`, or the corresponding row of `X`, should just contain `'DDE:'`. In this case, Dyalog automatically defines the application name and topic to be `dyalog` and `⎕WSID` respectively.


The result `R` is a numeric scalar or vector with one element for each name in `Y` and indicates the "degree of coupling".  A value of 2 indicates that the variable is fully coupled (via a warm or hot DDE link) with a shared variable in another APL workspace, or with a DDE item in another application.  A value of 1 indicates that there is no connection, or that the second application rejected a warm link.  In this case, a transfer of data may have taken place (via a cold link) but the connection is no longer open.  Effectively, APL treats an application that insists on a cold link as if it immediately retracts the sharing after setting or using the value, whichever is appropriate.

<h2 class="example">Examples</h2>
```apl
      'DDE:' ⎕SVO 'X'
1
 
      'DDE:' ⎕SVO 'X SALES_92'
1
 
      'DDE:' ⎕SVO ↑'X SALES_92' 'COSTS_92'
1 1
 
      'DDE:DYALOG|SERV_WS' ⎕SVO 'X'
2
 
      'DDE:EXCEL|SHEET1' ⎕SVO 'DATA R1C1:R10C12'
2
```


A special syntax is used to provide a mechanism for sending `DDE_EXECUTE` messages to another application.  This case is identified by specifying the `'⍎'` symbol in place of the external name.  The subsequent assignment of a character vector to a variable shared with the external name of `'⍎'` causes the value of the variable to be transmitted in the form of a `DDE_EXECUTE` message.  The value of the variable is then reset to 1 or 0 corresponding to a positive or negative acknowledgement from the partner.  In most (if not all) applications, commands transmitted in `DDE_EXECUTE` messages must be enclosed in square brackets `[]`.  For details, see the relevant documentation for the external application.

<h2 class="example">Examples</h2>
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


