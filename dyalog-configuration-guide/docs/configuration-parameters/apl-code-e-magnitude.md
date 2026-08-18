# APL_CODE_E_MAGNITUDE

The magnitude at or above which numbers in function bodies are descanned (written out as their character representation, for example by `⎕CR`) in exponential format. This controls whether large integers appear as, for example, `1E21` or `1000000000000000000000`, which affects the readability of code and the stability of its character representation across versions.

Valid values are:

- `0` – numbers are descanned and displayed normally (default)
- `¯1` – numbers greater than or equal to 10<sup>17</sup> use exponential format, as in Version 12.1
- an integer from `2` to `34` – numbers greater than or equal to 10<sup>value</sup> use exponential format

Default is `0`. The effect of any other value is undefined.
