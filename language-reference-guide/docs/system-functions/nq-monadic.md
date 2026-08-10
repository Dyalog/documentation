---
search:
  boost: 2
---

# <span>Enqueue Event</span> `{R}←⎕NQ Y`{{key}}

**Windows only.**

This system function generates an event or invokes a method.

To choose how the event is queued and what is returned, use [dyadic `⎕NQ`](nq-dyadic.md).

While APL is executing, events occur "naturally" as a result of user action or of communication with other applications.  These events are added to the event queue as and when they occur, and are subsequently removed and processed one by one by `⎕DQ`.  `⎕NQ` provides an "artificial" means to generate an event and is analogous to `⎕SIGNAL`.

`⎕NQ` adds the event specified by `Y` to the bottom of the event queue. The event will subsequently be processed by `⎕DQ` when it reaches the top of the queue.

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
      ⍝ Terminate ⎕DQ under program control

      'TEST'⎕WC 'Form' ... ('Event' 1001 1)
      ...
      ⎕DQ 'TEST'
      ...
      ⎕NQ TEST 1001  ⍝ From a callback

      ⍝ Call GetItemState method for a TreeView F.TV
      ⍝ Report where APL is installed
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NQ NQ
</div>
