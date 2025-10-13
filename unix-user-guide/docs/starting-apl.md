<h1 class="heading"><span class="name">Starting APL</span></h1>

By default, to start the non-GUI versions of Dyalog APL, run the mapl script which is in the installation directory of Dyalog APL.

<h2 class="example">Example</h2>
```apl
$ /opt/mdyalog/{{ version_majmin }}/64/unicode/mapl
```

The mapl script is supplied so that the user can start to use Dyalog APL immediately once the terminal environment has been setup. However, it should be treated more as a template for creating a startup script more appropriate for the environment and purposes that Dyalog will be used for.

The startup script usually sets a number of environment variables, and then calls the interpreter with one or more of its parameters. Although all the examples are written using the Korn shell, any shell can be used.

Note that under Microsoft Windows parameters appear *after* the name of the executable; this is not supported under UNIX, where values must be passed as environment variables.

The parameters are listed in the table below; the more frequently used environment variables are included in the following section.

Table: Parameters for the mapl or dyalog script:

|Parameter|Purpose|
|---|---|
|-tty|Start APL using the terminal development environment. This is not necessary unless the wine (-wine) or MainWin (-mainwin) versions are installed too.|
|-c -rt -server|Causes dyalog.rt (the server version) to be started. This parameter is for backwards compatibility; the use of the -rt or -server parameter is recommended. See also the Note at the bottom of this table.|
|-*|Any other parameter that starts with a "-" will be passed to the interpreter; all parameters that start with a "-" will be passed before any parameters that do not start with a "-".|
|*|This is usually the name of the workspace that is to be loaded when the interpreter is started. Unless the "-x" flag is passed to the interpreter, the latent expression in the workspace will be executed once the workspace has been loaded.|

!!! note
    The -c parameter has different uses depending on whether it is passed to the mapl script, or to the dyalog executable.

Table: Parameters for the Dyalog interpreter:

|Parameter|Purpose|
|---|---|
|-a|Start in "User mode". If not present, then APL will start in "Prog(rammer) mode". See the section on I/O for further details.|
|-b|Suppress the banner in the session.|
|-c|Comment: the "-c" and anything following it will be treated as a comment, but will show up in a long process listing. By adding a suitable comment the user or system administrator can uniquely identify the individual APL processes. See also the Note above this table.|
|-Dw|Check workspace integrity on return to session input.|
|-DW|Check workspace integrity after every line of APL (application will run slowly as a result)|
|-DK|Log session keystrokes in (binary) file **./apllog** .|
|-q|Continue to run even if an error causes a return to the six-space prompt. Used when redirecting input to the session from a pipe or file.|
|+q|A return to the six-space prompt will result in the interpreter terminating.|
|-s|Turn off the session: APL acts similarly to a scrolling terminal.|
|+s|forces APL to enable the session.|
|-x|Do not execute the latent expression of any workspace that is `)LOAD` ed or `⎕LOAD` ed. This applies to every `)LOAD` or `⎕LOAD` during the life of the APL session.|
|ws|This is assumed to be a workspace which will be loaded once the interpreter has started. Unless the -x parameter is included on the command line, the latent expression will be run.|
|-cef / -apl|See the Dyalog Version 17.0 Release Notes for more information|

<h3 class="example">Examples</h3>
```apl

mapl dfns
MAXWS=2G mapl dfns
MAXWS=2G DEFAULT_IO=0 mapl -x dfns
```
