---
search:
  boost: 2
---

# <span>Call Windows Command Processor</span> `{R}←⎕CMD Y`{{key}}

This function runs a command through the Windows Command Processor and returns its output, or starts a Windows program and returns immediately. [Dyadic `⎕CMD`](cmd-dyadic.md) starts an auxiliary processor instead.

`⎕CMD` is a synonym of `⎕SH`; this page describes their behaviour under Microsoft Windows, and [monadic `⎕SH`](execute-unix-command.md) describes it under Unix. The [`)CMD`](../system-commands/cmd.md) system command runs a command in the same way, and [`⎕SHELL`](shell.md) runs an external program with more control over its input, output, and environment.

<h2 class="example">Example</h2>

```apl
      ⎕CMD'echo Hello'
 Hello
```

## Right Argument

`Y` is one of:

- a simple character vector containing a [command](#running-a-command), which the Command Processor runs while APL waits
- a 2-item vector of character vectors that specifies a [program](#starting-a-program), which Windows starts while APL continues

## Result

If `Y` is a command, `R` is a vector of character vectors, with one item per line of output from the command, or empty if the output was not collected.

If `Y` specifies a program, `R` is the process identifier of the program, a numeric scalar, and is [shy](../../programming-reference-guide/introduction/results.md#shy-results).

!!! Info "Information"
    This function is disabled and instead generates a `DOMAIN ERROR` if the [RIDE_SPAWNED](../../windows-installation-and-configuration-guide/configuration-parameters/ride-spawned.md) parameter is non-zero. This is designed to prevent it being invoked from a Ride session, which does not support this type of user interface. For further details, see the [Ride User Guide](https://dyalog.github.io/ride).

## Running a Command

The command is an instruction that the Command Processor recognises, or the path name of a program, with optional parameters. APL waits for the command to finish, and returns its output in `R`.

<h3 class="example">Example</h3>

```apl
      Z←⎕CMD'echo Hello'
      ⍴Z
1
      ⊃Z
Hello
```

### Quotes in Commands

If the path name of a program contains spaces, it must be enclosed in double quotes:

```apl
      ⎕CMD'"C:\Program Files\Notepad++\notepad++.exe"'
```

Without the double quotes, the Command Processor takes `C:\Program` as the name of the program, and the command fails:

```apl
      ⎕CMD'C:\Program Files\Notepad++\notepad++.exe'
```

The Command Processor does not allow more than one pair of double quotes in a command. Each of these is valid:

```apl
      ⎕CMD'C:\Windows\System32\notepad.exe C:\temp\myfile.txt'
      ⎕CMD'C:\Windows\System32\notepad.exe "C:\temp\myfile.txt"'
      ⎕CMD'"C:\Windows\System32\notepad.exe" C:\temp\myfile.txt'
```

but this fails, because it has two pairs:

```apl
      ⎕CMD'"C:\Windows\System32\notepad.exe" "C:\temp\myfile.txt"'
```

[Starting the program](#starting-a-program) instead does not involve the Command Processor, so it has no such restriction, but `⎕CMD` then returns immediately, without the program's output:

```apl
      ⎕CMD'"C:\Windows\System32\notepad.exe" "C:\temp\myfile.txt"' ''
```

[Direct execution](shell.md#direct-execution) with `⎕SHELL` also avoids the Command Processor, and it takes the program and each of its arguments as separate items, so none of them need quoting; it waits for the program to finish and returns its output.

### Commands that Prompt for Input

The output of a command is collected through an unnamed pipe, so a command that prompts for input cannot be answered, and APL waits indefinitely. Such a command must redirect its input and output to the console, `CON`. `⎕CMD` then runs the Command Processor in a visible window, through which the user can respond, and `R` is empty:

```apl
      ⎕CMD'pause <CON >CON'
```

More generally, `⎕CMD` does not collect the output of a command that contains the redirection symbol `>`, and `R` is then empty.

The [`Input`](shell.md#variant-option-input) variant option of `⎕SHELL` can supply a command's input from APL, while its output is still collected.

### Command Processor

By default, `⎕CMD` runs the command `Y` as `'cmd.exe /c ',Y`. The [`CMD_PREFIX` and `CMD_POSTFIX`](../../windows-installation-and-configuration-guide/configuration-parameters/cmd-prefix-and-cmd-postfix.md) configuration parameters select another command processor: the command is preceded by `CMD_PREFIX`, which names the command processor and any parameters it requires, and followed by `CMD_POSTFIX`. If `CMD_PREFIX` is not defined, it is the value of the `COMSPEC` environment variable followed by `/c`, or `cmd.exe /c` if `COMSPEC` is not defined either. If `CMD_POSTFIX` is not defined, it is empty.

The [`Shell`](shell.md#variant-option-shell) variant option of `⎕SHELL` selects the command processor for a single call instead.

## Starting a Program

The program is specified by a 2-item vector of character vectors:

|Item |Content|
|-----|-------|
|`1⊃Y`|The name or full path name of an executable program, optionally followed by its parameters|
|`2⊃Y`|The [window mode](#window-modes) in which the program starts|

Windows starts the program, and `⎕CMD` returns immediately, without waiting for the program to finish or collecting its output. `R` is the process identifier of the program.

If `1⊃Y` contains only the name of the program, Windows searches for it in these directories, in order:

1. the current directory
2. the Windows directory
3. the Windows system directory
4. the directories in the `PATH` environment variable
5. the directories mapped in a network

If Windows cannot find the program, `FILE ERROR 2` is signalled.

APL cannot end a program that `⎕CMD` started; it runs until it finishes, or until it is ended outside APL. The [`Timeout`](shell.md#variant-option-timeout) and [`Signal`](shell.md#variant-option-signal) variant options of `⎕SHELL` can end a program that runs for too long.

<h3 class="example">Examples</h3>

```apl
      pid←⎕CMD'notepad.exe C:\temp\myfile.txt' ''
      ⎕CMD'notepad.exe' 'Maximised'
```

A Command Prompt window can be opened by starting the Command Processor as a program:

```apl
      ⎕CMD'cmd.exe' ''
```

### Window Modes

The window mode is one of the following; any other value signals `DOMAIN ERROR`:

|Window mode|The program starts in|
|-----------|---------------------|
|`'Normal'` or `''`|A normal window, which has the input focus|
|`'Unfocused'`|A normal window, which does not have the input focus|
|`'Hidden'`|An invisible window|
|`'Minimized'` or `'Minimised'`|A minimised window, which does not have the input focus|
|`'Maximized'` or `'Maximised'`|A maximised window, which has the input focus|

A program that starts in a hidden window cannot be seen or closed by the user, unless it makes itself visible.

The [`Window`](shell.md#variant-option-window) variant option of `⎕SHELL` takes the same window modes.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CMD CMD
</div>
