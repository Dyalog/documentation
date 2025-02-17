<h1 class="heading"><span class="name">The Tracer</span></h1>

The Tracer is a visual debugging aid that allows you to step through an application line by line. During a Trace you can track the path taken through your code, display variables in edit windows and watch them change, skip forwards and backwards in a function. You can cutback the stack to a calling function and use the Session and Editor to experiment with and correct your code. The Tracer may be invoked in several ways as discussed below.

## Tracing an expression

Firstly, you may explicitly trace an expression that executes one or more defined functions or operators by typing the expression then pressing <kbd>Ctrl</kbd>+<kbd>Enter</kbd> (**&lt;TC&gt;**) or by selecting Trace from the Action menu. This lets you step through the execution of an expression from the beginning.

In the same way as when you execute a statement by pressing <kbd>Enter</kbd>, the expression is (if necessary) copied down to the input line and then executed. However, if the expression includes a reference to an unlocked defined function or operator, execution halts at its first line and a Trace window containing the suspended function or operator is displayed on the screen. The cursor is positioned to the left of the first line which is highlighted.

## Naked Trace

The second way to invoke the Tracer is when you have a suspended function in the state indicator and you press <kbd>Ctrl</kbd>+<kbd>Enter</kbd> (**&lt;TC&gt;**) on the empty input line. This is termed *naked trace*. The same thing can be achieved by selecting *Trace* from the *Action* menu on the Session Window.

The effect of naked trace is to open the Tracer and to position the cursor on the currently suspended line. It is exactly as if you had traced to that point from the Input Line expression whose execution caused the suspension.

## Automatic Trace

The third way to invoke the Tracer is to have the system do it automatically for you whenever an error occurs. This is achieved by setting the Show trace stack on error option in the *Trace/Edit* tab of the *Configuration* dialog (**Trace_on_error** parameter). When an error occurs, the system will automatically deploy the Tracer. Note that this means that when an error occurs, the Trace window will then receive the input focus and not the Session window.

## Tracer Options

From Version 10.1 onwards, the Tracer is designed to be docked in the Session window.

In previous versions of Dyalog, the Tracer was implemented as a stack of separate windows (one per function on the calling stack) or as a single, but still separate, window.

There are three available layout modes (each of which can be adjusted and configured). They are available under the **Debugger Layout** menu:

- **Floating**
- **At the bottom**
- **On the left**

The layout is a matter of preference; the functionality is the same. The default behaviour is **Debugger at the bottom**. 

The **Floating** layout mode detaches the Tracer window, allowing it to be positioned according to preference. 

![](../img/tbt-classic.png)

The **At the bottom** layout mode:

![](../img/tbt-debugger-bottom.png)

The **To the left** layout mode:

![](../img/tbt-debugger-left.png)

In the latter two layout modes, the Tracer is docked into the main window.

In **Floating** mode,

- The trace window contains a combo box whose drop-down displays the contents of the SI stack. This box is not provided if there are multiple trace windows.
- The trace window is re-used when tracing into, or returning from, a called function. This means that there is never more than one trace window present.
- When the last function in a traced suspension exits, the trace window disappears.
- If you click the *Quit this function* button in the *Trace Tools* window, or press <kbd>Esc</kbd>, the current function is removed from the stack and the trace window reused to display the calling function if there is one.
- If you move or resize the trace window, Dyalog APL remembers its position, so that it reappears in the same position when next used.

## The Trace Window

The Tracer is implemented as a single dockable window that displays the function that is currently being executed. There are several subsidiary information panes which are also fully dockable. The first of these (*SIStack*) displays the current function calling stack; the second (*Threads*) displays a list of running threads.

 There are also two docked, but minimised panes, named **Left Argument** and **Right Argument**. They will open up automatically if you [trace primitives](trace-primitives.md).

