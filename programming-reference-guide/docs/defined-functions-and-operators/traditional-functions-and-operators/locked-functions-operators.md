# Locked Functions & Operators

A defined operation may be locked by the system function `⎕LOCK`.

Once locked, and operation may not be displayed or edited and the system functions `⎕CR`,  `⎕NR` and `⎕VR` return empty results.

Stop, trace and monitor settings are cancelled when an operation is locked.

A locked operation may not be suspended, nor may a locked operation remain pendent when execution is suspended.  Instead, the state indicator is cut back to the point where the locked operation was invoked.
