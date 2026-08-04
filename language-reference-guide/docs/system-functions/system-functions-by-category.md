---
search:
  exclude: true
---
# System Functions (by Category)

## System Functions by Subject

The following tables list the system functions (a collective term for system constants, variables, functions, and operators) divided into appropriate categories by usage.

The dyadic operator `⎕OPT` is unique in that it modifies the behaviour of other system functions (and function derived from system operators), effectively providing them with additional option arguments.

### Session Information and Management

These provide information on, or control, the execution environment.

|Name                   |Description                |Form|
|-----------------------|---------------------------|----|
|[`⎕AI`](ai.md)         |Account Information        |Constant|
|[`⎕AN`](an.md)         |Account Name               |Constant|
|[`⎕CLEAR`](clear.md)   |Clear workspace (WS)       |Constant|
|[`⎕CY`](cy.md)         |Copy objects into active WS|Function|
|[`⎕LOAD`](load.md)     |Load a saved WS            |Function|
|[`⎕OFF`](off.md)       |End the session            |Constant|
|[`⎕SAVE`](save.md)     |Save the active WS         |Function|
|[`⎕SYSTEM`](system.md) |System Information         |Reference|

### Workspace

These provide information on, and control, the current workspace and its contents.

|Name     |Description              |Form|
|---------|-------------------------|-----|
|[`⎕ATX`](atx.md)   |Extended Attributes     |Dyadic function|
|[`⎕EX`](ex.md)     |Expunge objects         |Monadic function|
|[`⎕LX`](lx.md)    |Latent Expression        |Variable|
|[`⎕NC`](nc.md)    |Name Classification      |Monadic function|
|[`⎕NL`](nl-monadic.md)|List Object Names        |Monadic function|
|[`⎕NL`](nl-dyadic.md)|List Object Names with Filter|Dyadic function |
|[`⎕SHADOW`](shadow.md)|Shadow names         |Monadic function|
|[`⎕SIZE`](size.md)  |Size of objects        |Monadic function|
|[`⎕WA`](wa.md)    |Workspace Available      |Constant|
|[`⎕WSID`](wsid.md)  |Workspace Identification|Variable|

### Manipulating Workspace Contents

These are tools that allow you perform development environment actions under program control.

|Name      |Description             |Form|
|----------|------------------------|-----|
|[`⎕ED`](ed-monadic.md)|Edit Objects            |Monadic function   |
|[`⎕ED`](ed-dyadic.md)|Edit Objects with Type  |Dyadic function    |
|[`⎕EX`](ex.md)     |Expunge objects         |Monadic function|
|[`⎕LOCK`](lock-monadic.md)|Lock Function         |Monadic function   |
|[`⎕LOCK`](lock-dyadic.md)|Custom Lock Function  |Dyadic function    |
|[`⎕MONITOR`](set-monitor.md)|Monitor set    |Dyadic function|
|[`⎕MONITOR`](query-monitor.md)|Monitor query|Monadic function|
|[`⎕OR`](or.md)     |Object Representation   |Monadic function|
|[`⎕PROFILE`](profile-monadic.md)|Profile Code       |Monadic function   |
|[`⎕PROFILE`](profile-dyadic.md)|Filter Profile Data|Dyadic function    |
|[`⎕REFS`](refs.md)   |Local References      |Monadic function|
|[`⎕STOP`](set-stop.md)   |Set Stop vector   |Dyadic function|
|[`⎕STOP`](query-stop.md)   |Query Stop vector|Monadic function|
|[`⎕TRACE`](set-trace.md)  |Set Trace vector  |Dyadic function|
|[`⎕TRACE`](query-trace.md)  |Query Trace vector|Monadic function|

### Namespaces and Objects

These are facilities to create, manipulate, and navigate namespaces and other objects, and for object oriented programming.

