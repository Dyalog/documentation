<h1 class="heading"><span class="name">Configuration Files</span></h1>

## Introduction

A configuration file is an optional text file containing configuration parameters and their values. It may cascade, that is, it can extend (inherit) configuration values from other configuration files, and supplement and/or override them.

Configuration files use JSON5 (a superset of standard JSON) syntax, as described below. These files are portable across all systems supported by Dyalog.

Although it is possible to include user credentials such as login details or passwords in configuration files, Dyalog very strongly recommends against doing this even if the credentials are encrypted as this should be considered to be a very significant security risk.

**Names of configuration parameters defined in Configuration files may be specified in any combination of alphabetic case.**

Dyalog processes up to two kinds of configuration file (each of which may cascade):

1. An application configuration file which contains configuration values associated with a specific application
2. A user configuration file which defines configuration values for the current, and possibly only, user of the system.

## Application Configuration File

When Dyalog starts, it derives the name of the application configuration file as follows:

- The name in the configuration parameter **ConfigFile** if it is set, otherwise
- The name of the workspace or script loaded at start-up using the **Load** parameter, with the extension replaced by `.dcfg`, if that file exists, otherwise
- Nothing.

## User Configuration File

The name of the user configuration file is specified by the **UserConfigFile**  parameter. Under Windows, this parameter is not set by default but may be defined by the user.

## Precedence

Configuration files supplement existing methods of defining  parameters. The following precedence table shows the order of precedence when a setting is defined in multiple places:

- Command-line settings override
- Application configuration file settings, which override
- Environment variable settings, which override
- User configuration file settings, which override
- Settings in the registry (Windows only), which override
- Built-in defaults

## Configuration Files and The Configuration Dialog

The Configuration Dialog reflects the values of parameters stored in the Windows Registry and ignores overriding values defined on the command-line, in configuration files or in environment variables. If the user changes parameters using the Configuration Dialog, the new values are recorded in the Registry, but remain overridden by those that take precedence.

## Configuration File Structure

Configuration files define configuration parameters using JSON5. A JSON object contains data in the form of key/value pairs and other JSON objects. The keys are strings and the values are the JSON types. Keys and values are separated by colon. Each entry (key/value pair) is separated by comma.

The top-level object defines an optional key named **Extend** and an optional object named **Settings**.

**Extend** is a string value containing the name of a configuration file to import. The extended (imported) file may in turn extend another configuration file. Configuration values from the imported file(s) may be overridden by redefining them. The file name is implicitly relative to the name of the file which imports it. Any file name extension must be explicitly specified.

**Settings** is an object containing the names of configuration parameters and their values. The values may be:

- A string
- A number
- An array of strings

The names and values correspond to configuration parameters, but names are not case sensitive. Any named values may be defined; an APL application may query the values using `+2⎕NQ'.' 'GetEnvironment' name`, or using the `]Config` user command. Note that `GetEnvironment` returns the value in use as defined by the precedence rules (see **Precedence above**).

<h3 class="example">Example</h3>
```apl
      +2 ⎕NQ '.' 'GetEnvironment' ('MaxWS' 'Captions\Session')
┌────┬───────────────────────┐
│256M│My Dyalog V18.0 Session│
└────┴───────────────────────┘
      ]Config MaxWS Captions\Session
┌────────────────┬───────────────────────┐
│MaxWS           │256M                   │
├────────────────┼───────────────────────┤
│Captions\Session│My Dyalog V18.0 Session│
└────────────────┴───────────────────────┘

```

A warning will be given if names  are redefined in the same configuration file; the second and subsequent definitions will be discarded.

## File Names

Pathnames specified in configuration files should be specified using portable forward slashes "/" rather than back-slashes "\" as the latter are used as escape characters by JSON.

`WSPATH: ["c:/Dyalog18.0"]` or  `WSPATH: ["c:\\Dyalog18.0"]` specifies the file `c:\Dyalog18.0`.

whereas,

`WSPATH: ["c:\Dyalog18.0"]` means  `c:Dyalog18.0`.

<h4 class="example">Example</h4>
```apl
{
  Extend: "my_default_configuration.dcfg",
  
  Settings: {
      // maximum workspace
      MAXWS: "2GB",
      WSPATH: ["/dir1", "/dir2", ""],      
      UserOption: 123,
      ROOTDIR: "/my/root/directory",
      // references to other configuration parameters
      FNAME: "[rootdir]/filename",
  }
}
```

## Arrays

An array may be used to define file paths etc. For example,
```apl
WSPATH: ["/dir1", "/dir2"]
```

The only parameters which may be defined as arrays are **WSPATH**, **WSEXT** and **CFEXT**.

#### References to other Configuration Parameters

Configuration parameters which are string values may include references to other configuration parameters (regardless of where they are defined) using square bracket delimiters. For example:
```apl
MySetting: "[DYALOG]/MyFile"
```

will replace `[DYALOG`] with the value of the **DYALOG** configuration value.

If the string inside the `[]` delimiters is "`.`", the "`.`" is replaced is replaced with the path of the directory containing the configuration file itself. Therefore,
```apl
FILENAME: "[.]/x.txt"
```

will set the parameter **FILENAME** to a value which is a reference to a file called `x.txt` in the same directory as the configuration file defining it.

Note that:

- If the referenced configuration parameter is not defined then no substitution will take place; the reference, including square bracket delimiters, will remain in place.
- To include square brackets in a string, prefix the '[' with a '\' character.

#### Nested Structures

Some parameters are stored in sub-folders in the Windows Registry. Currently, all such parameters used by Dyalog APL itself relate to the Windows IDE, but you can create your own application-specific structures..

The Configuration file supports this structure by defining an object that corresponds to a Registry sub-folder. For example:
```apl
Captions: {
    Session: "My Dyalog Session",
    Status: "My Status window",
}
```

```apl
      +2 ⎕NQ '.' 'GetEnvironment' 'Captions\Session'
My Dyalog Session

```
