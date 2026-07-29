#  APL Keyboards

The Classic and Unicode Editions of Dyalog APL for Windows use different techniques for mapping keystrokes to APL characters and to special command shortcuts.

The Classic Edition uses a proprietary technique for these mappings.

By default, the Unicode Edition uses Microsoft's IME (Input Method Editor) technology. Many other applications use the same technology, which means that the Dyalog Unicode IME may be used not only with *Dyalog APL for Windows Unicode Edition*, but also with word processing applications, spreadsheets, terminal emulators etc. Therefore, with the Dyalog Unicode IME installed, and with a suitable font selected, APL characters can be entered and viewed in many other applications.

As an alternative to the Dyalog Unicode IME, whose installation requires Administrator privileges, the key mapping for the Unicode Edition may be specified in the Windows registry. 

See the section [Unicode Edition and the Registry Keyboard](#unicode-edition-and-the-registry-keyboard) below.

In both Classic and Unicode Editions APL characters are generated when the user presses certain combinations of *meta keys* in conjunction with the normal character keys. Meta keys include <kbd>Shift</kbd>, <kbd>Ctrl</kbd> and <kbd>Alt</kbd>.

For both input techniques it is possible to alter the mapping of keystrokes to APL characters, and to add support for new languages. It is also possible to alter the keystrokes which define special command keyboard shortcuts. For further details, see [Unicode Edition Keyboard](unicode-edition-keyboard.md) or [Classic Edition Keyboard.](classic-edition-keyboard.md)

## Unicode Edition and the Dyalog Unicode IME

The Dyalog Unicode IME is the default input mechanism for generating APL characters for Unicode editions of Dyalog APL. The version of the IME supplied with version {{ version_majmin }} can be used  with version 12.1 and later, provided that they are patched to a version created on or after 1<sup>st</sup> April 2011.

The Dyalog Unicode IME defines the mapping of keystrokes to Unicode characters. Only keystrokes which resolve to characters that either do not appear on the standard keyboard or which differ from those that appear on the standard keyboard are included in the selectable translate table. In effect the Dyalog Unicode IME can be regarded as an overlay of the standard keyboard which contains just APL characters.

The Dyalog Unicode IME supplied with Version {{ version_majmin }} includes support for Belgian, Danish, Finnish, French, German, Italian, Spanish Swedish and British and American English keyboards, based on the Dyalog hardware keyboard layout; these keyboard layouts are described [here](https://dfns.dyalog.com/n_keyboards.htm). 

Note that for Danish, British and American English keyboards the older layouts, based on the Dyalog APL Ctrl Keyboard, are included in the `UnicodeIME\aplkeys` directory.

The default keyboard mapping for unsupported languages is American English.

The IME translate tables include mappings for the special command keystrokes used by Dyalog APL.

These command keystroke mappings are ignored by applications unless the application is explicitly named in the Dyalog Unicode IME configuration. It is expected that only terminal emulators used for running UNIX-based versions of Dyalog APL will use this feature.

In particular, Dyalog APL for Windows Unicode Edition does not use the mappings in the translate tables; the mappings are defined under `Options/Configure/Keyboard Shortcuts` (see [Keyboard Shortcuts Tab](../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-keyboard-shortcuts-tab/)).

Note that the Dyalog Unicode IME replaces any previous IME, as well as the Dyalog Ctrl and Dyalog AltGr keyboards.

## Unicode Edition and the Registry Keyboard

The Registry Keyboard provides an alternative mechanism for the Unicode Edition. This feature maps keystrokes to APL characters using entries in the Windows Registry. Dyalog supports the mechanism but does not provide the mappings which must therefore be defined by the user.

Note that the Dyalog IME is used if it is available; the Registry Keyboard mechanism is used only if the Dyalog IME is not installed.

The mappings are defined in the Registry sub-folder :
```
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Dyalog\Dyalog APL/W-64 {{ version_majmin }} Unicode\KeyboardShortcuts\chars
```

Each entry consists of theUnicode code point of an APL character followed by the keystroke to which it is mapped.

The keystroke is defined by 4 hexadecimal values which specify the key, the shift-state, and 2 zeros. The key is represented by the Unicode code point of the symbol engraved upon it, so (on a UK keyboard) the &lt;1&gt; key is hex 31 and the &lt;A&gt; key is hex 41. The Shift-states values are the sum of 1 (Shift), 2 (Ctrl), 4 (Alt).
```
"0x230A"=hex:44,02,00,00
"0x235F"=hex:38,03,00,00
```

In the first entry, the APL character is  Unicode code point  `230A` which is `⌊`. The key is &lt;D&gt; (hex 44) and the shift-state is Ctrl (hex 02).

In the second entry, the APL character is Unicode code point `235F` which is `⍟`. The character is entered by pressing &lt;\*&gt; (hex 38) with <kbd>Shift </kbd>+ <kbd>Ctrl</kbd> (hex 03).

## Classic Edition

The mapping for each of the `⎕AV` positions and its associated keystroke is defined by a selectable translate table. `⎕AV` includes all the APL symbols used by Dyalog APL as well as all the (non-APL) characters which appear on a standard keyboard. This mapping only works with Classic Edition.

The Classic Edition installation also includes the Dyalog Unicode IME (described below) so that users may enter APL characters into other applications; the Dyalog Unicode IME is however not used by the Classic Edition itself.

The Classic Edition includes support for Danish, Finnish, French, German, Italian, Swedish, and both British and American English keyboards. The default keyboard mapping for unsupported languages is American English.

## Backtick Keyboard

In addition to the standard APL keyboards, the Ride keyboard may be used natively. See [Backtick Keyboard](ime-configuration.md).
