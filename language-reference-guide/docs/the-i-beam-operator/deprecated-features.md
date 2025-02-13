<h1 class="heading"><span class="name">Log use of deprecated features</span> <span class="command">{R}←(13⌶)Y</span></h1>

Enables logging of the use of specified deprecated features.

For an overview of deprecated features see [Deprecated features](../../../../programming-reference-guide/deprecated-features) within the Programming Reference Guide.

`Y` is a character vector, or a vector of character vectors, each containing the name of a deprecated feature or one of the additional names defined in the table below. Subsequent uses of the selected deprecated features will be logged.

The result `R` is a list of zero or more names of deprecated feature names, according to the table below.

|Value(s) in Y|Meaning                                                   |Value(s) in R                                           |
|-------------|----------------------------------------------------------|--------------------------------------------------------|
|Feature names|Enable logging of the specified deprecated features (only)|Names of features for which logging is enabled (shy)    |
|'All'        |Enable logging of all deprecated features                 |Names of features for which logging is enabled (non-shy)|
|'None'       |Enable logging of no deprecated features                  |                                                        |
|'Enabled'    |List all features for which logging is enabled            |_                                                      _|
|'List'       |List names all deprecated features                        |Names of all deprecated features (non-shy)              |

The list of deprecated features varies with each version of Dyalog and are listed in the [Release Notes](xxxLINKxxx).

!!! Note
    The log file must also be configured using [109⌶](log-file-for-deprecations.md).

Each log entry is a complete JSON5 object which includes the following items:

* TS: a timestamp.
* Type: a description of the entry type ("Warning").
* Message: a message associated with the log entry ("Use of deprecated feature").
* Feature: a description of the deprecated feature.
* ExtraInfo: feature-specific additional information.
* WSID: the name of the workspace in which the feature was used.
* Stack: an array of strings indicating the SIstack at the point the feature was used

<h2 class="example">Example</h2>

```apl
      13⌶'Enabled'

      13⌶'User'
      13⌶'Enabled'
 User
```

See also [Deprecated APL Code](deprecated-apl-code.md), [Log File for Deprecations](log-file-for-deprecations.md).
