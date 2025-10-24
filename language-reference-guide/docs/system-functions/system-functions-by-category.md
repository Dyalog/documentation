<h1 class="heading"><span class="name">System Functions (by Category)</span></h1>

The following tables list the system functions divided into appropriate categories.

## Settings Affecting Behaviour of Primitive Functions

|Name  |Description                              |
|------|-----------------------------------------|
|[`⎕CT`](ct.md) |Comparison Tolerance         |
|[`⎕DCT`](dct.md)|Decimal Comp Tolerance      |
|[`⎕DIV`](div.md)|Division Method             |
|[`⎕FR`](fr.md) |Floating-Point Representation|
|[`⎕IO`](io.md) |Index Origin                 |
|[`⎕ML`](ml.md) |Migration Level              |
|[`⎕PP`](pp.md) |Print Precision              |
|[`⎕RL`](rl.md) |Random Link                  |

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

!!! note
    Tolerant comparisons depend on `⎕FR` to select which of `⎕CT` and `⎕DCT` is used; `⎕FR` also determines the precision of the comparison computation that can affect results. However, even primitives involving intolerant comparison (including the tolerant ones with all comparison tolerances set to 0) can depend on `⎕FR` if the argument contains DECFs. This is because DECFs must be converted to doubles for comparison. If two DECFs are different but correspond to the same double, then they will be treated as intolerantly unequal when `⎕FR` is `1287` but equal when it is `645`.

## Session Information/Management

|Name                   |Description                |
|-----------------------|---------------------------|
|[`⎕AI`](ai.md)      |Account Information        |
|[`⎕AN`](an.md)      |Account Name               |
|[`⎕CLEAR`](clear.md)|Clear workspace (WS)       |
|[`⎕CY`](cy.md)      |Copy objects into active WS|
|[`⎕DL`](dl.md)      |Delay execution            |
|[`⎕LOAD`](load.md)  |Load a saved WS            |
|[`⎕OFF`](off.md)    |End the session            |
|[`⎕PATH`](path.md)  |Search Path                |
|[`⎕SAVE`](save.md)  |Save the active WS         |
|[`⎕TS`](ts.md)      |Timestamp                  |


## System Constants

|Name   |Description                     |
|-------|--------------------------------|
|[`⎕A`](a.md)   |Alphabetic upper case characters|
|[`⎕D`](d.md)   |Digits                          |
|[`⎕NULL`](null.md)|Null Item                       |

## Tools and Access to External Utilities

|Name    |Description                                             |
|--------|--------------------------------------------------------|
|[`⎕C`](c.md)    |Case Convert                                            |
|[`⎕CMD`](execute-windows-command.md)  |Execute the Windows Command Processor or another program|
|[`⎕CMD`](start-windows-auxiliary-processor.md)  |Start a Windows AP        |
|[`⎕CSV`](csv.md)  |Comma Separated Values                                  |
|[`⎕DR`](data-representation-monadic.md)   |Data Representation (Monadic)                           |
|[`⎕DR`](data-representation-dyadic.md)   |Data Representation (Dyadic)                            |
|[`⎕DT`](dt.md)   |Datetime                                                |
|[`⎕FMT`](format-monadic.md)  |Resolve display                                         |
|[`⎕FMT`](format-dyadic.md)  |Format array                                            |
|[`⎕JSON`](json.md) |JSON Convert                                            |
|[`⎕MAP`](map.md)  |Map a file                                              |
|[`⎕NA`](na.md)   |Declare a DLL function                                  |
|[`⎕R`](r.md)    |Replace                                                 |
|[`⎕S`](s.md)    |Search                                                  |
|[`⎕SH`](execute-unix-command.md)   |Execute a UNIX command or another program               |
|[`⎕SH`](start-unix-auxiliary-processor.md)   |Start a UNIX AP                                         |
|[`⎕SHELL`](shell.md)|Execute a shell command or another program              |
|[`⎕UCS`](ucs.md)  |Unicode Convert                                         |
|[`⎕USING`](using.md)|Microsoft .NET Search Path                              |
|[`⎕VFI`](vfi.md)  |Verify and Fix numeric                                  |
|[`⎕XML`](xml.md)  |XML Convert                                             |

