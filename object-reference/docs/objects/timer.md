# <span>Timer</span> <span>Object</span>

[Parents](../parentlists/timer.md), [Properties](../proplists/timer.md), [Methods](../methodlists/timer.md), [Events](../eventlists/timer.md)

**Purpose:** To generate an action at regular intervals.

**Description**

The Timer object is used to generate an event at regular intervals. It can be used to produce animation and to implement "repeaters" such as spin buttons.

The [Interval](../properties/interval.md) property specifies how often the Timer generates events and is defined in milliseconds. Its default value is 1000.

The [Active](../properties/active.md) property determines whether or not the Timer generates events and can be used to switch the Timer off and on as required.

The [FireOnce](../properties/fireonce.md) property may be used to implement a once-off Timer event and has the value 0, 1 or 2.

Note that if you create a Timer object whose [Timer](../methodorevents/timer.md) event generates an error (for example by attaching it to a non-existent callback) it may be very difficult or even impossible to type into the Session, because the error will be displayed over and over again. Care is therefore recommended.
