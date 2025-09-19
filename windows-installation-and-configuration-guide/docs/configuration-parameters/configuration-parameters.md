<h1 class="heading"><span class="name">Configuration Parameters</span></h1>

## Introduction

Dyalog APL is customised using a set of **configuration parameters**. These may be defined  in a number of ways, which take precedence as follows:

- Command-line settings
- Application configuration file settings
- Environment variable settings
- User configuration file settings
- Settings in the registry section defined by the **IniFile** parameter (Windows only)
- Built-in defaults

This scheme provides a great deal of flexibility, and a system whereby you can override one setting with another. For example, you can define your normal workspace size (*maxws*) in the Registry, but override it with a new value specified on the APL command line. The way this is done is described in the following section.

Furthermore, you are not limited to the set of parameters employed by APL itself as you may add parameters of your own choosing.

Although for clarity parameter names are given here in mixed case, they are case-independent under Windows. Under UNIX and Linux, if Dyalog parameters are specified as environment variables they must be named entirely in upper-case.

Note that the value of a parameter obtained by the GetEnvironment method (see [GetEnvironment](../../../object-reference/methodorevents/getenvironment)) uses exactly the same set of rules.

The following section details those parameters that are implemented by Registry Values in the top-level folder identified by **IniFile**. Values that are implemented in sub-folders are *mainly* internal and are not described in detail here. However, any Value that is maintained via a configuration dialog box will be named and described in the documentation for that dialog box in The APL Environment.

## Specifying Size-related Parameters

Several of the configuration parameters define sizes.

The value of the parameter must consist of an integer value, optionally followed immediately by a single character which denotes the units to be used. If the value contains no character the units are assumed to be KiB.

Valid values for units are:

K(KiB), M(MiB), G(GiB), T(TiB), P(PiB) and E(EiB).

Specifying an invalid value will prevent Dyalog APL from starting.

## Changing parameter values in the Registry

You can change parameters in the Registry in one of two ways:

- Using the Configuration dialog box that is obtained by selecting *Configure* from the *Options* menu on the Dyalog APL/W session. See ["The Configuration Dialog Box"](../configuring-the-ide/configuration-dialog/configuration-dialog-general-tab.md) for details.
- By directly editing the Windows Registry using `REGEDIT.EXE` or `REGEDIT32.EXE`. This is necessary for parameters that are not editable via the Configuration dialog box.
