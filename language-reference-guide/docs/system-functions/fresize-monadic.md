---
search:
  boost: 2
---

# <span>Compact Component File</span> `{R}←⎕FRESIZE Y`{{key}}

## Access code 1024

`Y` must be a simple integer scalar or 1 or 2 element vector containing the file tie number followed by an optional passnumber.  If the passnumber is omitted it is assumed to be zero.

An attempt to update a component file that would cause it to exceed its maximum size will fail with a `FILE FULL` error (21). A side effect of `⎕FRESIZE` is to cause the file to be compacted. This process removes any gaps in the file caused by replacing a component with a shorter array. Any interrupt entered at the keyboard during the compaction is ignored. The file is compacted and its maximum size remains unchanged.

During compaction, the file is restructured by reordering the components and by amalgamating the free areas at the end of the file. The file is then truncated and excess disk space is released back to the operating system. For a large file with many components, this process may take a significant time.

The shy result of `⎕FRESIZE` is the tie number of the file.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FRESIZE FRESIZE
</div>
