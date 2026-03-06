# Upgrading from Previous Versions of Dyalog

The format of the bytecode used for compiled functions in Dyalog v15.0 onwards is not compatible with the bytecode used for compiled functions in previous versions of Dyalog. When loading a workspace containing compiled functions that was saved by a previous version of Dyalog, all bytecode for compiled functions will be discarded and you must use [`400⌶`](../compiler-control-ibeam.md) to recompile them).