|Name        |Description   |Form|
|------------|--------------|-----|
|[`⎕BASE`](base.md)     |Base Class   |Reference|
|[`⎕CLASS`](class-monadic.md)|Class Hierarchy|Monadic function|
|[`⎕CLASS`](class-dyadic.md)|Get Class/Interface Implementation|Dyadic function |
|[`⎕CS`](cs.md)       |Change Space   |Monadic function|
|[`⎕DF`](df.md)       |Display Format |Monadic function|
|[`⎕FIX`](fix-monadic.md)|Define Namespace|Monadic function   |
|[`⎕FIX`](fix-dyadic.md)|Define Objects|Dyadic function    |
|[`⎕INSTANCES`](instances.md)|Instances|Monadic function|
|[`⎕NEW`](new.md)      |New Instance  |Monadic function|
|[`⎕NS`](ns-monadic.md)|Create/Clone Namespace|Monadic function   |
|[`⎕NS`](ns-dyadic.md)|Create/Clone Custom Namespaces|Dyadic function    |
|[`⎕THIS`](this.md)     |Self-reference|Reference|
|[`⎕VGET`](vget-monadic.md)|Get Value from Current Namespace|Monadic function   |
|[`⎕VGET`](vget-dyadic.md)|Get Value from Namespace|Dyadic function    |
|[`⎕VSET`](vset-monadic.md)|Set Value in Current Namespace|Monadic function   |
|[`⎕VSET`](vset-dyadic.md)|Set Value in Namespace|Dyadic function    |

### Built-in Objects and Windows GUI

These are facilities for dealing with built-in objects. They mostly represent Microsoft Windows GUI elements, although a few other built-in objects are cross-platform and/or do not relate to the graphical interface.

|Name     |Description                |Form|
|---------|---------------------------|-----|
|[`⎕DQ`](dq.md)    |Await and process events   |Monadic function|
|[`⎕NQ`](nq-monadic.md)|Enqueue Event              |Monadic function   |
|[`⎕NQ`](nq-dyadic.md)|Custom Enqueue Event       |Dyadic function    |
|[`⎕SE`](se.md)    |Session Namespace          |Reference|
|[`⎕WC`](wc-monadic.md)|Convert Namespace to GUI Object|Monadic function   |
|[`⎕WC`](wc-dyadic.md)|Create GUI Object          |Dyadic function    |
|[`⎕WG`](wg-monadic.md)|Get Properties of Current GUI Object|Monadic function   |
|[`⎕WG`](wg-dyadic.md)|Get Properties of GUI Object|Dyadic function    |
|[`⎕WN`](wn-monadic.md)|Get GUI Child Names in Current Object|Monadic function   |
|[`⎕WN`](wn-dyadic.md)|Get GUI Child Names in Parent Object|Dyadic function    |
|[`⎕WS`](ws-monadic.md)|Set Properties of Current GUI Object|Monadic function   |
|[`⎕WS`](ws-dyadic.md)|Set Properties of GUI Object|Dyadic function    |
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

These constants simplify access to commonly-used values.

|Name   |Description                     |
|-------|--------------------------------|
|[`⎕A`](a.md)   |Alphabetic uppercase characters (lowercase characters can be obtained with `⎕C⎕A`)|
|[`⎕D`](d.md)   |Digits                          |
|[`⎕NULL`](null.md)|Null Item                       |

### Data Conversion

These are tools to convert between common representations of data.

|Name    |Description                                             |Form|
|--------|--------------------------------------------------------|----|
|[`⎕C`](c-monadic.md)|Case Fold                                              |Monadic function   |
|[`⎕C`](c-dyadic.md)|Case Map                                               |Dyadic function    |
|[`⎕CSV`](csv-monadic.md)|Import CSV                                           |Monadic function   |
|[`⎕CSV`](csv-dyadic.md)|Export CSV                                           |Dyadic function    |
|[`⎕DR`](data-representation-monadic.md)   |Data Representation          |Monadic function|
|[`⎕DR`](data-representation-dyadic.md)   |Data Representation           |Dyadic function|
|[`⎕DT`](dt.md)   |Datetime                                              |Dyadic function|
|[`⎕FMT`](format-monadic.md)  |Resolve display                           |Monadic function|
|[`⎕FMT`](format-dyadic.md)  |Format array                               |Dyadic function|
|[`⎕JSON`](json-monadic.md)|Auto-convert JSON                                   |Monadic function   |
|[`⎕JSON`](json-dyadic.md)|Convert JSON                                        |Dyadic function    |
|[`⎕TS`](ts.md)      |Timestamp                                          |Constant|
|[`⎕UCS`](ucs-monadic.md)|Convert Unicode Code Point                           |Monadic function   |
|[`⎕UCS`](ucs-dyadic.md)|Convert Unicode Representation                       |Dyadic function    |
|[`⎕VFI`](vfi-monadic.md)|Parse Numbers                                        |Monadic function   |
|[`⎕VFI`](vfi-dyadic.md)|Parse Numbers with Separators                        |Dyadic function    |
|[`⎕XML`](xml-monadic.md)|Convert XML                                          |Monadic function   |
|[`⎕XML`](xml-dyadic.md)|Custom Convert XML                                   |Dyadic function    |

