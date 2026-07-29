# yy_window

How Dyalog interprets a 2-digit year number (for `⎕SM` and GUI edit fields that use a 2-digit year format such as `MM/DD/YY`). It has no effect on applications that use a 4-digit year format. The value defines a *date window*, either fixed or sliding.

Valid values are:

- a 4-digit year : a **fixed** window whose earliest acceptable year is that value (for example `1970` maps 2-digit input to `1970`-`2069`)
- a 1- or 2-digit year, typically negative : a **sliding** window whose oldest acceptable year is that many years before the current year (for example `-30` in 1999 maps input to `1969`-`2068`)
- two values separated by a comma : the lower and upper limits of the window (each independently fixed (4-digit) or sliding (1- or 2-digit)); a 2-digit year that does not convert into the range signals a `DOMAIN ERROR`. If only the first is given, the second defaults to the first plus 99.

Default is unset: on Microsoft Windows, Dyalog then follows the Region and Language 2-digit year settings.

The number of digits in each value determines whether it is a fixed (4-digit) or sliding (1- or 2-digit) limit, so a window can mix the two, for example `YY_WINDOW=1990,10` allows dates from `1990` to at most 10 years hence.