## Manipulating Functions and Operators

|Name      |Description             |
|----------|------------------------|
|[`⎕AT`](at.md)     |Object Attributes       |
|[`⎕CR`](cr.md)     |Canonical Representation|
|[`⎕ED`](ed.md)     |Edit one or more objects|
|[`⎕EX`](ex.md)     |Expunge objects         |
|[`⎕FX`](fx.md)     |Fix definition          |
|[`⎕LOCK`](lock.md)   |Lock a function         |
|[`⎕MONITOR`](set-monitor.md)|Monitor set             |
|[`⎕MONITOR`](query-monitor.md)|Monitor query           |
|[`⎕OR`](or.md)     |Object Representation   |
|[`⎕NR`](nr.md)     |Nested Representation   |
|[`⎕PROFILE`](profile.md)|Profile Application     |
|[`⎕REFS`](refs.md)   |Local References        |
|[`⎕STOP`](set-stop.md)   |Set Stop vector         |
|[`⎕STOP`](query-stop.md)   |Query Stop vector       |
|[`⎕TRACE`](set-trace.md)  |Set Trace vector        |
|[`⎕TRACE`](query-trace.md)  |Query Trace vector      |
|[`⎕VR`](vr.md)     |Vector Representation   |

## Namespaces and Objects

|Name        |Description   |
|------------|--------------|
|[`⎕BASE`](base.md)     |Base Class    |
|[`⎕CLASS`](class.md)    |Class         |
|[`⎕CS`](cs.md)       |Change Space  |
|[`⎕DF`](df.md)       |Display Format|
|[`⎕FIX`](fix.md)      |Fix           |
|[`⎕INSTANCES`](instances.md)|Instances     |
|[`⎕NEW`](new.md)      |New Instance  |
|[`⎕NS`](ns.md)       |Namespace     |
|[`⎕SRC`](src.md)      |Source        |
|[`⎕THIS`](this.md)     |This          |

## Input and Output

|Name     |Description           |
|---------|----------------------|
|[`⎕`](evaluated-input-output.md)      |Evaluated Input/Output|
|[`⍞`](character-input-output.md)      |Character Input/Output|
|[`⎕ARBIN`](arbin.md) |Arbitrary Input       |
|[`⎕ARBOUT`](arbout.md)|Arbitrary Output      |
|[`⎕RTL`](rtl.md)   |Response Time Limit   |

## Component Files

|Name       |Description                |
|-----------|---------------------------|
|[`⎕FAPPEND`](fappend.md) |Append a component to File |
|[`⎕FAVAIL`](favail.md)  |File system Availability   |
|[`⎕FCHK`](fchk.md)    |File Check and Repair      |
|[`⎕FCOPY`](fcopy.md)   |Copy a File                |
|[`⎕FCREATE`](fcreate.md) |Create a File              |
|[`⎕FDROP`](fdrop.md)   |Drop a block of components |
|[`⎕FERASE`](ferase.md)  |Erase a File               |
|[`⎕FHIST`](fhist.md)   |File History               |
|[`⎕FHOLD`](fhold.md)   |File Hold                  |
|[`⎕FLIB`](flib.md)    |List File Library          |
|[`⎕FNAMES`](fnames.md)  |Names of tied Files        |
|[`⎕FNUMS`](fnums.md)   |Tie Numbers of tied Files  |
|[`⎕FPROPS`](fprops.md)  |File Properties            |
|[`⎕FRDAC`](frdac.md)   |Read File Access matrix    |
|[`⎕FRDCI`](frdci.md)   |Read Component Information |
|[`⎕FREAD`](fread.md)   |Read a component from File |
|[`⎕FRENAME`](frename.md) |Rename a File              |
|[`⎕FREPLACE`](freplace.md)|Replace a component on File|
|[`⎕FRESIZE`](fresize.md) |File Resize                |
|[`⎕FSIZE`](fsize.md)   |File Size                  |
|[`⎕FSTAC`](fstac.md)   |Set File Access matrix     |
|[`⎕FSTIE`](fstie.md)   |Share-Tie a File           |
|[`⎕FTIE`](ftie.md)    |Tie a File exclusively     |
|[`⎕FUNTIE`](funtie.md)  |Untie Files                |

