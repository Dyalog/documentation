<h1 class="heading"><span class="name">XML Format</span></h1>

Using the XML format generates very large files, but the content can be processed using `⎕XML` or many external tools (for more information on `⎕XML`, see the [Language Reference Guide](../../../language-reference-guide)). However, `tree` reports in XML format can be used as input to the `]Profile` user command (using the `-nfile` modifier) and are the only way to store a complete data set that can be reused for reporting at a later time. For example, entering the following command: 
```apl
      ]Profile tree -outfile=c:\temp\one.xml
```

saves the tree report in a file called `one.xml` in the `c:\temp` directory. This file can be opened later (in the same or a different Session) by entering:
```apl
      ]Profile summary -infile=c:\temp\one.xml
```
        <>In addition, as user commands can be executed under program control, an application can record its own usage data. For example:
```apl
      ⎕SE.UCMD 'profile tree -outfile=c:\temp\one.xml'
```
        The XML format produced by the `]Profile` user command comprises an outer `<ProfileData>` element; this contains a `<ProfileSettings>` element followed by a number of `<ProfileEntry>` elements, one for each row of output data.
        The `<ProfileSettings>` element contains the version number of the `]Profile` user command that produced the file, the report title, information about timer cost and other information, including the total registered time for the report.
        Each `<ProfileEntry>` element contains an element for each output column, depending on the command and switches, selected from the set listed in [](#_table-1)

Table: Elements that can be contained within the `ProfileEntry` element

|Element|Description|
|------|--------|
|`Depth`|Tree depth|
|`Element`|Function name|
|`Line`|Line number – empty for a function summary entry|
|`Calls`|Number of times the function or line was called|
|`InclusiveTime`<br />`ExclusiveTime`|Time consumed inclusive/exclusive of time consumed in any sub-functions called  (in ms)|
|`AvgTime`|Average time per call (in ms)|

<h2 class="example">Examples</h2>

This section contains a few examples of output files created using `-format=xml` (all files are encoded as UTF-8).

```apl
      ]Profile tree -outfile=tree.xml
Data written to: tree.xml</pre>
```
Content of the `tree.xml` file:`

```xml
<?xml version="1.0"?>
<ProfileData>
    <ProfileSettings>
        <Version>1.37</Version>
        <Title>2017/05/08 11:22:19</Title>
        <TimerBias>0.00007458669726290168</TimerBias>
        <Command>tree</Command>
        <TotalTime>173.41</TotalTime>
        <SelectedTime>173.41</SelectedTime>
    </ProfileSettings>
    <ProfileEntry>
        <Depth>0</Depth>
        <Element>#.Samples.Sample</Element>
        <Line>¯1</Line>
        <Calls>1</Calls>
        <ExclusiveTime>19.362</ExclusiveTime>
        <InclusiveTime>61.828</InclusiveTime>
    </ProfileEntry>
    ...
    ...many more occurrences of <ProfileEntry>...
    ...
</ProfileData>
```

```apl
      ]Profile summary -outfile=summary.xml
Data written to: summary.xml
```

Content of the <span class="path">summary.xml` file:
```xml
<?xml version="1.0"?>
<ProfileData>
    <ProfileSettings>
        <Version>1.37</Version>
        <Title>2017/05/08 11:31:00</Title>
        <TimerBias>0.00007458669726290168</TimerBias>
        <Command>summary</Command>
        <TotalTime>58.2</TotalTime>
        <SelectedTime>58.2</SelectedTime>
    </ProfileSettings>
    <ProfileEntry>
        <Element>#.Samples.Sample</Element>
        <Line/>
        <InclusiveTime>58.2</InclusiveTime>
        <PctOfTot>100</PctOfTot>
        <Calls>1</Calls>
    </ProfileEntry>
    ...
    ...many more occurrences of <ProfileEntry>...
    ...
</ProfileData>
```
