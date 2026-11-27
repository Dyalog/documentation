# UseXCV

!!! Info "Information"
    This configuration parameter is only relevant on the Microsoft Windows operating system. It is defined for the Unicode IME in the Registry section `HKEY_CURRENT_USER\Software\Dyalog\UnicodeIME\`.

How the common copy (Ctrl+C), cut (Ctrl+X), and paste (Ctrl+V) keystrokes are processed.

Valid values are:

- `0` : processed normally, through the appropriate `.DIN` file
- `1` : passed untranslated to the host application (`dyalog.exe` treats Ctrl+X, Ctrl+C, and Ctrl+V as CT, CP, and PT respectively)

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->

The standard Dyalog keyboard (`*.din`) files map Shift+Del to CT, Ctrl+Ins to CP, and Shift+Ins to PT, so these work regardless of this setting. Those files also map both Ctrl+X and Ctrl+Shift+X to `⊃`, so when this parameter is `1` you must use Ctrl+Shift+X to obtain `⊃` (and likewise for C and V).
