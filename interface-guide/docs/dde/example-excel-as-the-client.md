# Example: Excel as the Client

The following instructions will allow you to explore the DDE interface with APL acting as the server to another application; in this case Microsoft Excel.

Start APL (clear ws) and type the expressions :

```apl
      )WSID MYWS
      X←12
      'DDE:' ⎕SVO 'X SALES'
```

The workspace MUST have a name as this is broadcast as the DDE **topic**. Note that it is currently essential that `X` contains a value before you make the offer. The result of `⎕SVO` is 1, indicating that no client has yet joined in the conversation.

Start Excel (empty spreadsheet).

Size your windows so that both the Excel window and the APL Session window can be viewed comfortably at the same time. Do NOT iconify either one.

Select the Excel window and type the following formula into the first cell :

```apl
=dyalog|myws!sales
```

the value of `X` (12) will now appear in the cell.

Switch to the APL Session and type :

```apl
      ⎕SVO'X'
2
```

Notice that now that Excel has made the connection, the degree of coupling is 2.

Now type :

```apl
      X←34
```

You will immediately see the new value appear in your spreadsheet.

Create the following function in your workspace :

```apl
     ∇ FOO MSG
[1]    MSG
[2]    X←⎕AI[2]
     ∇
```

Then type the expressions :

```apl
      '.' ⎕WS 'EVENT' 50 'FOO'

      ⎕DQ '.'
```

The link between Excel and APL is a *warm* link (the type of link is determined by the client, so other applications may behave differently). This means that APL will send the new value of `X` (SALES) to Excel every time it changes. If you have DDESPY.EXE, you can verify what is happening.

To interrupt `⎕DQ`, type Ctrl+Break or select "Interrupt" from the *Action* menu in the Session Window.
