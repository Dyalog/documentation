<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕WA WA
</div>






<h1 class="heading"><span class="name">Workspace Available</span> <span class="command">R←⎕WA</span></h1>



This is a simple integer scalar.  It identifies the total available space in the active workspace area given as the number of bytes it could hold.


A side effect of using `⎕WA` is an internal reorganisation of the workspace and process memory, as follows:

1. Any un-referenced memory is discarded. This process, known as *garbage collection*, is required because whole cycles of refs can become un-referenced.
2. Numeric arrays are *demoted* to their tightest form. For example, a simple numeric array that happens to contain only values 0 or 1, is demoted or *squeezed* to have a `⎕DR` type of 11 (Boolean).
3. All remaining used memory blocks are copied to the low-address end of the workspace, leaving a single free block at the high-address end. This process is known as *compaction*.
4. All memory allocated is returned to the Operating System except the space required for the compacted workspace, plus a working overhead based on the configured maximum workspace size (**MAXWS**). If the compacted workspace occupies more than 1/16 of **MAXWS** then the overhead is 1/16 of MAXWS, otherwise it is 1/64 of **MAXWS**. On a Windows system, you can see the process size changing by using Task Manager.


<h2 class="example">Example</h2>
```apl
      ⎕WA
261412
```


See also: [Specify Workspace Available](../primitive-operators/i-beam/specify-workspace-available.md)


