---
search:
  exclude: true
---
<h1 class="heading"><span class="name">System Functions (by Category)</span></h1>

## System Functions by Subject

The following tables list the system functions (a collective term for system constants, variables, functions, and operators) divided into appropriate categories by usage.

The dyadic operator `⎕OPT` is unique in that it modifies the behaviour of other system functions (and function derived from system operators), effectively providing them with additional option arguments.

### Session Information and Management

These provide information on or control the execution environment.

|Name                   |Description                |Syntax|
|-----------------------|---------------------------|----|
|[`⎕AI`](ai.md)      |Account Information        |Constant|
|[`⎕AN`](an.md)      |Account Name               |Constant|
|[`⎕CLEAR`](clear.md)|Clear workspace (WS)       |Constant|
|[`⎕CY`](cy.md)      |Copy objects into active WS|Function|
|[`⎕LOAD`](load.md)  |Load a saved WS            |Function|
|[`⎕OFF`](off.md)    |End the session            |Constant|
|[`⎕SAVE`](save.md)  |Save the active WS         |Function|

### Workspace

These provide information and control the current workspace and its contents.

|Name     |Description              |Syntax|
|---------|-------------------------|-----|
|[`⎕EX`](ex.md)     |Expunge objects         |Monadic function|
|[`⎕LX`](lx.md)    |Latent Expression        |Variable|
|[`⎕NC`](nc.md)    |Name Classification      |Monadic function|
|[`⎕NL`](nl.md)    |Name List                |Monadic function|
|[`⎕SHADOW`](shadow.md)|Shadow names         |Monadic function|
|[`⎕SIZE`](size.md)  |Size of objects        |Monadic function|
|[`⎕WA`](wa.md)    |Workspace Available      |Constant|
|[`⎕WSID`](wsid.md)  |Workspace Identification|Variable|

### Manipulating Workspace Contents

These are tools that allow you perform development environment actions under program control.

|Name      |Description             |Syntax|
|----------|------------------------|-----|
|[`⎕ED`](ed.md)     |Edit one or more objects|Ambivalent function|
|[`⎕EX`](ex.md)     |Expunge objects         |Monadic function|
|[`⎕LOCK`](lock.md)   |Lock a function       |Ambivalent function|
|[`⎕MONITOR`](set-monitor.md)|Monitor set    |Dyadic function|
|[`⎕MONITOR`](query-monitor.md)|Monitor query|Monadic function|
|[`⎕OR`](or.md)     |Object Representation   |Monadic function|
|[`⎕PROFILE`](profile.md)|Profile Application|Ambivalent function|
|[`⎕REFS`](refs.md)   |Local References      |Ambivalent function|
|[`⎕STOP`](set-stop.md)   |Set Stop vector   |Dyadic function|
|[`⎕STOP`](query-stop.md)   |Query Stop vector|Monadic function|
|[`⎕TRACE`](set-trace.md)  |Set Trace vector  |Dyadic function|
|[`⎕TRACE`](query-trace.md)  |Query Trace vector|Monadic function|

### Namespaces and Objects

These are facilities to create, manipulate, and navigate namespaces and other objects, and for object oriented programming.

|Name        |Description   |Syntax|
|------------|--------------|-----|
|[`⎕BASE`](base.md)     |Base Class   |Reference|
|[`⎕CLASS`](class.md)    |Class       |Monadic function|
|[`⎕CS`](cs.md)       |Change Space   |Monadic function|
|[`⎕DF`](df.md)       |Display Format |Monadic function|
|[`⎕FIX`](fix.md)      |Fix           |Ambivalent function|
|[`⎕INSTANCES`](instances.md)|Instances|Monadic function|
|[`⎕NEW`](new.md)      |New Instance  |Monadic function|
|[`⎕NS`](ns.md)       |Namespace      |Ambivalent function|
|[`⎕THIS`](this.md)     |Self-reference|Reference|
|[`⎕VGET`](vget.md)     |Value Get    |Ambivalent function|
|[`⎕VSET`](vset.md)     |Value Set    |Ambivalent function|

### Built-in Objects and Windows GUI

