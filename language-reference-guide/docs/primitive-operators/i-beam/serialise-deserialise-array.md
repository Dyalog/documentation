
<!-- Hidden search keywords -->
<div style="display: none;">
  220⌶
</div>






<h1 class="heading"><span class="name">Serialise/Deserialise Array</span> <span class="command">R←X(220⌶)Y</span></h1>



In this section, the term *sint_vector* is used to refer to a simple integer vector whose items are all in the range `¯128` to `127`, that is, they are type 83. 
 For further information see [Data Representation (Monadic)](../../system-functions/data-representation-monadic.md).


It is expected that in many cases this I-Beam functionality will be used in conjunction with `219⌶` - Compress/Decompress vector of short integers. It would also be possible to encrypt the serialised form and write to a file (either component or native), and reverse the process at a later date.



`X` is a scalar which can take the value 0 or 1.


When `X` is 1, `Y` can be any array. The result `R` is the serialised form of the array, presented as a *sint_vector*.


When `X` is 0, `Y` must be a *sint_vector*. The result `R` is an array whose serialised form is represented by `Y`.


Typically it is not possible to construct a vector which can be deserialised; it is expected that the only source of a vector which can be deserialised is the result of using `1(220⌶)` to serialise an array.


The result of `1(220⌶)` will differ between interpreters of differing widths and editions, but the resulting vector can be deserialised in other interpreters, with the exception that, like arrays in component files, it may not be possible to deserialise an array which was serialised in a later interpreter



The following identity holds true:
```apl
      A≡ 0(220⌶) 0(219⌶) 1(219⌶) 1(220⌶) A
```


<h2 class="example">Example</h2>
```apl

      a←'ab'
      b←1(220⌶)a
      b
¯33 ¯108 5 0 0 0 31 39 0 0 2 0 0 0 97 98 0 0
      c←0(220⌶)b
      c≡a
1	 
     
```


