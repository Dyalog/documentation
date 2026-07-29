# APLMON output

The output file is a CSV matrix with values  separated by commas. Fields can be empty. The file may be read by `⎕CSV` and applications such as Microsoft Excel.

The eleven columns of the APLMON output file are :

|---|---|
|token|Name of  the primitive's   token (symbol, if  you   prefer)|
|lfn|Name of  the left  operand's token, if the  primitive was   an  operator|
|rfn|Name of  the right operand's token, if the  primitive was   an  operator|
|ltype|Data type of the  left    argument   of the  function|
|rtype|Data type of the right   argument   of the  function|
|lrank|Rank of  the left     argument of the  function. Arrays of  rank  greater   or equal to 3 will be  logged  as  «  3+  »|
|rrank|Rank of  the  right  argument of the  function. Arrays of  rank  greater   or equal to 3 will be  logged  as  «  3+  »|
|lbound|Range of the  left  argument sizes. A range is  made  of two numbers separated     by  a  « <  »  sign. The  real size  is between   these  two numbers. So arguments with similar  sizes are  grouped   together.|
|rbound|Range of the   right argument sizes. A range is  made  of two numbers separated     by  a  « <  »  sign. The  real size  is between   these  two numbers. So arguments with similar  sizes are  grouped   together.|
|hitcount|Number of times the primitive was called|
|time|Time spent     by  the primitive (in seconds)|

These fields are empty if not applicable (which will appear in the CSV file as two consecutive commas).

<h2 class="example">Example</h2>

In the following example, APLMON is used to analyse the execution of the expression `10 foo 20 30`. Note that expressions executed in the Session when APLMON is enabled also contribute to the analysis.
```apl
      ∇foo∇
     ∇ r←a foo b
[1]    r←(a+b)(a-b)(a×b)(a÷b)
     ∇
      ⊢2 ⎕NQ '.' 'APLMON' 'c:\dyalog17.0\aplmon'

      10 foo 20 30
 30 40  ¯10 ¯20  200 300  0.5 0.3333333333 
      ⊢ 2 ⎕NQ '.' 'APLMON' ''
      rslt←⎕CSV 'c:\dyalog17.0\aplmon'
      ⍴rslt
15 11
```

```apl
      rslt
 token                    lfn  rfn  ltype   rtype    lrank  rrank  lbound  rbound  hitcount  time      
 plus                               int8    int8     0      1      1<1     2<4     1         0.000001  
 minus                              int8    int8     0      1      1<1     2<4     1         0.000001  
 times                              int8    int8     0      1      1<1     2<4     1         0.000002  
 divide                             int8    int8     0      1      1<1     2<4     1         0.000003  
 left arrow                                 nested          1              2<4     1         0.000001  
 right tack                                 wchar8          1              0<0     1         0.000000  
 stranding                          int16   float64  1      1      2<4     2<4     1         0.000001  
 stranding                          int8    nested   1      1      2<4     2<4     2         0.000001  
 stranding                          wchar8  wchar8   1      1      5<9     0<0     1         0.000001  
 name lookup                                                                       10        0.000002  
 tradfn init                                                                       1         0.000002  
 aplmon measurement time                                                                     0.000013  
 aplmon unmeasured time                                                                      19.772147 
 aplmon total                                                                                19.772174 

```

APLMON measures time only for the atomic calls (that is, not complex expressions or user-defined functions). Primitives that evaluate APL expressions (such as `⍎`, `⎕FIX` and `⎕NEW`) are not included. For example :
```apl
      foo←{1+⍵} ⋄ foo¨(N⍴1)
```

The each will not appear in the log, but only the primitives called by `foo`, meaning that `+` will appear as being called `N` times
```apl
      +.×/(N⍴1
```

The `/` will not be measured, but `+.×` will appeared as called `(N-1)` times. This ensures that time measurements do not overlap, and can therefore be compared.

However, some non-atomic expressions are logged, and the non-primitive parts are logged as non primitive.
