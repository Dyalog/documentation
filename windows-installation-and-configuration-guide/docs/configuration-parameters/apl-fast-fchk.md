# APL_FAST_FCHK

This parameter specifies whether Dyalog APL should optimise `⎕FCHK` by allowing it to reliably determine whether a component file had been properly untied and therefore does not need to be checked (this is overridable using the `⎕FCHK` option force).

Optimising `⎕FCHK` in this way has a performance impact on `⎕FUNTIE` and it is recommended this optimisation is switched off if your application frequently ties and unties files.

This only affects component files with journaling enabled.

The values of the parameter are:

|---|----------------------------------------------------|
|0  |Do not optimise `⎕FCHK` (optimise `⎕FUNTIE` instead)|
|1  |Optimise `⎕FCHK`                                    |

The default value of the parameter is 0 on all platforms. On Windows, setting the value 1 has no effect.
