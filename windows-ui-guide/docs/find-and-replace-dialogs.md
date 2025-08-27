<h1 class="heading"><span class="name">Find and Replace Dialogs</span></h1>

The *Find* and *Find/Replace* dialog boxes are used to locate and modify text in an Edit window.

![](img/find-replace-dialog.png)

|---|---|
|Search For|Enter the text string that you want to find. Note that the text from the last 10 searches is available from the drop-down list. If appropriate, the search text is copied from the Find Objects tool. This makes it easy to first search for functions containing a particular string, and then to locate the same string in the functions.|
|Replace With|Enter the text string that you want to use as a replacement. Note that the text from the last 10 replacements is available from the drop-down list.|
|Match Case|Check this box if you want the search to be case-sensitive.|
|Match Whole Word|Check this box if you want the search to only match only whole words.|
|Use Regular Expressions|Check this box if you want to use Regular Expressions.|
|Move Dialog if Hiding Match|If checked, the *Find* or *Find/Replace* dialog box will automatically position itself so as not to obscure a matched search string in the edit window.|
|Find Next After Replace|If checked, following a replace operation, the selection will move to the next occurrence of the target string in the edit window.|
|Direction|Select *Up* or *Down* to control the direction of search.|

## Using Find and Replace

Find and Replace work on the concept of a *current search string* and a *current replace string* which are entered using the *Find* and *Find/Replace* Dialog boxes. These boxes also contain buttons for performing search/replace operations.

Suppose that you want to search through a function for references to the string "Adam". It is probably best to work from the start of the function, so first position the cursor there (by pressing Ctrl+Home). Then select *Find* from the *Edit* menu. The *Find* Dialog box will appear on your screen with the input cursor positioned in the edit box awaiting your input. Type "Adam" and click the *Find Next* button (or press Return), and the cursor will locate the first occurrence. Clicking *Find Next* again will locate the second occurrence. You can change the direction of the search by selecting *Up* instead of *Down*. You could search another function for "Adam" by opening a new Edit window for it and clicking *Find Next*. You do not have to redefine the search string.

Now let us suppose that you wish to replace all occurrences of "Adam" with "Amanda". First select *Replace* from the *Edit* menu. This will cause the *Find Dialog* box to be replaced by the *Find/Replace* Dialog box. Enter the string "Amanda" into the box labelled *Replace* With, then click *Replace All*. All occurrences of "Adam" in the current Edit window are changed to "Amanda". To repeat the same global change in another function, simply open an edit window and click *Replace All* again. If instead you only want to change particular instances of "Adam" to "Amanda" you may use *Find Next* to locate the ones you want, and then *Replace* to make each individual alteration.

Text searches are performed using PCRE. If the *Use Regular Expressions* box is checked, the full range of regular expressions provided by PCRE are available for use. See [PCRE Regular Expression Syntax Summary](../../language-reference-guide/pcre-specifications).

## Saving and Quitting

To save the function and terminate the edit, press Esc (EP) or select Exit from the *File* menu. The new version of the function replaces the previous one (if any) and the edit window is destroyed.

Alternatively, you can select *Fix* from the *File* menu. This fixes the new version of the function in the workspace, but leaves the edit window open. Note that the history is also retained, so you can subsequently undo some changes and fix the function again.

To abandon the edit, press Shift+Esc (QT) or select *Abort* from the *File* menu. This destroys the edit window but does not fix the function. The previous version (if any) is unchanged.
