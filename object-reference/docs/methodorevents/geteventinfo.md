# <span>GetEventInfo</span> <span>Method 551</span>

**Applies To:** [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md)

**Description**

This method is used to obtain information about a particular event or set of events supported by a COM object.

For each event supported by a COM object, the author will have registered the data type of its result (if it has a result), a help message or description of the event (optional) and the name and data type of each of its parameters. These event parameters make up the array returned by `⎕DQ` or supplied as an argument to your callback function. The GetEventInfo method returns this information.

The argument to GetEventInfo is a single item as follows:

|-----|-------------|---------|
|`[1]`|Event name(s)|see below|

*Event name(s)* is a simple character vector or a vector of character vectors specifying one or more names of events supported by the object.

The result is a nested vector with one element per event name. Each element of this vector is itself a vector of 2-element character vectors. For each event, the first item describes the help message or description (if any) registered for the event and the data type of its result. Each of the remaining elements contains a parameter name and its corresponding data type.

<h2 class="example">Example</h2>
```apl
      CLNAME←'Microsoft Multimedia Control, Version 6.0'
      'MM' ⎕WC 'OCXClass' CLNAME

      MM.EventList
 Done  BackClick  PrevClick  NextClick  PlayClick  ...

      DISPLAY ↑MM.GetEventInfo 'Done'
┌→───────────────────────────────────────────────────┐
↓ ┌→─────────────────────────────┐ ┌→──────┐         │
│ │Occurs when an MCI command ...│ │VT_VOID│         │
│ └──────────────────────────────┘ └───────┘         │
│ ┌→─────────┐                     ┌→──────────────┐ │
│ │NotifyCode│                     │VT_PTR to VT_I2│ │
│ └──────────┘                     └───────────────┘ │
└∊───────────────────────────────────────────────────┘
```

Note that if the event does not produce a result, the data type of the result is reported as `'VT_VOID'`.
