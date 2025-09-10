<!-- Hidden search keywords -->
<div style="display: none;">
  dyalogscript
</div>

<h1 class="heading"><span class="name">Shell Scripts</span></h1>

Shell scripts are typically executed  from a terminal (or *shell*).

A script is executed by typing its name. User input is entered from the same terminal or shell and output is displayed on the terminal or shell.

## UNIX

On UNIX (and related) systems a Dyalog APL *shell script* is a text file with the following as the first line:
```apl
#!/usr/local/bin/dyalogscript
```

The script file must be executable. There are three execute bits relating to the user, the group and everyone else.

## Windows

On Windows systems a Dyalog APL shell script is a text file with a `.apls` file extension. An initial line beginning with `#!` is only required to include configuration parameters (see below), but if included it must include a file name even though that will be ignored. For portability it is recommended that you include the `#!` line.

## Note

Shell scripts are Unicode only and are not supported by the Classic Edition.

Any content that follows  the `#!` line (if present) is used as input into a Dyalog session (as if the *Extended Multiline Input* feature has been enabled).

## Input and Output

`⎕` and `⍞` input are taken from characters typed by the user into the terminal or shell (Standard input or *stdin* for short).  Anything assigned to `⎕` and `⍞` will be displayed in the terminal window using streams Standard output (*stdout*) and Standard error (*stderr*) respectively. Note that default output, that is, output to the session without assignment to `⎕` or `⍞` is NOT displayed. Redirections of *stdin*, *stdout*, and *stderr* are supported.

<h3 class="example">Examples</h3>

The following then are all valid APL shell scripts:
```apl
#!/usr/local/bin/dyalogscript
'this text will not be seen'
⎕←2+2
```
```apl
#!/usr/local/bin/dyalogscript
∇r←l plus r
r←l+r
∇
⎕←2 plus 2
```
```apl
#!/usr/local/bin/dyalogscript
plus←{
⍺+⍵
}
⎕←2 plus 2
```

## Errors

Untrapped errors in a script will cause the termination of the process, further lines in the script will NOT be processed.
```apl
#!/usr/local/bin/dyalogscript
⎕←'this will be seen'
⎕←÷0
⎕←'this will NOT be seen'
```

However, the multiline input mechanism allows for `:Trap` statements, so the following will run to completion:
```apl
#!/usr/local/bin/dyalogscript
⎕←'this will be seen'
:Trap 0
    ⎕←÷0
:EndTrap
⎕←'this will ALSO be seen'
```

### Configuration Parameters

Configuration parameters may be specified in a Configuration file located in the same directory as the script, or may be specified on the first line of the script.  The name of the configuration file is derived from the name of the script file by replacing its file extension (if any) by the extension `.dcfg`. Configuration parameters specified in the Windows Registry or by environment variables are not honoured in Dyalog Shell Scripts.

### Example (first line of script)
```apl
#!/usr/local/bin/dyalogscript MAXWS=3GB
⎕←⎕WA
⎕←2 ⎕NQ '#' 'GetEnvironment' ('MAXWS' 'WSPATH')
```

### Example (configuration file)
```apl
{ settings: {
        /* Maximum workspace size */
        MAXWS: "256M",
        /* wspath */
        WSPATH: ["c:/tmp","f:/devt/tmp"]
}}
```

Note that the interpreter reads both of these locations, the command line in the script file overrides any setting in the .dcfg file.

### Debugging

It is not currently possible to use Ride to debug APL shell scripts. However there is an I-beam function, which can be used to provide some simple debugging/diagnostic information.
