
<!-- Hidden search keywords -->
<div style="display: none;">
  3500⌶
</div>

<h1 class="heading"><span class="name">Send Text to Ride-embedded Browser</span> <span class="command">R←{X}(3500⌶)Y</span></h1>

Optionally, `X` is a simple character vector or scalar, the contents of which are used as the caption for the tab in the Ride client that contains the embedded browser. If omitted, then the caption defaults to "`3500⌶`".

`Y` is a simple character vector the contents of which are displayed in the embedded browser tab.

The result `R` identifies whether the write to Ride was successful. Possible values are:

- `0` : the write to the Ride client was successful
- `¯1` : the write to the Ride client was not successful




