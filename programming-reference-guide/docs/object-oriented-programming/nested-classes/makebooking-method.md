---
search:
  exclude: true
---

<h1 class="heading"><span class="name">MakeBooking Method</span></h1>

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
