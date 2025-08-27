<h1 class="heading"><span class="name">Find Objects Tool</span></h1>

The *Find Objects* tool is a modeless dialog box that may be toggled on and off by the system action `[WSSearch]`. In a default Session, this action is attached to a MenuItem in the Tools menu and a Button on the session toolbar.

The Find Objects tool allows you to search the active workspace for objects that satisfy various criteria.

![](img/find-objects-dialog.png)

## Name

The *Named* field is used to search for objects with a particular name and is case-insensitive.

## Containing Text

The  *Containing Text*  field is used to search for objects that contain a particular text string. The string search is controlled by the fields *Match Case*, *Use Regular Expressions*, *Match Whole Word* and *As Symbol Reference*.

*Match Case* specifies whether or not the string search (for name and/or contents) is case sensitive.

*Use Regular Expressions* specifies whether or not regular expressions are applicable. For example, if you enter `FOO*` into the field labelled *Containing Text* and check this box, the system will find objects that contain any text string starting with the 3 characters `FOO`.

If this box is not checked, the system will find objects that contain the 4 characters `FOO*`.

Text searches are performed using PCRE. If the *Use Regular Expressions* box is checked, the full range of regular expressions provided by PCRE are available for use. See [PCRE Regular Expression Syntax Summary](../../language-reference-guide/pcre-specifications).

*Match Whole Word* specifies whether or not the search is restricted to entire words.

*As Symbol Reference* specifies whether or not the search is restricted to APL symbols. If so, matching text in comments and other strings is ignored.

## Object Criteria

Four check boxes are provided for you to specify the types of objects you wish to locate. For example, if you clear *Variables*, *Operators* and *Namespaces*, the system will only search for functions.

To make the search dependent upon modification, you must check the *Modified Objects* check box.

To locate objects modified by a particular user, enter the user name in the field labelled *Modified by*. Otherwise leave this blank.

To find objects which have been modified at a certain time or within a specified period of time, check the appropriate radio button and enter the appropriate dates or time spans.

If you wish to restrict the search to find only objects whose size is within a given range, check the box labelled *Size* is between and enter values into the fields provided.

## Location Criteria

You can restrict the search to a particular namespace by typing its name into the field labelled *Look in*. You can further restrict the search by clearing the *Include sub-namespaces* and *Include Session namespace* check boxes. Clearing the former restricts the search to the root namespace or to the namespace that you have specified in *Look in*, and does not search within any sub-namespaces contained therein. Clearing the latter causes the system to ignore `⎕SE` in its search.

When you press the *Find Now* button, the system searches for objects that satisfy all of the criteria that you have specified on all 3 pages of the dialog box and displays them in a ListView. The example below illustrates the result of searching the workspace for all objects containing references to the symbol `Speak`.

![](img/find-objects-dialog-results.png)

You may change the way in which the objects are displayed in the ListView using the *View* menu or the tool buttons, in the same manner as for objects displayed in the Workspace Explorer. You may also edit, delete and rename objects in the same way. Furthermore, objects can be copied or moved by dragging from the ListView in the Search tool to the TreeView in the Explorer.

If you wish to specify a completely new set of criteria, press the *New Search* button. This will reset all of the various controls  of the dialog box to their default values.
