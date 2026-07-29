# MaxWS

This parameter determines your workspace size and is the amount of memory allocated to the workspace at APL start-up. See [Specifying Size-related Parameters](./configuration-parameters.md) for further details about defining a valid value for this parameter.

The default value is 256M (256MiB), with the exception of the Raspberry Pi where the default is 64M. Values less than 4M are ignored, and the maximum value is 15E.

For example, to get a 4GiB workspace, set:
```apl
        MAXWS=4G
```

Dyalog APL places no implicit restriction on workspace size, and the virtual memory capability of the underlying operating system allows you to access more memory than you have physically installed. However if you use a workspace that **greatly** exceeds your physical memory you will encounter excessive *paging* and your APL programs will run slowly. You may also cause the system to crash.

Note that the memory used for the workspace must be *contiguous* .

32-bit versions of Dyalog APL are typically limited to between 1.3GiB to 1.9GiB under Windows, and 1.9GiB under UNIX. These are operating system limitations imposed on 32-bit processes rather than ones imposed by Dyalog APL, and are affected by the number and size of DLLs/shared libraries that are loaded into the process space.

64-bit versions of Dyalog APL have no such limitations; Dyalog has used workspaces of 96GiB on various platforms.

See also [Maximum workspace size](../configuring-the-ide/configuration-dialog/configuration-dialog-workspace-tab.md).
