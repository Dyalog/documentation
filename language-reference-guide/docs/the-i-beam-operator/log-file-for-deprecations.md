<h1 class="heading"><span class="name">Deprecated feature log file</span> <span class="command">{R}←{X} 109⌶Y</span></h1>

Manages the file used to log the use of deprecated features. For an overview of deprecated features see [Deprecated features](../../../../programming-reference-guide/deprecated-features) within the Programming Reference Guide.

`Y` indicates the action to perform.

## Set or query the log file name (Y = 0)

If `X` is omitted, the result `R` is the name of the log file. An empty character vector is returned when there is none.

If `X` is specified it is a character vector containing the name of the log file, or an empty character vector for none. Any existing file is closed, the specified file is opened and subsequent log messages will be appended to it. The shy result `R` is the previous name of the log file.

An error will be signalled if the specified file cannot be accessed, However, if a message cannot subsequently be appended to the file, any running application will not be interrupted; instead, further logging will stop, and the file status can be queried using `Y=1`.

## Query log file status (Y = 1)

`X` must be omitted. The result `R` is a two element vector consisting of a numeric status code (0 indicating no error), and a character vector which contains text describing any error.

<h2 class="example">Example</h2>

```apl
      ⊢'logfile.txt'(109⌶)0
old_logfile.txt
      (109⌶)1
┌─┬┐
│0││
└─┴┘
```

See also [Log use of deprecated features](deprecated-features.md), [Deprecated APL Code](deprecated-apl-code.md).