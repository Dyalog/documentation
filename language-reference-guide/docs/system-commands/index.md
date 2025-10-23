<h1 class="heading"><span class="name">Introduction</span></h1>

System commands are **not** executable APL expressions. They provide services or information associated with the workspace and the **external environment**.

## Command Presentation

System commands may be entered from immediate execution mode or in response to the prompt `⎕`: within evaluated input.  All system commands begin with the symbol `)`, known as a right parenthesis.  All system commands may be entered in upper or lower case.

Table: System Commands {: #SystemCommands }

|Command                                                           |Description                                |
|---------------------------------------------------------------|-------------------------------------------|
|[`)CLASSES`](classes.md)                                 |List classes                               |
|[`)CLEAR`](clear.md)                                                          |Clear the workspace                        |
|[`)CMD Y`](cmd.md)                                                          |Execute a Windows Command                  |
|[`)CONTINUE`](continue.md)                                                       |Save a Continue workspace and terminate APL|
|[`)COPY {Y}`](copy.md)                                                       |Copy objects from another workspace        |
|[`)CS {Y}`](cs.md)                                                         |Change current namespace                   |
|[`)DROP {Y}`](drop.md)                                                       |Drop named workspace                       |
|[`)ED Y`](ed.md)                                                           |Edit object(s)                             |
|[`)ERASE Y`](erase.md)                                                        |Erase object(s)                            |
|[`)EVENTS`](events.md)                                                         |List events of GUI namespace or object     |
|[`)FNS {Y}`](fns.md)                                                        |List user defined Functions                |
|[`)HOLDS`](holds.md)                                                          |Display Held tokens                        |
|[`)LIB {Y}`](lib.md)                                                        |List workspaces in a directory             |
|[`)LOAD {Y}`](load.md)                                                       |Load a workspace                           |
|[`)METHODS`](methods.md)                                                        |List methods in GUI namespace or object    |
|[`)NS {Y}`](ns.md)                                                         |Create a global Namespace                  |
|[`)OBJECTS {Y}`](objects.md)                                                    |List global namespaces                     |
|[`)OBS {Y}`](obs.md)                                                        |List global namespaces (alternative form)  |
|[`)OFF`](off.md)                                                            |Terminate the APL session                  |
|[`)OPS {Y}`](ops.md)                                                        |List user defined Operators                |
|[`)PCOPY {Y}`](pcopy.md)                                                      |Perform Protected Copy of objects          |
|[`)PROPS`](props.md)                                                          |List properties of GUI namespace or object |
|[`)RESET`](reset.md)                                                          |Reset the state indicator                  |
|[`)SAVE {Y}`](save.md)                                                       |Save the workspace                         |
|[`)SH {Y}`](sh.md)                                                         |Execute a (UNIX) Shell command             |
|[`)SI`](si.md)                                                             |State Indicator                            |
|[`)SIC`](sic.md)                                                            |Clear State Indicator                      |
|[`)SINL`](sinl.md)                                                           |State Indicator with local Name Lists      |
|[`)TID {Y}`](tid.md)                                                        |Switch current Thread Identity             |
|[`)VARS {Y}`](vars.md)                                                       |List user defined global Variables         |
|[`)WSID {Y}`](wsid.md)                                                       |Workspace Identification                   |
|[`)XLOAD Y`](xload.md)                                                        |Load a workspace; do not execute `⎕LX`     |
|`{ }` indicates that the parameter(s) denoted by `Y` are optional.                                           ||


