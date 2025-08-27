<h1 class="heading"><span class="name">Entering Characters</span></h1>

It is necessary to select a metakey which is to be used to enter characters. In this document this metakey is represented by the string "APL". In a terminal window under a Linux GUI Dyalog recommends using the Windows key as the metakey to generate APL characters; with PuTTY and the Unicode IME the <kbd>Ctrl</kbd> key is used (similarly to the Windows Unicode edition of Dyalog APL). For example, in a terminal window <kbd>WindowsKey</kbd>+<kbd>a</kbd>generates an `⍺`; when using PuTTY the same APL character is entered by using <kbd>Ctrl</kbd>+<kbd>a</kbd>. 

!!!note 
    Under PuTTY, <kbd>Ctrl</kbd>+<kbd>xcv</kbd> are reserved for the operating system; we shall see later that <kbd>Ctrl</kbd>+<kbd>x</kbd> is used for another purpose. Rather than  <kbd>Ctrl</kbd>+<kbd>xcv</kbd> you must use  <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>xcv</kbd>.

Linux Window managers are in generally in a state of flux, so it is best to look at the following article on the Dyalog Forum for the latest information about keyboard configuration:

[https://www.dyalog.com/forum/viewtopic.php?f=20&t=210](https://www.dyalog.com/forum/viewtopic.php?f=20&t=210)

## Recently-added Glyphs

Newly-added glyphs are not always added to the keymap (keyboard mapping file) included in Linux distributions before they start to be used within Dyalog.

The following glyphs are not yet present in the distributed Linux keymap:

- `⍛` (Jot Underbar, Unicode character "APL FUNCTIONAL SYMBOL JOT UNDERBAR"). Used from Dyalog v20.0 for the [_behind_](../../language-reference-guide/primitive-operators/behind/) operator.

In this situation, there are several methods in which such glyphs can be typed. For `⍛`, you can do any of the following:

- Update the keyboard mapping file manually (see below).
- Define a [<kbd>Compose</kbd>](https://en.wikipedia.org/wiki/Compose_key) key and enter `⍛` by pressing <kbd>Compose</kbd> <kbd>Jot</kbd> <kbd>Underscore</kbd>.
- Within the Session, use the _Insert_ command **<IN\>** to change to overstrike mode, enter <kbd>Jot</kbd> <kbd>&larr;</kbd> <kbd>Underscore</kbd>, and enter **<IN\>** again to return to insert mode.
- In Ride, use the Prefix key and <kbd>F</kbd>.

---
**To update the keyboard mapping file**

1. Open the keyboard mapping file. By default, this is located in */usr/share/X11/xkb/symbols/apl*
2. Search for the text **xkb_symbols "dyalog_base"**
3. Replace<br>*key <AC04\> { [ underscore		] };	// low line*<br/>with:<br/>*key <AC04\> { [ underscore,	U235b	] };	// low line, jot underbar*
4. Log out and back in again.
---
Be aware that:

- there are multiple occurrences of AC04 within the keyboard mapping file – you should only amend the one in the Dyalog APL section.
- any changes made to the keyboard mapping file might be lost if you update the operating system.
