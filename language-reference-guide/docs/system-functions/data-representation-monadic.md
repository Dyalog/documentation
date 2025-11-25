---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕DR DR
</div>






<h1 class="heading"><span class="name">Data Representation (Monadic)</span> <span class="command">R←⎕DR Y</span></h1>



Monadic `⎕DR` returns the type of its argument `Y`.  The result `R` is an integer scalar containing one of the following values. Note that the internal representation and data types for character data differ between the Unicode and Classic Editions.




Table: Unicode Edition


|Value|Data Type                                |
|-----|-----------------------------------------|
|11   |1 bit Boolean                            |
|80   |8 bits character                         |
|83   |8 bits signed integer                    |
|160  |16 bits character                        |
|163  |16 bits signed integer                   |
|320  |32 bits character                        |
|323  |32 bits signed  integer                  |
|326  |Pointer (32-bit or 64-bit as appropriate)|
|645  |64 bits Floating                         |
|1287 |128 bits Decimal                         |
|1289 |128 bits Complex                         |




Table: Classic Edition


|Value|Data Type                                 |
|-----|------------------------------------------|
|11   |1 bit Boolean                             |
|82   |8 bits character                          |
|83   |8 bits signed integer                     |
|163  |16 bits signed integer                    |
|323  |32 bits signed integer                    |
|326  |Pointer  (32-bit or 64-bit as appropriate)|
|645  |64 bits Floating                          |
|1287 |128 bits Decimal                          |
|1289 |128 bits Complex                          |



