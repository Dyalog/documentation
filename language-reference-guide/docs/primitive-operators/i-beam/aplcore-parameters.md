
<!-- Hidden search keywords -->
<div style="display: none;">
  1302⌶
</div>


<h1 class="heading"><span class="name">aplcore Parameters</span> <span class="command">R←1302⌶Y</span></h1>



Sets the aplcore parameters **AplCoreName** and/or **MaxAplCores** for the current process.


`Y` may be:

- a simple character vector that specifies AplCoreName
- a simple integer that specifies MaxAplCores 
- a 2-element nested vector containing new values for AplCoreName and MaxAplCores in that order
- an empty vector


`R` is a 2-element nested vector containing the old values.


If `Y` is empty, the function simply returns the values of these parameters without changing them.


See also: [AplCoreName](../../../../windows-installation-and-configuration-guide/configuration-parameters/aplcorename) and [MaxAplCores.](../../../../windows-installation-and-configuration-guide/configuration-parameters/maxaplcores)



