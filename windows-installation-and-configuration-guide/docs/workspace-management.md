<h1 class="heading"><span class="name">Workspace Management</span></h1>

## Workspace Size and Compaction

The *maximum* amount of memory allocated to a Dyalog APL workspace is defined by the **maxws** parameter (on non-Windows platforms this is defined by the environment variable MAXWS).

Upon `)LOAD` and `)CLEAR`, APL allocates an amount of memory corresponding to the size of the workspace being loaded (which is zero for a clear ws) plus the *workspace delta.*

The workspace delta is 1/16<sup>th</sup> of maxws, except if there is less than 1/16<sup>th</sup> of **maxws** in use, delta is 1/64<sup>th</sup> of **maxws**. This may also be expressed as follows:
```apl
      delta←maxws{⌈⍺÷⊃(⍵>⍺÷16)⌽64 16}ws
```

where `maxws` is the value of the **maxws** parameter and `ws` is the currently allocated amount of workspace. If **maxws** is 16384KB, the workspace delta is either 256KB or 1024 KB, and when you start with a `clear ws` the workspace occupies 256KB.

When you erase objects or release symbols, areas of memory become free. APL manages these free areas, and tries to reuse them for new objects. If an operation requires a contiguous amount of workspace larger than any of the available free areas, APL reorganises the workspace and amalgamates all the free areas into one contiguous block as follows:

1. Any un-referenced memory is discarded. This process, known as *garbage collection*, is required because whole cycles of refs can become un-referenced.
2. Numeric arrays are *demoted* to their tightest form. For example, a simple numeric array that happens to contain only values 0 or 1, is demoted or *squeezed* to have a `⎕DR` type of 11 (Boolean).
3. All remaining used memory blocks are copied to the low-address end of the workspace, leaving a single free block at the high-address end. This process is known as *compaction*.
4. In addition to any extra memory required to satisfy the original request, an additional amount of memory, equal to the workspace delta, is allocated. This will always cause the process size to increase (up to the **maxws** limit) but means that an application will typically achieve its working process size with at most 4+15 memory reorganisations.
5. However, if after compaction, the amount of used workspace is less than 1/16 of the Maximum workspace size (**maxws**), the amount reserved for working memory is reduced to 1/64th **maxws**. This means that workspaces that are operating within 1/16th of **maxws** will be more frugal with memory

Note that if you try to create an object which is larger than free space, APL reports `WS FULL`.

The following system function and commands force a workspace reorganisation as described above:
```apl
        ⎕WA, )RESET, )SAVE, )LOAD, )CLEAR
```

However, in contrast to the above, *any spare workspace above the workspace delta is returned to the Operating System*. On a Windows system, you can see the process size changing by using Task Manager.

The system function `⎕WA` may therefore be used judiciously (workspace reorganisation takes time) to reduce the process size after a particularly memory-hungry operation.

Note that in Dyalog APL, the SYMBOL TABLE is entirely dynamic and grows and shrinks in size automatically. There is no `SYMBOL TABLE FULL` condition.

Additional functions for managing the memory used by the workspace are described in [Memory Manager Statistics](../../language-reference-guide/primitive-operators/i-beam/memory-manager-statistics) and [Specify Workspace Available](../../language-reference-guide/primitive-operators/i-beam/specify-workspace-available).
