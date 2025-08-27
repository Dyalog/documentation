<h1 class="heading"><span class="name">Session logfile</span></h1>

By default the session logfile is called default.dlf. By default this file is created as ~/.dyalog/default.dlf on Linux, AIX and macOS, and in ~/.config/dyalog/default.dlf on the Pi. This can be overridden by setting the environment variable **LOGFILE**.

## Status window output

By default under UNIX what would appear in the status window in the GUI versions appears in the same terminal window as the APL session, but the text is not part of the session. If such text appears, the APL session can be redrawn using the <SR \> command, thus removing the status window text.

It is possible to redirect the status window output; to do so select an unused stream number as the stream have the status window output appear on, and then redirect that stream. Note that it will be necessary to associate a valid output translate table (usually apltrans/file) with that stream.

Example:
```
$ export APLSTATUSFD=9
$ export APLT9=file
$ mapl 9>/dev/null
```

More useful may be to redirect the status window output into a file, and in another terminal window run `tail -f` on that file.
