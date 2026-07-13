# yy_window

This parameter defines how Dyalog APL is to interpret a 2-digit year number. If **yy_window** is not set (the default) then under Windows, Version 13.2 onwards will adhere to the rules specified in the Windows Region and Language 2-digit year settings.

Dyalog allows a choice of input date formats for `⎕SM` and GUI edit fields. If you have chosen a 2-digit year format such as MM/DD/YY, then an input of 02/01/00 will by default be interpreted as 1<sup>st</sup>February 1900 - not 1<sup>st</sup>February 2000.

If your application uses a 4-digit year format such as YYYY-MM-DD, the problem will not arise.

You can use the **yy_window** parameter to cause your application to interpret 2-digit dates in as required without changing any APL code.

## Sliding versus Fixed Window

Two schemes are in common use within the industry: Sliding or Fixed date windows.

Use a Fixed window if there is a *specific year* , for example 1970, before which, dates are meaningless to your application. Note that with a fixed window, this date (say 1970) will still be the limit if your application is running in a hundred years' time.

Use a Sliding window if there is a *time period* , for example 30 years, before which dates are considered too old for your application. With a sliding window, you will always be able to enter dates up to (say) 30 years old, but after a while, specific years in the past (for example 1970) will become inaccessible.

## Setting a Fixed Window

To make a fixed window, set parameter **yy_window** to the 4-DIGIT year which is the earliest acceptable date. For example:

YY_WINDOW=1970

This will cause the interpreter to convert any 2-digit input date into a year in the range 1970, 1971 ... 2069

## Setting a Sliding Window

To make a sliding window, set parameter **yy_window** to the 1- or 2-DIGIT year which determines the oldest acceptable date. This will typically be negative.

YY_WINDOW=-30

Conversion of dates now depends on the current year:

If the current year is 1999, the earliest accepted date is 1999-30 = 1969.

This will cause the interpreter to convert any 2-digit input date into a year in the range 1969, 1970 ... 2068.

However if your application is still running in the year 2010, the earliest accepted date then will be 2010-30 = 1980. So in the year 2010, a 2-digit year will be interpreted in the range 1980, 1981 ... 2079.

## Advanced Settings

You can further restrict date windows by setting an upper as well as lower year limit.

YY_WINDOW=1970,1999

This causes 2-digit years to be converted only into the range 1970, 1971 ... 1999. Any 2-digit year (for example, 54) not convertible to a year in this range will cause a `DOMAIN ERROR` .

The sliding window equivalent is:

YY_WINDOW=-10,10

This would establish a valid date window, ten years either side of the current year. For example, if the current year is 1998, the valid range would be (1998-10) – (1998+10), in other words: 1988, 1989, `→` 2008.

One way of looking at the **yy_window** variable is that it specifies a 2-element vector. If you supply only the first element, the second one defaults to the first element + 99.

Note that the system uses only the number of digits in the year specification to determine whether it refers to a fixed (4-digits) or sliding (1-, or 2-digits) window. In fact you can have a fixed lower limit and a sliding upper limit, or vice versa.

YY_WINDOW=1990,10

Allows dates as early as 1990, but not more than 10 years hence.

YY_WINDOW=0,1999

Allows dates from the current year to the end of the century.

If the second date is before, or more than 99 years after the first date, then any date conversion will result in a `DOMAIN ERROR` . This might be useful in an application where the end-user has control over the input date format and you want to disallow any 2-digit date input.

YY_WINDOW=1,0
