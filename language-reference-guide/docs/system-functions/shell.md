---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SHELL SHELL
</div>

# <span>Execute External Program</span> `R←⎕SHELL Y`{{key}}

`⎕SHELL` executes an external program, either directly or using the operating system's shell.

`Y` describes the command to execute. `Y` is specified as either a character vector or a vector of character vectors.
`R` contains information about the termination reason, along with output collected.

Although `⎕SHELL` itself is cross-platform, the command specification depends on the platform's shell, the program being invoked, and the expected format of the command line arguments – `⎕SHELL` calls are only as cross-platform as the programs they execute.
In practice, many command line tools that are useful when building cross-platform applications, such as `git` and `aws-cli`, *are* cross-platform tools, which makes this less likely to be an issue.

### Using the System's Shell
When `Y` is a character vector, the contents are executed using the system's shell.
The shell being used can be changed using the [`Shell`](#shell) variant. The defaults are:

- Microsoft Windows: `PowerShell`
- Linux, macOS, AIX: `/bin/sh`

#### Example ( Microsoft Windows) { .example }
```apl
      ↑⊃⊃⎕SHELL 'Get-ChildItem -path C:\tmp'
      
                                                                                                                       
    Directory: C:\tmp
    
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        19-11-2024     12:42                ciderTest
d-----        19-11-2024     12:58                test2
d-----        26-11-2024     12:56                ullu
-a----        20-12-2024     14:14            803 log.txt
-a----        26-11-2024     14:11             12 test.apls
```

### Direct Execution

When `Y` is a vector of character vectors or an enclosed character vector, the first element of the array is treated as a program name, and the rest as individual arguments. The program is executed directly, without invoking the system's shell first. The program name can be an absolute path, a relative path, or the name of an executable in the current search path (operating-system specific). When the program is specified as a relative path, the name is resolved relative to the working directory, which can be set with the [`WorkingDir`](#workingdir) variant.

If the command does not depend on any shell features, then direct execution should be used as it has lower overhead.

!!! Info "Information"
    This difference in performance can be very significant, especially under Microsoft Windows where PowerShell is the default.
    Direct calls can be 5-10x faster.
    
    See [the example below](#example-using-cmdexe-microsoft-windows) for information about how to use `cmd.exe` instead of PowerShell.

## Return Value

The result is a five element nested vector:
```apl
(StreamData StreamIds ExitCode ExitReason Pid)←R
```

Within this:

- `StreamData` and `StreamIds`, describe the output that was collected while the program ran.
- `ExitCode` and `ExitReason` describe why the `⎕SHELL` call ended.
- `Pid` is either the positive integer process ID of the child process (if the `⎕SHELL` call ends before the child process has ended), or `¯1`.

### Stream Data

A stream is a connection between the process and some resource, such as a file, or a pipe connecting two different processes. All running processes have a set of open, numbered, streams that they can read from or write to. Even though the streams are referenced by number, some streams have typical usage conventions:

| Stream number | Name | Type | Description |
| --- | --- | --- | --- |
| 0 | Standard input | Input | In interactive programs running in a terminal window, input typed on the keyboard typically goes to standard input. In a shell pipeline, standard output of one program is connected to standard input of another program. |
| 1 | Standard output | Output | Used to print regular output data. |
| 2 | Standard error | Output | Used to print error messages or other information that is not part of the main output. |

`⎕SHELL` provides great flexibility in what the streams should point to, by using the [`Output`](#output) and [`Input`](#input) variants. By default, the two output streams, 1 and 2, are configured such that the output produced on standard error is redirected to standard output and effectively merged together, and then turned into an APL array representing the lines of text.

The StreamData and StreamIds vectors have the same length. The StreamIds are always sorted in ascending order. Each index describes one collected output stream; StreamIds contains the integer stream IDs, and the elements of StreamData depend on how the output is collected (see the [`Output`](#output) variant).

By default, `⊃⊃⎕SHELL cmd` returns a vector of character vectors representing the lines of the collected output text from the child process (both standard output and standard error).

### Exit Reasons

The  reasons why a call to `⎕SHELL` ends are described in the table below. `ExitReason` is an integer that describes the overall reason, and `ExitCode` provides additional information.

| `ExitReason` | Description | `ExitCode` |
| --- | --- | --- |
| 0 | The child process finished and exited normally. | The non-negative exit code. |
| 1 | The child process was terminated by a signal. | The negated signal number that caused the termination. |
| 2 | `⎕SHELL` timed out before the child process exited (see the [`Timeout`](#timeout) option). | The constant `¯1006`. |
| 3 | `⎕SHELL` was interrupted by a weak interrupt in the IDE. | The constant `¯1002`. |

!!! windows "Dyalog on Microsoft Windows"
    `ExitReason` cannot be 1 on Microsoft Windows.

Returning the exit code (instead of `⎕SHELL` producing some trappable error) makes it possible to access the other parts of the result, such as the error messages that were printed on the standard error stream. However, it is possible to turn non-successful exits into trappable errors using the [`ExitCheck`](#exitcheck) variant.

When the `ExitReason` is 2 or 3, the child process had not stopped running before `⎕SHELL` stopped, which means it might still be running, and require some appropriate cleanup (see [8373⌶](../../primitive-operators/i-beam/shell-process-control)).
In practice, the child process often closes shortly after without the need for intervention, either due to the default signal being sent to it on non-Windows platforms (see the [`Signal`](#signal) option), or because the connected streams are closed on the `⎕SHELL` end.

## Thread Switching
`⎕SHELL` is a thread switch point, which means the interpreter will run other APL threads while a long-running `⎕SHELL` call is in progress.

When an APL thread running `⎕SHELL` is terminated by [`⎕TKILL`](tkill.md) or [`)RESET`](../system-commands/reset.md), the child process might be left running, as if `⎕SHELL` was interrupted.

## Variant Options
`⎕SHELL` supports the following variant options to control certain parts of the program execution context.

### Output
The `Output` variant option controls output stream redirections. The value must describe a set of redirections, in one of the following formats:

- a two-column matrix.
- a two-element vector.
- a vector of two-element vectors.

Each row or two-element vector should be of the form `(Stream Destination)`, in which:
- `Stream` is the integer stream number.
- `Destination` is one of the possible destinations described in the table below.

Any output the child process produces on its stream `Stream` will go to the specified destination.

| Format | Description |
| --- | --- |
| `('Stream' n)` | Redirect the output to another stream with the ID `n`, which is also configured. For example, to redirect standard error to standard output, merging the two, the variant value would be `(2 ('Stream' 1))`. |
| `('File' n)` | Redirect the output to an open native file with tie number `n`. The file must be writable. |
| `('File' path)` | Redirect the output to an existing file with a path described by the character vector `path`. The output is appended to the end of the file. |
| `('Array' type)` | Redirect the output to the interpreter, which will convert it into a vector with data type `type`, and include it in the result of `⎕SHELL`. For example, to get standard output as a Boolean vector, the variant value would be `(1 ('Array' 11))`. |
| `'Array'` | Redirect the output to the interpreter, which will convert it to a vector of character vectors, split into the separate lines of text. Note that the line endings and text encoding are determined automatically, like when reading files using monadic [`⎕NGET`](nget.md). The nested array is included as part of the result of `⎕SHELL`. |
| `('Array' textEncoding)` | Redirect the output to the interpreter like with the `'Array'` format above, but use a specific text encoding, described by the character vector `textEncoding`. The possible values for `textEncodings` are those which are allowed as the left argument to dyadic [`⎕NGET`](nget.md). |
| `'Null'` | Redirect the output to the operating-system's null device, which effectively means the output is ignored. |
| `('Callback' fn encodingOrType)` | Redirect the output to the interpreter, which periodically will turn the data produced into an array, and run a callback function specified in `fn`. `fn` can either be a character vector, in which case it is the name of the function to run, or it can be a 2-element vector where the first element is the function name, and the second element is some arbitrary data which will be passed as the left argument to the callback function. When `encodingOrType` is a scalar integer, the conversion behaves as with `('Array' type)`, and otherwise it behaves as `('Array' textEncoding)`. |
| `('Callback' fn)` | This is identical to the other callback format, with the difference that the data is converted into lines of text in the same way as when the `'Array'` format is used, using heuristics to determine the line endings and text encoding. |
| `n` | When the destination is a scalar integer, it is treated as a shorthand for either `('Stream' n)` or `('File' n)`, depending on the sign of the integer. All non-negative numbers are treated as stream IDs, while negative numbers are treated as native file ties.

The default is is `0 2⍴0`, but see [Default Redirections](#default-redirections).

#### Callbacks
The callbacks supported by the `(Callback fn)` and `(Callback fn encodingOrType)` can be invoked either monadically or dyadically, depending on the format of `fn`:

- A simple character vector: the name of the function to call.
- A two-element vector `(name leftarg)`: the character vector name, and some arbitrary data to be passed as the left argument to the callback function.

When `encodingOrType` is a scalar integer, specifying a data type, the callback runs in *simple vector mode*, otherwise it runs in *line mode*. `(Callback fn)` without an explicit encoding is similar, but the text encoding is deduced automatically on the first call to the callback, and reused for subsequent calls.

The right argument is a namespace that contains the members described in the table below. The namespace is created once for each callback specification and updated just before each call.

| Name | Description |
| --- | --- |
| `Data` | Initially contains `⍬`, and provides a name where the user code can store information between subsequent calls to the callback function. |
| `Done` | A Boolean scalar indicating that this is the last call to the callback for the given stream. Under normal circumstances where `ExitReason` is 0 or 1, it is guaranteed that there will be a single call with `Done=1`, even if no data was produced since the previous call. |
| `Encoding` | A character vector describing the text encoding that was used to decode the raw bytes. When the callback runs in simple vector mode, this member is an empty vector. It is most useful when the callback is specified as `('Callback' fn)`, without an explicit text encoding. |
| `Output` | The APL array produced from converting the bytes produced since the previous callback, according to the encoding or type specified. When the callback is running in line mode, it will also include any partial line from the end of the previous call's `Output`. |
| `Stream` | A scalar integer specifying the stream number. This allows the same callback function to be used on multiple output streams, and provides a way for the callback code to determine which stream it is currently processing. |
| `PartialLine` | A Boolean scalar indicating whether the last line in `Output` was terminated by a newline character or sequence (1 indicates that the line is partial, not terminated by a newline character or sequence). As partial lines are included again in the next call's `Output`, it is possible to process only the complete lines by conditionally ignoring the last element of `Output` when `PartialLine=1`. In simple vector mode, this is always 0. |

The callback is invoked when:

- the internal buffer for the given stream is full.
- there is data in the internal buffer, but no I/O is immediately possible between the interpreter and the child process.
- there is data in the internal buffer, and the child process has finished running.

Depending on the type or encoding, some of these conditions could happen when the buffer contains a number of bytes that do not make up a full item, such as when the buffer is full and the last byte is only one of multiple bytes needed to encode a UTF-8 character.

### Input
The Input variant option controls input stream redirections. The value must describe a set of redirections, in one of the following formats:

- a two-column matrix.
- a two-element vector.
- a vector of two-element vectors.

Each row or two-element vector should be of the form `(Stream Source)`, in which:
- `Stream` is the integer stream number.
- `Source` is one of the possible sources described in the table below.

Any input the child process tries to read on its stream `Stream` will come from the specified source.

| Format | Description |
| --- | --- |
| `('File' n)` | Input on the stream comes from an open native file with tie number `n`. The file must be readable. |
| `('File' path)` | Input comes from an existing file with a path described by the character vector `path`. |
| `('Array' Data Type)` | The APL array `Data` is raveled and converted to a vector of type `Type`. The input on the stream comes from the bytes of the converted array. |
| `('Array' Data)` | Shorthand for `('Array' Data (⎕DR Data))`. In Unicode interpreters when `Data` is a character array, this is the same as `('Array' Data 80)`. |
| `('Array' Data Encoding)` | This is similar to `('Array' Data Type)`, but `Data` must be either a character vector, or a vector of character vectors. Each character vector is converted to text in the given `Encoding`, and terminated by a newline character/character sequence. The `Encoding` must be one of those supported by [`⎕NPUT`](nput.md). |
| `('Array' Data Encoding Newline)` | Similar to `('Array' Data Encoding)`, but provides explicit control over the newline character/sequence. `Newline` must be one of the values supported by [`⎕NPUT`](nput.md). |
| `'Null'` | Input comes from the operating-system's null device, which effectively means no input is provided. |
| `('Token' n)` | `⎕SHELL` will periodically see if any tokens are available on the token number `n`, such as those produced by `X ⎕TPUT n`. When one becomes available, the token data `X` is parsed as one of the `('Array' ...)` sources, and appended to a buffer of data that the child process then sees on the specified stream. A token with no data, as constructed by a monadic [`⎕TPUT`](tput.md) call, closes the stream. This, combined with running `⎕SHELL` on its own APL thread, provides a mechanism for feeding a child process input input dynamically. |

The default is `0 2⍴0`, but see [Default Redirections](#default-redirections).

### WorkingDir
The `WorkingDir` variant option sets the working directory of the child process. The value must be a character vector that refers to a valid directory, such as `'/tmp/somedir'` on Linux, or `'C:\tmp\somedir'` on Microsoft Windows.

The default is the current working directory of the interpreter.

### InheritEnv
The `InheritEnv` variant option specifies whether the set of environment variables from the interpreter should be inherited by the child process. The value must be a Boolean scalar.

The default is `1`.

### Env
The `Env` variant option specifies any additional environment variables and their values. If an environment variable that already exists in the set of inherited variables (see [`InheritEnv`](#inheritenv)) is specified here, the value from `Env` takes precedence. The option value must be one of the following:

- a two-column matrix.
- a two-element vector.
- a vector of two-element vectors.

Each row or two-element vector consists of an environment variable name and its value, both specified as character vectors.

Example: Add three environment variables: `DAY=monday`, `MONTH=december`, and `WEEK=50`.

```apl
      ⍝ Using a two-column matrix and array notation
      env←[
        'DAY' 'monday'
        'MONTH' 'december'
        'WEEK' '50'
      ]
      ⎕SHELL⍠'Env' env⊢cmd
...
      
      ⍝ Using a nested vector
      env←('DAY' 'monday') ('MONTH' 'december') ('WEEK' '50')
      ⎕SHELL⍠'Env' env⊢cmd
...
```

All the environment variable names must be unique within the scope of the call to `⎕SHELL`.

The default is `0 2⍴⍬`.

### Shell
The `Shell` variant option sets the shell to be used when `Y` is a character vector.

The value must be a character vector or a vector of character vectors with a length of at least 1.

!!! info
    Shells typically takes some argument which specify that the next argument is a command to run, such as `/bin/bash -c` on Linux, but since the argument differs from shell to shell, it must be specified manually.

#### Example using cmd.exe (Microsoft Windows) { .example }
```apl
      ⎕SHELL⍠'Shell' ('cmd.exe' '/C')⊢'someCmd'
...
```

#### Example using bash (Linux) { .example }
```apl
      ⎕SHELL⍠'Shell' ('/bin/bash' '-c')⊢'someCmd'
...
```

There is no difference between the following two calls; the `Shell` variant option is simply a convenience.
```apl
      ⎕SHELL'/bin/bash' '-c' 'a b c'
      ⎕SHELL⍠'Shell' ('/bin/bash' '-c')⊢'a b c'
```

When the right argument of `⎕SHELL` is a nested vector, the `Shell` option has no effect.

The default depends on the operating-system:

- Microsoft Windows: `('C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe' '-Command')`.
- Linux, macOS, AIX: `('/bin/sh' '-c')`.

### ExitCheck
The `ExitCheck` variant option specifies whether `⎕SHELL` should convert abnormal exit reasons and exit codes into a `DOMAIN ERORR`. The value must be a boolean scalar; if set to 1, a `DOMAIN ERROR` is reported if `ExitReason` and `ExitCode` are not both 0.

The default `0`.

### Timeout
The `TimeOut` variant option specifies an upper limit for the duration of the `⎕SHELL` call.
The value must be a non-negative numeric scalar representing the number of milliseconds.
The value `0` allows the `⎕SHELL` call to run for as long as it needs.

The default is `0`.

### Signal
The `Signal` variant option specifies a signal to send to the child process when it is being abandoned by `⎕SHELL`.
The value must be either an integer representing a valid signal number, or `0` (which means no signal should be sent).

!!! note "Dyalog on Microsoft Windows"
    On Microsoft Windows, the only valid signal number is `9`, which causes `⎕SHELL` to call `TerminateProcess()` on the child process, which is similar to signal `9` on the other platforms where it is `SIGKILL`.

The default depends on the operating-system:

- Microsoft Windows: `0`.
- Linux, macOS, AIX: the numeric value of `SIGTERM` which is the signal that asks the child process to shut itself down.

### Window
!!! windows "Dyalog on Microsoft Windows"
    This option only has an effect on Windows.

The `Window` variant option specifies the initial window mode. The value must be a character vector containing one of the initial window parameters described on [`⎕CMD`](execute-windows-command.md#starting-a-windows-program).

The default is `'Hidden'`.

See also [8373⌶](../../primitive-operators/i-beam/shell-process-control).

## Default Redirections
Most programs assume that the three standard streams are configured when the program starts. For this reason, `⎕SHELL` always sets up some redirections for those three, even when variant options have explicitly only set up some of them. For example, when `⎕SHELL⍠'Output' (1 ('File' '/tmp/log.txt'))⊢cmd` is run, stream 0 and stream 2 are set up to their default values.

The default redirections for the two output streams are:

- `(1 'Array')`: Collect standard output as lines of text.
- `(2 ('Stream' 1))`: Send standard error to standard output, so it is collected together.

The default for the input stream is

- `(0 'Null')`: Provide no data on standard input.


!!! unix "Dyalog on AIX"
    The performance of `⎕SHELL` on AIX can be improved using the [`DYALOG_SHELL_SUBPROCESS`](../../../unix-installation-and-configuration-guide/configuration-parameters/environment-variables/#_table-4) configuration parameter; this configuration parameter is active by default.
