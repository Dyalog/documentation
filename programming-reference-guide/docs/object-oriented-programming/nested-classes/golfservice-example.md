# GolfService Example

The [GolfService Example Class](golfservice-example-class.md) illustrates the use of nested classes. [GolfService](golfservice-example-class.md) was originally developed as a Web Service for Dyalog.NET and is one of the samples distributed in samples\asp.net\webservices. This version has been reconstructed as a stand-alone APL Class.

[GolfService](golfservice-example-class.md) contains the following nested classes, all of which are `Private`.

|---|---|
|[GolfCourse](golfcourse-class.md){: .noprint }|A Class that represents a Golf Course, having Fields `Code` and `Name` .|
|[Slot](slot-class.md){: .noprint }|A Class that represents a tee-time or match, having Fields `Time` and `Players` . Up to 4 players may play together in a match.|
|[Booking](booking-class.md){: .noprint }|A Class that represents a reservation for a particular tee-time at a particular golf course. This has Fields `OK` , `Course` , `TeeTime` and `Message` . The value of `TeeTime` is an Instance of a Slot Class.|
|[StartingSheet](startingsheet-class.md){: .noprint }|A Class that represents a day's starting-sheet at a particular golf course. It has Fields `OK` , `Course` , `Date` , `Slots` , `Message` . `Slots` is an array of Instances of Slot Class.|

The [GolfService](golfservice-example-class.md) constructor takes the name of a file in which all the data is stored. This file is initialised by method `InitFile` if it doesn't already exist.
```apl
      G←⎕NEW GolfService 'F:\HELP11.0\GOLFDATA'
      G
#.[Instance of GolfService]
```

The [GetCourses](getcourses-method.md){: .noprint } method returns an array of Instances of the internal (nested) Class [GolfCourse](golfcourse-class.md){: .noprint }. Notice how the display form of each Instance is established by the [GolfCourse](golfcourse-class.md){: .noprint } constructor, to obtain the output display shown below.
```apl
      G.GetCourses
 St Andrews(1)  Hindhead(2)  Basingstoke(3) 
```

All of the dates and times employ instances of the .NET type System.DateTime, and the following statements just set up some temporary variables for convenience later.
```apl
      ⎕←Tomorrow←(⎕NEW DateTime(3↑⎕TS)).AddDays 1
31/03/2006 00:00:00
      ⎕←TomorrowAt7←Tomorrow.AddHours 7
31/03/2006 07:00:00
```

The [MakeBooking](makebooking-method.md){: .noprint } method takes between 4 and 7 parameters viz.

- the code for the golf course at which the reservation is required
- the date and time of the reservation
- a flag to indicate whether or not the nearest available time will do
- a list of up to 4 players who wish to book that time.

- the code for the golf course at which the reservation is required
- the date and time of the reservation
- a flag to indicate whether or not the nearest available time will do
- a list of up to 4 players who wish to book that time.

The result is an Instance of the internal Class [Booking](booking-class.md){: .noprint }. Once again, `⎕DF` is used to make the default display of these Instances meaningful. In this case, the reservation is successful.
```apl
      G.MakeBooking 2 TomorrowAt7 1 'Pete' 'Tiger'
  Hindhead(2)   31/03/2006 07:00:00   Pete  Tiger    OK 
```

Bob, Arnie and Jack also ask to play at 7:00 but are given the 7:10 tee-time instead (4-player restriction).
```apl
      G.MakeBooking 2 TomorrowAt7 1 'Bob' 'Arnie' 'Jack'
 Hindhead(2)   31/03/2006 07:10:00   Bob  Arnie  Jack    OK 
```

However, Pete and Tiger are joined at 7:00 by Dave and Al.
```apl
       G.MakeBooking 2 TomorrowAt7 1 'Dave' 'Al'
  Hindhead(2)   31/03/2006 07:00:00   Pete  Tiger  Dave  Al    OK 
```

Up to now, all bookings have been made with the tee-time flexibility flag set to 1. Inflexible Jim is only interested in playing at 7:00...
```apl
      G.MakeBooking 2 TomorrowAt7 0 'Jim'
 Hindhead(2)  31/03/2006 07:00:00  Not available 
```

... so his reservation fails (4-player restriction).

Finally the [GetStartingSheet](getstartingheet-method.md){: .noprint } method is used to obtain an Instance of the internal Class [StartingSheet](startingsheet-class.md){: .noprint } for the given course and day.
```apl
      G.GetStartingSheet 2 Tomorrow
  Hindhead(2)  31/03/2006 00:00:00              
  31/03/2006 07:00:00   Pete  Tiger  Dave  Al   
  31/03/2006 07:10:00   Bob  Arnie  Jack        
  31/03/2006 07:20:00                           
  ....
```