### Input and Output

These are communication facilities.

|Name     |Description           |Form|
|---------|----------------------|-----|
|[`⎕`](evaluated-input-output.md)      |Evaluated Input/Output|Variable|
|[`⍞`](character-input-output.md)      |Character Input/Output|Variable|
|[`⎕ARBIN`](arbin.md) |Arbitrary Input       |Dyadic function|
|[`⎕ARBOUT`](arbout.md)|Arbitrary Output      |Dyadic function|
|[`⎕KL`](kl.md)   |Key Labels                       |Monadic function|
|[`⎕PFKEY`](pfkey-monadic.md)|Query Programmable Function Key|Monadic function   |
|[`⎕PFKEY`](pfkey-dyadic.md)|Program Function Key          |Dyadic function    |
|[`⎕RTL`](rtl.md)   |Response Time Limit   |Variable|
|[`⎕SD`](sd.md)   |Screen Dimensions                |Constant|
|[`⎕SM`](sm.md)   |Screen Map                       |Variable|
|[`⎕SR`](sr-monadic.md)|Screen Read                      |Monadic function   |
|[`⎕SR`](sr-dyadic.md)|Custom Screen Read               |Dyadic function    |

### External Utilities

These are APL interfaces to various facilities outside Dyalog.

|Name    |Description                                             |Form|
|--------|--------------------------------------------------------|----|
|[`⎕MAP`](map-monadic.md)|Map Array File                                          |Monadic function   |
|[`⎕MAP`](map-dyadic.md)|Map Raw Data File                                       |Dyadic function    |
|[`⎕NA`](na-monadic.md)|Associate External Function with Own Name               |Monadic function   |
|[`⎕NA`](na-dyadic.md)|Associate External Function with Custom Name            |Dyadic function    |
|[`⎕R`](r.md)    |Replace                                                 |Dyadic operator|
|[`⎕S`](s.md)    |Search                                                  |Dyadic operator|
|[`⎕SHELL`](shell.md)|Execute a shell command or another program              |Monadic function|
|[`⎕USING`](using.md)|Microsoft .NET Search Path                              |Variable|

### Component Files

These create, control, and manipulate component files.

|Name       |Description                |Form|
|-----------|---------------------------|-----|
|[`⎕FAPPEND`](fappend.md) |Append a component to File |Dyadic function|
|[`⎕FAVAIL`](favail.md)  |File system Availability   |Constant|
|[`⎕FCHK`](fchk-monadic.md)|Check/Repair Component File|Monadic function   |
|[`⎕FCHK`](fchk-dyadic.md)|Custom Check/Repair Component File|Dyadic function    |
|[`⎕FCOPY`](fcopy.md)   |Copy a File                |Dyadic function|
|[`⎕FCREATE`](fcreate.md) |Create a File              |Dyadic function|
|[`⎕FDROP`](fdrop.md)   |Drop a block of components |Dyadic function|
|[`⎕FERASE`](ferase.md)  |Erase a File               |Dyadic function|
|[`⎕FHIST`](fhist.md)   |File History               |Monadic function|
|[`⎕FHOLD`](fhold-monadic.md)|Component File Hold        |Monadic function   |
|[`⎕FHOLD`](fhold-dyadic.md)|Component File Hold with Timeout|Dyadic function    |
|[`⎕FLIB`](flib.md)    |List File Library          |Monadic function|
|[`⎕FNAMES`](fnames.md)  |Names of tied Files        |Constant|
|[`⎕FNUMS`](fnums.md)   |Tie Numbers of tied Files  |Constant|
|[`⎕FPROPS`](fprops.md)  |File Properties            |Dyadic function|
|[`⎕FRDAC`](frdac.md)   |Read File Access matrix    |Monadic function|
|[`⎕FRDCI`](frdci.md)   |Read Component Information |Monadic function|
|[`⎕FREAD`](fread.md)   |Read a component from File |Monadic function|
|[`⎕FRENAME`](frename.md) |Rename a File              |Dyadic function|
|[`⎕FREPLACE`](freplace.md)|Replace a component on File|Dyadic function|
|[`⎕FRESIZE`](fresize-monadic.md)|Compact Component File     |Monadic function   |
|[`⎕FRESIZE`](fresize-dyadic.md)|Resize Component File      |Dyadic function    |
|[`⎕FSIZE`](fsize.md)   |File Size                  |Monadic function|
|[`⎕FSTAC`](fstac.md)   |Set File Access matrix     |Dyadic function|
|[`⎕FSTIE`](fstie.md)   |Share-Tie a File           |Dyadic function|
|[`⎕FTIE`](ftie.md)    |Tie a File exclusively     |Dyadic function|
|[`⎕FUNTIE`](funtie.md)  |Untie Files                |Monadic function|

