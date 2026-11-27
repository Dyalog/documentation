# Miscellaneous

## Session logfile

By default the session logfile is called default.dlf. By default this file is created as ~/.dyalog/default.dlf on Linux, AIX and macOS, and in ~/.config/dyalog/default.dlf on the Pi. This can be overridden by setting the environment variable **LOGFILE**.

## Status window output

Under Unix, text that the GUI versions show in the status window appears in the terminal window running the APL session instead, although it is not part of the session. The [Screen Refresh](../unix-user-guide/driving-tty-dyalog-apl.md) keystroke, `SR`, redraws the session and removes it.

It is possible to redirect the status window output; to do so select an unused stream number as the stream have the status window output appear on, and then redirect that stream. It will be necessary to associate a valid output translate table (usually apltrans/file) with that stream.

Example:
```
$ export APLSTATUSFD=9
$ export APLT9=file
$ mapl 9>/dev/null
```

More useful may be to redirect the status window output into a file, and in another terminal window run `tail -f` on that file.
