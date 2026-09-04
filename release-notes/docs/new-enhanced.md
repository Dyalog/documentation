# New Features, Changes, and Enhancements

This page describes the changes and new features in Dyalog v20.0 compared with Dyalog v19.0.

## Syntax Changes

### Array Notation

[Array notation](../../programming-reference-guide/introduction/arrays/array-notation/) is a literal syntax for most arrays (including nested and high-rank arrays) and namespaces. Array notation is an extension of APL syntax, and, as such, can be used inside and around all other APL expressions, and wherever an APL expression can appear (for example in the Session, in functions, and in namespace scripts). It can also be used in the Editor to manipulate arrays directly.

You can edit variables using array notation in the following ways:

- Invoke the _Edit_ command (**&lt;ED>**) from within the Editor.
- Call the system command `)ED` and prefix the variable name with a diamond character, for example, `)ED ⋄foo`
- Call the system function `⎕ED` with a left argument `'⋄'`, for example, `'⋄' ⎕ED 'foo'`.

In addition, in the Microsoft Windows IDE, array notation can be accessed in the following ways:

- Click the ![](img200/session-arraynotation.png){width=20 height=20 vertical-align:text-bottom} icon in the **Session** toolbar – this button toggles on/off the use of array notation for output (when possible).
- Click the ![](img200/object-arraynotation.png){width=20 height=20 vertical-align:text-bottom} icon in the **Object** toolbar when the cursor is over the name of an array – this opens the array in the Editor in the same way as `)ED ⋄foo`.
- Click the ![](img200/object-arraynotation.png){width=20 height=20 vertical-align:text-bottom} icon in the Editor's toolbar – this displays the contents of the Editor using array notation.
- Select **Show as Array Notation** from the Editor's **Syntax** menu – this displays the contents of the Editor using array notation.

When using array notation in the Editor, the _Reformat_ command (**&lt;RD>**) evaluates the Editor's content and regenerates it using array notation.

Setting the `APLAN_FOR_OUTPUT` configuration parameter to `1` sets use of array notation for output to be on; this is equivalent to setting `]APLAN.Output on` at start-up time. In the Microsoft Windows IDE, this can be overridden using the toolbar icons/menu items.

Setting the `APLAN_FOR_EDITOR` configuration parameter to `1` sets use of array notation for editors to be on; this is equivalent to setting `]APLAN.Editor on` at start-up time.

## Language Changes

### Primitive Functions/Operators

