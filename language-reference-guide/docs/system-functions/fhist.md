---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FHIST FHIST
</div>






<h1 class="heading"><span class="name">File History</span> <span class="command">R←⎕FHIST Y</span></h1>


## Access code 16384


`Y` must be a simple integer vector of length 1 or 2 containing the file tie number and an optional passnumber. If the passnumber is omitted it is assumed to be zero.


The result is a numeric matrix with shape (5 2) whose rows represent the most recent occurrence of the following events.

1. File creation (see note)
2. Undefined, currently `(0 0)`
3. Last update of the access matrix
4. Undefined, currently `(0 0)`
5. Last update performed by `⎕FAPPEND`, `⎕FCREATE`, `⎕FDROP` or `⎕FREPLACE`



For each event, the first column contain the user number and the second a timestamp. Like the timestamp reported by `⎕FRDCI` this is measured in 60<sup>th</sup>s of a second since 1st January 1970 (UTC).


**Note:** `⎕FHIST` collects information only if journaling and/or checksum is in operation. If neither is in use, the collection of data for `⎕FHIST` is disabled and its result is entirely 0. If a file has both journaling and checksum disabled, and then either is  enabled, the collection of data for `⎕FHIST` is enabled too. In this case, the information in row 1 of `⎕FHIST` relates to the most recent enabling `⎕FPROPS` operation rather than the original `⎕FCREATE`.


In the examples that follow, the `FHist` function is used below to format the result of `⎕FHIST`.
```apl

     ∇ r←FHist tn;cols;rows;fhist;fmt;ToTS;I2D
[1]    rows←'Created' 'Undefined' 'Last ⎕FSTAC'
[2]    rows,←'Undefined' 'Last Updated'
[3]    cols←'User' 'TimeStamp'
[4]    fmt←'ZI4,2(⊂-⊃,ZI2),⊂ ⊃,ZI2,2(⊂:⊃,ZI2)'
[5]    I2D←{+2 ⎕NQ'.' 'IDNToDate'⍵}
[6]    ToTS←{d t←1 1 0 0 0⊂⍉⌊0 24 60 60 60⊤⍵
[7]        ↓fmt ⎕FMT(0 ¯1↓↑I2D¨25568+,d),0 ¯1↓t}
[8]    fhist←⎕FHIST tn
[9]    fhist[;2]←ToTS fhist[;2]
[10]   fhist[;1]←⍕¨fhist[;1]
[11]   r←((⊂''),rows),cols⍪fhist
     ∇ 

```

<h1 class="example">Examples</h1>
```apl
     'c:\temp'⎕FCREATE 1 ⋄ FHist 1
               User  TimeStamp            
 Created       0     2012-01-14 12:29:53  
 Undefined     0     1970-01-01 00:00:00  
 Last ⎕FSTAC   0     2012-01-14 12:29:53  
 Undefined     0     1970-01-01 00:00:00  
 Last Updated  0     2012-01-14 12:29:53
  
      (⍳10)⎕FAPPEND 1  ⋄ FHist 1
               User  TimeStamp            
 Created       0     2012-01-14 12:29:53  
 Undefined     0     1970-01-01 00:00:00  
 Last ⎕FSTAC   0     2012-01-14 12:29:53  
 Undefined     0     1970-01-01 00:00:00  
 Last Updated  0     2012-01-14 12:29:55 
 
      ⎕FUNTIE 1

      'c:\temp'⎕FCREATE 1 ⋄ FHist 1
               User  TimeStamp            
 Created       0     2012-01-14 12:29:53  
 Undefined     0     1970-01-01 00:00:00  
 Last ⎕FSTAC   0     2012-01-14 12:29:53  
 Undefined     0     1970-01-01 00:00:00  
 Last Updated  0     2012-01-14 12:29:55  
```


