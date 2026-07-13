---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕SD SD
</div>

# <span>Screen Dimensions</span> `R←⎕SD`{{key}}

`⎕SD` is a 2-element integer vector containing the number of rows and columns on the screen, or in the USER window.

For asynchronous terminals under UNIX, the screen size is taken from the terminal database *terminfo* or *termcap*.

In window implementations of Dyalog APL, `⎕SD` reports the current size (in characters) of the USER window or the current size of the SM object, whichever is appropriate.
