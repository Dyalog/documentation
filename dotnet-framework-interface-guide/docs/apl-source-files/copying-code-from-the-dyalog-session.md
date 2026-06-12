<h1 class="heading"><span class="name">Copying Code from the Dyalog Session</span></h1>

You might find it easy to write APL code using the Dyalog Session's function/class editor, or you might already have code in a workspace that you want to copy into an APL Source file. In either case, you can transfer code from the Session into your editor (for example, Notepad) using the clipboard.

As APL Source files require Unicode encoding (for APL symbols), you must ensure that character data is written to the clipboard in Unicode. In the Unicode interpreter this is always done. In the Classic interpreter, the UnicodeToClipboard configuration parameter specifies whether data is transferred to and from the Microsoft Windows clipboard as Unicode. The value of this parameter can be changed using the **Trace/Edit** tab of the **Configure** dialog box. If set (the default), APL text pasted to the clipboard from the Session is written as Unicode, and APL requests Unicode data back from the clipboard when it is required. This makes it easy to transfer APL code between the Session and an editor.

In the Classic interpreter, when pasting code into the Dyalog editor, there are two menu items under the **Edit** menu that allow you to explicitly select whether the Unicode mapping should be used or the old mapping (which corresponds to the Dyalog Std TT or Dyalog Alt TT fonts). You should use **Paste non-Unicode** when transferring text from the online documentation or text copied from earlier versions of Dyalog without the Unicode option.

When pasting APL code from the Session into an editor, line numbers can be included; although this is allowed, it is not recommended in APL Source files.

**To paste APL code from the Session into an editor**

1. Open the function in the function editor.
2. Select the lines of code that you want to copy.
3. Copy them (for example, by selecting **Edit** > **Copy** or pressing <kbd>Ctrl</kbd>+<kbd>Insert</kbd>).
4. Open your editor and paste the copied code (for example, by selecting **Edit** > **Paste** or pressing <kbd>Shift</kbd>+<kbd>Insert</kbd>).
5. Insert _del_ (`∇`) characters at the beginning and end of the function.

**To paste APL code from the Session into an editor including line numbers**

1. In the Session window, enter a _del_ (`∇`) character, then the name of the function, and then press <kbd>Enter</kbd>.<br />The function is displayed, with line numbers, in the **Session** window.
2. Complete the function definition, ending another _del_ (`∇`) character.
3. Select the function lines, including the surrounding _del_ (`∇`) characters, and copy them (for example, by selecting **Edit** > **Copy** or pressing <kbd>Ctrl</kbd>+<kbd>Insert</kbd>).
4. Open your editor and paste the copied code (for example, by selecting **Edit** > **Paste** or pressing <kbd>Shift</kbd>+<kbd>Insert</kbd>).
