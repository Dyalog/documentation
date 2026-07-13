# Signals and `⎕TRAP, 4007⌶`

## Signals and `⎕TRAP`

Certain signals sent to a Dyalog APL process can be trapped and an event issued. These signals are:

|---|-------|
|1  |SIGHUP |
|2  |SIGINT |
|3  |SIGQUIT|
|15 |SIGTERM|

No other signal is trapped by the interpreter; their default action will occur. For example when a Dyalog APL process receives a SIGSEGV (11) then it will terminate with a segmentation fault. Note that SIG_USR1 is used by the interface between Dyalog APL and Auxiliary Processors: sending this signal to the interpreter may have "interesting" consequences.

The mapping between these signals and the event issued is non-trivial:

- If a SIGHUP is received, then the input stream is closed immediately, and an event 1002 will be issued at the end of the current line of code. Any subsequent attempt to read from the session will result in an EOF INTERRUPT being issued.
- If a SIGINT is received, then execution will end at the end of the current line of code. An event 1002 will be issued.
- If a SIGQUIT is received, then APL will terminate executing the current line of code as soon as possible - usually at the end of the current built-in command, and an event 1003 will be issued. However, if the end of the current line is reached, then an event 1002 will be signalled too.
- If a SIGTERM is received, then the input stream is closed immediately, and an event 1002 will be issued at the end of the current line of code. Any subsequent attempt to read from the session will result in an EOF INTERRUPT being issued.

## `4007⌶`

To aid the programmer in determining which signal was issued, the newly implemented system operator, `⌶` (I-Beam) has been extended to report this information.

WARNING: Although documentation is provided for I-Beam functions, any service provided using I-Beam should be considered as "experimental" and subject to change - without notice - from one release to the next. Any use of I-Beams in applications should therefore be carefully isolated in cover-functions that can be adjusted if necessary.

`4007⌶⍬` can be used to identify which signals have been received by the APL process and how many of them have been received. A side effect of calling `4007⌶⍬` is to reset all counters to 0.

`4007⌶⍬` returns a vector of integers; the length is dependent on the APL interpreter and the operating system, but is typically 63 or 255 elements long. Each element is a count number of each signal received and processed by the interpreter. Note that when a SIGQUIT is received by APL the count for both SIGINT and SIGQUIT will be incremented by one.

<h3 class="example">Example</h3>
```apl
      8↑4007⌶⍬
1 5 3 0 0 0 0 0
```

This means that since either the start of the current APL process, or since the last invocation of `4007⌶` APL has processed 1 SIGHUP, 2 SIGINTs and 3 SIGQUITs.

It is recommended that rather than trapping either event 1002 or 1003, the user traps event 1000, and queries the vector returned by `4007⌶⍬`. In particular if a SIGHUP or a SIGTERM has been received, then the user's code should terminate the application as soon as possible, and should be careful to avoid requiring input. SIGHUP has either been issued using the kill(1) command, or because either the device at the other end of the connection or the connection has terminated. This used to be common with serial or dialup terminals, but is now most frequently seen when terminal emulators or the PCs on which they run are terminated.
