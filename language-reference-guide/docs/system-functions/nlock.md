<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NLOCK NLOCK
</div>






<h1 class="heading"><span class="name">Native File Lock</span> <span class="command">{R}←X ⎕NLOCK Y</span></h1>



This function assists the controlled update of shared native files by locking a range of bytes.


Locking enables controlled update of native files by co-operating users. A process requesting a lock on a region of a file will be *blocked* until that region becomes available. A *write-lock* is exclusive, whereas a *read-lock* is shared. In other words, any byte in a file may be in one of only three states:

- Unlocked
- Write-locked by exactly one process.
- Read-locked by any number of processes.



`Y` must be a simple integer scalar or vector containing 1, 2 or 3 items namely:

1. Tie number
2. Offset (from 0) of first byte of region. Defaults to 0
3. Number of bytes to lock. Defaults to maximum possible file size


`X` must be a simple integer scalar or vector containing 1 or 2 items, namely:

1. Type: 0: Unlock, 1:Read lock, 2:Write lock.
2. Timeout: Number of seconds to wait for lock before generating a `TIMEOUT` error. Defaults to indefinite wait.


The shy result `R` is `Y`. To unlock the file, this value should subsequently be supplied in the right argument to `0 ⎕NLOCK`.

<h2 class="example">Examples</h2>
```apl
    2 ⎕NLOCK ¯1        ⍝ write-lock whole file
    0 ⎕NLOCK ¯1        ⍝ unlock whole file.
    1 ⎕NLOCK ¯1        ⍝ read (share) lock whole file.
    2 ⎕NLOCK¨⎕NNUMS    ⍝ write-lock all files.
    0 ⎕NLOCK¨⎕NNUMS    ⍝ unlock all files.
 
    1 ⎕NLOCK ¯1 12 1   ⍝ read-lock byte 12.
    1 ⎕NLOCK ¯1 0 10   ⍝ read-lock first 10 bytes.
    2 ⎕NLOCK ¯1 20     ⍝ write-lock from byte 20 onwards.
    2 ⎕NLOCK ¯1 10 2   ⍝ write-lock 2 bytes from byte 10
    0 ⎕NLOCK ¯1 12 1   ⍝ remove lock from byte 12.
```



To lock the region immediately beyond the end of the file prior extending it:
```apl
   ⎕←region←2 ⎕NLOCK ¯1, ⎕NSIZE ¯1 ⍝ write-lock from EOF.
¯1 1000   
   ... ⎕NAPPEND ¯1                 ⍝ append bytes to file
   ... ⎕NAPPEND ¯1                 ⍝ append bytes to file
 
   0 ⎕NLOCK region                 ⍝ release lock.
```



The left argument may have a second optional item that specifies a *timeout* value. If a lock has not been acquired within this number of seconds, the acquisition is abandoned and a `TIMEOUT` error reported.
```apl
    2 10 ⎕NLOCK ¯1      ⍝ wait up to 10 seconds for lock.
```


## Notes

- There is no *per-byte* cost associated with region locking. It takes the same time to lock/unlock a region, irrespective of that region's size.
- Different file servers implement locks in slightly different ways. For example on some systems, locks are *advisory*. This means that a write lock on a region precludes other locks intersecting that region, but doesn't stop reads or writes across the region. On the other hand, *mandatory* locks block both other locks *and* read/write operations. `⎕NLOCK` will just pass the server's functionality along to the APL programmer without trying to standardise it across different systems.
- All locks on a file will be removed by `⎕NUNTIE`.
- Blocked locking requests can be freed by a strong interrupt. Under Windows, this operation is performed from the Dyalog APL pop-up menu in the system tray.



### Errors

- In this release, an attempt to unlock a region that contains bytes that have not been locked results in a `DOMAIN ERROR`.
- A `LIMIT ERROR` results if the operating system lock daemon has insufficient resources to honour the locking request.
- Some systems support only write locks. In this case an attempt to set a read lock will generate a `DOMAIN ERROR`, and it may be appropriate for the APL programmer to trap the error and apply a write lock.
- No attempt will be made to detect deadlock. Some servers do this and if such a condition is detected, a `DEADLOCK` error (1008) will be reported.



