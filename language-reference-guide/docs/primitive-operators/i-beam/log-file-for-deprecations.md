<h1 class="heading"><span class="name">Log File for Deprecations</span> <span class="command">{R}←{X} 109⌶Y</span></h1>

Manages the file used to log the use of deprecated features. For an overview of deprecated features and this I-beam's role in identifying them within your code, see [Deprecated functionality](../../../../programming-reference-guide/deprecated-functionality).

`Y` indicates the action to perform.

## Set or query the log file name (Y = 0)

If `X` is omitted, the result `R` is the name of the log file currently being written to. An empty character vector is returned if a name has not been set.

Otherwise, `X` is a simple character scalar or vector containing a valid filename, or is empty. Any existing log file is closed and, if `X` is not empty, the specified file is opened and subsequent log messages will be appended to it. The shy result `R` is the previous name of the log file.

An error will be signalled if the specified file cannot be opened in append mode. However, if messages cannot subsequently be written to it, the running application will continue uninterrupted and the messages will be silently discarded. The log file status can be queried at any time.

## Query log file status (Y = 1)

`X` must be omitted. The result `R` is a two element vector consisting of a numeric status code (`0` indicating no error) and a character vector containing text describing the error that was encountered (empty if no error).

<h2 class="example">Example</h2>

```apl
      ⊢'logfile.txt'(109⌶)0
old_logfile.txt
      (109⌶)1
┌─┬┐
│0││
└─┴┘
```

See also [`13⌶` – Log Use of Deprecated Features](log-use-of-deprecated-features.md).
