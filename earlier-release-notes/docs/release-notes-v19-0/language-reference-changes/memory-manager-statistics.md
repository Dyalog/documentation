<h1 class="heading"><span class="name">Memory Manager Statistics</span> <span class="command">R←{X}(2000⌶)Y</span></h1>

This function returns information about the state of the workspace and provides a means to reset certain statistics and to control workspace allocation. This I-Beam is provided for performance tuning and is VERY LIKELY to change in the next release. See also [Workspace Management](https://help.dyalog.com/19.0/index.htm#UserGuide/Installation%20and%20Configuration/Workspace%20Management.htm).

`Y` is a simple integer scalar or vector containing values listed in the table below.

If `X` is omitted, the result `R` is an array with the same structure as `Y`, but with values in `Y` replaced by the following statistics.  For any value in `Y` outside those listed below, the result is undefined.

|Value|Description                                                                                                                                                      |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
|0    |Workspace available (a "quick" `⎕WA` ).                                                                                                                          |
|1    |Workspace used.                                                                                                                                                  |
|2    |Number of compactions since the workspace was loaded.                                                                                                            |
|3    |Number of garbage collections that found garbage.                                                                                                                |
|4    |Current number of garbage pockets in the workspace.                                                                                                              |
|9    |Current number of free pockets in the workspace.                                                                                                                 |
|10   |Current number of used pockets in the workspace.                                                                                                                 |
|12   |Sediment size.                                                                                                                                                   |
|13   |Current workspace allocation, that is, the amount of memory that is actually being used.                                                                         |
|14   |Workspace allocation high-water mark, that is, the maximum amount of memory that has been allocated since the workspace was loaded or since this count was reset.|
|15   |Limit on minimum workspace allocation.                                                                                                                           |
|16   |Limit on maximum workspace allocation.                                                                                                                           |
|19   |The number of calls to `⎕WA` or `2002⌶` since the last time `2000⌶` was called, or when the process started.                                                     |
|20   |The requested size of the `WS Full Buffer` , that is, the amount of workspace requested for handling `WS FULL` errors.                                           |
|21   |The actual size of the `WS Full Buffer` .                                                                                                                        |
|22   |The number of `WS FULL` handlers that are currently running.                                                                                                     |
|23   |The total number of `WS FULL` errors that have occurred.                                                                                                         |
|24   |The total number of `WS FULL` errors that have been trapped.                                                                                                     |

Note: While all other operations are relatively fast, the operation to count the number of garbage pockets (4) may take a noticeable amount of time, depending upon the size and state of the workspace.

See also [Specify Workspace Available](https://help.dyalog.com/19.0/index.htm#Language/I%20Beam%20Functions/Specify%20Workspace%20Available.htm).

<h2 class="example">Examples</h2>
```apl
      2000⌶0
55414796
      2000⌶0,⍳16   ⍝ with MAXWS=95G
1.02004292E11 1181312 1 1 0 ¯1 ¯1 ¯1 ¯1 78 13280 ¯1 1180800 1595016496 1595042464 0 1.020054733E11
```

If `X` is specified, it must be either a simple integer scalar, or a vector of the same length as `Y`, and the result `R` is `⍬`. In this case, the value in `Y` specifies the item to be set and `X` specifies its new value according to the table below.

|Value|Description|
|---|---|
|2|0 resets the compaction count; no other values allowed.|
|3|0 resets the count of garbage collections that found garbage; no other values allowed.|
|14|0 resets the workspace allocation high-water mark; no other values allowed. This should be called following a call to `⎕WA` (which compacts the workspace and returns unused memory to the operating system).|
|15|Sets the minimum workspace allocation to the corresponding value in `X` ; must be between 0 and the current workspace allocation.|
|16|Sets the maximum workspace allocation to the corresponding value in `X` ; 0 implies **MAXWS** otherwise must be between the current workspace allocation and **MAXWS** .|
|19|0 resets the compaction count; no other values allowed.|
|20|Sets the requested size of the `WS Full Buffer` to the value specified by `X` . The actual space allocated may be less than that requested.|

## Notes

- The workspace allocation high-water mark indicates a minimum value for **MAXWS**.
- Limiting the maximum workspace allocation can be used to prevent code that reserves as much workspace as it can from skewing the peak usage result.
- Limiting the minimum workspace allocation can avoid repeatedly committing and releasing memory to the Operating System when memory usage is fluctuating.

<h2 class="example">Examples</h2>
```apl
      2000⌶2 3
6 0 33216252
      0 (2000⌶)2 3 14 ⍝ Reset compaction count

      2000⌶2 3
0 0
      30000000 40000000(2000⌶)15 16 ⍝ Restrict min/max ws

      (2000⌶)15 16
30000000 40000000

      0 (2000⌶)15 16 ⍝ Reset min/max ws

      (2000⌶)15 16
0 65536000

```
```apl
      (2000⌶)13 14 ⍝ Current, peak WS allocation
4072532 4072532

      a←10e6⍴'x' ⍝ Increase WS allocation

      (2000⌶)13 14 ⍝ Current, peak WS allocation
15108580 15108580

      ⎕EX 'a' ⋄ {}⎕WA ⍝ Decrease current WS allocation

      (2000⌶)13 14 ⍝ Current, peak WS allocation
1962856 15108580

      0 (2000⌶) 14 ⍝ Reset High-water mark

      (2000⌶)13 14 ⍝ Current, peak WS allocation
1962856 1962856
```

## WS Full Handling

Potentially, a `WS FULL` error represents a terminal condition that would prevent a program from continuing because the process has, quite literally, run out of memory.

To alleviate the problem,. Dyalog reserves a special *WS Full Buffer* for handling `WS FULL` errors. The default size of this buffer is `(1MB)⌊(0.01×⎕WA)`.

In simple terms, when a `WS FULL` error occurs that triggers a handler, that is, an expression executed via `⎕TRAP` or `:Trap`,  the reserved workspace in the *WS Full Buffer* is released to provide additional memory space for that expression to execute. When the expression terminates, the system removes the memory that it had previously released, reserving it once more for another potential `WS FULL`.

Note that until a `WS FULL` handler starts, the memory allocated to the *WS Full Buffer* is unavailable and inaccessible for any other purpose, thereby reducing the amount of active workspace available (`⎕WA`).

Further considerations are:

- Multiple `WS FULL` handlers can run concurrently as a result of muti-threading or nesting (when a `WS FULL` handler itself generates a `WS FULL` error).
- When the `WS Full Buffer` is restored when the handler (more accurately, the last handler) terminates, or when a saved workspace is re-loaded, there may be insufficient memory available. In these circumstances, the system allocates a reduced amount, without reporting an error. However, the system will later try to reclaim more (up to the desired amount), if more workspace has become free. The desired and actual sizes of the `WS Full Buffer` are reported by `(2000⌶)20` and `(2000⌶)21` respectively.
- When a `WS FULL` handler is activated and the `WS Full Buffer` is freed, `(2000⌶)21` will return 0 until the handler terminates.
