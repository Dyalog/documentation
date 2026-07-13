# Notes

## Indexing

Simple indexing is the case when the indexer is a list of semicolon-separated   simple arrays,  as opposed to choose and reach indexing, where indexer is a nested array:

## Simple Indexing Example
```apl
      A[;;2;(2 3⍴1)]
```

## Choose Indexing Example
```apl
      A[(2 1)(2 2)]
```

## Reach Indexing Example
```apl
      A[⊂((2 1) 1 5)]
```

For choose and reach indexing, the indexer will be represented by itself, in the monitor log, because it is a true array. A simple indexer, though, is not a true array but a collection of arrays, so it is treated specially : it is represented in the monitor log by a character array, the rank of which is the number of subscript, and the shape of which is the number of items in each subscript.

### Indexer Examples

`[2 3⍴1]` will be represented as a rank-1 character array of shape 6

`[1;4 5;7 8 9]` will be represented as a rank-3 character array of shape 1 2 3

`[;]` will be represented as a rank-0 character array

`[;5;0 2⍴1]` will be represented as a rank-2 character array of shape 1 0

They cannot be misinterpreted because character arrays are illegal as an indexer.

In the monitor, for indexing, `A[I]`, the left argument will be `A` and the right argument will be the representation of `I` as described above.

For indexed assignment, `A[I]←B`, the right argument will be `B`, and the left argument will be the representation of `I` as described above.

## Operators

In an expression in which an operator  takes primitive operands, APLMON will report the time for the operator itself.   If one of the operands is non-primitive, APLMON will report the time used by the operands.

<h2 class="example">Examples</h2>
```apl
      ∇ APLMON expr
[1]    2 ⎕NQ'.' 'APLMON' 'c:\dyalog17.0\aplmon'
[2]    ⍎expr
[3]    ⎕CSV 2 ⎕NQ'.' 'APLMON' ''
     ∇

      APLMON '+/1 2 3'
6
 token                    lfn   rfn  ltype   rtype   lrank  rrank  lbound  rbound  hitcount  time     
 slash                    plus               int8           1              2<4     1         0.000003 
 stranding                           wchar8  wchar8  1      1      5<9     0<0     1         0.000001 
 name lookup                                                                       1         0.000001 
 aplmon measurement time                                                                     0.000005 
 aplmon unmeasured time                                                                      0.003220 
 aplmon total                                                                                0.003229 
      APLMON '{⍺+⍵}/1 2 3'
6
 token                    lfn  rfn  ltype   rtype   lrank  rrank  lbound  rbound  hitcount  time     
 plus                               int8    int8    0      0      1<1     1<1     2         0.000001 
 stranding                          wchar8  wchar8  1      1      5<9     0<0     1         0.000001 
 name lookup                                                                      1         0.000001 
 aplmon measurement time                                                                    0.000007 
 aplmon unmeasured time                                                                     0.003490 
 aplmon total                                                                               0.003500 
      APLMON '+.×/1 2 3'
6
 token                    lfn   rfn    ltype   rtype   lrank  rrank  lbound  rbound  hitcount  time     
 dot                      plus  times  int8    int8    0      0      1<1     1<1     1         0.000007 
 dot                      plus  times  int8    int32   0      0      1<1     1<1     1         0.000001 
 stranding                             wchar8  wchar8  1      1      5<9     0<0     1         0.000001 
 name lookup                                                                         1         0.000001 
 aplmon measurement time                                                                       0.000005 
 aplmon unmeasured time                                                                        0.003058 
 aplmon total                                                                                  0.003073 

```