These are facilities for dealing with built-in objects that mostly represent Windows GUI elements, although a few other built-in objects are cross-platform and/or do not relate to the graphical interface.

|Name     |Description                |Syntax|
|---------|---------------------------|-----|
|[`⎕DQ`](dq.md)    |Await and process events   |Monadic function|
|[`⎕NQ`](nq.md)    |Place an event on the Queue|Ambivalent function|
|[`⎕WC`](wc.md)    |Create GUI object          |Ambivalent function|
|[`⎕WG`](wg.md)    |Get GUI object properties  |Ambivalent function|
|[`⎕WN`](wn.md)    |Query GUI object Names     |Ambivalent function|
|[`⎕WS`](ws.md)    |Set GUI object properties  |Ambivalent function|
|[`⎕WX`](wx.md)    |Expose GUI property names  |Variable|

### Modifying Language Behaviour

Certain primitives and system functions have behaviour that is customised globally via a set of system variables. They are: 

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

The following table describes the dependencies that exist between language elements and these system variables.

Table: Implicit Arguments {: #Implicit_Arguments }

|System Variable|Monadic Functions|Dyadic Functions|Other|
|---|---|---|---|
|`⎕CT`, `⎕DCT`|`⌈` `⌊` `∪`|`~` `<` `≤` `=` `≥` `>` `≠` `≡` `≢` `⍳` `∊` `∪` `∩` `⍷` `|` `∨` `∧` `⎕FMT`|`⌸`|
|`⎕DIV`|`÷`|`÷`|&nbsp;|
|`⎕FR`<sup>1</sup>|`÷` `*` `⍟` `!` `○` `⌹`|`+` `-` `×` `÷` `*` `⍟` `|` `!` `○` `∨` `∧` `⊥` `⊤` `⌹`|&nbsp;|
|`⎕FR`<sup>2</sup>|`⌈` `⌊` `∪`|`~` `<` `≤` `=` `≥` `>` `≠` `≡` `≢` `⍳` `∊` `∪` `∩` `⍷`|`⌸`|
|`⎕FR`<sup>3</sup>|`⍒` `⍋`|`⌈` `⌊` `⍒` `⍋` `⍸` `⎕FX`|&nbsp;|
|`⎕IO`|`⍳` `?` `⍒` `⍋` `⍸`|`⍳` `?` `⍒` `⍋` `⍉` `⊃` `⌷` `⍸` `⎕FX`|`⌸` `@` `[]`<sup>4</sup> `⎕DMX`<sup>5</sup>
|`⎕ML`|`∊` `↑` `⊃` `≡`|&nbsp;|`⎕TC`|
|`⎕PP`|`⍕` `⎕FMT`|&nbsp;|`⎕←` `⍞←`|
|`⎕RL`|`?`|`?`|&nbsp;|

<sup>1</sup> functions that compute real numbers and whose precision depends on `⎕FR`

<sup>2</sup> functions that perform tolerant comparisons (intolerant if `⎕CT`/`⎕DCT` is `0`)

<sup>3</sup> functions that perform intolerant comparisons (as if `⎕CT`/`⎕DCT` was `0`)

<sup>4</sup> that is, bracket indexing and bracket axis

<sup>5</sup> that is, some extended error messages take `⎕IO` into account

Tolerant comparisons depend on `⎕FR` to select which of `⎕CT` and `⎕DCT` is used. Even  intolerant comparison depends on `⎕FR` in the case of comparing DECFs: If two DECFs are different but correspond to the same double, then they will be treated as unequal when `⎕FR` is `1287` but equal when it is `645`.

### System Constants

These constants are convenient names for commonly used values that would otherwise be tedious or errorprone to type out or produce.

|Name   |Description                     |
|-------|--------------------------------|
|[`⎕A`](a.md)   |Alphabetic uppercase<sup>1</sup> characters|
|[`⎕D`](d.md)   |Digits                          |
|[`⎕NULL`](null.md)|Null Item                       |

<sup>1</sup> The alphabetic lowercase characters can be obtained with `⎕C⎕A`.

### Data Conversion

These are tools to convert between common representations of data.

|Name    |Description                                             |Syntax|
|--------|--------------------------------------------------------|----|
|[`⎕C`](c.md)    |Case Convert                                           |Ambivalent function|
|[`⎕CSV`](csv.md)  |Comma Separated Values                               |Ambivalent function|
|[`⎕DR`](data-representation-monadic.md)   |Data Representation (Monadic)|Ambivalent function|
|[`⎕DR`](data-representation-dyadic.md)   |Data Representation (Dyadic)  |Ambivalent function|
|[`⎕DT`](dt.md)   |Datetime                                              |Dyadic function|
|[`⎕FMT`](format-monadic.md)  |Resolve display                           |Monadic function|
|[`⎕FMT`](format-dyadic.md)  |Format array                               |Dyadic function|
|[`⎕JSON`](json.md) |JSON Convert                                        |Ambivalent function|
|[`⎕TS`](ts.md)      |Timestamp                                          |Constant|
|[`⎕UCS`](ucs.md)  |Unicode Convert                                      |Ambivalent function|
|[`⎕VFI`](vfi.md)  |Verify and Fix numeric                               |Ambivalent function|
|[`⎕XML`](xml.md)  |XML Convert                                          |Ambivalent function|

### Input and Output

These are communication facilities.

|Name     |Description           |Syntax|
|---------|----------------------|-----|
|[`⎕`](evaluated-input-output.md)      |Evaluated Input/Output|Variable|
|[`⍞`](character-input-output.md)      |Character Input/Output|Variable|
|[`⎕ARBIN`](arbin.md) |Arbitrary Input       |Dyadic function|
|[`⎕ARBOUT`](arbout.md)|Arbitrary Output      |Dyadic function|
|[`⎕KL`](kl.md)   |Key Labels                       |Monadic function|
|[`⎕PFKEY`](pfkey.md)|Programmable Function Keys    |Ambivalent function|
|[`⎕RTL`](rtl.md)   |Response Time Limit   |Variable|
|[`⎕SD`](sd.md)   |Screen Dimensions                |Constant|
|[`⎕SM`](sm.md)   |Screen Map                       |Variable|
|[`⎕SR`](sr.md)   |Screen Read                      |Ambivalent function|

### External Utilities

These are APL interfaces to various facilities outside Dyalog.

|Name    |Description                                             |Syntax|
|--------|--------------------------------------------------------|----|
|[`⎕MAP`](map.md)  |Map a file                                              |Abivalent function|
|[`⎕NA`](na.md)   |Declare a DLL function                                  |Abivalent function|
|[`⎕R`](r.md)    |Replace                                                 |Dyadic operator|
|[`⎕S`](s.md)    |Search                                                  |Dyadic operator|
|[`⎕SHELL`](shell.md)|Execute a shell command or another program              |Monadic function|
|[`⎕USING`](using.md)|Microsoft .NET Search Path                              |Variable|

### Component Files

These create, control, and manipulate component files.

|Name       |Description                |Syntax|
|-----------|---------------------------|-----|
|[`⎕FAPPEND`](fappend.md) |Append a component to File |Dyadic function|
|[`⎕FAVAIL`](favail.md)  |File system Availability   |Constant|
|[`⎕FCHK`](fchk.md)    |File Check and Repair      |Ambivalent function|
|[`⎕FCOPY`](fcopy.md)   |Copy a File                |Dyadic function|
|[`⎕FCREATE`](fcreate.md) |Create a File              |Dyadic function|
|[`⎕FDROP`](fdrop.md)   |Drop a block of components |Dyadic function|
|[`⎕FERASE`](ferase.md)  |Erase a File               |Dyadic function|
|[`⎕FHIST`](fhist.md)   |File History               |Monadic function|
|[`⎕FHOLD`](fhold.md)   |File Hold                  |Ambivalent function|
|[`⎕FLIB`](flib.md)    |List File Library          |Monadic function|
|[`⎕FNAMES`](fnames.md)  |Names of tied Files        |Constant|
|[`⎕FNUMS`](fnums.md)   |Tie Numbers of tied Files  |Constant|
|[`⎕FPROPS`](fprops.md)  |File Properties            |Dyadic function|
|[`⎕FRDAC`](frdac.md)   |Read File Access matrix    |Monadic function|
|[`⎕FRDCI`](frdci.md)   |Read Component Information |Monadic function|
|[`⎕FREAD`](fread.md)   |Read a component from File |Monadic function|
|[`⎕FRENAME`](frename.md) |Rename a File              |Dyadic function|
|[`⎕FREPLACE`](freplace.md)|Replace a component on File|Dyadic function|
|[`⎕FRESIZE`](fresize.md) |File Resize                |Ambivalent function|
|[`⎕FSIZE`](fsize.md)   |File Size                  |Monadic function|
|[`⎕FSTAC`](fstac.md)   |Set File Access matrix     |Dyadic function|
|[`⎕FSTIE`](fstie.md)   |Share-Tie a File           |Dyadic function|
|[`⎕FTIE`](ftie.md)    |Tie a File exclusively     |Dyadic function|
|[`⎕FUNTIE`](funtie.md)  |Untie Files                |Monadic function|

### Native Files

These create and manipulate files of any type as well as directories.

|Name       |Description                                                  |Syntax|
|-----------|-------------------------------------------------------------|----|
|[`⎕MKDIR`](mkdir.md)   |Create a directory                                           |Ambivalent function|
|[`⎕NAPPEND`](nappend.md) |Append to File                                               |Dyadic function|
|[`⎕NCOPY`](ncopy.md)   |Copy files and directories                                   |Dyadic function|
|[`⎕NCREATE`](ncreate.md) |Create a File                                                |Dyadic function|
|[`⎕NDELETE`](ndelete.md) |Delete a File or Directory                                   |Ambivalent function|
|[`⎕NERASE`](nerase.md)  |Erase a File                                                 |Dyadic function|
|[`⎕NEXISTS`](nexists.md) |Discover whether or not a file or directory exists           |Monadic function|
|[`⎕NGET`](nget.md)    |Read Text File                                               |Ambivalent function|
|[`⎕NINFO`](ninfo.md)   |Query or set information about one or more files and/or directories|Ambivalent function|
|[`⎕NLOCK`](nlock.md)   |Lock a region of a file                                      |Ambivalent function|
|[`⎕NMOVE`](nmove.md)   |Move files and directories                                   |Dyadic function|
|[`⎕NNAMES`](nnames.md)  |Names of tied Files                                          |Constant|
|[`⎕NNUMS`](nnums.md)   |Tie Numbers of tied Files                                    |Constant|
|[`⎕NPARTS`](nparts.md)  |Split a file name into its constituent parts.                |Ambivalent function|
|[`⎕NPUT`](nput.md)    |Write Text File                                              |Dyadic function|
|[`⎕NREAD`](nread.md)   |Read from File                                               |Monadic function|
|[`⎕NRENAME`](nrename.md) |Rename a File                                                |Dyadic function|
|[`⎕NREPLACE`](nreplace.md)|Replace data on File                                         |Dyadic function|
|[`⎕NRESIZE`](nresize.md) |File Resize                                                  |Dyadic function|
|[`⎕NSIZE`](nsize.md)   |File Size                                                    |Monadic function|
|[`⎕NTIE`](ntie.md)    |Tie a File exclusively                                       |Dyadic function|
|[`⎕NUNTIE`](nuntie.md)  |Untie Files                                                  |Monadic function|

### Threads

These are facilities to handle threads such as those created by [Spawn](../../primitive-operators/spawn.md) (`&`).

|Name     |Description                  |Syntax|
|---------|-----------------------------|-----|
|[`⎕TALLOC`](talloc.md) |Allocate Token Range         |Abivalent function|
|[`⎕TCNUMS`](tcnums.md) |Thread Child Numbers         |Monadic function|
|[`⎕TID`](tid.md)   |Current Thread Identity      |Constant|
|[`⎕TKILL`](tkill.md) |Kill Threads        |Ambivalent function|
|[`⎕TNAME`](tname.md) |Current Thread Name          |Variable|
|[`⎕TNUMS`](tnums.md) |Thread Numbers               |Constant|
|[`⎕TSYNC`](tsync.md) |Wait for Threads to Terminate|Monadic function|

### Synchronisation

These are facilities to ensure proper timing in the relationship between threads such as those created by [Spawn](../../primitive-operators/spawn.md) (`&`).

|Name     |Description         |Syntax|
|---------|--------------------|-----|
|[`⎕DL`](dl.md)      |Delay execution            |Function|
|[`⎕TALLOC`](talloc.md)|Allocate Token Range|Ambivalent function|
|[`⎕TGET`](tget.md)  |Get Tokens          |Ambivalent function|
|[`⎕TPOOL`](tpool.md) |Token Pool          |Monadic function|
|[`⎕TPUT`](tput.md)  |Put Tokens          |Ambivalent function|
|[`⎕TREQ`](treq.md)  |Token Requests      |Monadic function|

### Stack

These provide information about and manipulate the current call stack.

|Name     |Description              |Syntax|
|---------|-------------------------|-----|
|[`⎕LC`](lc.md)    |Line Count               |Constant|
|[`⎕NSI`](nsi.md)   |Namespace Indicator      |Constant|
|[`⎕RSI`](rsi.md)   |Space Indicator          |Constant|
|[`⎕SI`](si.md)    |State Indicator          |Constant|
|[`⎕SHADOW`](shadow.md)|Shadow names             |Monadic function|
|[`⎕STACK`](stack.md) |Report Stack             |Constant|
|[`⎕STATE`](state.md) |Return State of an object|Monadic function|
|[`⎕XSI`](xsi.md)   |Extended State Indicator |Constant|

### Error Handling

These are facilities to catch, cause, and investigate error events and interruptions.

|Name        |Description                                     |Syntax|
|------------|------------------------------------------------|----|
|[`⎕DMX`](dmx.md)      |Extended Diagnostic Message                     |Reference|
|[`⎕EM`](em.md)       |Event Messages                                  |Monadic function|
|[`⎕EXCEPTION`](exception.md)|Reports the most recent Microsoft .NET Exception|Reference|
|[`⎕SIGNAL`](signal.md)   |Signal event                                    |Ambivalent function|
|[`⎕TRAP`](trap.md)     |Event Trap                                      |Variable|

### Shared Variables

These constitute the [shared variable](../../../interface-guide/dde/shared-variable-principles.md) interface.

|Name  |Description                |Syntax|
|------|---------------------------|-----|
|[`⎕SVC`](set-access-control.md)|Set access Control         |Dyadic function|
|[`⎕SVC`](query-access-control.md)|Query access Control       |Monadic function|
|[`⎕SVO`](shared-variable-offer.md)|Shared Variable Offer      |Dyadic function|
|[`⎕SVO`](query-degree-of-coupling.md)|Query degree of coupling   |Monadic function|
|[`⎕SVQ`](svq.md)|Shared Variable Query      |Monadic function|
|[`⎕SVR`](svr.md)|Retract offer              |Monadic function|
|[`⎕SVS`](svs.md)|Query Shared Variable State|Monadic function|

### Features for Classic

These are relevant only for the Classic (non-Unicode) edition and dealing with its data.

|Name     |Description                |Syntax|
|---------|---------------------------|-----|
|[`⎕NXLATE`](nxlate.md)  |Specify Translation Table |Ambivalent function|
|[`⎕Ⓐ` or `⎕Á`](underscored-alphabetic-characters.md) |Underscored Alphabetic Characters|Constant|
|[`⎕AV`](av.md)   |Atomic Vector              |Constant|
|[`⎕AVU`](avu.md)  |Atomic Vector - Unicode         |Variable|

### Archaic and Deprecated

These are outdated facilites that have newer and better alternatives.

|Name    |Description                      |Syntax|Alternative|
|--------|---------------------------------|----|-----------|
|[`⎕AT`](at.md)     |Object Attributes       |Ambivalent function|`⎕ATX` supports many more attributes|
|[`⎕CMD`](execute-windows-command.md)  |Execute the Windows Command Processor or another program|Monadic function|`⎕SHELL` is interruptible, can separate output streams, and has lots of advanced options|
|[`⎕CMD`](start-windows-auxiliary-processor.md)  |Start a Windows Auxiliary Processor|Dyadic function|DLL/shared libraries via `⎕NA`|
|[`⎕CR`](cr.md)     |Canonical Representation|Monadic function|`⎕ATX` can provide source as typed|
|[`⎕DM`](dm.md)       |Diagnostic Message    |Constant|`⎕DMX.DM` is thread-safe|
|[`⎕EN`](en.md)       |Event Number          |Constant|`⎕DMX.EN` is thread-safe|
|[`⎕EXPORT`](export.md)|Export objects       |Ambivalent function|&nbsp;|
|[`⎕FX`](fx.md)     |Fix definition          |Monadic function|`⎕FIX` saves source as typed|
|[`⎕NR`](nr.md)     |Nested Representation   |Monadic function|`⎕ATX` can provide source as typed|
|[`⎕PATH`](path.md)  |Search Path            |Variable|&nbsp;|
|[`⎕SH`](execute-unix-command.md)   |Execute a UNIX command or another program|Monadic function|`⎕SHELL` is interruptible, can separate output streams, and has lots of advanced options|
|[`⎕SH`](start-unix-auxiliary-processor.md)   |Start a UNIX Auxiliary Processor|Dyadic function|DLL/shared libraries via `⎕NA`|
|[`⎕SRC`](src.md)      |Source        |Monadic function|`⎕ATX` can provide source for non-objects|
|[`⎕TC`](tc.md)   |Terminal Control           |Constant|`⎕UCS 8`, `⎕UCS 10`, and `⎕UCS 13`|
|[`⎕VR`](vr.md)     |Vector Representation   |Monadic function|`⎕ATX` can provide source as typed|
|[`⎕XT`](query-external-variable.md)   |Query External variable  |Monadic function|`⎕MAP` or [component files](../../../programming-reference-guide/introduction/component-files/)|
|[`⎕XT`](set-external-variable.md)   |Associate External variable|Dyadic function|`⎕MAP` or [component files](../../../programming-reference-guide/introduction/component-files/)|

## System Variables

System variables retain information used by the system in some way. Many system variables affect the behaviour of primitive functions and operators to which they act as _implicit arguments_.

System variables can be localised by inclusion in the header line of a defined function or in the argument list of the system function `⎕SHADOW`. When a system variable is localised, it retains its previous value until it is assigned a new one. This feature is known as "pass-through localisation". The exception to this rule is `⎕TRAP`.

A system variable can never be undefined. Default values are assigned to all system variables in a clear workspace.

[`⎕PATH`](path.md) and [`⎕PW`](pw.md) relate to the session. [`⎕LX`](lx.md), [`⎕SM`](sm.md), [`⎕TRAP`](trap.md), and [`⎕WSID`](wsid.md) relate to the active workspace, and all the other system variables relate to the current namespace:

|Name           |Description                               |Scope      |
|---------------|-----------------------------------------|-----------|
|[`⎕AVU`](avu.md)  |Atomic Vector – Unicode              |Namespace  |
|[`⎕CT`](ct.md)    |Comparison Tolerance                |Namespace  |
|[`⎕DCT`](dct.md)  |Decimal Comparison Tolerance              |Namespace  |
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

Note that the value assigned to a system variable must be appropriate, otherwise an error will be reported immediately.

<h2 class="example">Example</h2>

```apl
      ⎕IO←3
DOMAIN ERROR
      ⎕IO←3
      ∧
```

Most system variables normalise their value structure:
```apl
      ⍴⎕DIV←⍪0  ⍝ matrix in
1 1
      ⍴⎕DIV     ⍝ scalar out

      ⍴⎕LX←'+'  ⍝ scalar in

      ⍴⎕LX     ⍝ vector out
1
      ≡⎕TRAP←0'C' '''Eh?'''  ⍝ depth 2 array in
¯2
      ≡⎕TRAP                 ⍝ depth 3 array out
¯3
```
