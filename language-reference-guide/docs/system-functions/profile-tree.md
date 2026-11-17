---
search:
  boost: 2
---

# <span>Get Profiling Data Tree</span> `R←{X}⎕PROFILE'tree'`{{key}}

This function returns the data that the [profiler](profile.md) has collected as a tree of calls, in which the rows for each function or operator that a line called follow the row for that line. [`⎕PROFILE 'data'`](profile-data.md) returns the same data with one row for each function, operator, and line, however it was called.

<h2 class="example">Example</h2>

`Main` calls `Wait` twice, and `Wait` has rows under each line that calls it:

```apl
      ∇ Main
[1]    Wait 0.2
[2]    Wait 0.1
      ∇
      ∇ Wait s
[1]    ⎕DL s
      ∇
      ⎕PROFILE 'start' 'elapsed'
      Main
      ⎕PROFILE 'stop'
      ⎕PROFILE 'tree'
0  #.Main     1   0.00812599319    301.043435         9 19
1  #.Main  0  1   0.00005000038072   0.00005000038072 1  1
1  #.Main  1  1   0.002474000212   200.670393         2  7
2  #.Wait     1 200.667919         200.667919         5  5
3  #.Wait  0  1   0.00005000038072   0.00005000038072 1  1
3  #.Wait  1  1 200.666577         200.666577         1  1
1  #.Main  2  1   0.005191002856   100.372581         2  7
2  #.Wait     1 100.36739          100.36739          5  5
3  #.Wait  0  1   0.00005000038072   0.00005000038072 1  1
3  #.Wait  1  1 100.366248         100.366248         1  1
```

Columns 1 and 3 give the depths and the line numbers, with `¯1` for the whole functions:

```apl
      1 3⎕PROFILE 'tree'
 0 1 1 2 3 3 1 2 3 3  ¯1 0 1 ¯1 0 1 2 ¯1 0 1
```

## Left Argument

`X` is a simple integer vector of [column](#result) numbers from `1` to `8`, counted from `1` whatever the value of `⎕IO`. A scalar signals `RANK ERROR`, and a number outside the range signals `DOMAIN ERROR`.

## Right Argument

`Y` is `'tree'`, which is not case-sensitive.

## Result

If `X` is omitted, `R` is a matrix with a row for each [entry](#entries) and these columns:

|Column|Content|
|------|-------|
|1|the depth of the entry in the tree|
|2|the name of the function or operator, including its namespace path|
|3|the line number, or `⍬` for the whole function or operator|
|4|the number of times that it ran|
|5|the time, in milliseconds, spent in it, excluding the functions and operators that it called|
|6|the time, in milliseconds, spent in it, including the functions and operators that it called|
|7|the number of timer calls for the time in column 5|
|8|the number of timer calls for the time in column 6|

If `X` is given, `R` has one item for each item of `X`, which is the column that it selects, as a vector. Column 3 then has `¯1` instead of `⍬` for whole functions and operators.

## Entries

A function or operator that is called from the session has depth `0`, its lines have depth `1`, the functions and operators that they call have depth `2`, and so on. Therefore, the rows with an even depth are whole functions and operators, and the rows with an odd depth are lines. Each row for a whole function or operator is followed by the rows for its lines that ran, and each row for a line by the rows for the functions and operators that it called. Lines that never ran have no row. A function or operator that is called from more than one line, or that calls itself, has separate rows for each call path and each level of recursion.

Line 0 is the header of a tradfn or tradop, or the first line of a dfn or dop, which contains its `{`. A single-line dfn or dop is all on line 0.

The times and timer calls of a whole function or operator include those of its lines, and any time that cannot be attributed to a line, such as the time spent setting up the function. With the timer `'none'`, the times are `0`. With `'coverage'`, the number of runs is `1` for each function, operator, and line that ran, and the other numbers are `0`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PROFILE PROFILE
</div>
