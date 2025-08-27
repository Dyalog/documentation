<h1 class="heading"><span class="name">DYALOG_GUTTER_ENABLE</span></h1>

This Boolean parameter specifies whether (1) or not (0) a Gutter is displayed in the left-most column of the Session window. This gutter is used to display:

- A small red circle. This indicator is used on every line that is modified in the session, including old ones (for example, if you move up the session and modify them, without pressing `<ER>`) . The indicators show which session lines will be re-executed when you subsequently press `<ER>`.
- A left bracket `[` to identify groups of default output. Note that other forms of output are not identified in this way.

The default value is 0 for the TTY interface, and 1 otherwise.
