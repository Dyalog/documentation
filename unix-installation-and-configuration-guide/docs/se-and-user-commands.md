# `⎕SE`, User Commands and SALT

## Summary

Support for user commands is included in non-Windows versions of Dyalog. Many of the user commands that were originally written for running under Microsoft Windows will run under the various flavours of Unix.

Under Unix there is no autocompletion of user command names.

The SALT code resides in `⎕SE`, which is saved in a session file. The location of the session file is controlled by the environment variable SESSION_FILE; by default this file is $DYALOG/default.dse. Setting SESSION_FILE=/dev/null results in an empty `⎕SE` and SALT being disabled.

Further information is available about [user commands](https://docs.dyalog.com/latest/User%20Commands%20User%20Guide.pdf) and [SALT](https://docs.dyalog.com/latest/SALT%20User%20Guide.pdf).

## Caching User Command information

When a Dyalog APL session is started, SALT is loaded, and checks the details of all of the files which contain user commands with a previously cached version of this information. If Dyalog APL has never been run before, or the cache file does not exist, SALT rebuilds the cache file. This can take a few seconds, especially on the Raspberry Pi.

By default the cache file is called $HOME/.dyalog/UserCommand20.cache.

This can be overridden by specifying the environment variable UCMDCACHEFILE.

It is expected that the structure of files in ~/.dyalog will change in future versions of Dyalog APL.

## Assigning Contents of Session Log

It is possible to assign the contents of the Session Log to a variable:
```apl
      z←'⎕SE'⎕WG'Log'
```
