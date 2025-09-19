<h1 class="heading"><span class="name">Introduction</span></h1>

This manual is designed to assist users of Dyalog APL on platforms other than Microsoft Windows. For further information, see[ the Dyalog UNIX and Linux forum](https://forums.dyalog.com/viewforum.php?f=20).

The *Dyalog for UNIX UI Guide* and the *Dyalog for Raspberry Pi User Guide* are also non-Windows specific. Users should also review the *Dyalog Version {{ version_majmin }} Release Notes* and the file *dyalog_readme.htm*. All of these files and the other Dyalog-supplied documentation can be found in the directory $DYALOG/help, and are available online at [https://docs.dyalog.com/{{ version_majmin }}](https://docs.dyalog.com/16.0). [https://help.dyalog.com/{{ version_majmin }}](https://help.dyalog.com/16.0) contains an online help system for the Dyalog APL documentation. These websites are updated from time to time, and have the latest revisions of the documentation.

Version {{ version_majmin }} supports Ride, the Dyalog Remote IDE, versions 3 or 4. Ride 3 is available for Windows and macOS (it is the default interface on macOS), and Ride D4 is available on Windows, Linux, macOS and Raspberry Pi; over time Dyalog intends to make Ride the default interface under windows managers on all platforms. For more information about Ride, see the [Ride User Guide](https://dyalog.github.io/ride) for more information.

Throughout the document the  directory in which Dyalog APL has been installed is referred to as **$DYALOG**; this is because it is the name of an environment variable, whose value can most easily found by running the following expression in Dyalog:
```apl
      +2 ⎕NQ '.' 'GetEnvironment' 'DYALOG'
```

Two versions of the interpreter are shipped with each Dyalog APL release: the development version and the server version.

The server version has the same functionality as the development version, other than that any attempt to read from the session, or use `⎕SM` or use `⎕ARBIN` will result in an `EOF INTERRUPT`. It is mainly intended for using Dyalog APL as a server process, where all I/O is processed using TCPSockets, or possibly via an auxiliary processor written by the user. Dyalog recommends using Conga in preference to native TCPSockets.

There are different licences associated with the development and server versions, which affects how each might be distributed. For more information, please contact sales@dyalog.com.

All examples are written assuming that the Korn shell is being used.
