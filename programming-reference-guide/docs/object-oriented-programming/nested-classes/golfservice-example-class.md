---
search:
  exclude: true
---

# GolfService Example Class

```apl
:Class GolfService
:Using System
    
    :Field Private GOLFILE←'' ⍝ Name of Golf data file
    :Field Private GOLFID←0 ⍝ Tie number Golf data file
    
```

```apl

    :Class GolfCourse
        :Field Public Code←¯1
        :Field Public Name←''
        
        ∇ ctor args
          :Implements Constructor
          :Access Public Instance
          Code Name←args
          ⎕DF Name,'(',(⍕Code),')'
        ∇
    
    :EndClass
    
```

```apl

    :Class Slot
        :Field Public Time
        :Field Public Players
        
        ∇ ctor1 t
          :Implements Constructor
          :Access Public Instance
          Time←t
          Players←0⍴⊂''
        ∇
        ∇ ctor2 (t pl)
          :Implements Constructor
          :Access Public Instance
          Time Players←t pl
        ∇
        ∇ format
          :Implements Trigger Players
          ⎕DF⍕Time Players
        ∇
    :EndClass
```

```apl
    :Class Booking
        :Field Public OK
        :Field Public Course
        :Field Public TeeTime
        :Field Public Message
        
        ∇ ctor args
          :Implements Constructor
          :Access Public Instance
          OK Course TeeTime Message←args
        ∇
        ∇ format
          :Implements Trigger OK,Message
          ⎕DF⍕Course TeeTime(⊃OK⌽Message'OK')
        ∇
    :EndClass
    
```

```apl

    :Class StartingSheet
        :Field Public OK
        :Field Public Course
        :Field Public Date
        :Field Public Slots←⎕NULL
        :Field Public Message
        
        ∇ ctor args
          :Implements Constructor
          :Access Public Instance
          OK Course Date←args
        ∇
        ∇ format
          :Implements Trigger OK,Message
          ⎕DF⍕2 1⍴(⍕Course Date)(↑⍕¨Slots)
        ∇
    :EndClass
    
```

```apl

    ∇ ctor file
      :Implements Constructor
      :Access Public Instance
      GOLFILE←file
      ⎕FUNTIE(((↓⎕FNAMES)~' ')⍳⊂GOLFILE)⊃⎕FNUMS,0
      :Trap 22
          GOLFID←GOLFILE ⎕FTIE 0
      :Else
          InitFile
      :EndTrap
    ∇
```
```apl
    ∇ dtor
      :Implements Destructor
      ⎕FUNTIE GOLFID
    ∇
    
    ∇ InitFile;COURSECODES;COURSES;INDEX;I
      :Access Public
      :If GOLFID≠0
          GOLFILE ⎕FERASE GOLFID
      :EndIf
      GOLFID←GOLFILE ⎕FCREATE 0
      COURSECODES←1 2 3
      COURSES←'St Andrews' 'Hindhead' 'Basingstoke'
      INDEX←(⍴COURSES)⍴0
      COURSECODES COURSES INDEX ⎕FAPPEND GOLFID
      :For I :In ⍳⍴COURSES
          INDEX[I]←⍬ ⍬ ⎕FAPPEND 1
      :EndFor
      COURSECODES COURSES INDEX ⎕FREPLACE GOLFID 1
    ∇
    
```

```apl

    ∇ R←GetCourses;COURSECODES;COURSES;INDEX
      :Access Public
      COURSECODES COURSES INDEX←⎕FREAD GOLFID 1
      R←{⎕NEW GolfCourse ⍵}¨↓⍉↑COURSECODES COURSES
    ∇
```

```apl
    ∇ R←GetStartingSheet ARGS;CODE;COURSE;DATE;COURSECODES
                             ;COURSES;INDEX;COURSEI;IDN
                             ;DATES;COMPS;IDATE;TEETIMES
                             ;GOLFERS;I;T
      :Access Public
      CODE DATE←ARGS
      COURSECODES COURSES INDEX←⎕FREAD GOLFID 1
      COURSEI←COURSECODES⍳CODE
      COURSE←⎕NEW GolfCourse(CODE(COURSEI⊃COURSES,⊂''))
      R←⎕NEW StartingSheet(0 COURSE DATE)
      :If COURSEI>⍴COURSECODES
          R.Message←'Invalid course code'
          :Return
      :EndIf
      IDN←2 ⎕NQ'.' 'DateToIDN',DATE.(Year Month Day)
      DATES COMPS←⎕FREAD GOLFID,COURSEI⊃INDEX
      IDATE←DATES⍳IDN
      :If IDATE>⍴DATES
          R.Message←'No Starting Sheet available'
          :Return
      :EndIf
      TEETIMES GOLFERS←⎕FREAD GOLFID,IDATE⊃COMPS
      T←DateTime.New¨(⊂DATE.(Year Month Day)),¨↓[1]
                                   24 60 1⊤TEETIMES
      R.Slots←{⎕NEW Slot ⍵}¨T,∘⊂¨↓GOLFERS
      R.OK←1
    ∇
```

