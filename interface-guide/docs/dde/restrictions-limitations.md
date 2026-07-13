# Restrictions and Limitations

Although shared variables have been implemented as closely to the APL standard as is possible, certain restrictions are imposed by the nature of DDE itself.

The server cannot make an offer to a specific client. Instead, it must broadcast a "general" offer, which could be accepted by any client. Indeed neither the client nor the server can specifically identify the other task.

Dyalog supports Excel "Fast Table Format" for communications with Microsoft Excel (and with any other application that supports this format). This imposes the following restrictions :

- The maximum number of numbers that you can send to Excel is 8191. Any attempt to send more will result in a LENGTH ERROR. This is because APL currently tries to send all the data in a single block. Larger amounts of data can be received from Excel, because Excel will send several blocks if required. The restriction may be lifted in due course.
- The maximum length of a character vector (which represents a string within a cell) is 255.

A client APL program can only use indexed assignment to change the value of a shared variable if it already knows the up-to-date value of the variable, that is, if its `⎕SVS` is 0 0 1 1 or 1 0 1 0. An attempt to use indexed assignment on a variable whose `⎕SVS` is 0 1 0 1 will cause a NONCE error.

Consider Excel as a server and APL as client with several warm links to an Excel spreadsheet. For example:
```apl
      'DDE:EXCEL|SHEET1' ⎕SVO 'X R1C1'
      'DDE:EXCEL|SHEET1' ⎕SVO 'Y R2C2'
      'DDE:EXCEL|SHEET1' ⎕SVO 'Z R3C3'
```

If R1C1 is changed in Excel, APL expects to be told only of that change. Instead, Excel tells APL that ALL the linked cells have changed.

If APL pokes a value back to R1C1, Excel again tells APL that ALL the linked cells have changed.

You must take care to avoid this problem when dealing with DDE between Excel and APL.
