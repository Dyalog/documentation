# Grid Comments

## Introduction

Grid comments are implemented in a manner that is consistent with the way comments are handled in Microsoft Excel.

If a comment is associated with a cell, a small red triangle is displayed in its top right corner. When the user rests the mouse pointer over a commented cell, the comment is displayed as a pop-up with an arrow pointing back to the cell to which it refers. The comment disappears when the mouse pointer is moved away. This is referred to as *tip* behaviour.

It is also possible to display and hide comments under program control. A comment window displayed under program control does not (normally) disappear automatically when the user moves the mouse, but instead must be hidden explicitly. It is therefore possible to have several comments visible.

## Implementation

Because comments are typically sparse, this facility is implemented by a small set of *methods* rather than as a property, and comments are stored internally in data structures that minimise storage space. The following methods and events are provided.

|Event/Method|Number|Description                                            |
|------------|------|-------------------------------------------------------|
|AddComment  |220   |Associates a comment with a cell                       |
|DelComment  |221   |Deletes the comment associated with a particular cell  |
|GetComment  |222   |Retrieves the comment associated with a given cell     |
|ShowComment |223   |Displays a comment either as a pop-up or on-top window |
|HideComment |224   |Hides a comment                                        |
|ClickComment|225   |Reported when user clicks the mouse on a comment window|

A comment is described by its text content and the size of the window in which it appears. The text may optionally be *Rich Text* (RTF) such as that produced by the value of the RTFText property of a RichEdit object. The size of the window is specified in pixels.

## AddComment Method

This method is used to add a new comment. For example, the following statement associates a comment with the cell at row 2, column 1; the text of the comment is "Hello", and the size of the comment window is 50 pixels (high) by 60 pixels (wide).
```apl
      2 ⎕NQ'F.G' 'AddComment' 2 1 'Hello' 50 60
```

The height and width of the comment window, specified by the last 2 elements of the right argument to `⎕NQ` are both optional. If the cell already has an associated comment, the new comment replaces it.

Note that just before the comment is displayed, the Grid generates a ShowComment event which gives you the opportunity to (temporarily) change the text and/or window size of a comment dynamically.

## DelComment Method

This method is used to delete a comment. For example, the following expression removes the comment associated with the cell at row 2, column 1.
```apl
      2 ⎕NQ'F.G' 'DelComment' 2 1
```

If the row and column number are omitted, all comments are deleted.

## GetComment Method

This method is used to retrieve the comment associated with a cell. For example, the following expression retrieves the comment associated with the cell at row 3, column 1.
```apl
      ⎕←2 ⎕NQ 'F.G' 'GetComment' 3 1
 1 3  Hello  175 100
```

If there is no comment associated with the specified cell, the result is a scalar 1.

## ShowComment Event/Method

If enabled, a Grid will generate a ShowComment event when the user rests the mouse pointer over a commented cell. You may use this event to modify the appearance of the comment dynamically.

You may display the comment associated with a particular cell under program control by generating a ShowComment event using `⎕NQ`. By default, a comment displayed under program control does not exhibit tip behaviour but remains visible until it is explicitly removed using the HideComment method.

Note that a comment will only be displayed if the specified cell is marked as a commented cell.

## HideComment Event/Method

If enabled, a HideComment event is generated just before a comment window is hidden as a result of the user moving the mouse-pointer away from a commented cell.

Invoked as a method, HideComment is used to hide a comment that has previously been displayed by ShowComment. For example, the following expression hides the comment associated with the cell at row 2, column 1.
```apl
      2 ⎕NQ'F.G' 'HideComment' 2 1
```

## ClickComment Event

If enabled, a ClickComment event is generated when the user clicks the mouse in a comment widow. The event message reports the co-ordinates of the cell. The result of a callback function (if any) is ignored.
