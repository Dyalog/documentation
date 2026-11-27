# ErrorOnExternalException

The behaviour when a system exception occurs in a call on an external DLL or shared library.

Valid values are:

- `0` : Dyalog terminates with a system error
- `1` : Dyalog generates a trappable `EXTERNAL DLL EXCEPTION` error (91) instead of terminating

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->
