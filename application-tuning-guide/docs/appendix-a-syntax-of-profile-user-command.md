<h1 class="heading"><span class="name">Appendix A</span></h1>

Syntax of the `]Profile` User Command

The `]Profile` user command is always followed by a report type; modifiers can be included to customise the output.

Syntax: ]Profile [reporttype][-avg][-code][-lines]|[-outfile{=name}] [-format{=xml|csv|txt}][-cumpct][-exclusive][-first{=n}|-pct{=n}][-fn{=name}][-infile{=name}][-separators{="decimalsep phrasesep"}][-bias{=t}][-decimal{=n}][-expr{=expression}][-title{=name}]

# Report Types

The six possible report types are detailed below. If no report type is specified then a default report type is assumed; this is dashboard on the Microsoft Windows operating system and summary on the AIX, Linux and Mac OS operating systems.

|Report Type|Description|
|-----------|-----------|
|`calls`|Shows how the consumption of a named function (the `-fn` modifier is required) is broken down by calling function. <br>The `summary` and `calls` report types are the most frequently used reporting tools.|
|`dashboard`|Opens the Dashboard, a graphical overview of the profiling data collected by the `⎕PROFILE` system function. For more information on the Dashboard, see Appendix B.
|`data`|Writes the raw data produced by `⎕PROFILE'data'` to a file for use with tools other than `]Profile`, for example, Microsoft Excel.|
|`state`|Displays the current profiling state of `⎕PROFILE` (see Section).|
|`summary`|Reports the number of calls, total consumption and consumption as a percentage of overall consumption.<br>The `summary` and `calls` report types are the most frequently used reporting tools. <br>This is the default report type on the AIX, Linux and macOS operating systems.|
|`tree`|Writes the raw data produced by `⎕PROFILE'tree'` to a file for later use. Intended as a tool for storing data using the `-outfile=<name>` modifier, for subsequent reporting using the `-infile=<name>` modifier.|

# Modifiers

The report types can be qualified using modifiers. These can, for example, filter the data that is displayed, add optional output columns, read input from a previously saved file or store the results of a command in a file.

Each of the report types can have different combinations of modifiers applied. The state report type does not take any modifiers; the valid modifiers for each of the other report types are shown in. the following table:

|Modifier   |Report Types                  ||||
|_^        _|calls|dashboard|data|summary|tree|
|-avg        |y| |y|y| |
|-bias       |y|y|y|y|y|
|-code       |y| | | |y|
|-cumpct    |y| |y| |y|
|-decimal   |y| |y|y|y|
|-exclusive |y| |y| |y|
|-expr      |y|y|y|y|y|
|-first     |y| |y| |y|
|-fn        |y|y|y|y| |
|-format    |y| |y|y|y|
|-infile    |y|y|y|y|y|
|-lines     |y| |y|y|y|
|-outfile   |y| |y|y|y|
|-pct       |y| |y|y| |
|-separators|y *| |y *|y *|y *|
|-title**   |y** |y **| y **| y **| y **|

* can only be used when -“format=csv is included
** only relevant when -“format=xml or -“format=txt

|Modifier| Description|
---------|------------
|-avg| Includes the average CPU consumption (in ms) per execution of each function call (or line if the -lines modifier is specified).
|-code| Includes the source code for the line being executed (including the -code modifier forces the -lines modifier).<br> Cannot be used with the -outfile modifier.|
|-cumpct|Displays the cumulative percentage of overall CPU consumption that each function call (or line if the -lines modifier is specified) and each function call above it was responsible for.<br>This is usually only useful if the -exclusive modifier is also set.|
|-exclusive|Displays the CPU consumption of each function call (or line if the -lines modifier is specified) excluding consumption due to called functions.|
|-first= n|After sorting into descending order of CPU consumption, displays only the first n function calls (or lines if the -lines modifier is specified).<br>This is usually only useful if the -exclusive modifier is also set.<br>Cannot be used with the -pct modifier.
|-fn= name|Mandatory for a calls report type, when it specifies the function that the calls analysis report is for. Optional for other report types, when output is filtered to only include data for the specified function and other functions that it calls.
|-lines|Displays a breakdown of consumption by individual line rather than a total for each function (the default).<br>Assumed when the -code modifier is specified.|
|-pct= n|After sorting into descending order of CPU consumption, displays only those function calls (or lines if the -lines modifier is specified) for which the cumulative percentage of overall CPU consumption is less than or equal to n.<br>This is usually only useful if the -exclusive modifier is also set.<br>Cannot be used with the -first modifier.|
|-format= n|Selects the file format to use when saving a file using the -outfile modifier. Possible values are:<br> * xml - writes data to an XML file (the default),<br> * csv - writes data to a CSV file<br> * txt - writes data to a text file (and retains the display format)|
|-infile= n| Opens the Dashboard on the dataset contained in the specified.xml file.<br> Doing this does not destroy any existing `⎕PROFILE` data.|
|-separators= nn|For use with -format=csv.<br>Specifies the decimal and comma separators to use.<br>The default is '.,'|
|-title= n|For use with -format=xml or -format=txt.<br>Specifies the string that is used as a title caption in the Dashboard and XML reports. Especially useful when running the same expression multiple times as different captions can differentiate between different sets of results.<br> If the -title modifier is not specified, then the caption defaults to the string specified by the -expr modifier. If neither the -title nor the -expr modifiers are specified, then the caption defaults to `]profile Dashboard: <date> <time>`|
|-outfile= n| Redirects the output from the Session to the specified full path and filename (the full path must already exist).<br> Cannot be used with the -code modifier.
|-bias= t| Overrides the function call overhead estimated by â••PROFILE during the current session (or read from an infile), and uses t instead. Use -bias=0 to ignore bias, or a fixed value if you want to make sure that you use the same bias for data collected at different times. Depending on environment, t is likely to be in the range 0.00001-0.001 (in ms).|
|-decimal= n| Specifies the number of decimal places to display for non-integer numbers.<br>The default is 1.|
|-expr= n| Executes the expression specified as the modifier value and replaces any existing â••PROFILE data with that for the specified expression.|