```apl
    ∇ R←MakeBooking ARGS;CODE;COURSE;SLOT;TEETIME
                        ;COURSECODES;COURSES;INDEX
                        ;COURSEI;IDN;DATES;COMPS;IDATE
                        ;TEETIMES;GOLFERS;OLD;COMP;HOURS
                        ;MINUTES;NEAREST;TIME;NAMES;FREE
                        ;FREETIMES;I;J;DIFF
      :Access Public
      ⍝ If GimmeNearest is 0, tries for specified time          ⍝ If GimmeNearest is 1, gets nearest time     
      CODE TEETIME NEAREST←3↑ARGS
      COURSECODES COURSES INDEX←⎕FREAD GOLFID 1
      COURSEI←COURSECODES⍳CODE
      COURSE←⎕NEW GolfCourse(CODE(COURSEI⊃COURSES,⊂''))
      SLOT←⎕NEW Slot TEETIME
      R←⎕NEW Booking(0 COURSE SLOT'')
      :If COURSEI>⍴COURSECODES
          R.Message←'Invalid course code'
          :Return
      :EndIf
      :If TEETIME.Now>TEETIME
          R.Message←'Requested tee-time is in the past'
          :Return
      :EndIf
      :If TEETIME>TEETIME.Now.AddDays 30
          R.Message←'Requested tee-time is more than 30
                                          days from now'
          :Return
      :EndIf
      IDN←2 ⎕NQ'.' 'DateToIDN',TEETIME.(Year Month Day)
      DATES COMPS←⎕FREAD GOLFID,COURSEI⊃INDEX
      IDATE←DATES⍳IDN
      :If IDATE>⍴DATES
          TEETIMES←(24 60⊥7 0)+10×¯1+⍳1+8×6
          GOLFERS←((⍴TEETIMES),4)⍴⊂''llowed per tee time
          :If 0=OLD←⊃(DATES<2 ⎕NQ'.' 'DateToIDN',3↑⎕TS)/
                                                 ⍳⍴DATES
              COMP←(TEETIMES GOLFERS)⎕FAPPEND GOLFID
              DATES,←IDN
              COMPS,←COMP
              (DATES COMPS)⎕FREPLACE GOLFID,COURSEI⊃INDEX
          :Else
              DATES[OLD]←IDN
              (TEETIMES GOLFERS)⎕FREPLACE GOLFID,
                                          COMP←OLD⊃COMPS
              DATES COMPS ⎕FREPLACE GOLFID,COURSEI⊃INDEX
          :EndIf
```

```apl
          :Else
          COMP←IDATE⊃COMPS
          TEETIMES GOLFERS←⎕FREAD GOLFID COMP
      :EndIf
      HOURS MINUTES←TEETIME.(Hour Minute)
      NAMES←(3↓ARGS)~⍬''
      TIME←24 60⊥HOURS MINUTES
      TIME←10×⌊0.5+TIME÷10
      :If ~NEAREST
          I←TEETIMES⍳TIME
          :If I>⍴TEETIMES
          :OrIf (⍴NAMES)>⊃,/+/0=⍴¨GOLFERS[I;]
              R.Message←'Not available'
              :Return
          :EndIf
      :Else
          :If ~∨/FREE←(⍴NAMES)≤⊃,/+/0=⍴¨GOLFERS
              R.Message←'Not available'
              :Return
          :EndIf
          FREETIMES←(FREE×TEETIMES)+32767×~FREE
          DIFF←|FREETIMES-TIME
          I←DIFF⍳⌊/DIFF
      :EndIf
      J←(⊃,/0=⍴¨GOLFERS[I;])/⍳4
      GOLFERS[I;(⍴NAMES)↑J]←NAMES
      (TEETIMES GOLFERS)⎕FREPLACE GOLFID COMP
      TEETIME←DateTime.New TEETIME.(Year Month Day),
                                  3↑24 60⊤I⊃TEETIMES
      SLOT.Time←TEETIME
      SLOT.Players←(⊃,/0<⍴¨GOLFERS[I;])/GOLFERS[I;]
      R.(OK TeeTime)←1 SLOT
    ∇
    
:EndClass
```
