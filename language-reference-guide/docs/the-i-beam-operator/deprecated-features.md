<h1 class="heading"><span class="name">Log use of deprecated features</span> <span class="command">{R}←(13⌶)Y</span></h1>

Controls which deprecated features are logged when used. For an overview of deprecated features see [Deprecated features](../../../../programming-reference-guide/deprecated-features) within the Programming Reference Guide.

`Y` is a character vector, or a vector of character vectors, each containing the name of a deprecated feature or one of the additional names defined in the table below. Subsequent uses of the selected deprecated features will be logged.

The result `R` is a vector of zero or more names, per the table below.

|Value(s) in Y|Meaning                                                   |Value(s) in R                                           |
|---------------|----------------------------------------------------------|--------------------------------------------------------|
|*Feature names*|Enable logging of the specified deprecated features (only)|Names of features for which logging is enabled (shy)    |
|`'All'`        |Enable logging of all deprecated features                 |Names of features for which logging is enabled (non-shy)|
|`'None'`       |Enable logging of no deprecated features                  |                                                        |
|`'Enabled'`    |List all features for which logging is enabled            |_                                                      _|
|`'List'`       |List names all deprecated features                        |Names of all deprecated features (non-shy)              |

The list of deprecated features varies with each version of Dyalog and are listed in the [Release Notes](xxxLINKxxx).

!!! Note
    The log file must also be configured using [109⌶](log-file-for-deprecations.md).

Each log entry is a complete JSON5 object definition which includes the following items:

* `TS`: a timestamp.
* `Type`: a description of the entry type (always `'Warning'`).
* `Message`: a message associated with the log entry (always `'Use of deprecated feature'`).
* `Feature`: a description of the deprecated feature.
* `ExtraInfo`: feature-specific additional information (may be an empty string).
* `WSID`: the name of the workspace in which the feature was used.
* `Stack`: an array of strings indicating the SIstack at the point the feature was used.

<h2 class="example">Example</h2>

```apl
      13⌶'Enabled'

      13⌶'User'
      13⌶'Enabled'
 User
```

See also [Deprecated feature log file](log-file-for-deprecations.md), [Deprecated APL Code](deprecated-apl-code.md).