# Examples

These examples are intended to show at least one use of every modifier.

```apl
      )LOAD sharpplot
C:\...\ ws\sharpplot.dws saved Mon May  8 09:57:02 2017
      ⎕PROFILE 'start'
</pre><pre class="APLcode" xml:space="preserve">
      #.Samples.Sample 'Sample.svg'
mySharpPlot  Sample.svg
      ⎕PROFILE 'stop'
```

To see which 5 functions consumed the most CPU time:
```apl
      ]Profile summary -expr="#.Samples.Sample 'Sample.svg'" -first=5
 Element                      msec       %  Calls
 #.Samples.Sample             56.1   100.0      1
 #.SharpPlot.DrawLineGraph    24.9    44.4      1
 #.SharpPlot.Plot             18.0    32.1      1
 #.SharpPlot.DrawBarChart      7.8    14.0      1
 #.SharpPlot.CH∆PLOT           3.2     5.6      1
```
Show the five biggest CPU consumers, excluding CPU time spent in sub-functions. Display decimal numbers to 3 decimal places, include a cumulative percentage and only include functions up to 65% of the cumulative CPU:
```apl
      ]Profile summary -exclusive -decimal=3 -cumpct -pct=65
 Element               msec        %  Calls   %(cum)
 #.Samples.Sample    19.351   33.249      1   33.249
 #.SharpPlot.Plot    14.719   25.290      1   58.540
```

To see the average CPU consumption per call without adjusting for timer bias:
```apl
      ]Profile summary -exclusive -decimal=3 -avg -bias=0 -first=3
 Total time: 61.8 msec
 Element                        msec        %  Calls      Avg
 #.Samples.Sample             19.362   31.316      1   19.362
 #.SharpPlot.Plot             14.733   23.829      1   14.733
 #.SharpPlot.DrawLineGraph     7.254   11.733      1    7.254</pre>
```

The second set of numbers are higher than the first – the total time is 3.6 ms higher when the timer bias adjustment is not made and the function with the highest consumption, `#.Samples.Sample`, is reported as having consumed 0.011 ms more. The raw data recorded for a function can be displayed (without bias adjustment) by the data report type; in this case the function with the highest consumption is the one of interest:
```apl
      ]Profile data –fn=#.Samples.Sample
 Total time: 389.7 msec; Selected time: 104475.0 msec
 Element                Calls  msec(exc)  msec(inc)
 #.Samples.Sample           1       23.0      104.5
 #.Samples.Sample[1]        1        0.0        0.0
 #.Samples.Sample[2]        1        0.0        0.0
 #.Samples.Sample[3]        1        0.0        0.0
 #.Samples.Sample[4]        1        0.0        0.0
 #.Samples.Sample[5]        1        0.0        0.0
 #.Samples.Sample[6]        1        0.0        0.0
 #.Samples.Sample[7]        1        1.4        2.3
 #.Samples.Sample[8]        1        0.0        0.0
 ...etc...
```

For a summary or calls report, the `-code` modifier can be used to include source code in a report:
```apl
      ]Profile summary -code -lines -first=5
 Total time: 56.1 msec</pre><pre class="APLcode" xml:space="preserve"> Element                          msec      %  Calls  Code
 #.Samples.Sample[33]             25.5   45.4      1  sp.DrawBarChart⊂data1
 #.Samples.Sample[42]             24.9   44.4      1  sp.DrawLineGraph⊂data2
 #.SharpPlot.DrawLineGraph[43]    24.9   44.3      1  Plot yValues xValues'linegraph'
 #.SharpPlot.Plot[174]            17.3   30.9      1  cv←CH∆PLOT DATA VAL ptype iLine iMarker(bFramed∨bCropped)
 #.Samples.Sample[7]               2.0    3.5      1  sp←⎕NEW Causeway.SharpPlot</pre>
```

The `-outfile` modifier allows output to be directed to a file instead of displaying it in the Session. By default, the format of the data in the file is XML, but this can be changed to CSV or text with the `-format` modifier. For example:
```apl
      ]Profile data -outfile=c:\temp\data.csv -format=csv &#8209;separators='.,'
```
creates a CSV file using a period as the decimal separator and a comma as the field separator. For more information on the `-outfile` modifier, see data_storage.

If output is directed to an XML or text file, then the `-title` modifier can be used to specify a title that will be displayed when viewing that file in the Dashboard:
```apl
      ]Profile tree -expr="queens 8" -title="queens eight" &#8209;outfile="c:\temp\q8profile.xml"
```

If the `-title` modifier is omitted then the specified expression is used as the title.


The `-infile` modifier loads a previously-saved dataset for analysis – specifying this does not destroy any existing `⎕PROFILE` data:
`]Profile -infile="c:\temp\test.xml"`

This only applies when the dataset being loaded was a tree report saved in XML format (see Section 5.1).
