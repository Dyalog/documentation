---
search:
  exclude: true
---

# Native Look and Feel

Windows *Native Look and Feel* is an optional feature of Windows. It is enabled by default in Dyalog Version 15.0. In previous Versions, it was disabled by default. It may be that the ability to disable *Native Look and Feel* cannot be supported in future versions.

When *Native Look and Feel* is enabled, user-interface controls such as Buttons take on a different appearance and certain controls (such as the ListView) provide enhanced features.

## Dyalog Session

During development, both the Dyalog Session and the Dyalog APL GUI  displays native style buttons, combo boxes, and other GUI components if *Native Look and Feel* is enabled. The option is provided in the *General* tab of the *Configuration* dialog.

## Applications

There are two ways to disable *Native Look and Feel* in end-user applications.

If you use the *File/Export…* menu item on the Session MenuBar  to create a bound executable, an OLE Server (in-process or out-of-process), an ActiveX Control or a .NET Assembly, clear the option box labelled *Enable Native Look and Feel* in the *create bound file* dialog box. See  .

If not, set the **XPLookandFeel** parameter to 0, when you run the program. For example:
```apl
dyalogrt.exe XPLookAndFeel=0 myws.dws
```

**Note that to have effect, Native Look and Feel must also be enabled at the Windows level.**
