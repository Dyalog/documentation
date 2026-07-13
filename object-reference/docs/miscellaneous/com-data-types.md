# COM data types



The table below shows the correspondence between COM data types and APL arrays.


|----------------|----------------------------------|
|**OLE DataType**|APL array                         |
|VT_BOOL         |numeric scalar                    |
|VT_I1           |numeric scalar                    |
|VT_I2           |numeric scalar                    |
|VT_I4           |numeric scalar                    |
|VT_R4           |numeric scalar                    |
|VT_R8           |numeric scalar                    |
|VT_BSTR         |character vector                  |
|VT_CY           |2-element numeric vector          |
|VT_DATE         |6 element numeric vector          |
|VT_VARIANT      |any array                         |
|VT_SAFEARRAY    |any array (VT_ARRAY OF VT_VARIANT)|
|VT_DISPATCH     |`⎕OR` of a namespace              |
|VT_COLOR        |3-element RGB                     |



APL vectors may be described by pre-fixing the data type string with `'VT_ARRAY OF '`. For example `'VT_ARRAY OF BSTR'` specifies a vector of character vectors.


If the APL array is the `⎕OR` of a namespace, its data type should be specified as `'VT_DISPATCH'`.


