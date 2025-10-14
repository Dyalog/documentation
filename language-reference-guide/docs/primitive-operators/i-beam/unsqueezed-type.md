
<!-- Hidden search keywords -->
<div style="display: none;">
  181⌶
</div>






<h1 class="heading"><span class="name">Unsqueezed Type</span> <span class="command">R←181⌶Y</span></h1>



`Y` is any array.


The result `R` is an integer scalar containing an integer value which indicates the type of the array.
 For further information see [Data Representation (Monadic)](../../system-functions/data-representation-monadic.md).


`181⌶` is functionally identical to monadic `⎕DR`, except that no attempt is made to squeeze the data into smaller data types. `⎕DR` always attempts to squeeze the data; `181⌶` does not, but if a workspace compaction occurs during execution of `181⌶`, the data may still be squeezed before the type is identified.

<h2 class="example">Example</h2>
```apl

      ⎕DR 1↑1 1000
11
      (181⌶) 1↑1 1000
163
```



