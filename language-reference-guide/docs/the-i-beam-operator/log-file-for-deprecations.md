<h1 class="heading"><span class="name">Log File for Deprecations</span> <span class="command">{R}←{X} 109⌶Y</span></h1>

Manages the file used for logging the use of deprecated features.

For an overview of deprecated features see [Deprecated features](../../../../programming-reference-guide/deprecated-features) within the Programming Reference Guide.

`Y` indicates the action to perform.

## Set or query the log file name (Y = 0)

If `X` is omitted, the result `R` is the name of the log file. An empty character vector is returned when there is no log file.

If `X` is specified it is a character vector containing the name of the log file, or an empty character vector for none. Any existing file is closed, the specified file is opened and subsequent log messages will be appended to it. The shy result `R` is the previous name of the log file.

Note: if the log file cannot be opened, an error will be signalled. If a message cannot subsequently be appended to the file, logging will stop and no error will be signalled.

## Query log file status (Y = 1)

`X` must be omitted. The result `R` is a two element vector consisting of a numeric status code (0 = no error), and a character vector which is either empty (code = 0) or contains error text describing the file error.

Thus, after enabling logging of deprecated features, the log file will be complete if the status code is 0.

<h2 class="example">Example</h2>

```apl
      ⊢'logfile.txt'(109⌶)0
old_logfile.txt
      (109⌶)1
┌─┬┐
│0││
└─┴┘
```

See also [Deprecated Features](deprecated-features.md), [Deprecated APL Code](deprecated-apl-code.md).