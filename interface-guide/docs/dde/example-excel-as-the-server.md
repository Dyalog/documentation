# Example: Excel as the Server

The following instructions will allow you to explore the DDE interface with another application (in this case Microsoft Excel) acting as the server.

Start Excel and enter some data into (say) the cells R1C1 to R4C3 of the spreadsheet "SHEET1". The data can be character strings and/or numbers. Note that if the spreadsheet is NOT called "SHEET1", the function RUN below should be changed accordingly.

Start Dyalog APL/W (clear ws).

Size your windows so that both the Excel window and the APL Session window can be viewed comfortably at the same time.

Type the following statement in the APL Session :
```apl
      'DDE:EXCEL|SHEET1' ⎕SVO 'X R1C1:R4C3'
2
```

The result should be 2. If not, please check that you have typed the expression correctly, and that the name of the topic (SHEET1) corresponds to the spreadsheet name displayed by Excel.

Note that the character between "EXCEL" and "SHEET1" may be the ASCII *pipe* symbol or the APL stile. Also note that in some countries, you use Lnn instead of Rnn to refer to rows in Excel. You may therefore need to use the following expression instead:
```apl
      'DDE:EXCEL|SHEET1' ⎕SVO 'X L1C1:L4C3'
2
```

Remaining in the APL Session, type `X`. It is a matrix containing as many cells as you have requested in the `⎕SVO` statement. If you entered any character strings, `X` will be nested.

Switch to your Excel window and change the data in one or more of the cells.

Switch back to the APL Session and look at `X` again. It will contain the new data.

Look at the state of the shared variable `X` using `⎕SVS`. It indicates that both partners are aware of the current value of `X`.
```apl
      ⎕SVS 'X'
0 0 1 1
```

Now switch to Excel and change the data again. Repeat step 8. Note the result indicates that Excel has changed `X`, but you have not yet referenced it.
```apl
      ⎕SVS 'X'
0 1 0 1
```

Type the expressions :
```apl
      '.' ⎕WS 'EVENT' 50 1
      ⎕DQ'.'
```

Now switch to Excel and change the data again. Note that the `⎕DQ` terminates and returns a result.
```apl
  . 50
```

Switch back to APL and create the following function :
```apl
      ∇ FOO MSG
   [1] 'MSG IS ' MSG
   [2] 'X IS' X
      ∇
```

Then type :
```apl
      '.' ⎕WS 'EVENT' 50 'FOO'
      ⎕DQ'.'
```

Now switch back to Excel and change the data. Note that every time you change a cell, the DDE event fires your callback function `FOO`. In fact the function is fired twice because it itself alters the STATE of `X` by *referencing* it. This causes a second DDE event.

Switch back to APL, and type Ctrl+Break or select "Interrupt" from the *Action* menu to interrupt `⎕DQ`.
