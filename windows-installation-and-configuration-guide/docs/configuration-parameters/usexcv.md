# UseXCV

This Boolean parameter specifies how the commonly used keystrokes for copy (ctrl+c), cut Ctrl+x) and paste (ctrl+v) are processed.

0 = process  normally (via the appropriate .DIN file)1 = pass  untranslated to the host application

The **UseXCV** parameter is defined for the IME in the Registry section `HKEY_CURRENT_USER\Software\Dyalog\UnicodeIME\`

When **UseXCV** is 1, the keystrokes Ctrl+X, Ctrl+C and Ctrl+V are passed untranslated to `dyalog.exe` which treats them as CT, CP and PT respectively. This is likely to be true for other host applications using the Dyalog keyboard.

The standard Dyalog keyboard (*.din) files map  Shift+Del to CT, Ctrl+Ins to CP, and Shift+Ins to PT. These will therefore work independently of the **UseXCV** option.

The standard Dyalog keyboard (*.din) files map BOTH Ctrl+X and Ctrl+Shift+Xto `⊃` So if **UseXCV** is set to 1, you must use Ctrl+Shift+X to obtain `⊃`. Likewise for C and V.
