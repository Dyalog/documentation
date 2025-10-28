<h1 class="heading"><span class="name">DECF Conversion</span></h1>

Incoming .NET data types VT_DECIMAL (96-bit integer) and VT_CY (currency value represented by a 64-bit two's complement integer, scaled by 10,000) are converted to 126-bit decimal numbers (DECFs). This conversion is performed independently of the value of `⎕FR`.

If you want to perform arithmetic on values imported in this way, then you should set `⎕FR` to 1287, at least for the duration of the calculations.

Note that the .NET interface converts System.Decimal to DECFs but does not convert System.Int64 to DECFs.
