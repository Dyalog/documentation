# MaxWS

The amount of memory allocated to the workspace at start-up. See [Specifying Size-related Parameters](configuration-parameters.md) for how to give a valid size; for example `MAXWS=4G` requests a 4 GiB workspace. Values less than `4M` are ignored, and the maximum is `15E`.

Default depends on platform:

- Raspberry Pi: `64M`
- all other platforms: `256M`

The memory used for the workspace must be contiguous. Dyalog places no implicit restriction on workspace size, and virtual memory allows more than the physically installed memory to be addressed; however, a workspace that greatly exceeds physical memory causes excessive paging. 32-bit versions are typically limited to 1.3-1.9 GiB (a limitation of the operating system on 32-bit processes, not of Dyalog); 64-bit versions have no such limit.

See also the [Workspace tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-workspace-tab) of the Windows Configuration Dialog.