A new primitive operator, [_behind_](../../language-reference-guide/primitive-operators/behind/), has been added. This completes the set of [function composition](../../language-reference-guide/primitive-operators/operator-syntax/#function-composition) operators, which allow functions to be glued together to build up more complex functions:

- Glyph: `⍛` (Classic: `⎕U235B`)
- Derived function equivalence:
    - monadic: `(f Y) g Y`
	- dyadic: `(f X) g Y`

### System Functions

The following system functions have been added:

- [`⎕SHELL`](../../language-reference-guide/system-functions/shell/) – Execute External Program  
This enables execution of external programs with more control and options than [`⎕SH`](../../language-reference-guide/system-functions/start-unix-auxiliary-processor/)/[`⎕CMD`](../../language-reference-guide/system-functions/start-windows-auxiliary-processor/).
- [`⎕VGET`](../../language-reference-guide/system-functions/vget/) – Value Get  
This enables values to be read for names in a source namespace/namespaces.
- [`⎕VSET`](../../language-reference-guide/system-functions/vset/) – Value Set  
This enables values to be set for names in a target namespace/namespaces.

The following system functions have been enhanced:

- [`⎕DT`](../../language-reference-guide/system-functions/dt/) – Date-Time  
Additional conversion types have been added:
    - 15 – Go UnixMicro
	- 16 – Go UnixNano
	- 17 – APL+Win and APL64 workspace timestamp
	- 21 – Apollo NCS UUID
	- 22 – OSF DCE UUID
	- 70  – AmigaOS
- [`⎕FSTIE`](../../language-reference-guide/system-functions/fstie/) – File Share Tie  
A new variant option, **Mode**, has been added. This specifies the intended purpose of the tie, and can affect when/how errors are generated.
- [`⎕FTIE`](../../language-reference-guide/system-functions/ftie/) – Exclusive File Tie  
A new variant option, **Mode**, has been added. This specifies the intended purpose of the tie, and can affect when/how errors are generated.
- [`⎕FIX`](../../language-reference-guide/system-functions/fx/) and [`⎕FX`](../../language-reference-guide/system-functions/fx/) – Fix Script/Definition  
The rules around whether a function can be fixed have been tightened to prevent dfns with unmatched parentheses and brackets from being fixed. This is to accommodate array notation, which changes the meaning of parentheses and brackets that span more than one statement. TradFns will continue to fix as before, but subtle differences in how the code behaves might not be backwards-compatible and could have unexpected results.

    !!! Hint "Hints and Recommendations"
        If the enhanced restrictions on `⎕FIX` and `⎕FX` cause problems for you, please contact [support@dyalog.com](mailto:support@dyalog.com) to discuss tools and techniques for mitigation.

- [`⎕MKDIR`](../../language-reference-guide/system-functions/mkdir/) – Make Directory  
A new variant option, **Unique**, has been added. This specifies whether the base name in the right argument is modified so that the name is unique.
- [`⎕NGET`](../../language-reference-guide/system-functions/nget/) – Read Text File  
If `Y` is a 2-item vector, the second element (which specifies `flags` for the operation) can now be set to `2`. In this situation, the first element of the result `R` is a matrix, with each row corresponding to a line in the text file specified within `X`.
- [`⎕NINFO`](../../language-reference-guide/system-functions/ninfo/) – Native File Information  
    - Several of the properties can now be set by extending the appropriate element in the left argument from a `propertyNumber` to a `(propertyNumber newValue)` pair.
    - A new variant option, **ProgressCallBack**, has been added. This causes `⎕NINFO` to invoke an APL callback function as the file operations (for example, a query relating to a file's size, name, or modification date) proceed.
- [`⎕NPUT`](../../language-reference-guide/system-functions/nput/) – Write Text File  
The single/first element of `X` (which specifies `content`) can now be a matrix. In this situation, the resulting text file will include one line for each row of the matrix, with trailing spaces stripped.
- [`⎕NS`](../../language-reference-guide/system-functions/ns/) – Namespace  
    - The left argument `X` has been extended to allow references to namespaces to be specified. It can also now be an array in which each element identifies a namespace. 
	- The right argument `Y` has been extended to allow multiple references to namespaces to be specified.
	- A new variant option, **Trigger**, has been added. This specifies whether any triggers should run when `⎕NS` modifies names in the target namespace.

### I-beams

!!! Warning "Warning"  
    Any service provided using an I&#8209;Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I&#8209;Beams in applications should, therefore, be carefully isolated in cover-functions that can be adjusted if necessary.

The following I&#8209;beams have been added:

- [`13⌶`](../../language-reference-guide/primitive-operators/i-beam/log-use-of-deprecated-features/) – Log Use of Deprecated Features  
Records information in the log file set by `109⌶` about the specified deprecated feature names or keywords
- [`43⌶`](../../language-reference-guide/primitive-operators/i-beam/monadic-operator-generator/) – Monadic Operator Generator  
Generates a monadic operator with specified functionality. The exact functionaity of the generated operator depend on the right argument. Current options are:  
    - `43⌶632` – Generics Operator<br />Generates a .NET-specific operator that can create concrete versions of generic classes and execute generic methods<br />This is likely to be superseded by a new language construct in Dyalog v21.0.
- [`109⌶`](../../language-reference-guide/primitive-operators/i-beam/log-file-for-deprecations/) – Deprecated Feature Log File  
Manages the file used to log the use of deprecated features.
- [`120⌶`](../../language-reference-guide/primitive-operators/i-beam/generate-uuid/) – Generate UUID  
Generates a UUID (Universally Unique IDentifier) according to the RFC 9562 specification.
- [`3535⌶`](../../language-reference-guide/primitive-operators/i-beam/scan-for-deprecated-files/) – Scan For Deprecated Files  
Scans the specified directory (and, optionally, sub-directories) for deprecated saved workspaces, component files, and external variables.
- [`5581⌶`](../../language-reference-guide/primitive-operators/i-beam/unicode-normalisation/) – Unicode Normalisation  
Applies the specified Unicode normalisation form to given character data.
- [`8373⌶`](../../language-reference-guide/primitive-operators/i-beam/shell-process-control/) – Shell Process Control  
Provides a way to determine the process IDs of processes started by `⎕SHELL`, as well as enabling the sending of signals to any of those processes.

The following I-beams have been removed:

- `819⌶` – Case Convert (introduced in Dyalog v15.0)  
The functionality provided by this I-beam is available through the [`⎕C`](../../language-reference-guide/system-functions/c/) system function.
- `8468⌶` – Hash Table Size (introduced in Dyalog v19.0)  
Temporary functionality used for identification of potential side-effects of a change that has now been implemented. No longer relevant.
- `8469⌶` – Lookup Table Size (introduced in Dyalog v19.0)  
Temporary functionality used for identification of potential side-effects of a change that has now been implemented. No longer relevant.

## Development Environment Changes

### Inline Tracing

[Inline Tracing](../../windows-ui-guide/tracer/inline-tracing/) is an extension to tracing that allows you to step through the execution of individual primitives within expressions, examining intermediate results and arguments of sub-expressions. It enables an in-depth inspection of complex expressions.

Inline tracing can be initiated in the following ways:

- Invoke the _Inline Tracing_ command (**&lt;IT>**) from within the Session when the cursor is within the expression of interest.

In addition, in the Microsoft Windows IDE, inline tracing can be initiated in the following ways:

- Click the ![](img200/tracer-inlinetracing.png){width=20 height=20 vertical-align:text-bottom} icon in the **Tracer** toolbar
- Select **Trace Inline...** from the Session's **Action** menu.
- Select **Action** > **Trace Inline...** from the Session's context ("right-click") menu.

### Configuration Parameters

The following configuration parameters have been added:

- `APLAN_FOR_EDITOR`  
This initialises editors using array notation when possible (unless it is overridden within the session). The default is `0` (array notation is not in use). 
- `APLAN_FOR_OUTPUT`  
This displays session output using array notation when possible (unless it is overridden within the session). The default is `0` (array notation is not in use).
- `DYALOG_SHELL_SUBPROCESS`  
This improves the performance of `⎕SHELL` on AIX. When set to `1` (the default on AIX), the interpreter starts a (small) child process that handles calls to `⎕SHELL`, mitigating some of the performance issues seen on AIX when <code class="language-nonAPL">fork()</code>ing large processes.

### Command Shortcuts

The following command shortcuts have been extended:

- The _Reformat_ command (**&lt;RD>**) will now reformat and indent an array when array notation is switched on (previously this functionality was restricted to functions); it will also execute any expressions within the array notation and replace the text with a representation of their results.
- The _Undo All_ command (**&lt;UA>**) will now exit multi-line input (previously this only "unmarked" input lines within multi-line input).

### Home and End Keys

The actions of the <kbd>Home</kbd> and <kbd>End</kbd> keys have been enhanced to provide finer granularity.

When the cursor is placed in a line in the Session:

- <kbd>Home</kbd> moves the cursor left to whichever of these it encounters first from its starting position:
    - the start of the content of the line
    - the six space prompt (except when in the **Editor**, in which case this is skipped)
    - the left edge of the session
- <kbd>End</kbd> moves the cursor right to whichever of these it encounters first from its starting position:
	- the end of the content of the line excluding trailing space characters
    - the end of the content of the line including trailing space characters
    - the six space prompt (only when the cursor is on a blank line)

Pressing <kbd>Home</kbd> or <kbd>End</kbd> multiple times progresses through the list in the order shown.

### Microsoft Windows IDE

The following changes have been made to the Microsoft Windows IDE:

- A new menu, **Layout**, provides options for the location (or undocking) of the **Debugger** window.
- A new keyboard shortcut has been added to toggle inline tracing:
    - key code: **&lt;IT&gt;**
	- keystroke: <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Enter</kbd>
- A new icon (![](img200/object-arraynotation.png){width=20 height=20 vertical-align:text-bottom}) has been added to the **Object** toolbar. This enables array notation to be used when editing an object, and replaces the previous Array Editor icon.
- A new icon (![](img200/session-arraynotation.png){width=20 height=20 vertical-align:text-bottom}) has been added to the **Session** toolbar to toggle the use of array notation.
- The Session caption can now include the current thread by adding the `{TID}` field to the `⎕SE.Caption` property.
- In the **Configuration** dialog box's **Keyboard Shortcuts** tab, the **Available shortcuts** now include function keys (code F1-F48). These can be used in conjunction with `⎕PFKEY` to define keyboard shortcuts for function key actions.
- The left bracket that appears in the Session gutter when entering multi-line input now includes a close icon at the bottom (![](img200/multilineinput-gutter-cross.png){width=20 height=20 vertical-align:text-bottom}). Clicking this cancels the multi-line input.
+ The appearance/layout of several of the dialog boxes has been adjusted, but their options and functionality have not been changed.
	
### TTY Interface

The following changes have been made to the TTY interface:

- A new keyboard shortcut has been added to toggle inline tracing:
    - key code: **&lt;IT&gt;**
	- keystroke – terminal emulator under Linux GUIs: _&lt;undefined&gt;_
	- keystroke – PuTTY terminal emulator: <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Enter</kbd>
- The _Left Limit_ command (**&lt;LL>**) and _Right Limit_ command (**&lt;RL>**) have been enhanced to match the extended behaviour of the <kbd>Home</kbd> and <kbd>End</kbd> keys respectively (see [Home and End Keys](#home-and-end-keys)).

## Interfaces and Libraries

### PCRE Library

The Perl Compatible Regular Expressions (PCRE) library used by the interpreter has been upgraded from PCRE v8.45 to PCRE2 v10.45.

The new version of PCRE is not 100% compatible with the previous version. Although it is unlikely that typical uses will be affected, advanced users of `⎕S` or `⎕R` might want to consult the PCRE documentation and run tests.
	
### .NET Interface

In .NET, a _generic_ class is a class that has type parameters which must be given values to create a concrete version of the class. Similarly, a generic method has type parameters which must be specified before the method can be called. 

The introduction of [`43⌶632`](../../language-reference-guide/primitive-operators/i-beam/monadic-operator-generator/) means that the .NET interface now supports creating concrete versions of generic classes, instantiating them, and calling generic methods. For more information, see the [_.NET Interface Guide_](../../files/dotNET_Interface_Guide.pdf).

The .NET Framework interface does not support generic classes.
