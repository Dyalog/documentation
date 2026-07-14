

# <span>TRANSLATION ERROR</span> `92`

This report is given when the system cannot convert a character from Unicode to an Atomic Vector index or vice versa. Conversion is controlled by the value of  `⎕AVU`. Note that this error can occur when you **reference a variable** whose value has been obtained by reading data from a TCPSocket or by calling an external function. This is because in these cases the conversion to/from `⎕AV` is deferred until the value is used.
