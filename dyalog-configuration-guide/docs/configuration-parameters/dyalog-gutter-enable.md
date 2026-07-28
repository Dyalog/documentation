# DYALOG_GUTTER_ENABLE

Whether a gutter is displayed in the left-most column of the Session window. The gutter shows:

- a small red circle on every line that has been modified in the Session (including older lines moved to and edited without pressing `<ER>`), indicating which lines will be re-executed when `<ER>` is next pressed;
- a left bracket `[` identifying groups of [implicit output](../../../programming-reference-guide/introduction/output). Other forms of output are not marked in this way.

Valid values are:

- `0` : no gutter is displayed
- `1` : the gutter is displayed

Default depends on the interface: `0` for the TTY interface, `1` otherwise.
