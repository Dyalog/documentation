<h1 class="heading"><span class="name">Session Gutter</span></h1>

The first column of the Session Window (the Session Gutter) is by default reserved to display the following information:

- A small red circle. This indicator is used on every line that is modified in the session, including old ones (for example, if you move up the session and modify them, without pressing `<ER>`) . The indicators show which session lines will be re-executed when you subsequently press `<ER>`.
- A left bracket `[` to identify groups of default output. Note that other forms of output are not identified in this way.

![session gutter](../../img190/session-gutter.png)

The Session Gutter may be enabled and disabled using the **DYALOG_GUTTER_ENABLE** parameter. It is disabled by default in the TTY interface.
