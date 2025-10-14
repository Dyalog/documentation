<h1 class="heading"><span class="name">Execute (UNIX) Command</span> <span class="command">)SH {cmd}</span></h1>

This command allows WINDOWS or UNIX shell commands to be given from APL.  `)SH` is a synonym of `)CMD`. Either command may be given in either environment (Windows or UNIX) with exactly the same effect.  `)SH` is probably more natural for the UNIX user. This section describes the behaviour of `)SH` and `)CMD` under UNIX. See [Windows Command Processor](cmd.md) for a discussion of their behaviour under Windows.

The system functions [`⎕SH`](../system-functions/execute-unix-command.md) and [`⎕CMD`](../system-functions/execute-windows-command.md) provide similar facilities but may be executed from within APL code. For further information, see [Execute (UNIX) Command](../system-functions/execute-unix-command.md) and [Execute Windows Command](../system-functions/execute-windows-command.md).


`)SH` allows UNIX shell commands to be given from APL. The argument must be entered in the appropriate case (usually lower-case).  The result of the command, if any, is displayed.

`)SH` causes Dyalog to invoke the `system()` library call. The shell which is used to run the command is therefore the shell which `system()` is defined to call. For example, under AIX this would be `/usr/bin/sh`.

When the shell is closed, control returns to APL. See *Dyalog for UNIX UI Guide* for further information.

The parameters CMD_PREFIX and CMD_POSTFIX may be used to execute a different shell under the shell associated with `system()`.

<h2 class="example">Example</h2>
```apl
      )SH ps -u andys | grep -v ps
   UID      PID    TTY  TIME CMD
  6179  9437326  pts/0  0:00 ksh
  6179 10223736  pts/0  0:00 dyalog
  6179 10354810  pts/0  0:00 sh
  6179 10879188  pts/0  0:00 ksh
  6179 11665660      -  0:00 sshd
```

!!! note
    This function is disabled and instead generates a `DOMAIN ERROR` if the RIDE_SPAWNED parameter is non-zero. This is designed to prevent it being invoked from a Ride session which does not support this type of user interface. For further details, see the [Ride User Guide](https://dyalog.github.io/ride).


