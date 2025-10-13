<h1 class="heading"><span class="name">Log Use of Deprecated Features</span> <span class="command">{R}←(13⌶)Y</span></h1>

Controls which deprecated features are logged when logging is enabled. For an overview of deprecated features and this I-beam's role in identifying them within your code, see [Deprecated functionality](../../../../programming-reference-guide/deprecated-functionality).

`Y` is a character vector, or a vector of character vectors, each containing the name of a deprecated feature, or one of the names defined in the table below. The names are release-dependent; for a list of valid names see the [Release Notes](../../../../release-notes/announcements/deprecated-functionality).

Subsequent uses of the selected deprecated features will be logged, provided that [`109⌶`](log-file-for-deprecations.md) has been called to set the name of the log file.

If `13⌶` is called again, the list of features that are logged is replaced.

The result `R` is a vector of zero or more names, as described in the table below.

|Value(s) in `Y`|Meaning                                          |Value(s) in `R`                                           |
|---------------|-----------------------------------------------|--------------------------------------------------------|
|*Feature names*|Enable logging of the specified features       |Names of features for which logging is enabled (shy)    |
|`'All'`        |Enable logging of all deprecated features      |Names of features for which logging is enabled (non-shy)|
|`'None'`       |Disable logging of deprecated features         |                                                        |
|`'Enabled'`    |List all features for which logging is enabled |_                                                      _|
|`'List'`       |List names of all possible features            |Names of all deprecated features (non-shy)              |

Before any logging information is created, the log file must also be configured using [`109⌶`](log-file-for-deprecations.md). Without selecting a log file, all logging is silently discarded.

Each log entry is a complete JSON5 object definition that includes the following items:

* `TS`: a timestamp.
* `Type`: a description of the entry type (always `'Warning'`).
* `Message`: a message associated with the log entry (always `'Use of deprecated feature'`).
* `Feature`: a description of the deprecated feature.
* `ExtraInfo`: feature-specific additional information (can be an empty string).
* `WSID`: the name of the workspace in which the feature was used.
* `Stack`: an array of strings indicating the SIstack at the point the feature was used.

<h2 class="example">Example</h2>

```apl
      13⌶'List'
 This  That  TheOther 
      13⌶'Enabled'

      13⌶'That' 'This'
      13⌶'Enabled'
 This  That
      13⌶'All'
      13⌶'Enabled'
 This  That  TheOther
```

See also [`109⌶` – Log File for Deprecations](log-file-for-deprecations.md).