### Native Files

These create and manipulate files of any type as well as directories.

|Name       |Description                                                  |Form|
|-----------|-------------------------------------------------------------|----|
|[`⎕MKDIR`](mkdir-monadic.md)|Create Directory                                             |Monadic function   |
|[`⎕MKDIR`](mkdir-dyadic.md)|Custom Create Directory                                      |Dyadic function    |
|[`⎕NAPPEND`](nappend.md) |Append to File                                               |Dyadic function|
|[`⎕NCOPY`](ncopy.md)   |Copy files and directories                                   |Dyadic function|
|[`⎕NCREATE`](ncreate.md) |Create a File                                                |Dyadic function|
|[`⎕NDELETE`](ndelete-monadic.md)|Delete Native File                                           |Monadic function   |
|[`⎕NDELETE`](ndelete-dyadic.md)|Custom Delete Native File                                    |Dyadic function    |
|[`⎕NERASE`](nerase.md)  |Erase a File                                                 |Dyadic function|
|[`⎕NEXISTS`](nexists.md) |Discover whether or not a file or directory exists           |Monadic function|
|[`⎕NGET`](nget-monadic.md)|Get Text File Content                                        |Monadic function   |
|[`⎕NGET`](nget-dyadic.md)|Decode Text File Content                                     |Dyadic function    |
|[`⎕NINFO`](ninfo-monadic.md)|Native File Name                                                   |Monadic function   |
|[`⎕NINFO`](ninfo-dyadic.md)|Native File Information                                            |Dyadic function    |
|[`⎕NLOCK`](nlock.md)   |Lock a region of a file                                      |Dyadic function|
|[`⎕NMOVE`](nmove.md)   |Move files and directories                                   |Dyadic function|
|[`⎕NNAMES`](nnames.md)  |Names of tied Files                                          |Constant|
|[`⎕NNUMS`](nnums.md)   |Tie Numbers of tied Files                                    |Constant|
|[`⎕NPARTS`](nparts-monadic.md)|File Name Parts                                              |Monadic function   |
|[`⎕NPARTS`](nparts-dyadic.md)|Normalised File Name Parts                                   |Dyadic function    |
|[`⎕NPUT`](nput.md)    |Write Text File                                              |Dyadic function|
|[`⎕NREAD`](nread.md)   |Read from File                                               |Monadic function|
|[`⎕NRENAME`](nrename.md) |Rename a File                                                |Dyadic function|
|[`⎕NREPLACE`](nreplace.md)|Replace data on File                                         |Dyadic function|
|[`⎕NRESIZE`](nresize.md) |File Resize                                                  |Dyadic function|
|[`⎕NSIZE`](nsize.md)   |File Size                                                    |Monadic function|
|[`⎕NTIE`](ntie.md)    |Tie a File exclusively                                       |Dyadic function|
|[`⎕NUNTIE`](nuntie.md)  |Untie Files                                                  |Monadic function|

### Threads

These are facilities to handle threads such as those created by [Spawn](../primitive-operators/spawn.md) (`&`).

|Name     |Description                  |Form|
|---------|-----------------------------|-----|
|[`⎕TALLOC`](talloc-monadic.md)|Allocate New Token Range     |Monadic function   |
|[`⎕TALLOC`](talloc-dyadic.md)|Allocate Existing Token Range|Dyadic function    |
|[`⎕TCNUMS`](tcnums.md) |Thread Child Numbers         |Monadic function|
|[`⎕TID`](tid.md)   |Current Thread Identity      |Constant|
|[`⎕TKILL`](tkill-monadic.md)|Kill Threads        |Monadic function   |
|[`⎕TKILL`](tkill-dyadic.md)|Kill Threads and Descendants|Dyadic function    |
|[`⎕TNAME`](tname.md) |Current Thread Name          |Variable|
|[`⎕TNUMS`](tnums.md) |Thread Numbers               |Constant|
|[`⎕TSYNC`](tsync.md) |Wait for Threads to Terminate|Monadic function|

### Synchronisation

