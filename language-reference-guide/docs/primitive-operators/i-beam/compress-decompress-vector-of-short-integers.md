
<!-- Hidden search keywords -->
<div style="display: none;">
  219⌶
</div>






<h1 class="heading"><span class="name">Compress/Decompress Vector of Short Integers</span> <span class="command">R←X(219⌶)Y</span></h1>



In this section, the term *sint_vector* is used to refer to a simple integer vector whose items are all in the range `¯128` to `127`, that is, they are type 83. 
 For further information see [Data Representation (Monadic)](../../system-functions/data-representation-monadic.md).


In most cases this I-Beam functionality will be used in conjunction with `220⌶` (Serialise/Deserialise Array). However, it may be possible to pass the raw compressed data to and from other applications.


`X` specifies the operation to be performed, either compression or decompression, the compression library to be used, and any  optional parameters. `Y` contains the data to be operated on.


## Compression


`Y` must be a *sint_vector*.


`R` is a two item vector, each of which is a *sint_vector*. `R[1]` describes the compression, and `R[2]` contains the raw data which is the result of applying the compression library to the input data `Y`.



`X` is specified as follows:


|------|------|----------------------------------------|
|`X[1]`|`X[2]`|Compression Library                     |
|1     |n/a   |LZ4                                     |
|2     |0 .. 9|zlib                                    |
|3     |0 .. 9|gzip                                    |
|4     |n/a   |LZ4 with frames (compresses arrays >2GB)|



If LZ4 compression is required, then `X` must either be a scalar or a one element vector. Otherwise, `X[2]`, if present, specifies the compression level; higher numbers produce better compression, but take longer.

## Decompression


`R` is a *sint_vector*, containing the output of applying the decompression library to the input data, `Y`.


If `X` is a scalar or a one item vector, and has the value 0, then `Y` must be a vector of two items which is the result of previously calling `219⌶` to compress a *sint_vector*.


Otherwise, `X` is a scalar or one or two element vector and `Y` must be a *sint_vector*.



The first element of `X` must be one of the following values.


|------|-------------------|
|`X[1]`|Compression Library|
|`¯1`  |LZ4                |
|`¯2`  |zlib               |
|`¯3`  |gzip               |



The second, optional, element of `X` specifies the length of the uncompressed data. Its presence results in a more efficient use of the compression library.


`X` may not be a two item vector whose first item has the value 0.

<h1 class="example">Examples</h1>
```apl

      sint←{⍵-256×⍵>127}
      utf8←'UTF-8'∘⎕UCS
      str←'empty←⍬'
      ⊣v←sint utf8  str
101 109 112 116 121 ¯30 ¯122 ¯112 ¯30 ¯115 ¯84			
      ⊣comp←1 (219⌶) v
8 ¯55 1 0 0 0 0 11  ¯80 101 109 112 116 121 ¯30 ¯122 ¯112 ¯30 ¯115 ¯84			
      
      utf8 256| 0(219⌶)comp
empty←⍬
      utf8 256| ¯1(219⌶)2⊃comp
empty←⍬					  
```


