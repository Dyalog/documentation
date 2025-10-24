
<!-- Hidden search keywords -->
<div style="display: none;">
  8373⌶
</div>

<h1 class="heading"><span class="name">Shell Process Control</span> <span class="command">R←{X}(8373⌶)Y</span></h1>

This function provides a way to determine the process IDs of processes started by [`⎕SHELL`](../../system-functions/shell.md), as well as enabling the sending of signals to any of those processes.

## Monadic Use: Query Process IDs

If `Y` is a positive integer that identifies an APL thread number, and that thread is currently running `⎕SHELL`, then `R` is the child process ID.

If `Y` is `⍬`, then `R` is a numeric vector containing all the process IDs of the processes that remained running after `⎕SHELL` completed (due to timeouts or interrupts for example - see [`⎕SHELL`](../../system-functions/shell.md) for more information). Any call to `8373⌶` starts by removing the "dead" processes from the list; dead processes are ones that are no longer running but their ID is still reserved so that it is not reused by a different process.

### Example { .example }
```apl
	tid←{
        ...
        r←⎕SHELL ...
        ...
    }&⍬

    processID←(8373⌶)tid
    processID
84093
```

## Dyadic Use: Signal Child Process

`X` must be a integer scalar representing a signal number that is to be sent to the child process.

`Y` must be an integer scalar that identifies the child process:

- Positive values (including `0`) are interpreted as APL thread numbers, and identify the child process of any currently running `⎕SHELL` call on that thread.
- Negative values are negated and treated as process IDs. The process ID *must* be one of the processes left behind by a finished call to `⎕SHELL`.

`R` is a Boolean scalar indicating whether the signal was successfully sent (`1`), as reported by the operating-system.


!!! windows "Dyalog on Microsoft Windows"
	On Microsoft Windows, the only valid value for `X` is `9`, which makes the I-beam call `TerminateProcess()` on the child process.