In the default Session files, the Tracer is docked along the bottom edge of the Session window. When you invoke the Tracer, it springs up as illustrated below. In this example, the function being traced is `⎕SE.UCMD`, which is invoked by typing a user-command, in this case `]APLCart`.

![](../img/tracer-1.png)

In the default layout, the *SIstack* window is displayed alongside the main Tracer window, although this can be hidden or made to appear as a separate floating window, as required.

## Trace Tools

The Tracer may be controlled from the keyboard, or by using the *Trace Tools* which are arranged along the title bar of the Debugger window. Note that the button names are solely for reference purposes in the description that follows.

|Button|Name|Key Code|Keystroke|Description|
|---|---|---|---|---|
|<span class="toolbar-icon" style="background-position: -64px 0"></span>|Exec|**&lt;ER&gt;**|<kbd>Enter</kbd>|Execute expression|
|<span class="toolbar-icon" style="background-position: -80px 0"></span>|Trace|**&lt;TC&gt;**|<kbd>Ctrl</kbd>+<kbd>Enter</kbd>|Trace expression|
|<span class="toolbar-icon" style="background-position: -432px 0"></span>|Trace Primitive|**&lt;TP&gt;**|<kbd>Shift</kbd>+<kbd>Alt</kbd>+<kbd>Enter</kbd>|Trace Primitive|
|<span class="toolbar-icon" style="background-position: 0 0"></span>|Back|**&lt;BK&gt;**|<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Bksp</kbd>|Go back one line|
|<span class="toolbar-icon" style="background-position: -16px 0"></span>|Fwd|**&lt;FD&gt;**|<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Enter</kbd>|Skip current line|
|<span class="toolbar-icon" style="background-position: -96px 0"></span>|Continue|**&lt;BH&gt;**|&nbsp;|Stop on next line of calling function|
|<span class="toolbar-icon" style="background-position: -112px 0"></span>|Restart|**&lt;RM&gt;**|`→⎕LC`|Continue execution of this thread|
|<span class="toolbar-icon" style="background-position: -160px 0"></span>|Restart all|&nbsp;|&nbsp;|Continue execution of all threads|
|<span class="toolbar-icon" style="background-position: -48px 0"></span>|Edit|**&lt;ED&gt;**|<kbd>Shift</kbd>+<kbd>Enter</kbd>|Edit name|
|<span class="toolbar-icon" style="background-position: -32px 0"></span>|Exit|**&lt;EP&gt;**|<kbd>Esc</kbd>|Quit this function|
|<span class="toolbar-icon" style="background-position: -128px 0"></span>|Intr|&nbsp;|<kbd>Ctrl</kbd>+<kbd>Pause</kbd>|Interrupt|
|<span class="toolbar-icon" style="background-position: -144px 0"></span>|Reset|**&lt;CB&gt;**|&nbsp;|Clear trace/stop/monitor for this object|
|<span class="toolbar-icon" style="background-position: -224px 0"></span>|&nbsp;|**&lt;LN&gt;**|&nbsp;|Toggle line numbers|
|<span class="toolbar-icon" style="background-position: -256px 0"></span>|&nbsp;|&nbsp;|&nbsp;|Search for next match|
|<span class="toolbar-icon" style="background-position: -240px 0"></span>|&nbsp;|&nbsp;|&nbsp;|Search for previous match|
|<span class="toolbar-icon" style="background-position: -272px 0"></span>|&nbsp;|&nbsp;|&nbsp;|Search hidden text|
|<span class="toolbar-icon" style="background-position: -336px 0"></span>|&nbsp;|&nbsp;|&nbsp;|Match case|
|<span class="toolbar-icon" style="background-position: -352px 0"></span>|&nbsp;|&nbsp;|&nbsp;|Match whole word|
|<span class="toolbar-icon" style="background-position: -368px 0"></span>|&nbsp;|&nbsp;|&nbsp;|Use Regular Expressions|

