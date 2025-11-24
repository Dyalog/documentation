---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕OFF OFF
</div>






<h1 class="heading"><span class="name">Sign Off APL</span> <span class="command">⎕OFF</span></h1>



This niladic system function terminates the APL session, returning to the shell command level.  The active workspace does not replace the last continuation workspace.


Although `⎕OFF` is niladic, you may specify an optional integer `I` to the right of the system function which will be reported to the Operating System as the exit code. If `I` is an *expression* generating an integer, you should put the expression in parentheses. `I` must be in the range 0..255, but note that on UNIX processes use values greater than 127 to indicate the signal number which was used to terminate a process, and that currently APL itself generates values 0..8; this list may be extended in future. This list is documented in the *Dyalog for Microsoft Windows Installation and Configuration Guide: APL Exit Codes*.



