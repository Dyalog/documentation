<h1 class="heading"><span class="name">Dyalog Serial Number</span></h1>

If you have registered your copy of Dyalog or have a commercial licence then you will have been sent a Dyalog serial number; this serial number is individual to you and corresponds to the type of licence that you are entitled to use.

The serial number should be entered during the installation process (if you already have a version of Dyalog installed then the installer should pre-populate this field with your serial number). This is recommended because  if you enter it as part of the installation process then all users will automatically detect the same serial number.

If the serial number is not entered during the installation process, then it can be set by running `⎕SE.Dyalog.Serial` from within a Dyalog session. However, each individual user of that installation will have to perform this task.

To set your Dyalog serial number from within a Session:
```apl
      ⎕SE.Dyalog.Serial serialnumber
```

where `serialnumber` is your Dyalog serial number. This updates the registry string value **DYALOG_SERIAL** in `HKEY_CURRENT_USER\Software\Dyalog\Dyalog <version>`[^1]. To complete the process you must exit and restart the Session.

When you start a Session, your serial number is displayed in the banner. To see your serial number at any time, enter:
```apl
      +2⎕NQ'.' 'GetEnvironment' 'DYALOG_SERIAL'
```

or
```apl
      ⎕SE.Dyalog.Serial ''
```

!!! note 
    Using or entering a serial number other than the one issued to you is not permitted. Transferring the serial number to anyone else is not permitted. For the full licence terms and conditions, see: [Terms and Conditions](https://www.dyalog.com/uploads/documents/Terms_and_Conditions.pdf)

[^1]: This string can also be set using regedit but Dyalog Ltd does not recommend this approach.