Using the Trace Tools, you can **single-step** through the function or operator by clicking the *Exec* and/or *Trace* buttons. If you click *Exec* the current line of the function or operator is executed and the system halts at the next line. If you click *Trace*, the current line is executed but any defined functions or operators referenced on that line are themselves traced. After execution of the line the system again halts at the next one. Using the keyboard, the same effect can be achieved by pressing <kbd>Enter</kbd> or <kbd>Ctrl</kbd>+<kbd>Enter</kbd>.

The illustration below shows the state of execution having clicked *Exec*, *Trace*, *Exec* 19 times:

![](../img/tracer-2.png)

The next illustration shows the result of clicking *Trace* at this point. This caused the system to trace into `⎕SE.Dyalog.APLCart`, the function called from `⎕SE.UCMD[35]`.

Notice how each function call on the stack is represented by an item in the *SIstack* window.

![](../img/tracer-4.png)

At this stage, the state indicator is as follows:
```apl
      )SI
⎕SE.Dyalog.Utils.APLcart[1]*
⎕SE.input.c.APLcart.Run[47]
⍎
⎕SE.SALTUtils.CallUserCode[0]
⎕SE.UCMD[2]
```

See also the section on [tracing primitives](trace-primitives.md).

## Controlling Execution

The point of execution may be moved by clicking the *Back* and *Fwd* buttons in the *Trace Tools* window or, using the keyboard, by pressing <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Bksp</kbd> and <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Enter</kbd>. Notice however that these buttons do not themselves change the state indicator or the display in the *SIStack* window. This happens only when you restart execution from the new point.

You can cut back the stack by clicking the **&lt;EP&gt;** button in the *Trace Tools* window. This causes execution to be suspended at the start of the line which was previously traced. The same effect can be achieved using the keyboard by pressing Esc. It can also be done by selecting *Exit* from the *File* menu on the Trace Window or by selecting *Close* from its system menu.

The **&lt;RM&gt;** button removes the Trace window and resumes execution. The same is achieved by the expression `→⎕LC`.

The **&lt;BH&gt;** button continues execution until the current function has run to completion and control has returned to the calling function. It leaves the Trace window displayed and allows you to watch execution progress.

## Using the Session and the Editor

Whilst using the Tracer you can skip to the Session or to any Edit window and back again. While it is docked, you may resize the Tracer pane by dragging its title bar, and you may use the buttons provided to maximise, minimise and restore the Tracer pane within the Session window.

Unless you move it, the cursor is positioned to the left of the suspended line in the top Trace window.

Depending where the cursor is in the tracer window, pressing <kbd>Shift</kbd>+<kbd>Enter</kbd> (**&lt;ED&gt;**) or selecting *Edit* from the *File* menu may cause an edit window to open.  If the cursor is in the first column of the Trace window, or on whitespace, the Editor is opened on function or operator on top of the stack.  If the cursor in on a name, the Editor is opened on the name under the cursor (point-and-edit).  With the cursor in any other location, no action is undertaken.

When you finish editing, the window reverts to a trace window with the new definition of the function or operator displayed.

You may also open a new edit window from within the Tracer using point-and-edit.

You can copy text from a trace window to the session for editing and execution or for experimentation.

It is possible to skip from the Tracer to the Session and then re-invoke the Tracer on a different expression.

## Setting Breakpoints

Breakpoints are defined by `⎕STOP` and may be toggled on and off in an Edit or Trace window by clicking in the appropriate column. The example below illustrates a function with a `⎕STOP` breakpoint set on line `[5]`.

![](../img/tracer-5.png)

`⎕STOP` breakpoints set or cleared in an Edit window are not established until the function is fixed. `⎕STOP` breakpoints set or cleared in a Trace window are established immediately.

## Clearing All Break-Points

<span class="toolbar-icon" style="background-position: -144px 0"></span>

You can clear all breakpoints by pressing the above button in the Trace Tools window. This in fact resets `⎕STOP` for all functions in the workspace.


