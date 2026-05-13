<h1 class="heading"><span class="name">DECF Conversion</span></h1>

Incoming .NET data types <code class="language-nonAPL">System.Decimal</code> and <code class="language-nonAPL">System.Int64</code> are converted to 126-bit decimal numbers (DECFs). This conversion is performed independently of the value of [`⎕FR`](../../../language-reference-guide/system-functions/fr/).

To perform arithmetic on values imported in this way, set `⎕FR` to 1287, at least for the duration of the calculations.
