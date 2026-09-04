# Introduction

System commands are **not** executable APL expressions. They provide services or information associated with the workspace and the **external environment**.

## Command Presentation

System commands may be entered from immediate execution mode or in response to the prompt `⎕`: within evaluated input.  All system commands begin with the symbol `)`, known as a right parenthesis.  All system commands may be entered in upper or lower case.

The output of a system command appears in the Session log interactively, or on the [stderr stream](../../../programming-reference-guide/introduction/output) when the interpreter is attached to operating-system streams.
