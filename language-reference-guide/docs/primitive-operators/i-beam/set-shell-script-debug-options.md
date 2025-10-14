
<!-- Hidden search keywords -->
<div style="display: none;">
  1010⌶
</div>






<h1 class="heading"><span class="name">Set Shell Script Debug Options</span> <span class="command">R←{X}(1010⌶)Y</span></h1>



`Y` is an integer that selects options as follows.


If `Y` is 1, the lines in the script to be echoed to stderr before they are executed.. The optional left argument `X` specifies a character scalar of vector that prefixes each line of output. If `X` is omitted, the default is `'+'`.


If `Y` is 2, the effect is as if `⎕TRACE` was set for every line of every function in the script. In this case the left argument (if any) is ignored.


If `Y` is 3, it specifies a combination of the above.


The result `R` is the previous value of the debug options.



