---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕OFF OFF
</div>

# <span>Sign Off APL</span> `⎕OFF`

This niladic system function terminates the APL session, returning to the shell command level. The active workspace does not replace the last continuation workspace.

Although `⎕OFF` is niladic, you can specify an optional integer `I` to the right of the system function; this will be reported to the operating system as the exit code. If `I` is an *expression* generating an integer, you should put the expression in parentheses. `I` must be in the range 0-255, but note that Unix processes use values greater than 127 to indicate the signal number that was used to terminate a process, and currently APL itself generates values 0-13; this list is documented in [APL Exit Codes](../../../language-reference-guide/system-functions/off) and could be extended in future releases.
