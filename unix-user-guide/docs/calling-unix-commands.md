<h1 class="heading"><span class="name"><span class="command">⎕SH</span>, exit codes and stderr</span></h1>

Note that `⎕SH` calls /bin/sh; this cannot be altered.

If the command, or command pipe issued using `⎕SH` exits with a non-zero exit code, then `⎕SH` will terminate with a `DOMAIN ERROR`, and all output from the command will be lost. To avoid this, add an exit 0 to the end of the command string, and the `DOMAIN ERROR` will be suppressed. However, this technique does require that some other method is used to determine that the command pipe failed.
        Example:
```apl
      ⍴⎕SH 'grep no_such_user /etc/passwd'
DOMAIN ERROR
      ⍴⎕SH 'grep no_such_user /etc/passwd'
     ∧
```

but
```apl
      ⍴⎕SH 'grep no_such_user /etc/passwd ; exit 0'
0
```

If you are interested in the exit code from the command pipe, rather than any partial output, then, in Version{{ version_majmin }} onwards `⎕DMX.Message` has the exit code at the end of the text. Dyalog intends that this value will appear in a more user-friendly form in `⎕DMX` at some point.

Example:
```apl

      z←⎕SH 'exit 17'
DOMAIN ERROR
      ⎕DMX.Message
Command interpreter returned failure code 17

```

`⎕SH` only captures stdout; unless redirected, any output on stderr will appear in the same terminal window as the session; hitting RD (default Ctrl-L) will force a screen redraw, thereby returning the session to its state before the error output appeared.

## `⎕SH` and starting jobs in background

It is possible to run tasks from within APL using `⎕SH`:
```apl
      ⎕SH'myjob'
```

However, in this case, APL will wait until myjob has completed, and will return the output from myjob (assuming that is that myjob completes with a non-zero exit code). It is possible to start a job that will run in background, without APL waiting for that job to complete, with the job continuing even if APL is terminated:

Example:
```apl
      ⎕SH 'sleep 40000 </dev/null >/dev/null 2>&1 &'
```

More useful might be to save the stdout and stderr of the command, and pipe the input in from a file; it might also be useful to have the job continue to run even after the user has both quit APL and logs out from the server:
```apl
      ⎕SH 'nohup myjob <my.in >my.out 2>my.err &'
```
