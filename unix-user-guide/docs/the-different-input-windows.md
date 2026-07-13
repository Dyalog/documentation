# The Different Types of Input Windows

The tty version of Dyalog APL comprises of four different types of window:

## The Session window

There is one and only one session window. It is always present (although may be obscured by other windows. It cannot be resized from within APL (the terminal window or PuTTY session can be resized, and APL will respond to the resize event. Note that the contents of the window, including the status bar, may not correctly update until input is next received by the interpreter).

## Edit windows

Multiple edit windows can be open at any time, each on a separate object. The contents of edit windows can be altered, and these windows can be resized using the Move/Resize (MR) command.

## Trace windows

Multiple trace windows can be open at any time, one for each item on the stack. These windows are read-only, but these windows can be resized using the Move/Resize (MR) command.

## `⎕SM` (Screen manager) window

There can be only one `⎕SM` window; it exists only when `⎕SM` is not empty, and becomes visible either when waiting for user input (using `⎕SR`) or can be toggled to using the HotKey (HK) command.
