# Example: APL as Compute Server for Excel

The following instructions illustrate how APL can act as a "compute server" for Microsoft Excel, using two shared variables. One variable is used to read the data from Excel; the other is used to pass back the result.

Start Excel and enter some NUMBERS into the cells R1C1 to R3C3 of the spreadsheet "SHEET1".

Start Dyalog APL/W and size your windows so that both the Excel window and the APL Session window can be viewed comfortably at the same time.

`)LOAD` the EXCEL workspace. This contains the following functions :

```apl
     ∇ RUN;Z;⎕WSID
[1]    Z←'DDE:EXCEL|SHEET1'⎕SVO 'DATA R1C1:R3C3'
[2]    →(2=Z)/L1
[3]    'No Excel out there ?' ⋄ →0
[4]   L1:
[5]    CALC
[6]    ⎕WSID←'EXCEL'
[7]    Z←'DDE:'⎕SVO 'RESULT ANSWER'
[8]    'Now type "=dyalog|excel!answer" into'
[9]    'cell A4 in your spreadsheet'
[10]  L2:⎕DL 1
[11]   →(2≠⎕SVO 'RESULT')/L2 ⍝Wait for Excel to connect
[12]   'Connected ...'
[13]   '.'⎕WS 'EVENT' 50 'CALLB'
[14]  ⎕DQ '.'
     ∇

```

```apl

     ∇ CALLB MSG
[1]   ⍝ Callback to recalculate when Excel changes DATA
[2]    →(0 0 1 1≡⎕SVS 'DATA')/0
[3]    CALC
     ∇
 
     ∇ CALC;⎕TRAP
[1]    ⎕TRAP←0 'C' '→ERR'
[2]    RESULT←+/,DATA
[3]    →0
[4]   ERR:RESULT←⊂⎕EM ⎕EN
     ∇
```

Type the following statement in the APL Session :

```apl
      RUN
```

Now type "=dyalog|excel!answer" into cell A4 in your spreadsheet

Follow the above instructions to establish a link from APL to cell A4 in your Excel spreadsheet. The result of the computation will be displayed.

Try changing some of the numbers in the spreadsheet and watch as APL re-calculates the sum.

Try entering a character string in cell A1. Note that APL sends back a character string containing `DOMAIN ERROR`.

Use Ctrl+Break or select "Interrupt" from the *Action* menu in the Session window to stop `⎕DQ`.
