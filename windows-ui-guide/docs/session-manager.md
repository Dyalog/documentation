# Session Manager

The Dyalog APL/W session is fully configurable. Not only can you change the appearance of the menus, tool bars and status bars, but you can add new objects of your choice and attach your own APL functions and expressions to them. Functions and variables can be stored in the session *namespace*. This is *independent* of the active workspace; so there is no conflict with workspace names, and your utilities remain permanently accessible for the duration of the session. Finally, you may set up different session configurations for different purposes which can be saved and loaded as required.

The session window is defined by an object called `⎕SE`. This is very similar to a Form object, but has certain special properties. The menu bar, tool bar and status bars on the session window are in fact MenuBar, ToolControl and StatusBar objects owned by `⎕SE`. All of the other components such as menu items and tool buttons are also standard GUI objects. You may use `⎕WC` to create new session objects and you may use `⎕WS` to change the properties of existing ones. `⎕WG` and `⎕WN` may also be used with `⎕SE` and its children.

Components of the session that perform actions (MenuItem and Button objects) do so because their Event properties are defined to execute system operations or APL expressions. System operations comprise a pre-defined set of actions that can be performed by Dyalog APL/W. These are coded as keywords within square brackets. For example, the system operation `[WSClear]` produces a `clear ws`, after first displaying a dialog box for confirmation. You may customise your session by adding or deleting objects and by attaching system operations or APL expressions to them.

Like any other object, `⎕SE` is a namespace that may contain functions and variables. Furthermore, `⎕SE` is independent of the active workspace and is unaffected by `)LOAD` and `)CLEAR`. It is therefore sensible to store commonly used utilities, particularly those utilities that are invoked by events on session objects, in `⎕SE` itself, rather than in each of your application workspaces.

The possibility of configuring your APL session so extensively leads to the requirement to have different sessions for different purposes. To meet this need, sessions are stored in special files with a .DSE (Dyalog Session) extension. The default session (that is, the one loaded when you start APL) is specified by the **session_file** parameter. You may customise this session and then save it over the default one or in a separate file. You can load a new session from file at any stage without affecting your active workspace.

## Positioning the Cursor

The cursor may be positioned within the current APL window by moving the mouse pointer to the desired location and then clicking the Left Button. The APL cursor will then move to the character under the pointer.

## Selection

Dragging the mouse selects the text from the point where the mouse button is depressed to the point where the button is released. When you select multiple lines, the use of the left mouse button always selects text from the start of the line. A contiguous block of text can be selected by dragging with the right mouse button.

Double-clicking the left mouse button to the left of a line selects the whole line, including the end-of-line character.

## Scrolling

Data can be scrolled in a window using the mouse in conjunction with the scrollbar.

## Invoking the Editor

The Editor can be invoked by placing the mouse pointer over the name of an editable object and double-clicking the left button on the mouse. If you double-click on the empty Input Line it acts as "Naked Edit" and opens an edit window for the suspended function (if any) on the APL stack. For further details, see [Invoking the Editor](editor.md). See also "Installation and Configuration Guide: DoubleClickEdit".

## The Current Object

If you position the input cursor over the name of an object in the session window, that object becomes the current object. This name is stored in the CurObj property of the Session object and may be used by an application or a utility program. This means that you can click the mouse over a name and then select a menu item or click a button that executes code that accesses the name.

## The Session Pop-up Menu

Clicking the right mouse button brings up the Session pop-up menu. This is described later in this chapter.

## Drag-and-Drop Editing

Drag-and-Drop editing is the easiest way to move or copy a selection a short distance within an edit window or between edit windows.

### To *move* text using drag-and-drop editing

1. Select the text you want to move.
2. Point to the selected text and then press and hold down the left mouse button. When the drag-and-drop pointer appears, drag the cursor to a new location.
3. Release the mouse button to drop the text into place.

### To *copy* text using drag-and-drop editing

1. Select the text you want to move.
2. Hold down the Ctrl key, point to the selected text and then press and hold down the left mouse button. When the drag-and-drop pointer appears, drag the cursor to a new location.
3. Release the mouse button to drop the text into place.

If you drag-and-drop text within the Session window, the text is copied and not moved whether or not you use the Ctrl key.

## Interrupts

To generate an interrupt, click on the Dyalog icon in the Windows System Tray; then choose *Weak Interrupt* or *Strong Interrupt*. To close the menu, click *Cancel*. Alternatively, to generate a weak interrupt, press Ctrl+Break, or select *Interrupt* from the *Action* menu on the Session Window.
