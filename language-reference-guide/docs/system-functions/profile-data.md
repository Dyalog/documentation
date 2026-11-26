---
search:
  boost: 2
---

# <span>Get Flat Profiling Data</span> `R←{X}⎕PROFILE'data'`{{key}}

This function returns the data that the [profiler](profile.md) has collected, with one row for each defined function and operator that ran, and one for each of their lines that ran. [`⎕PROFILE 'tree'`](profile-tree.md) returns the same data as a tree of calls.

<h2 class="example">Example</h2>

`Main` calls `Wait` twice, and `Wait` has one row for both calls:

```apl
      ∇ Main
        Wait 0.2
        Wait 0.1
      ∇
      ∇ Wait s
        ⎕DL s
      ∇
      ⎕PROFILE 'start' 'elapsed'
      Main
      ⎕PROFILE 'stop'
      ⎕PROFILE 'data'
 #.Wait     2 300.992763         300.992763         10 10
 #.Wait  0  2   0.00007000926416   0.00007000926416  2  2
 #.Wait  1  2 300.989708         300.989708          2  2
 #.Main     1   0.007795009878   301.000558          9 19
 #.Main  0  1   0.00004000321496   0.00004000321496  1  1
 #.Main  1  1   0.001722990419   200.562285          2  7
 #.Main  2  1   0.005561014405   100.437762          2  7
```

Columns 2 and 3 give the line numbers, with `¯1` for the whole functions, and the numbers of runs:

```apl
      2 3⎕PROFILE 'data'
 ¯1 0 1 ¯1 0 1 2  2 2 2 1 1 1 1 
```

## Left Argument

`X` is a simple integer vector of [column](#result) numbers from `1` to `7`, counted from `1` whatever the value of `⎕IO`. A scalar signals `RANK ERROR`, and a number outside the range signals `DOMAIN ERROR`.

## Right Argument

`Y` is `'data'`, which is not case-sensitive.

## Result

If `X` is omitted, `R` is a matrix with a row for each [entry](#entries) and these columns:

|Column|Content|
|------|-------|
|1|the name of the function or operator, including its namespace path|
|2|the line number, or `⍬` for the whole function or operator|
|3|the number of times that it ran|
|4|the time, in milliseconds, spent in it, excluding the functions and operators that it called|
|5|the time, in milliseconds, spent in it, including the functions and operators that it called|
|6|the number of timer calls for the time in column 4|
|7|the number of timer calls for the time in column 5|

If `X` is given, `R` has one item for each item of `X`, which is the column that it selects, as a vector. Column 2 then has `¯1` instead of `⍬` for whole functions and operators.

## Entries

For each defined function or operator that ran, there is a row for the whole function or operator, followed by a row for each of its lines that ran. Lines that never ran have no row. All the calls of a function or operator share its rows.

Line 0 is the header of a tradfn or tradop, or the first line of a dfn or dop, which contains its `{`. A single-line dfn or dop is all on line 0.

The times and timer calls of a whole function or operator include those of its lines, and any time that cannot be attributed to a line, such as the time spent setting up the function. With the timer `'none'`, the times are `0`. With `'coverage'`, the number of runs is `1` for each function, operator, and line that ran, and the other numbers are `0`.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PROFILE PROFILE
</div>
