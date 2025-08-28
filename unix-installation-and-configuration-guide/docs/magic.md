<h1 class="heading"><span class="name">The file command and magic</span></h1>

All Dyalog APL binary files have a unique magic number: the first byte is always 0xAA (decimal 170), and the second identifies the type of Dyalog file. Additional bytes may in some cases be used to further identify the type, version and state of the file. UNIX systems include the `file` command which use the information in the magic file to describe the contents of files.

## magic and AIX

AIX still uses a very early version of `magic`, so it is not possible to give as much information about Dyalog APL files as on Linux.

Dyalog provides a file, `magic`, which is located in the top level installation directory of Dyalog APL. To use this file to extend the capabilities of the `file` command either run
```
file -m /opt/mdyalog/{{ version_majmin }}/64/unicode/p9/magic *
```

or catenate the contents of /opt/mdyalog/{{ version_majmin }}/64/unicode/p9/magic onto /etc/magic, and then run
```
file *
```

<h3 class="example">Example</h3>
```
$ file -m /opt/mdyalog/{{ version_majmin }}/64/unicode/p9/magic *
apl64u.dws: Dyalog APL workspace type 20 subtype 14 64-bit unicode big-endian
aplcore: Dyalog APL aplcore
j1c0.dcf: Dyalog APL component file 64-bit level 1 journaled non-checksummed
j1c1.dcf: Dyalog APL component file 64-bit level 1 journaled checksummed
j2c1.dcf: Dyalog APL component file 64-bit level 2 journaled checksummed
```

### magic and Linux

Most Linux distributions include details about Dyalog-related files in their magic files; Dyalog has submitted two versions of the magic file for inclusion in distributions. To check whether your Linux distribution has the more recent version, create a journaled component file and then run the file command against that component file. The two examples below show the output with the earlier and later versions of magic in use.

## Example, using the older default magic file
```
$ file *
1_apl_j1: data
1_apl_j2: data
1_apl_qfile: data
1_big1: data
1_big2: data
apl64u: \012- Dyalog APL\012- workspace\012- version 12\012- .4
aplout: \012- Dyalog APL\012- workspace\012- version 12\012- .0
aplcore: \012- Dyalog APL\012- workspace\012- version 12\012- .4
colours: \012- Dyalog APL\012- workspace\012- version 12\012- .4
core: ELF 32-bit LSB core file Intel 80386, version 1 (SYSV), SVR4-style
signals: \012- Dyalog APL\012- workspace\012- version 12\012- .4
utf8: \012- Dyalog APL\012- workspace\012- version 12\012- .4
```

### Example, with more recent magic file
```
$ file *
apl64u.dws: Dyalog APL workspace 64-bit unicode big-endian version 20.14
aplcore:    Dyalog APL aplcore version 20.14
j1c0.dcf:   Dyalog APL component file 64-bit level 1 journaled non-checksummed version 20.0
j1c1.dcf:   Dyalog APL component file 64-bit level 1 journaled checksummed version 20.0
j2c1.dcf:   Dyalog APL component file 64-bit level 2 journaled checksummed version 20.0
```

The most recent version of the magic file can be found in the top level of the installation directory; see the man page for the file command for details of how to update the system magic file, or use the syntax described in the /etc/magic and AIX section above to override the default magic file with the one supplied in the installation directory.
