---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NQ NQ
</div>






# <span>Enqueue Event</span> `{R}←{X}⎕NQ Y`{{key}}



**Windows only.**


This system function generates an event or invokes a method.


While APL is executing, events occur "naturally" as a result of user action or of communication with other applications.  These events are added to the event queue as and when they occur, and are subsequently removed and processed one by one by `⎕DQ`.  `⎕NQ` provides an "artificial" means to generate an event and is analogous to `⎕SIGNAL`.



If the left argument `X` is omitted or is 0, `⎕NQ` adds the event specified by `Y` to the bottom of the event queue. The event will subsequently be processed by `⎕DQ` when it reaches the top of the queue.


If `X` is 1, the event is actioned **immediately** by `⎕NQ` itself and is processed in exactly the same way as it would be processed by `⎕DQ`.  For example, if the event has a callback function attached, `⎕NQ` will invoke it directly. See [Dequeue Events](dq.md) for further details. If the event generates any subsidiary events (for example, a KeyPress might generate a GotFocus), the subsidiary events are added to the event queue rather than being executed immediately.


Note that it is not possible for one thread to use `1 ⎕NQ` to send an event to another thread.


If `X` is 2 and the name supplied is the name of an event, `⎕NQ` performs the default processing for the event immediately, but does **not** invoke a callback function if there is one attached.


If `X` is 2 and the name supplied is the name of a (Dyalog APL) method, `⎕NQ` invokes the method.  Its (shy) result is the result produced by the method.


If `X` is 3, `⎕NQ` invokes a method in an OLE Control.  The (shy) result of `⎕NQ` is the result produced by the method.


If `X` is 4, `⎕NQ` signals an event from an ActiveXControl object to its host application.  The (shy) result of `⎕NQ` is the result returned by the host application and depends upon the syntax of the event. This case is only applicable to ActiveXControl objects.



`Y` is a nested vector containing an event message.  The first two elements of `Y` are:


|-----|------|---------------------------------------------------------------------|
|`[1]`|Object|ref or character vector                                              |
|`[2]`|Event |numeric scalar or character vector which specifies an event or method|



`Y[1]` must specify an *existing* object.  If not, `⎕NQ` terminates with a `VALUE ERROR`.


If `Y[2]` specifies a standard event type, subsequent elements must conform to the structure defined for that event type.  If not, `⎕NQ` terminates with a `SYNTAX ERROR`. If additional elements (beyond those defined for the event type) are supplied this will not cause an error, but is not recommended because Dyalog may extend the event message in the future.


If `Y[2]` specifies a non-standard event type, `Y[3]` onwards (if present) may contain arbitrary information.  Although any event type not listed herein may be used, numbers in the range 0-1000 are reserved for future extensions.


If `⎕NQ` is used monadically, or with a left argument of 0, its (shy) result is always an empty character vector.  If a left argument of 1 is specified, `⎕NQ` returns `Y` unchanged or a modified `Y` if the callback function returns its modified argument as a result.


If the left argument is 2, `⎕NQ` returns either the value 1 or a value that is appropriate.

<h2 class="example">Examples</h2>
```apl
      ⍝ Send a keystroke ("A") to an Edit Field
      ⎕NQ TEST.ED 'KeyPress' 'A'

      ⍝ Iconify all top-level Forms
      {⎕NQ ⍵ 'StateChange' 1}¨'Form'⎕WN'.'

      ⍝ Set the focus to a particular field
      ⎕NQ TEST.ED3 40

      ⍝ Throw a new page on a printer
      1 ⎕NQ PR1 'NewPage'

      ⍝ Terminate ⎕DQ under program control

      'TEST'⎕WC 'Form' ... ('Event' 1001 1)
      ...
      ⎕DQ 'TEST'
      ...
      ⎕NQ TEST 1001  ⍝ From a callback

      ⍝ Call GetItemState method for a TreeView F.TV
      +2 ⎕NQ F.TV 'GetItemState' 6
96
			
      ⍝ Report where APL is installed
      +2 ⎕NQ'.' 'GetEnvironment' 'DYALOG'
C:\Program Files\Dyalog\Dyalog APL-64 15.0 Unicode
```


