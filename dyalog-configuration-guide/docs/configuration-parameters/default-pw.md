# Default_PW

The value of [`⎕PW`](../../../language-reference-guide/system-functions/pw) in a clear workspace. `⎕PW` is a property of the Session, so this value is overridden when a Session file is loaded, and when [`Auto_PW`](auto-pw.md) causes `⎕PW` to track the width of the Session (Windows) or terminal (UNIX and macOS) window.

Valid values are those of `⎕PW`: an integer from `42` to `32767`.

<!-- REVIEW(default): clear-workspace default for ⎕PW not stated in the migrated source; confirm per operating system. -->

Related parameters: [Auto_PW](auto-pw.md).
