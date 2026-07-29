# APL_FAST_FCHK

Whether `⎕FCHK` is optimised so that it can reliably determine that a component file was properly untied and so need not be checked (this can be overridden with the `⎕FCHK` `force` option). The optimisation has a performance cost on `⎕FUNTIE`, so it is best switched off in applications that frequently tie and untie files. It affects only component files with journaling enabled.

Valid values are:

- `0` : do not optimise `⎕FCHK` (optimise `⎕FUNTIE` instead)
- `1` : optimise `⎕FCHK`

Default is `0` on all platforms. On Microsoft Windows, setting the value `1` has no effect.
