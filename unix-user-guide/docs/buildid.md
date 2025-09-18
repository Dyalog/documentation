<h1 class="heading"><span class="name">BuildID</span></h1>

Each interpreter has its own unique  BuildID. This is a 32-bit checksum of the program file which is the Dyalog APL interpreter. This checksum allows Dyalog Ltd. support staff to uniquely identify the interpreter and from that determine the version, edition, platform etc. of the interpreter.

For that reason, Dyalog Ltd. support staff ask that whenever an issue is raised with them that the BuildID is included in all communications.

The BuildID is included in binary form in any aplcore that is generated; if a core file is created, then is it possible to identify the BuildID using the following command:
```apl
$ strings -a -n 14 core | grep "BuildID="
```

Additionally, the BuildID is included in the "Interesting Information" section of aplcore files provided that the environment variable APL_TEXTINAPLCORE is set to 1.

The BuildID can be identified both from within the interpreter (using the GetBuildID method), and also from the BuildID executable which is supplied with the product on UNIX.

Both of these methods can be used for any file; they are useful and very fast ways of keeping track of workspaces versions etc. although md5sum and others may be more appropriate.

<h2 class="example">Examples</h2>

At the command line:
```apl
$ cd /opt/mdyalog/12.1/32/classic/p6
$ ./BuildID dyalog
70a3446e
$ ./BuildID magic
0a744663
```

In APL:
```apl

      +2 ⎕NQ '.' 'GetbuildID'
70a3446e
      magicfile←'/opt/mdyalog/12.1/32/classic/p6/magic'
      +2 ⎕NQ '.' 'GetBuildID' magicfile
0a744663
      )SH
$ echo $PPID
$ kill -11 $PPID
/opt/mdyalog/12.1/32/classic/p6/mapl[58]: 274434 Segmentation fault(coredump)
$ strings -a -n14 core | grep BuildID=
BuildID=70a3446e
```
