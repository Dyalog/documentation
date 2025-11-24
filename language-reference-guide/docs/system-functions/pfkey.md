---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PFKEY PFKEY
</div>






<h1 class="heading"><span class="name">Program Function Key</span> <span class="command">R←{X}⎕PFKEY Y</span></h1>



`⎕PFKEY` is a system function that sets or queries the programmable function keys.  `⎕PFKEY` associates a sequence of keystrokes with a function key.  When the user subsequently presses the key, it is as if he had typed the associated keystrokes one by one.


Note that Ride does not currently support the use of `⎕PFKEY`; it is possible however to associate simple strings to function keys - see the [Ride User Guide](https://dyalog.github.io/ride) for more information.



`Y` is an integer scalar in the range 0-255 specifying a programmable function key.  If `X` is omitted the result `R` is the current setting of the key.  If the key has not been defined previously, the result is an empty character vector.


If `X` is specified it is a simple or nested character vector defining the new setting of the key.  The value of `X` is returned in the result `R`.


The elements of `X` are either character scalars or 2-element character vectors which specify keycodes. See [Keyboard Shortcuts](../../../windows-ui-guide/keyboard-shortcuts).


Programmable function keys are recognised in any of the three types of window (SESSION, EDIT and TRACE) provided by the Dyalog APL development environment. `⎕SR` operates with the 'raw' function keys and ignores programmed settings.


Note that key definitions can reference other function keys, such as "F1" or "F123".


The size of the buffer associated with `⎕PFKEY` is specified by the *pfkey_size* parameter.

<h2 class="example">Examples</h2>
```apl
       (')FNS',⊂'ER')⎕PFKEY 1
┌─┬─┬─┬─┬──┐
│)│F│N│S│ER│
└─┴─┴─┴─┴──┘
       (')VARS',⊂'ER')⎕PFKEY 2
┌─┬─┬─┬─┬─┬──┐
│)│V│A│R│S│ER│
└─┴─┴─┴─┴─┴──┘
      'F1' 'F2' ⎕PFKEY 3 ⍝ Does )FNS and )VARS
┌──┬──┐
│F1│F2│
└──┴──┘

```



The following expression defines the action for F12 to be "move the text to the right of the cursor to the left of the cursor".
```apl
   
      'Rl' 'CT' 'LL' 'PT'⎕PFKEY 12
┌──┬──┬──┬──┐
│Rl│CT│LL│PT│
└──┴──┴──┴──┘

```



