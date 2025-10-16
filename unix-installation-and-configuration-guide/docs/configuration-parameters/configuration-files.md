<h1 class="heading"><span class="name">Configuration Files</span></h1>

A configuration file is a text file containing configuration parameters and values. It can cascade, that is, it can extend (inherit) configuration values from other configuration files, and supplement and/or override them. Configuration files use JSON5 (a superset of standard JSON) syntax and are portable across all systems supported by Dyalog.

The key benefits of defining configuration parameters using configuration files include:

- Configuration files are text-based. They are, therefore, easily managed along with the source code for an application, using industry standard tools for source code management and continuous integration.
- Application configuration files can be placed in application folders and define the configuration settings for a specific application.
- User configuration files provide settings that are the same for all applications. Typically, these files are used to configure the development environment.
- Interpreter configuration can be performed in the same way across all supported platforms.
- Dyalog can be launched from a text file that defines a function, namespace or class. If a configuration file exists with the same name as this file (but with a *.dcfg* extension), then Dyalog will detect this on launching and use the configuration parameter settings it defines.
- Configuration files are easy to read, and can be written directly or by using `⎕JSON` (which supports JSON5).
- Both application and user configuration files can cascade, overriding settings defined in a more generic configuration file; this simplifies the configuration of components which share some configuration.

Dyalog Ltd recommends that configuration files are used for all run-time applications, and that the use of environment variables for this purpose is eliminated.

There are two different types of configuration file:

- A user configuration file – this defines configuration values for the current (possibly only) user of the system. The first time a new version of Dyalog is launched it creates and initialises a user configuration file called *\$HOME/.dyalog/dyalog.&lt;version-specific&gt;.dcfg*, where the version-specific information comprises the version number, edition and width. For example, a 64‑bit Unicode edition of Dyalog version 18.0 will be identified as *180U64*. The name of this file should not be changed.
- An application configuration file – this contains configuration values associated with a specific application. This is created by the user and should be saved at the same level as the application. It can either be given the same name as the workspace/script that is loaded when the application starts (but with the extension *.dcfg*) or the name should be stored in the CONFIGFILE parameter.

An additional configuration file called *\$HOME/.dyalog/dyalog.dcfg* is also created the first time any version of Dyalog is run. This can be edited to include configuration parameter values that should always be applied irrespective of Dyalog version so that they do not have to be redefined in multiple version-specific user configuration files.

Prior to Dyalog version 18.0, configuration parameters could be specified as environment variables and set in the *\$HOME/.dyalog/dyalog.config* script. This is no longer referenced, and any settings that should be retained must be re-entered in the appropriate *\$HOME/.dyalog/dyalog.&lt;version-specific&gt;.dcfg* configuration file.

## Configuration File Structure

Configuration files define configuration parameters using JSON5. A JSON object contains data in the form of key/value pairs and other JSON objects. The keys are strings and the values are the JSON types. A key and its value are seperated by a colon (`:`) character. Entries (key/value pairs) are separated by comma (`,`) characters.

The top-level object defines an optional key called `Extend` and an optional object called `Settings`:

- `Extend` is a string value containing the name of a configuration file to import. The extended (imported) file can extend another configuration file. Configuration values from the imported file(s) can be overridden by redefining them. The file name is implicitly relative to the name of the file that imports it (any file name extension must be explicitly specified).
- `Settings` is an object containing the names of configuration parameters and their values. The values can be a string, a number or an array of strings.

The names and values correspond to configuration parameters, and names are not case sensitive. Any named values can be defined; an APL application could query the values using `+2⎕NQ'.' 'GetEnvironment' <name>` or using the `]Config` user command.

If the same name is defined multiple times within a configuration file then the first definition will be used and a warning will be generated.

## Arrays

An array can be used to define file paths, for example, `WSPATH: ["/dir1", "/dir2"]`. The only parameters which can be defined as arrays are **WSPATH**, **WSEXT** and **CFEXT**.

## References to other Configuration Parameters

Configuration parameters that are string values can include references to other configuration parameters (irrespective of where they are defined) using square bracket delimiters. For example, `MySetting: "[DYALOG]/MyFile"` will replace `[DYALOG]` with the value of the **DYALOG** configuration parameter.

If the referenced configuration parameter is not defined then no substitution will take place; the reference, including the square bracket delimiters, will remain in place.

To include literal square brackets in a string, prefix them with a `\` character.

## Nested Structures

Configuration files support nested parameter structures by defining an object that corresponds to the structure. For example:
```
Captions: {
    Session: "My Dyalog Session"
    Status: "My Status window"
}
```
```apl
      +2 ⎕NQ '.' 'GetEnvironment' 'Captions\Session'
My Dyalog Session
```

## Example Configuration File Content
```
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
