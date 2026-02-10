# DECF Conversion

Incoming .NET data types System.Decimal and System.Int64  are converted to 126-bit decimal numbers (DECFs). This conversion is performed independently of the value of `⎕FR`.

To perform arithmetic on values imported in this way, set `⎕FR` to 1287, at least for the duration of the calculations.
