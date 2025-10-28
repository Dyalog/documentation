<h1 class="heading"><span class="name">Copying code from the Dyalog  Session</span></h1>

You may find it easier to write APL code using the Dyalog APL function or class editor that is provided by the Dyalog APL Session. Or you may already have code in a workspace that you want to copy into an `APLScript` file.

If so, you can transfer code from the Session into your `APLScript` editor (for example, Notepad) using the clipboard. Notice that because APLScript requires Unicode encoding (for APL symbols), you must ensure that character data is written to the clipboard in Unicode.

In the Unicode interpreter this is always done. In the Classic interpreter this is controlled by a parameter called UnicodeToClipboard that specifies whether or not data is transferred to and from the Windows clipboard as Unicode. This parameter may be changed using the Trace/Edit page of the Configure dialog box.

If set (the default), APL text pasted to the clipboard from the Session is written as Unicode and APL requests Unicode data back from the clipboard when it is required. This makes it easy to transfer APL code between the Session and an APLScript editor.

In the Classic interpreter when pasting code *into* the Dyalog editor, there are two menu items under the Edit menu, which allow you to explicitly select whether the Unicode mapping should be used, or the old mapping which corresponds to the Dyalog Std TT or Dyalog Alt TT fonts. You should use "Paste non-Unicode" when transferring text from the on line help, or text copied from earlier versions of Dyalog APL without the Unicode option.

Unless you explicitly want to have line numbers in your `APLScript`, the simplest way to paste APL code from the Session into an APLScript text editor is as follows:

1. open the function in the function editor
2. select all the lines of code, or just the lines you want to copy
3. select *Edit/Copy* or press Ctrl+Ins
4. switch to your `APLScript` editor and select *Edit/Paste* or press Shift+Ins.
5. insert Del (`∇`) symbols at the beginning and end of the function.

If you want to preserve line numbers (this is allowed, but not recommended in APLScript files), you may use the following technique:

1. in the Session window, type a del  (`∇`) symbol followed by the name of the function, followed by another del  (`∇`) and then press Enter. This causes the function to be displayed, with line numbers, in the Session window.
2. select the function lines, including the surrounding Dels (`∇`) and choose *Edit/Copy* or press Ctrl+Insert.
3. switch to your `APLScript` editor and select *Edit/Paste* or press Shift+Ins.