## Native Files

|Name       |Description                                                  |
|-----------|-------------------------------------------------------------|
|[`⎕MKDIR`](mkdir.md)   |Create a directory                                           |
|[`⎕NAPPEND`](nappend.md) |Append to File                                               |
|[`⎕NCOPY`](ncopy.md)   |Copy files and directories                                   |
|[`⎕NCREATE`](ncreate.md) |Create a File                                                |
|[`⎕NDELETE`](ndelete.md) |Delete a File or Directory                                   |
|[`⎕NERASE`](nerase.md)  |Erase a File                                                 |
|[`⎕NEXISTS`](nexists.md) |Discover whether or not a file or directory exists           |
|[`⎕NGET`](nget.md)    |Read Text File                                               |
|[`⎕NINFO`](ninfo.md)   |Query or set information about one or more files and/or directories|
|[`⎕NLOCK`](nlock.md)   |Lock a region of a file                                      |
|[`⎕NMOVE`](nmove.md)   |Move files and directories                                   |
|[`⎕NNAMES`](nnames.md)  |Names of tied Files                                          |
|[`⎕NNUMS`](nnums.md)   |Tie Numbers of tied Files                                    |
|[`⎕NPARTS`](nparts.md)  |Split a file name into its constituent parts.                |
|[`⎕NPUT`](nput.md)    |Write Text File                                              |
|[`⎕NREAD`](nread.md)   |Read from File                                               |
|[`⎕NRENAME`](nrename.md) |Rename a File                                                |
|[`⎕NREPLACE`](nreplace.md)|Replace data on File                                         |
|[`⎕NRESIZE`](nresize.md) |File Resize                                                  |
|[`⎕NSIZE`](nsize.md)   |File Size                                                    |
|[`⎕NTIE`](ntie.md)    |Tie a File exclusively                                       |
|[`⎕NUNTIE`](nuntie.md)  |Untie Files                                                  |
|[`⎕NXLATE`](nxlate.md)  |Specify Translation Table                                    |

## Threads

|Name     |Description                  |
|---------|-----------------------------|
|[`⎕TALLOC`](talloc.md) |Allocate Token Range         |
|[`⎕TCNUMS`](tcnums.md) |Thread Child Numbers         |
|[`⎕TID`](tid.md)   |Current Thread Identity      |
|[`⎕TKILL`](tkill.md) |Kill Threads                 |
|[`⎕TNAME`](tname.md) |Current Thread Name          |
|[`⎕TNUMS`](tnums.md) |Thread Numbers               |
|[`⎕TSYNC`](tsync.md) |Wait for Threads to Terminate|

## Synchronisation

|Name     |Description         |
|---------|--------------------|
|[`⎕TALLOC`](talloc.md)|Allocate Token Range|
|[`⎕TGET`](tget.md)  |Get Tokens          |
|[`⎕TKILL`](tkill.md) |Kill Threads        |
|[`⎕TPOOL`](tpool.md) |Token Pool          |
|[`⎕TPUT`](tput.md)  |Put Tokens          |
|[`⎕TREQ`](treq.md)  |Token Requests      |

## Error Handling

