# APL_CODE_E_MAGNITUDE

The introduction of decimal floating point numbers lead to the maximum allowable print precision being increased from 17 to 34, which resulted in a change in the way numbers in the range `(10*17) to (10*34)` in function bodies are descanned[^1]. For example, the number one sextillion (10<sup>21</sup>) in a function is descanned by Version 12.1 as `1E21` and by Version 13.0 as `1000000000000000000000`.

Whilst this change has no other deleterious effect, it means that code that contains such numbers is  harder to read, and the result of `⎕CR` (and other character representations) of the same function may have changed between Version 12.1 and later versions of Dyalog causing undesired affects in code management systems.

The **APL_CODE_E_MAGNITUDE** parameter allows the user to choose between the behaviour seen in Version 12.1 and earlier and in more recent behaviour. It also allows the user to specify the size of numbers above which those numbers are display in exponential format.

If the **APL_CODE_E_MAGNITUDE** parameter is undefined or set to 0 (the default), numbers are descanned and displayed as normal.

If **APL_CODE_E_MAGNITUDE** has the value -1, numbers greater than or equal to 10<sup>17</sup> will be displayed using exponential format, as in  Version 12.1.

If **APL_CODE_E_MAGNITUDE** has a value between 2 and 34, numbers greater than or equal to 10<sup>value</sup> will be displayed using exponential format.

The effect of setting this parameter to any other value is undefined.

[^1]: Descanning refers to the internal process used to convert the internal representation of APL code into a character array. For numbers in function statements, this process  uses the maximum  value of Print Precision.
