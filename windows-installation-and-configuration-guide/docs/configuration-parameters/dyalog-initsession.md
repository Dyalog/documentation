# DYALOG_INITSESSION

Whether [Session initialisation](../../../windows-ui-guide/the-session-object/session-initialisation/) activities are performed when Dyalog is started. Session initialisation populates `⎕SE`, so that tools and functionality such as Link, SALT, user commands, and the numeric editor can work, together with everything related to `⎕SE.Dyalog`: event hooks, editor callbacks, output modification, serial number registration, and the collection of utilities listed by `⎕SE.Dyalog.Utils.⎕NL-⍳9`.

Valid values are:

- `0` – Session initialisation activities are not performed when Dyalog is started, and the [**DYALOGLINK**](dyaloglink.md), [**DYALOGSTARTUP**](dyalogstartup.md), [**DYALOGSTARTUPSE**](dyalogstartupse.md), and [**DYALOGSTARTUP_X**](dyalogstartup-x.md) parameters are ignored.
- `1` – Session initialisation activities are performed when Dyalog is started.

The default is `1` for development interpreters, and `0` for runtime interpreters and the shell script interpreters.

Which value to set depends on how you run Dyalog:

- If you use a runtime interpreter to distribute your application, you do not need to change the default. If you use one on a machine that you control, and you want the affected tools, set **DYALOG_INITSESSION** to `1`; this lengthens the start-up process.
- If you use shell scripts for deployment, you do not need to change the default. If you use shell scripts as an alternative to the interactive interface, set **DYALOG_INITSESSION** to `1`.
- If you are developing an application that is intended to run with a runtime interpreter, set **DYALOG_INITSESSION** to `0` for the development interpreter, so that it emulates the runtime environment. This identifies any inadvertent calls to tools that a runtime interpreter does not provide.
