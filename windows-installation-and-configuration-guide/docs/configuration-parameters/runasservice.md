# RunAsService

When RunAsService is set to 1 or 2 (the default is 0) Dyalog APL will not prompt for confirmation when the user logs off, and the interpreter will continue to run across the logoff /logon process. The value 2 reduces the resources used by a Dyalog service by disabling the graphical user-interface features. In this mode, `⎕WC object` will fail with a `LIMIT ERROR` unles the object is Timer, which is the only one that remains enabled.
