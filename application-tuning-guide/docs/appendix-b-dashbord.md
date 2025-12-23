<h1 class="heading"><span class="name">Appendix B</span></h1>

The Dashboard

!!! windows "Dyalog on Microsoft Windows"
    The Dashboard is only available on the Microsoft Windows operating system.


To open the Dashboard on a dataset, call the `]Profile` user command without specifying any report type, that is: `]Profile`

The Dashboard will open and display an  overview of the data currently stored by `⎕PROFILE` (`⎕PROFILE` must  be stopped/inactive).

## Panels

The main body of the Dashboard is divided into four panels by moveable splitters, as shown in Figure

The panels shown in the figure above are:

* panel 1 – Functions panel<br />Consumption broken down by function. Displayed as a pie chart by default, but can be displayed as a table using the drop-down selector in the top right corner.

* panel 2 – Lines panel<br />Consumption broken down by line. Displayed as a table with lines presented in order of decreasing CPU percentage consumed, but can be displayed as a pie chart using the drop-down selector in the top right corner.

* panel 3 – Line details panel<br />Only populated when a line is clicked in panel 2; displays the code of the function in which the selected line appears.

* panel 4 – Function details panel<br />Only populated when a function is clicked in panel 1; displays the code of the selected function.<br />

In the figure above, the Function details panel was populated by clicking on the pie segment for `#.SharpPlot.Plot` in the Functions panel and the Line Details panel was populated by clicking on the row for `#.SharpPlot.Plot[174]` in the table in the Lines panel.

## Display Options

The information presented in the four panels can be configured using the options described in this section.

Immediately above the Lines panel are two drop-down lists:

* **Pcts of** – how the percentages listed in tables and as labels on pie charts are computed:

	* Total: The given percentage is the percentage of overall consumption.
This is the default.

	* Selection: The given percentage is the percentage of consumption of the
function currently being displayed.

* **Showing** – whether tables report time consumed inclusive or exclusive of time
consumed in any sub-functions called (pie charts always report exclusive time):

	* Exclusive: Show the consumption of each line or function excluding time
consumed in any sub-functions called. This is the default.

	* Inclusive: Show the consumption of each line or function including time
consumed in any sub-functions called.


Changing the selections in these drop-down lists changes the display in the Functions panel and Lines panel.

The Functions panel and Lines panel each have a drop-down list in the top-right
corner:

* Table – if selected, functions/lines are displayed in tabular form. Left-clicking a row in a table displays information related to that row's function/line in the
Function details/Line details panel. This is the default for the Lines panel.

* Pie – if selected, functions/lines are displayed in a pie chart with segment sizes related to CPU percentage consumed. Left-clicking a segment in a pie chart
displays information related to that segment's function/line in the Function
details/Line details panel. This is the default for the Functions panel.

The Function details panel and Line details panel each have two check boxes in the top-right corner:

* **Blanks/comments** – if selected, the details presented will include lines that are blank or only comprise a comment. The default is for these to be omitted.
* **Lines not called** – if selected, any lines that were not called at all when running the function will be included. The default is for these to be omitted.

## Navigating the Functions/Lines

A left-click in a pie segment (or on its label) or table row displays the source code for the selected function/line in the quadrant below. A double-click drills down on the relevant function/line (if possible) and updates all quadrants accordingly. Drilling down always allows indirect calls.

### Breadcrumb Trail

Immediately above the panelled body of the Dashboard (see Section ##Panels) is a breadcrumb trail describing the function currently displayed in the panels. At the end of this breadcrumb trail is a label that reports the percentage of the overall consumption that this function accounts for. Figure B-2  shows an example breadcrumb trail.


Each breadcrumb in the trail has one of the following symbol/highlighting colour combinations:

* A right arrow (`→`) and blue highlighting indicate a direct call to a function without intermediate functions.

* A star (`*`) and green highlighting indicate a call sequence in which other functions could have been called.

* An upwards arrow (`↑`) and pink highlighting indicate a "show calls" step has been made, that is, consumption is displayed according to the functions/lines that have called the relevant function/line (see Section ##B3.2).

Clicking a function in the breadcrumb trail displays that function in the panels.

### Right-click Menu

A right-click in a pie segment (or on its label) or table row displays a pop-up menu with the following options, each of which impacts one or more panels of the display:

* **Drill Down** – Drills down one level on the relevant function/line (equivalent to double-clicking on the relevant segment/label/row). This option is only included in the pop-up menu when it is possible to drill down.

* **Make Root** – Only displays consumption that originates in the relevant function/line.

* **Reset** – Returns to the starting position.

* **Show Calls** – Breaks down consumption according to the functions/lines that have called the relevant function/line (higher levels of filtering are retained).

* **Up 1 Level** –  Drills up one level (equivalent to clicking on the penultimate breadcrumb in the breadcrumb trail). This option is only included in the pop-up menu when it is possible to drill up.

## Menu Bar

This section details the options available under each of the menu items in the menu bar.

### File Menu

The options available under the *File* menu are detailed in the following table:

|Item |Description|
|-----|-----------|
|Open |Opens an explorer window from which an XML file can be selected and analysed.<br>Equivalent to starting the Dashboard with the `-infile` modifier set.|
|Save |Saves the current dataset.<br>Equivalent to calling the `]Profile` user command with the  `-outfile` modifier set.|
|Reset|Returns the Dashboard to its the initial state, displaying the initial top-level function in four panels (as shown in Figure #).
|Exit |Terminates the Dashboard and returns to the Dyalog Session.|

For panel number references, see Section #

### Windows Menu

The options available under the *Windows* menu are detailed in the following table:

|Item|Description|
|----|---------|
|Reset|Positions the vertical and horizontal splitters in their default position, as seen when first opening the Dashboard, and display the first function in the breadcrumb trail.|
|Functions|Moves the vertical splitter to the right hand edge of the Dashboard, displaying only the functions panels (panels 1 and 4).<br>This can also be achieved by double-clicking at the top of the Functions panel (panel 1).
|Function Details|Moves the vertical splitter to the right-hand edge of the Dashboard and the horizontal splitter to the top of the Dashboard, displaying only the Function details panel (panel 4).<br>This can also be achieved by double-clicking at the top of the Function details panel (panel 4).
|Lines|Moves the vertical splitter to the left-hand edge of the Dashboard, displaying only the lines panels (panels 2 and 3).<br>This can also be achieved by double-clicking at the top of the Lines panel (panel 2).
|Line Details|Moves the vertical splitter to the left-hand edge of the Dashboard and the horizontal splitter to the top of the Dashboard, displaying only the Line details panel (panel 3).<br>This can also be achieved by double-clicking at the top of the Line details panel (panel 3).

For panel number references, see Section 


### Help Menu

The options available under the *Help menu* are detailed in the table below.

|Item |Description|
|-----|---------|
|About|Displays the version number of the `]PROFILE` user command and the corresponding user command framework.

## Single Function Mode

If the data set only pertains to a single function, then the dashboard displays two panels rather than four (as shown in [](#B-3)). In this situation, the panel on the left displays the detailed view of the function body (equivalent to panel 3 or 4 in panels.md#moveablesplitters"); the panel on the right displays the Lines panel (equivalent to panel 2 in panels.md#moveablesplitters).

<h3 class="example">Example</h3>
```apl
      )LOAD dfns
      ]Profile -eqpr="⍴queens 8"
```

![Dashboard in single function mode](){ #B-3}
