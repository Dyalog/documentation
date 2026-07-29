# Introduction

Control Structures are blocks of code in which the execution of APL statements follows certain rules and conditions.  Control structures are implemented using a set of *control words* that all start with the colon symbol (:).  Control Words are case-insensitive.

There are a number of different types of control structures defined by the control words, `:If`, `:While`, `:Repeat`, `:For` (with the supplementary control words `:In` and `:InEach`), `:Select`, `:With`, `:Trap`, `:Hold` and `:Disposable`.  Each one of these control words may occur only at the beginning of an APL statement and indicates the start of a particular type of control structure.

Within a control structure, certain other control words are used as qualifiers.  These are `:Else`, :`ElseIf`, `:AndIf`, `:OrIf`, `:Until`, `:Case` and `:CaseList`.

A third set of control words is used to identify the end of a particular control structure.  These are `:EndIf`, `:EndWhile`, `:EndRepeat`, `:EndFor`, `:EndSelect`, `:EndWith`, `:EndTrap`, `:EndHold` and  `:EndDisposable`.  Although formally distinct, these control words may all be abbreviated to `:End`.

Finally, the `:GoTo`, `:Return`, `:Leave` and `:Continue` control words may be used to conditionally alter the flow of execution within a control structure.

Control words, including qualifiers such as `:Else` and :`ElseIf`, may occur only at the beginning of a line or expression in a diamond-separated statement. The only exceptions are `:In` and `:InEach` which must appear on the same line within a `:For` expression.

## Key to Notation

The following notation is used to describe Control Structures within this section:

<table>
    <col />
    <col />
    <tr>
        <td><code>aexp</code></td>
        <td>an expression returning an array,</td>
    </tr>
    <tr>
        <td><code>bexp</code></td>
        <td>an expression returning a single Boolean value (0 or 1),</td>
    </tr>
    <tr>
        <td><code>var</code></td>
        <td>loop variable used by <code>:For</code> control structure,</td>
    </tr>
    <tr>
        <td><code>code</code></td>
        <td>0 or more lines of APL code, including other (nested) control structures,</td>
    </tr>
    <tr>
        <td><code>andor</code></td>
        <td><i>either</i> one or more <code>:AndIf</code> statements, <i>or</i> one or more <code>:OrIf</code> statements. For further details, see below.<br /><pre>
|
.-----------------------.
|                       |
|<--------------.       |<--------------.
|               |       |               |
code            |       code            | 
|               |       |               |
|               |       |               |
:AndIf bexp-----'       :OrIf bexp------'
|                       |
|<----------------------'
|
</pre></td>
   </tr>
</table>

## Notes

## Code preceding `:OrIf` and `:AndIf`

Code that precedes a `:OrIf` control statement, e.g. code placed between a `:If` statement and a subsequent `:OrIf`, will be executed only if the outer condition is false. If instead the outer condition is true, there is no need to execute the `:OrIf`statement , so it and any preceding lines of code are skipped.

Code that precedes a `:AndIf` control statement, e.g. code placed between a `:If` statement and a subsequent `:AndIf`, will only be executed if the outer condition is true. If instead the outer condition is false, there is no need to execute the `:AndIf` statement , so it and any preceding lines of code are skipped.

The above behaviour may be  examined using the Tracer.

A potential use for code before a `:OrIf` or `:AndIf` is to prepare for the conditional test. This preparatory work will only be done if required. For example:
```apl
:If x   ⍝ if x is false, skip everything up to the :EndIf
    y←..⍝ set up stuff for the condition on the next line
    :AndIf y
      do stuff
:EndIf
```

!!! warning
    With the exception of a diamondised statement, a control statement that should **not** be followed by an expression will generate an error if an expression is supplied.

    A line in a function consisting of a control statement followed by a `⋄` and subsequent expression(s) is not **currently** disallowed but may exhibit unexpected behaviour. In particular, the line will not honour  `⎕STOP` and will not be metered by `⎕MONITOR`. This syntax is not recommended.
