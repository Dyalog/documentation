<h1 class="heading"><span class="name">Appendix B</span></h1>

Keycodes, their common keystrokes, and the keystrokes specific to the PuTTY terminal emulator.

## Notes

1. APL represents the metakey used as the APL character and command shift
2. Cmd represents the keystroke <kbd>Ctrl</kbd>+<kbd>x</kbd>
3. CMD represents the keystrokes <kbd>Ctrl</kbd>+<kbd>x</kbd> <kbd>Ctrl</kbd>+<kbd>x</kbd>
4. The file $DYALOG\aplkeys\xterm is certain to be uptodate and should be treated as the definitive source of the keycode-keystroke translations

|Keycode|Command            |Common keystrokes    |PuTTY               |
|-------|-------------------|---------------------|--------------------|
|AC     |Align Comments     |Cmd a                |&nbsp;              |
|AO     |Comment Out        |Cmd ,                |&nbsp;              |
|BH     |Run to Exit        |Cmd <                |&nbsp;              |
|BK     |Back               |Cmd b                |Shift+Ctrl+Backspace|
|BP     |Toggle Breakpoint  |CMD b                |Shift+End           |
|BT     |Back Tab Window    |CMD Tab              |Shift+Ctrl+Tab      |
|CB     |Clear Breakpoints  |CMD B                |&nbsp;              |
|CP     |Copy               |Cmd c                |Ctrl+Insert         |
|CT     |Cut                |CMD c                |Shift+Delete        |
|DB     |Backspace          |Backspace            |Backspace           |
|DC     |Down Cursor        |Down                 |&nbsp;              |
|DI     |Delete Item        |Delete               |&nbsp;              |
|DK     |Delete Block       |Cmd Delete           |Ctrl+Delete         |
|DL     |Down Limit         |Ctrl+Down            |Ctrl+End            |
|DO     |Uncomment          |Cmd .                |&nbsp;              |
|DS     |Down Screen        |Shift+Down           |PgDn                |
|ED     |Edit               |Cmd e                |Shift+Enter         |
|EP     |Escape             |Esc                  |Esc                 |
|ER     |Enter              |Enter                |Enter               |
|FD     |Forward            |Cmd f                |Shift+Ctrl+Enter    |
|FX     |Fix                |Cmd x                |&nbsp;              |
|HK     |Hot Key ( `⎕SM` )  |Cmd u                |&nbsp;              |
|HO     |Home Cursor        |Cmd h                |&nbsp;              |
|IN     |Insert Mode        |Cmd i                |&nbsp;              |
|IT     | Inline Tracing    |Cmd k                |Alt+Ctrl+Enter      |
|JP     |Jump               |Cmd j                |Shift+Ctrl+Home     |
|LC     |Left Cursor        |Cursor Left          |&nbsp;              |
|LL     |Left Limit         |Ctrl+Left            |&nbsp;              |
|LN     |Line Numbers       |Cmd l                |&nbsp;              |
|LS     |Left Screen        |Shift+Left           |Ctrl+Left           |
|MO     |Move to Outline    |CMD %                |Shift+Ctrl+Up       |
|MR     |Move/Resize        |CMD m                |&nbsp;              |
|MV     |Move block         |Cmd m                |Shift+Ctrl+Delete   |
|NX     |Next               |Cmd n                |Shift+Ctrl+Right    |
|OP     |Open line          |Cmd o                |Shift+Ctrl+Insert   |
|PT     |Paste              |CMD p                |Shift+Insert        |
|PV     |Previous           |Cmd p                |Shift+Ctrl+Left     |
|QT     |Quit               |Cmd q                |Shift+Esc           |
|RA     |Repeat All         |CMD d                |Ctrl+Down           |
|RC     |Cursor Right       |Right                |&nbsp;              |
|RD     |Redraw Function    |CMD r                |Shift+PgUp          |
|RL     |Right Limit        |Ctrl+Right           |&nbsp;              |
|RM     |Resume All Threads |Cmd >                |&nbsp;              |
|RP     |Replace String     |Cmd r                |&nbsp;              |
|RS     |Right Screen       |Shift+Right          |Ctrl+PgDn           |
|RT     |Repeat (Do)        |Cmd d                |Shift+Ctrl+Down     |
|SC     |Search             |Cmd s                |&nbsp;              |
|SR     |Redraw Screen      |Ctrl+l <sup>(1)</sup>|&nbsp;              |
|TB     |Tab Window         |Cmd Tab              |Ctrl+Tab            |
|TC     |Trace              |Cmd Enter            |Ctrl+Enter          |
|TG     |Tag                |Cmd t                |&nbsp;              |
|TL     |Toggle Localisation|CMD l                |Ctrl+Up             |
|TO     |Toggle Outline     |CMD o                |Shift+Up            |
|UC     |Cursor Up          |Cursor Up            |&nbsp;              |
|UL     |Up Limit           |Ctrl+Up              |Ctrl+Home           |
|US     |Up Screen          |Shift+Up             |PgUp                |
|ZM     |Zoom               |Cmd z                |Shift+Ctrl+PgUp     |

## Notes

- If you are using PuTTY or another emulator that uses the Dyalog Unicode IME, it will be necessary to swap to a non-Dyalog APL keyboard before hitting Ctrl-l; hitting Ctrl-l while in a Dyalog APL keyboard will generate a Quad symbol.
