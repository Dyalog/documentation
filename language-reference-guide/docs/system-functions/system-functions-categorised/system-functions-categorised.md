<h1 class="heading"><span class="name">System Functions Categorised</span></h1>

The following tables list the system functions divided into appropriate categories.

## Settings Affecting Behaviour of Primitive Functions

|Name  |Description                  |
|------|-----------------------------|
|`⎕CT` |Comparison Tolerance         |
|`⎕DCT`|Decimal Comp Tolerance       |
|`⎕DIV`|Division Method              |
|`⎕FR` |Floating-Point Representation|
|`⎕IO` |Index Origin                 |
|`⎕ML` |Migration Level              |
|`⎕PP` |Print Precision              |
|`⎕RL` |Random Link                  |

The following table describes the dependencies that exist between functions, operators and these system variables.

Table: Implicit Arguments {: #Implicit_Arguments }

|System Variable|Monadic Functions|Dyadic Functions|Operators|
|---|---|---|---|
|`⎕CT, ⎕DCT`|`⌈ ⌊ ∪`|`~ < ≤ = ≥ > ≠ ≡ ≢ ⍳ ∊ ∪ ∩ ⍷ | ∨ ∧`|`⌸`|
|`⎕DIV`|`÷`|`÷`|&nbsp;|
|`⎕FR   ⍝ 1`|`÷ * ⍟ ! ○ ⌹`|`+ - × ÷ * ⍟ | ! ○ ∨ ∧ ⊥ ⊤ ⌹`|&nbsp;|
|`⎕FR   ⍝ 2`|`⌈ ⌊ ∪`|`~ < ≤ = ≥ > ≠ ≡ ≢ ⍳ ∊ ∪ ∩ ⍷`|`⌸`|
|`⎕FR   ⍝ 3`|`⍒ ⍋`|`⌈ ⌊ ⍒ ⍋ ⍸`|&nbsp;|
|`⎕IO`|`⍳ ? ⍒ ⍋ ⍸`|`⍳ ? ⍒ ⍋ ⍉ ⊃ ⌷ ⍸`|`⌸ @ []`|
|`⎕ML`|`∊ ↑ ⊃ ≡`|&nbsp;|&nbsp;|
|`⎕PP`|`⍕`|&nbsp;|&nbsp;|
|`⎕RL`|`?`|`?`|&nbsp;|

where, for `⎕FR`, `1` indicates functions that compute real numbers and whose precision depends on `⎕FR`, `2` indicates functions that perform tolerant comparisons and `3` indicates functions that perform tolerant comparisons.

NOTE: Tolerant comparisons depend on `⎕FR` to select which of `⎕CT` and `⎕DCT` is used; `⎕FR` also determines the precision of the comparison computation that can affect results. However, even primitives involving intolerant comparison (including the tolerant ones with all comparison tolerances set to 0) can depend on `⎕FR` if the argument contains DECFs. This is because DECFs must be converted to doubles for comparison. If two DECFs are different but correspond to the same double, then they will be treated as intolerantly unequal when `⎕FR` is `1287` but equal when it is `645`.

## Session Information/Management

|Name    |Description                |
|--------|---------------------------|
|`⎕AI`   |Account Information        |
|`⎕AN`   |Account Name               |
|`⎕CLEAR`|Clear workspace (WS)       |
|`⎕CY`   |Copy objects into active WS|
|`⎕DL`   |Delay execution            |
|`⎕LOAD` |Load a saved WS            |
|`⎕OFF`  |End the session            |
|`⎕PATH` |Search Path                |
|`⎕SAVE` |Save the active WS         |
|`⎕TS`   |Timestamp                  |

## Constants

|Name   |Description                     |
|-------|--------------------------------|
|`⎕A`   |Alphabetic upper case characters|
|`⎕D`   |Digits                          |
|`⎕NULL`|Null Item                       |

## Tools and Access to External Utilities

|Name    |Description                                             |
|--------|--------------------------------------------------------|
|`⎕C`    |Case Convert                                            |
|`⎕CMD`  |Execute the Windows Command Processor or another program|
|`⎕CMD`  |Start a Windows AP                                      |
|`⎕CSV`  |Comma Separated Values                                  |
|`⎕DR`   |Data Representation (Monadic)                           |
|`⎕DR`   |Data Representation (Dyadic)                            |
|`⎕DT`   |Datetime                                                |
|`⎕FMT`  |Resolve display                                         |
|`⎕FMT`  |Format array                                            |
|`⎕JSON` |JSON Convert                                            |
|`⎕MAP`  |Map a file                                              |
|`⎕NA`   |Declare a DLL function                                  |
|`⎕R`    |Replace                                                 |
|`⎕S`    |Search                                                  |
|`⎕SH`   |Execute a UNIX command or another program               |
|`⎕SH`   |Start a UNIX AP                                         |
|`⎕UCS`  |Unicode Convert                                         |
|`⎕USING`|Microsoft .NET Search Path                              |
|`⎕VFI`  |Verify and Fix numeric                                  |
|`⎕XML`  |XML Convert                                             |

## Manipulating Functions and Operators

|Name      |Description             |
|----------|------------------------|
|`⎕AT`     |Object Attributes       |
|`⎕CR`     |Canonical Representation|
|`⎕ED`     |Edit one or more objects|
|`⎕EX`     |Expunge objects         |
|`⎕FX`     |Fix definition          |
|`⎕LOCK`   |Lock a function         |
|`⎕MONITOR`|Monitor set             |
|`⎕MONITOR`|Monitor query           |
|`⎕OR`     |Object Representation   |
|`⎕NR`     |Nested Representation   |
|`⎕PROFILE`|Profile Application     |
|`⎕REFS`   |Local References        |
|`⎕STOP`   |Set Stop vector         |
|`⎕STOP`   |Query Stop vector       |
|`⎕TRACE`  |Set Trace vector        |
|`⎕TRACE`  |Query Trace vector      |
|`⎕VR`     |Vector Representation   |

## Namespaces and Objects

|Name        |Description   |
|------------|--------------|
|`⎕BASE`     |Base Class    |
|`⎕CLASS`    |Class         |
|`⎕CS`       |Change Space  |
|`⎕DF`       |Display Format|
|`⎕FIX`      |Fix           |
|`⎕INSTANCES`|Instances     |
|`⎕NEW`      |New Instance  |
|`⎕NS`       |Namespace     |
|`⎕SRC`      |Source        |
|`⎕THIS`     |This          |

## Input/Output

|Name     |Description           |
|---------|----------------------|
|`⎕`      |Evaluated Input/Output|
|`⍞`      |Character Input/Output|
|`⎕ARBIN` |Arbitrary Input       |
|`⎕ARBOUT`|Arbitrary Output      |
|`⎕RTL`   |Response Time Limit   |

## Component Files

|Name       |Description                |
|-----------|---------------------------|
|`⎕FAPPEND` |Append a component to File |
|`⎕FAVAIL`  |File system Availability   |
|`⎕FCHK`    |File Check and Repair      |
|`⎕FCOPY`   |Copy a File                |
|`⎕FCREATE` |Create a File              |
|`⎕FDROP`   |Drop a block of components |
|`⎕FERASE`  |Erase a File               |
|`⎕FHIST`   |File History               |
|`⎕FHOLD`   |File Hold                  |
|`⎕FLIB`    |List File Library          |
|`⎕FNAMES`  |Names of tied Files        |
|`⎕FNUMS`   |Tie Numbers of tied Files  |
|`⎕FPROPS`  |File Properties            |
|`⎕FRDAC`   |Read File Access matrix    |
|`⎕FRDCI`   |Read Component Information |
|`⎕FREAD`   |Read a component from File |
|`⎕FRENAME` |Rename a File              |
|`⎕FREPLACE`|Replace a component on File|
|`⎕FRESIZE` |File Resize                |
|`⎕FSIZE`   |File Size                  |
|`⎕FSTAC`   |Set File Access matrix     |
|`⎕FSTIE`   |Share-Tie a File           |
|`⎕FTIE`    |Tie a File exclusively     |
|`⎕FUNTIE`  |Untie Files                |

## Native Files

|Name       |Description                                                        |
|-----------|-------------------------------------------------------------------|
|`⎕MKDIR`   |Create a directory                                                 |
|`⎕NAPPEND` |Append to File                                                     |
|`⎕NCOPY`   |Copy files and directories                                         |
|`⎕NCREATE` |Create a File                                                      |
|`⎕NDELETE` |Delete a File or Directory                                         |
|`⎕NERASE`  |Erase a File                                                       |
|`⎕NEXISTS` |Discover whether or not a file or directory exists                 |
|`⎕NGET`    |Read Text File                                                     |
|`⎕NINFO`   |Query or set information about one or more files and/or directories|
|`⎕NLOCK`   |Lock a region of a file                                            |
|`⎕NMOVE`   |Move files and directories                                         |
|`⎕NNAMES`  |Names of tied Files                                                |
|`⎕NNUMS`   |Tie Numbers of tied Files                                          |
|`⎕NPARTS`  |Split a file name into its constituent parts.                      |
|`⎕NPUT`    |Write Text File                                                    |
|`⎕NREAD`   |Read from File                                                     |
|`⎕NRENAME` |Rename a File                                                      |
|`⎕NREPLACE`|Replace data on File                                               |
|`⎕NRESIZE` |File Resize                                                        |
|`⎕NSIZE`   |File Size                                                          |
|`⎕NTIE`    |Tie a File exclusively                                             |
|`⎕NUNTIE`  |Untie Files                                                        |
|`⎕NXLATE`  |Specify Translation Table                                          |

## Threads

|Name     |Description                  |
|---------|-----------------------------|
|`⎕TALLOC`|Allocate Token Range         |
|`⎕TCNUMS`|Thread Child Numbers         |
|`⎕TID`   |Current Thread Identity      |
|`⎕TKILL` |Kill Threads                 |
|`⎕TNAME` |Current Thread Name          |
|`⎕TNUMS` |Thread Numbers               |
|`⎕TSYNC` |Wait for Threads to Terminate|

## Synchronisation

|Name     |Description         |
|---------|--------------------|
|`⎕TALLOC`|Allocate Token Range|
|`⎕TGET`  |Get Tokens          |
|`⎕TKILL` |Kill Threads        |
|`⎕TPOOL` |Token Pool          |
|`⎕TPUT`  |Put Tokens          |
|`⎕TREQ`  |Token Requests      |

## Error Handling

|Name        |Description                                     |
|------------|------------------------------------------------|
|`⎕DM`       |Diagnostic Message                              |
|`⎕DMX`      |Extended Diagnostic Message                     |
|`⎕EM`       |Event Messages                                  |
|`⎕EN`       |Event Number                                    |
|`⎕EXCEPTION`|Reports the most recent Microsoft .NET Exception|
|`⎕SIGNAL`   |Signal event                                    |
|`⎕TRAP`     |Event Trap                                      |

## Stack and Workspace Information

|Name     |Description              |
|---------|-------------------------|
|`⎕LC`    |Line Count               |
|`⎕LX`    |Latent Expression        |
|`⎕NC`    |Name Classification      |
|`⎕NL`    |Name List                |
|`⎕NSI`   |Namespace Indicator      |
|`⎕RSI`   |Space Indicator          |
|`⎕SI`    |State Indicator          |
|`⎕SHADOW`|Shadow names             |
|`⎕SIZE`  |Size of objects          |
|`⎕STACK` |Report Stack             |
|`⎕STATE` |Return State of an object|
|`⎕WA`    |Workspace Available      |
|`⎕WSID`  |Workspace Identification |
|`⎕XSI`   |Extended State Indicator |

## Shared Variables

|Name  |Description                |
|------|---------------------------|
|`⎕SVC`|Set access Control         |
|`⎕SVC`|Query access Control       |
|`⎕SVO`|Shared Variable Offer      |
|`⎕SVO`|Query degree of coupling   |
|`⎕SVQ`|Shared Variable Query      |
|`⎕SVR`|Retract offer              |
|`⎕SVS`|Query Shared Variable State|

## GUI and COM Support

|Name     |Description                |
|---------|---------------------------|
|`⎕DQ`    |Await and process events   |
|`⎕EXPORT`|Export objects             |
|`⎕NQ`    |Place an event on the Queue|
|`⎕WC`    |Create GUI object          |
|`⎕WG`    |Get GUI object properties  |
|`⎕WN`    |Query GUI object Names     |
|`⎕WS`    |Set GUI object properties  |
|`⎕WX`    |Expose GUI property names  |

## Miscellaneous

|Name    |Description                      |
|--------|---------------------------------|
|`⎕Á`    |Underscored Alphabetic Characters|
|`⎕AV`   |Atomic Vector                    |
|`⎕AVU`  |Atomic Vector - Unicode          |
|`⎕KL`   |Key Labels                       |
|`⎕PFKEY`|Programmable Function Keys       |
|`⎕SD`   |Screen Dimensions                |
|`⎕SM`   |Screen Map                       |
|`⎕SR`   |Screen Read                      |
|`⎕OPT`  |Variant Operator                 |
|`⎕TC`   |Terminal Control                 |
|`⎕XT`   |Associate External variable      |
|`⎕XT`   |Query External variable          |
