---
search:
  boost: 2
---

# <span>Query Programmable Function Key</span> `R←⎕PFKEY Y`{{key}}

`⎕PFKEY` is a system function that sets or queries the programmable function keys.  `⎕PFKEY` associates a sequence of keystrokes with a function key.  When the user subsequently presses the key, it is as if he had typed the associated keystrokes one by one.

To set a programmable function key, use [dyadic `⎕PFKEY`](pfkey-dyadic.md).

Note that Ride does not currently support the use of `⎕PFKEY`; it is possible however to associate simple strings to function keys - see the [Ride User Guide](https://dyalog.github.io/ride) for more information.

`Y` is an integer scalar in the range 0-255 specifying a programmable function key.  The result `R` is the current setting of the key.  If the key has not been defined previously, the result is an empty character vector.

Programmable function keys are recognised in any of the three types of window (SESSION, EDIT and TRACE) provided by the Dyalog APL development environment. `⎕SR` operates with the 'raw' function keys and ignores programmed settings.

Note that key definitions can reference other function keys, such as "F1" or "F123".

The size of the buffer associated with `⎕PFKEY` is specified by the *pfkey_size* parameter.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕PFKEY PFKEY
</div>
