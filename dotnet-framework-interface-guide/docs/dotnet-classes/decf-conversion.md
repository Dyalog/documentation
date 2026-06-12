<h1 class="heading"><span class="name">DECF Conversion</span></h1>

Incoming .NET data types <code class="language-nonAPL">VT_DECIMAL</code> (96-bit integer) and <code class="language-nonAPL">VT_CY</code> (currency value represented by a 64-bit two's complement integer, scaled by 10,000)  are converted to 126-bit decimal numbers (DECFs). This conversion is performed independently of the value of `⎕FR`.

To perform arithmetic on values imported in this way, set `⎕FR` to 1287, at least for the duration of the calculations.

!!! Info "Information"
    The .NET Framework converts <code class="language-nonAPL">System.Decimal</code> to DECFs but does not convert <code class="language-nonAPL">System.Int64</code> to DECFs.