|Name        |Description                                     |
|------------|------------------------------------------------|
|[`⎕DM`](dm.md)       |Diagnostic Message                              |
|[`⎕DMX`](dmx.md)      |Extended Diagnostic Message                     |
|[`⎕EM`](em.md)       |Event Messages                                  |
|[`⎕EN`](en.md)       |Event Number                                    |
|[`⎕EXCEPTION`](exception.md)|Reports the most recent Microsoft .NET Exception|
|[`⎕SIGNAL`](signal.md)   |Signal event                                    |
|[`⎕TRAP`](trap.md)     |Event Trap                                      |

## Stack and Workspace Information

|Name     |Description              |
|---------|-------------------------|
|[`⎕LC`](lc.md)    |Line Count               |
|[`⎕LX`](lx.md)    |Latent Expression        |
|[`⎕NC`](nc.md)    |Name Classification      |
|[`⎕NL`](nl.md)    |Name List                |
|[`⎕NSI`](nsi.md)   |Namespace Indicator      |
|[`⎕RSI`](rsi.md)   |Space Indicator          |
|[`⎕SI`](si.md)    |State Indicator          |
|[`⎕SHADOW`](shadow.md)|Shadow names             |
|[`⎕SIZE`](size.md)  |Size of objects          |
|[`⎕STACK`](stack.md) |Report Stack             |
|[`⎕STATE`](state.md) |Return State of an object|
|[`⎕VGET`](vget.md)  |Value Get              |
|[`⎕VSET`](vset.md)  |Value Set              |
|[`⎕WA`](wa.md)    |Workspace Available      |
|[`⎕WSID`](wsid.md)  |Workspace Identification |
|[`⎕XSI`](xsi.md)   |Extended State Indicator |

## Shared Variables

|Name  |Description                |
|------|---------------------------|
|[`⎕SVC`](set-access-control.md)|Set access Control         |
|[`⎕SVC`](query-access-control.md)|Query access Control       |
|[`⎕SVO`](shared-variable-offer.md)|Shared Variable Offer      |
|[`⎕SVO`](query-degree-of-coupling.md)|Query degree of coupling   |
|[`⎕SVQ`](svq.md)|Shared Variable Query      |
|[`⎕SVR`](svr.md)|Retract offer              |
|[`⎕SVS`](svs.md)|Query Shared Variable State|

## GUI and COM Support

|Name     |Description                |
|---------|---------------------------|
|[`⎕DQ`](dq.md)    |Await and process events   |
|[`⎕EXPORT`](export.md)|Export objects             |
|[`⎕NQ`](nq.md)    |Place an event on the Queue|
|[`⎕WC`](wc.md)    |Create GUI object          |
|[`⎕WG`](wg.md)    |Get GUI object properties  |
|[`⎕WN`](wn.md)    |Query GUI object Names     |
|[`⎕WS`](ws.md)    |Set GUI object properties  |
|[`⎕WX`](wx.md)    |Expose GUI property names  |

## Miscellaneous

|Name    |Description                      |
|--------|---------------------------------|
|[`⎕Ⓐ`](underscored-alphabetic-characters.md)    |Underscored Alphabetic Characters|
|[`⎕AV`](av.md)   |Atomic Vector                    |
|[`⎕AVU`](avu.md)  |Atomic Vector - Unicode          |
|[`⎕KL`](kl.md)   |Key Labels                       |
|[`⎕PFKEY`](pfkey.md)|Programmable Function Keys       |
|[`⎕SD`](sd.md)   |Screen Dimensions                |
|[`⎕SM`](sm.md)   |Screen Map                       |
|[`⎕SR`](sr.md)   |Screen Read                      |
|[`⎕OPT`](opt.md)  |Variant Operator                 |
|[`⎕TC`](tc.md)   |Terminal Control                 |
|[`⎕XT`](set-external-variable.md)   |Associate External variable      |
|[`⎕XT`](query-external-variable.md)   |Query External variable          |

## System Variables

