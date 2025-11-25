---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FRENAME FRENAME
</div>






<h1 class="heading"><span class="name">File Rename</span> <span class="command">{R}←X ⎕FRENAME Y</span></h1>


## Access code 128


`Y` must be a simple 1 or 2 element integer vector containing a file tie number and an optional passnumber.  If the passnumber is omitted it is assumed to be zero.


`X` must be a simple character scalar or vector containing the new name of the file.  This name must be in accordance with the operating system's conventions, and may be specified with a relative or absolute pathname. If no file extension is supplied, the first extension specified by the   **CFEXT** parameter will be added. See [ CFEXT](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters).



The file being renamed must be tied exclusively.


The shy result of `⎕FRENAME` is the tie number of the file.

<h2 class="example">Examples</h2>
```apl
      'SALES' ⎕FTIE 1
      'PROFIT' ⎕FTIE 2
 
      ⎕FNAMES
SALES
PROFIT
 
      'SALES.85' ⎕FRENAME 1
      '../profits/PROFITS.85' ⎕FRENAME 2
```
```apl
      ⎕FNAMES
SALES.85
../profits/PROFITS.85
 
Rename←{
    fm to←⍵
    ⎕FUNTIE to ⎕FRENAME fm ⎕FTIE 0
}
```


