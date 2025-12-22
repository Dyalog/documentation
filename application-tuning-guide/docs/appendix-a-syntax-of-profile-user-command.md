<h1 class="heading"><span class="name">Appendix A</span></h1>

Syntax of the `]Profile` User Command

The `]Profile` user command is always followed by a report type; modifiers can be included to customise the output.

Syntax: ]Profile [reporttype][-avg][-code][-lines]|[-outfile{=name}] [-format{=xml|csv|txt}][-cumpct][-exclusive][-first{=n}|-pct{=n}][-fn{=name}][-infile{=name}][-separators{="decimalsep phrasesep"}][-bias{=t}][-decimal{=n}][-expr{=expression}][-title{=name}]

# Report Types

The six possible report types are detailed below. If no report type is specified then a default report type is assumed; this is dashboard on the Microsoft Windows operating system and summary on the AIX, Linux and Mac OS operating systems.

|Report Type|Description|
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
-avg        |y| |y|y| |
-bias       |y|y|y|y|y|
-code       |y| | | |y|
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
|-title**   |y ** y **| y **| y **| y **|

* can only be used when -“format=csv is included
** only relevant when -“format=xml or -“format=txt

|Modifier| Description|
|-avg| Includes the average CPU consumption (in ms) per execution of each function call (or line if the -lines modifier is specified).
|-code| Includes the source code for the line being executed (including the -code modifier forces the -lines modifier).<br> Cannot be used with the -outfile modifier.|
|-cumpct|Displays the cumulative percentage of overall CPU consumption that each function call (or line if the -lines modifier is specified) and each function call above it was responsible for.<br>This is usually only useful if the -exclusive modifier is also set.|
|-exclusive|Displays the CPU consumption of each function call (or line if the -lines modifier is specified) excluding consumption due to called functions.|
|-first= n|After sorting into descending order of CPU consumption, displays only the first n function calls (or lines if the -lines modifier is specified).<br>This is usually only useful if the -exclusive modifier is also set.<br>Cannot be used with the -pct modifier.
|-fn= name|Mandatory for a calls report type, when it specifies the function that the calls analysis report is for. Optional for other report types, when output is filtered to only include data for the specified function and other functions that it calls.
|-lines|Displays a breakdown of consumption by individual line rather than a total for each function (the default).<br>Assumed when the -code modifier is specified.|
|-pct= n|After sorting into descending order of CPU consumption, displays only those function calls (or lines if the -lines modifier is specified) for which the cumulative percentage of overall CPU consumption is less than or equal to n.<br>This is usually only useful if the -exclusive modifier is also set.<br>Cannot be used with the -first modifier.|
|-format= n|Selects the file format to use when saving a file using the -outfile modifier. Possible values are:
* xml - writes data to an XML file (the default)
* csv - writes data to a CSV file
* txt - writes data to a text file (and retains the display format)
|-infile= n| Opens the Dashboard on the dataset contained in the specified.xml file.<br> Doing this does not destroy any existing `⎕PROFILE` data.|
|-separators= nn|For use with -format=csv.<br>Specifies the decimal and comma separators to use.<br>The default is '.,'|
|-title= n|For use with -format=xml or -format=txt.<br>Specifies the string that is used as a title caption in the Dashboard and XML reports. Especially useful when running the same expression multiple times as different captions can differentiate between different sets of results.<br> If the -title modifier is not specified, then the caption defaults to the string specified by the -expr modifier. If neither the -title nor the -expr modifiers are specified, then the caption defaults to `]profile Dashboard: <date> <time>`|
|-outfile= n| Redirects the output from the Session to the specified full path and filename (the full path must already exist).<br> Cannot be used with the -code modifier.
|-bias= t| Overrides the function call overhead estimated by â••PROFILE during the current session (or read from an infile), and uses t instead. Use -bias=0 to ignore bias, or a fixed value if you want to make sure that you use the same bias for data collected at different times. Depending on environment, t is likely to be in the range 0.00001-0.001 (in ms).|
|-decimal= n| Specifies the number of decimal places to display for non-integer numbers.
The default is 1.
|-expr= n| Executes the expression specified as the modifier value and replaces any existing â••PROFILE data with that for the specified expression.|


# Examples