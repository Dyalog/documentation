
<!-- Hidden search keywords -->
<div style="display: none;">
  3002⌶
</div>






<h1 class="heading"><span class="name">Disable Component Checksum Validation</span> <span class="command">{R}←3002⌶Y</span></h1>



Checksums allow component files to be validated and repaired using [`⎕FCHK`](../../system-functions/fchk.md).


From Version 13.1 onwards, components which contain checksums are also validated on every component read.


Although not recommended, applications which favour performance over security may disable checksum validation by `⎕FREAD` using this function.


`Y` is an integer defined as follows:


|Value|Description                                                                 |
|-----|----------------------------------------------------------------------------|
|0    |`⎕FREAD` will not validate checksums.                                       |
|1    |`⎕FREAD` will validate checksums when they are present. This is the default.|


The shy result `R` is the previous value of this setting.