These are facilities to ensure proper timing in the relationship between threads such as those created by [Spawn](../primitive-operators/spawn.md) (`&`).

|Name     |Description         |Form|
|---------|--------------------|-----|
|[`⎕DL`](dl.md)      |Delay execution            |Function|
|[`⎕TALLOC`](talloc-monadic.md)|Allocate New Token Range|Monadic function   |
|[`⎕TALLOC`](talloc-dyadic.md)|Allocate Existing Token Range|Dyadic function    |
|[`⎕TGET`](tget-monadic.md)|Get Tokens          |Monadic function   |
|[`⎕TGET`](tget-dyadic.md)|Get Tokens with Timeout|Dyadic function    |
|[`⎕TPOOL`](tpool.md) |Token Pool          |Monadic function|
|[`⎕TPUT`](tput-monadic.md)|Put Tokens          |Monadic function   |
|[`⎕TPUT`](tput-dyadic.md)|Put Tokens with Values|Dyadic function    |
|[`⎕TREQ`](treq.md)  |Token Requests      |Monadic function|

### Stack

These provide information about and manipulate the current call stack.

|Name     |Description              |Form|
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

|Name        |Description                                     |Form|
|------------|------------------------------------------------|----|
|[`⎕DMX`](dmx.md)      |Extended Diagnostic Message                     |Reference|
|[`⎕EM`](em.md)       |Event Messages                                  |Monadic function|
|[`⎕EXCEPTION`](exception.md)|Reports the most recent Microsoft .NET Exception|Reference|
|[`⎕SIGNAL`](signal-monadic.md)|Signal Default/Custom Event                     |Monadic function   |
|[`⎕SIGNAL`](signal-dyadic.md)|Signal Event with Custom Name                   |Dyadic function    |
|[`⎕TRAP`](trap.md)     |Event Trap                                      |Variable|

### Shared Variables

These constitute the [shared variable](../../interface-guide/dde/shared-variable-principles.md) interface.

|Name  |Description                |Form|
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

|Name     |Description                |Form|
|---------|---------------------------|-----|
|[`⎕NXLATE`](nxlate-monadic.md)|Query Native File Translation Vector|Monadic function   |
|[`⎕NXLATE`](nxlate-dyadic.md)|Set Native File Translation Vector|Dyadic function    |
|[`⎕Ⓐ` or `⎕Á`](underscored-alphabetic-characters.md) |Underscored Alphabetic Characters|Constant|
|[`⎕AV`](av.md)   |Atomic Vector              |Constant|
|[`⎕AVU`](avu.md)  |Atomic Vector - Unicode         |Variable|

### Archaic and Deprecated

These are deprecated facilities that are still supported for legacy purposes; Dyalog Ltd recommends using alternative approaches.

|Name    |Description                      |Form|Alternative|
|--------|---------------------------------|----|-----------|
|[`⎕AT`](at-monadic.md)|Object Attributes       |Monadic function   |`⎕ATX` supports many more attributes|
|[`⎕AT`](at-dyadic.md)|Object Attributes for APL2|Dyadic function    |`⎕ATX` supports many more attributes|
|[`⎕CMD`](execute-windows-command.md)  |Execute the Windows Command Processor or another program|Monadic function|`⎕SHELL` is interruptible, can separate output streams, and has lots of advanced options|
|[`⎕CMD`](start-windows-auxiliary-processor.md)  |Start a Windows Auxiliary Processor|Dyadic function|DLL/shared libraries via `⎕NA`|
|[`⎕CR`](cr.md)     |Canonical Representation|Monadic function|`⎕ATX` can provide source as typed|
|[`⎕DM`](dm.md)       |Diagnostic Message    |Constant|`⎕DMX.DM` is thread-safe|
|[`⎕EN`](en.md)       |Event Number          |Constant|`⎕DMX.EN` is thread-safe|
|[`⎕EXPORT`](export-monadic.md)|Query Export Type    |Monadic function   |Use full (absolute or relative) namespace paths|
|[`⎕EXPORT`](export-dyadic.md)|Set Export Type      |Dyadic function    |Use full (absolute or relative) namespace paths|
|[`⎕FX`](fx.md)     |Fix definition          |Monadic function|`⎕FIX` saves source as typed|
|[`⎕NR`](nr.md)     |Nested Representation   |Monadic function|`⎕ATX` can provide source as typed|
|[`⎕PATH`](path.md)  |Search Path            |Variable|Use full (absolute or relative) namespace paths|
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
