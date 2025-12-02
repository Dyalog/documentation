<h1 class="heading"><span class="name">Dyalog Serial Number</span></h1>

If you have registered your copy of Dyalog or have a commercial licence then you will have been sent a Dyalog serial number; this serial number is individual to you and corresponds to the type of licence that you are entitled to use.

Dyalog Ltd recommends setting the serial number either by editing a file containing the serial number directly or by running a function in a Dyalog Session to update the file containing the serial number. The next time Dyalog is started after setting the serial number, the **DYALOG_SERIAL** environment variable is set to the contents of this file. However, if the **DYALOG_SERIAL** environment variable already exists and has a non-empty value, then its value is not updated.

In a multi-user environment it might be desirable to set the **DYALOG_SERIAL** environment variable in a system configuration file so that the serial number is held in a single location.

To set your Dyalog serial number by editing the serial number file directly, edit the `$HOME/.dyalog/serial`[^1] text file so that it contains just the string `serialnumber`, where `serialnumber` is your Dyalog serial number.

To set your Dyalog serial number from within a Session:
```apl
      ⎕SE.Dyalog.Serial serialnumber
```

where `serialnumber` is your Dyalog serial number. This updates the value stored in the serial number file `$HOME/.dyalog/serial`. To complete the process you must exit and restart the Session.

When you start a Session, your serial number is displayed in the banner. To see your serial number at any time, enter:
```apl
      +2⎕NQ'.' 'GetEnvironment' 'DYALOG_SERIAL'
```

or
```apl
      ⎕SE.Dyalog.Serial ''
```


!!! note
    Using or entering a serial number other than the one issued to you is not permitted. Transferring the serial number to anyone else is not permitted. For the full licence terms and conditions, see: [https://www.dyalog.com/uploads/documents/Terms_and_Conditions.pdf](https://www.dyalog.com/uploads/documents/Terms_and_Conditions.pdf)

[^1]: $HOME/.dyalog/serial is the default location for your serial number file but you can set the DYALOG_SERIALFILE environment variable to point to any other valid location.
