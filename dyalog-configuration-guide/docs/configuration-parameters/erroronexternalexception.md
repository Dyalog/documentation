# ErrorOnExternalException

This parameter specifies the behaviour when a System Exception occurs in an external DLL. If this parameter is set to 1, and an exception occurs in a call on an external DLL. APL generates an `EXTERNAL DLL EXCEPTION` error (91), instead of terminating with a System Error. This error may be trapped.
