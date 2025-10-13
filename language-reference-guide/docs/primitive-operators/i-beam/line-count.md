
<!-- Hidden search keywords -->
<div style="display: none;">
  50100⌶
</div>






<h1 class="heading"><span class="name">Line Count</span> <span class="command">R←50100⌶Y</span></h1>



This function is a compact version of the system function `⎕LC`. If an expression requires only the  most recent line(s) in the function calling stack, this is a more efficient alternative to using `⎕LC`.


`Y` may be an integer specifying the depth of the function calling stack that is required in the result.


The result R is the same as `⎕LC`, but truncated to the number of stack levels specified by `Y`.

<h2 class="example">Example</h2>
```apl
          ∇ Foo
[1]    :If 4=⍴⎕LC
[2]        50100⌶0
[3]        50100⌶1
[4]        50100⌶2
[5]        50100⌶3
[6]        50100⌶4
[7]        50100⌶5
[8]        →
[9]    :Else
[10]       Foo
[11]   :EndIf
     ∇

      Foo

3
4 10
5 10 10
6 10 10 10
7 10 10 10
```