System variables retain information used by the system in some way. Many system variables affect the behaviour of primitive functions and operators to which they act as _implicit arguments_.

System variables can be localised by inclusion in the header line of a defined function or in the argument list of the system function `⎕SHADOW`. When a system variable is localised, it retains its previous value until it is assigned a new one. This feature is known as "pass-through localisation". The exception to this rule is `⎕TRAP`.

A system variable can never be undefined. Default values are assigned to all system variables in a clear workspace.

|Name           |Description                               |Scope      |
|---------------|-----------------------------------------|-----------|
|[`⎕AVU`](avu.md)  |Atomic Vector – Unicode              |Namespace  |
|[`⎕CT`](ct.md)    |Comparison Tolerance                |Namespace  |
|[`⎕DCT`](dct.md)  |Decimal Comp Tolerance              |Namespace  |
|[`⎕DIV`](div.md)  |Division Method                     |Namespace  |
|[`⎕FR`](fr.md)    |Floating-Point Representation       |Namespace  |
|[`⎕IO`](io.md)    |Index Origin                        |Namespace  |
|[`⎕LX`](lx.md)    |Latent Expression                   |Workspace  |
|[`⎕ML`](ml.md)    |Migration Level                     |Namespace  |
|[`⎕PATH`](path.md)|Search Path                         |Session    |
|[`⎕PP`](pp.md)    |Print Precision                     |Namespace  |
|[`⎕PW`](pw.md)    |Print Width                         |Session    |
|[`⎕RL`](rl.md)    |Random Link                         |Namespace  |
|[`⎕RTL`](rtl.md)  |Response Time Limit                 |Namespace  |
|[`⎕SM`](sm.md)    |Screen Map                          |Workspace  |
|[`⎕TNAME`](tname.md)|Thread Name                      |Workspace  |
|[`⎕TRAP`](trap.md)|Event Trap                          |Workspace  |
|[`⎕USING`](using.md)|Microsoft .NET Search Path       |Namespace  |
|[`⎕WSID`](wsid.md)|Workspace ID                        |Workspace  |
|[`⎕WX`](wx.md)    |Window Expose                       |Namespace  |

In other words, [`⎕PATH`](path.md) and [`⎕PW`](pw.md) relate to the session. [`⎕LX`](lx.md), [`⎕SM`](sm.md), [`⎕TRAP`](trap.md), and [`⎕WSID`](wsid.md) relate to the active workspace. All the other system variables relate to the current namespace.

|Session   |Workspace     |Namespace        |
|----------|--------------|-----------------|
|[`⎕PATH`](path.md) |[`⎕LX`](lx.md)    |[`⎕AVU`](avu.md)   |
|[`⎕PW`](pw.md)     |[`⎕SM`](sm.md)    |[`⎕CT`](ct.md)     |
|&nbsp;                 |[`⎕TRAP`](trap.md) |[`⎕DCT`](dct.md)   |
|&nbsp;                 |[`⎕WSID`](wsid.md) |[`⎕DIV`](div.md)   |
|&nbsp;                 |&nbsp;               |[`⎕FR`](fr.md)     |
|&nbsp;                 |&nbsp;               |[`⎕IO`](io.md)     |
|&nbsp;                 |&nbsp;               |[`⎕ML`](ml.md)     |
|&nbsp;                 |&nbsp;               |[`⎕PP`](pp.md)     |
|&nbsp;                 |&nbsp;               |[`⎕RL`](rl.md)     |
|&nbsp;                 |&nbsp;               |[`⎕RTL`](rtl.md)   |
|&nbsp;                 |&nbsp;               |[`⎕USING`](using.md)|
|&nbsp;                 |&nbsp;               |[`⎕WX`](wx.md)     |

Note that the value assigned to a system variable must be appropriate, otherwise an error will be reported immediately.

<h2 class="example">Example</h2>
```apl
      ⎕IO←3
DOMAIN ERROR
      ⎕IO←3
      ^
```
