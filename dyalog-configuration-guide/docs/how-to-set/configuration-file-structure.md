# Configuration File Structure

Both [application](application-configuration-files.md) and [user](user-configuration-files.md) configuration files use JSON5 (a superset of standard JSON) syntax, and are portable across all platforms that Dyalog supports. A file can be written directly or produced by `⎕JSON` (which supports JSON5).

A JSON object holds data as key/value pairs and other JSON objects. A key and its value are separated by a colon (`:`); entries are separated by commas (`,`).

The top-level object defines an optional key `Extend` and an optional object `Settings`:

- `Extend` is a string naming another configuration file to import. The imported file can itself extend a further file. Imported values can be overridden by redefining them. The file name is relative to the file that imports it, and any extension must be given explicitly.
- `Settings` is an object holding configuration parameter names and their values. A value can be a string, a number, or an array of strings. Names are not case-sensitive.

If the same name is defined more than once within a file, the first definition is used and a warning is generated.

<h2 class="example">Example</h2>
```apl
{
    Extend: "my_default_configuration.dcfg",
    Settings: {
        // maximum workspace
        MAXWS: "2GB",
        WSPATH: ["/dir1", "/dir2", ""],
        UserOption: 123,
        ROOTDIR: "/my/root/directory",
        // reference to another configuration parameter
        FNAME: "[rootdir]/filename",
    }
}
```

## Arrays

A value can be an array of strings, used mainly for file paths, for example `WSPATH: ["/dir1", "/dir2"]`. The only parameters that can be defined as arrays are **WSPATH**, **WSEXT**, and **CFEXT**.

## References Relative to the Configuration File

Within a configuration file, a [reference to another configuration parameter](overview.md#references-to-other-configuration-parameters) can also refer to the location of the file itself. If the string inside the `[]` delimiters is `.`, it is replaced with the path of the directory containing the configuration file. For example, `FILENAME: "[.]/x.txt"` sets **FILENAME** to a reference to a file called `x.txt` in the same directory as the configuration file defining it.

## File Names

Path names in configuration files should use portable forward slashes (`/`) rather than back-slashes (`\`), because JSON uses the back-slash as an escape character. For example, `WSPATH: ["c:/Dyalog21.0"]` (or `["c:\\Dyalog21.0"]`) specifies `c:\Dyalog21.0`.

An unescaped back-slash is not reported as an error. The file is accepted, and the resulting value silently differs from the path intended:

- `["c:\Dyalog21.0"]` gives `c:Dyalog21.0`. Because `\D` is not a recognised escape sequence, the back-slash is discarded, and an absolute path becomes a drive-relative one.
- `["c:\temp"]` gives `c:`, followed by a tab character, followed by `emp`, because `\t` is the escape sequence for a tab.

## Nested Structures

A configuration file represents a nested parameter structure (for example, a Windows Registry sub-folder) as a nested object:
```apl
Captions: {
    Session: "My Dyalog Session",
    Status: "My Status window",
}
```
The value is then queried with a back-slash separator:
```apl
      +2 ⎕NQ '.' 'GetEnvironment' 'Captions\Session'
My Dyalog Session
```
