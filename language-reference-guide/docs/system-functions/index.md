---
search:
  boost: 2
---
<h1 class="heading"><span class="name">Introduction</span></h1>

Dyalog includes a collection of built-in facilities that provide various services related to both the APL and the external environment. They have distinguished case-insensitive names beginning with the `⎕` symbol, and are implicitly available in a clear workspace. Collectively, these  facilities are referred to as **System Functions** but they are variously implemented as constants, variables, functions, operators, and namespaces.

!!! Hint "Hints and Recommendations"
    Dyalog can extend any of these facilities by, for example, adding extra elements, rows, or columns to a result, so code should take this possibility into account.

|Name                   |Description                |Syntax|
|-----------------------|---------------------------|----|
|[`⎕`](evaluated-input-output.md)      |Evaluated Input/Output|Variable|
|[`⍞`](character-input-output.md)      |Character Input/Output|Variable|
|[`⎕A`](a.md)   |Alphabetic uppercase characters|Variable|
|[`⎕Ⓐ` or `⎕Á`](underscored-alphabetic-characters.md) |Underscored Alphabetic Characters|Constant|
|[`⎕AI`](ai.md)      |Account Information        |Constant|
|[`⎕AN`](an.md)      |Account Name               |Constant|
|[`⎕ARBIN`](arbin.md) |Arbitrary Input       |Dyadic function|
|[`⎕ARBOUT`](arbout.md)|Arbitrary Output      |Dyadic function|
|[`⎕AT`](at.md)     |Object Attributes       |Ambivalent function|
|[`⎕AV`](av.md)   |Atomic Vector              |Constant|
|[`⎕AVU`](avu.md)  |Atomic Vector - Unicode         |Variable|
|[`⎕BASE`](base.md)     |Base Class   |Reference|
|[`⎕C`](c.md)    |Case Convert                                           |Ambivalent function|
|[`⎕CLASS`](class.md)    |Class       |Monadic function|
|[`⎕CLEAR`](clear.md)|Clear workspace (WS)       |Constant|
|[`⎕CMD`](execute-windows-command.md)  |Execute the Windows Command Processor or another program|Monadic function|
|[`⎕CMD`](start-windows-auxiliary-processor.md)  |Start a Windows Auxiliary Processor|Dyadic function|
|[`⎕CR`](cr.md)     |Canonical Representation|Monadic function|
|[`⎕CS`](cs.md)       |Change Space   |Monadic function|
|[`⎕CSV`](csv.md)  |Comma Separated Values                               |Ambivalent function|
|[`⎕CT`](ct.md) |Comparison Tolerance         |Variable|
|[`⎕CY`](cy.md)      |Copy objects into active WS|Function|
|[`⎕D`](d.md)   |Digits                          |Variable|
|[`⎕DCT`](dct.md)|Decimal Comp Tolerance      |Variable|
|[`⎕DF`](df.md)       |Display Format |Monadic function|
|[`⎕DIV`](div.md)|Division Method             |Variable|
|[`⎕DL`](dl.md)      |Delay execution            |Function|
|[`⎕DM`](dm.md)       |Diagnostic Message    |Constant|
|[`⎕DMX`](dmx.md)      |Extended Diagnostic Message                     |Reference|
|[`⎕DQ`](dq.md)    |Await and process events   |Monadic function|
|[`⎕DR`](data-representation-dyadic.md)   |Data Representation (Dyadic)  |Ambivalent function|
|[`⎕DR`](data-representation-monadic.md)   |Data Representation (Monadic)|Ambivalent function|
|[`⎕DT`](dt.md)   |Datetime                                              |Dyadic function|
|[`⎕ED`](ed.md)     |Edit one or more objects|Ambivalent function|
|[`⎕EM`](em.md)       |Event Messages                                  |Monadic function|
|[`⎕EN`](en.md)       |Event Number          |Constant|
|[`⎕EX`](ex.md)     |Expunge objects         |Monadic function|
|[`⎕EX`](ex.md)     |Expunge objects         |Monadic function|
|[`⎕EXCEPTION`](exception.md)|Reports the most recent Microsoft .NET Exception|Reference|
|[`⎕EXPORT`](export.md)|Export objects       |Ambivalent function|
|[`⎕FAPPEND`](fappend.md) |Append a component to File |Dyadic function|
|[`⎕FAVAIL`](favail.md)  |File system Availability   |Constant|
|[`⎕FCHK`](fchk.md)    |File Check and Repair      |Ambivalent function|
|[`⎕FCOPY`](fcopy.md)   |Copy a File                |Dyadic function|
|[`⎕FCREATE`](fcreate.md) |Create a File              |Dyadic function|
|[`⎕FDROP`](fdrop.md)   |Drop a block of components |Dyadic function|
|[`⎕FERASE`](ferase.md)  |Erase a File               |Dyadic function|
|[`⎕FHIST`](fhist.md)   |File History               |Monadic function|
|[`⎕FHOLD`](fhold.md)   |File Hold                  |Ambivalent function|
|[`⎕FIX`](fix.md)      |Fix           |Ambivalent function|
|[`⎕FLIB`](flib.md)    |List File Library          |Monadic function|
|[`⎕FMT`](format-dyadic.md)  |Format array                               |Dyadic function|
|[`⎕FMT`](format-monadic.md)  |Resolve display                           |Monadic function|
|[`⎕FNAMES`](fnames.md)  |Names of tied Files        |Constant|
|[`⎕FNUMS`](fnums.md)   |Tie Numbers of tied Files  |Constant|
|[`⎕FPROPS`](fprops.md)  |File Properties            |Dyadic function|
|[`⎕FR`](fr.md) |Floating-Point Representation|Variable|
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
|[`⎕FX`](fx.md)     |Fix definition          |Monadic function|
|[`⎕INSTANCES`](instances.md)|Instances|Monadic function|
|[`⎕IO`](io.md) |Index Origin                 |Variable|
|[`⎕JSON`](json.md) |JSON Convert                                        |Ambivalent function|
|[`⎕KL`](kl.md)   |Key Labels                       |Monadic function|
|[`⎕LC`](lc.md)    |Line Count               |Constant|
|[`⎕LOAD`](load.md)  |Load a saved WS            |Function|
|[`⎕LOCK`](lock.md)   |Lock a function       |Ambivalent function|
|[`⎕LX`](lx.md)    |Latent Expression        |Variable|
|[`⎕MAP`](map.md)  |Map a file                                              |Abivalent function|
|[`⎕MKDIR`](mkdir.md)   |Create a directory                                           |Ambivalent function|
|[`⎕ML`](ml.md) |Migration Level              |Variable|
|[`⎕MONITOR`](query-monitor.md)|Monitor query|Monadic function|
|[`⎕MONITOR`](set-monitor.md)|Monitor set    |Dyadic function|
|[`⎕NA`](na.md)   |Declare a DLL function                                  |Abivalent function|
|[`⎕NAPPEND`](nappend.md) |Append to File                                               |Dyadic function|
|[`⎕NC`](nc.md)    |Name Classification      |Monadic function|
|[`⎕NCOPY`](ncopy.md)   |Copy files and directories                                   |Dyadic function|
|[`⎕NCREATE`](ncreate.md) |Create a File                                                |Dyadic function|
|[`⎕NDELETE`](ndelete.md) |Delete a File or Directory                                   |Ambivalent function|
|[`⎕NERASE`](nerase.md)  |Erase a File                                                 |Dyadic function|
|[`⎕NEW`](new.md)      |New Instance  |Monadic function|
|[`⎕NEXISTS`](nexists.md) |Discover whether or not a file or directory exists           |Monadic function|
|[`⎕NGET`](nget.md)    |Read Text File                                               |Ambivalent function|
|[`⎕NINFO`](ninfo.md)   |Query or set information about one or more files and/or directories|Ambivalent function|
|[`⎕NL`](nl.md)    |Name List                |Monadic function|
|[`⎕NLOCK`](nlock.md)   |Lock a region of a file                                      |Ambivalent function|
|[`⎕NMOVE`](nmove.md)   |Move files and directories                                   |Dyadic function|
|[`⎕NNAMES`](nnames.md)  |Names of tied Files                                          |Constant|
|[`⎕NNUMS`](nnums.md)   |Tie Numbers of tied Files                                    |Constant|
|[`⎕NPARTS`](nparts.md)  |Split a file name into its constituent parts.                |Ambivalent function|
|[`⎕NPUT`](nput.md)    |Write Text File                                              |Dyadic function|
|[`⎕NQ`](nq.md)    |Place an event on the Queue|Ambivalent function|
|[`⎕NR`](nr.md)     |Nested Representation   |Monadic function|
|[`⎕NREAD`](nread.md)   |Read from File                                               |Monadic function|
|[`⎕NRENAME`](nrename.md) |Rename a File                                                |Dyadic function|
|[`⎕NREPLACE`](nreplace.md)|Replace data on File                                         |Dyadic function|
|[`⎕NRESIZE`](nresize.md) |File Resize                                                  |Dyadic function|
|[`⎕NS`](ns.md)       |Namespace      |Ambivalent function|
|[`⎕NSI`](nsi.md)   |Namespace Indicator      |Constant|
|[`⎕NSIZE`](nsize.md)   |File Size                                                    |Monadic function|
|[`⎕NTIE`](ntie.md)    |Tie a File exclusively                                       |Dyadic function|
|[`⎕NULL`](null.md)|Null Item                       |Variable|
|[`⎕NUNTIE`](nuntie.md)  |Untie Files                                                  |Monadic function|
|[`⎕NXLATE`](nxlate.md)  |Specify Translation Table |Ambivalent function|
|[`⎕OFF`](off.md)    |End the session            |Constant|
|[`⎕OR`](or.md)     |Object Representation   |Monadic function|
|[`⎕PATH`](path.md)  |Search Path            |Variable|
|[`⎕PFKEY`](pfkey.md)|Programmable Function Keys    |Ambivalent function|
|[`⎕PP`](pp.md) |Print Precision              |Variable|
|[`⎕PROFILE`](profile.md)|Profile Application|Ambivalent function|
|[`⎕R`](r.md)    |Replace                                                 |Dyadic operator|
|[`⎕REFS`](refs.md)   |Local References      |Ambivalent function|
|[`⎕RL`](rl.md) |Random Link                  |Variable|
|[`⎕RSI`](rsi.md)   |Space Indicator          |Constant|
|[`⎕RTL`](rtl.md)   |Response Time Limit   |Variable|
|[`⎕S`](s.md)    |Search                                                  |Dyadic operator|
|[`⎕SAVE`](save.md)  |Save the active WS         |Function|
|[`⎕SD`](sd.md)   |Screen Dimensions                |Constant|
|[`⎕SH`](execute-unix-command.md)   |Execute a UNIX command or another program|Monadic function|
|[`⎕SH`](start-unix-auxiliary-processor.md)   |Start a UNIX Auxiliary Processor|Dyadic function|
|[`⎕SHADOW`](shadow.md)|Shadow names             |Monadic function|
|[`⎕SHADOW`](shadow.md)|Shadow names         |Monadic function|
|[`⎕SHELL`](shell.md)|Execute a shell command or another program              |Monadic function|
|[`⎕SI`](si.md)    |State Indicator          |Constant|
|[`⎕SIGNAL`](signal.md)   |Signal event                                    |Ambivalent function|
|[`⎕SIZE`](size.md)  |Size of objects        |Monadic function|
|[`⎕SM`](sm.md)   |Screen Map                       |Variable|
|[`⎕SR`](sr.md)   |Screen Read                      |Ambivalent function|
|[`⎕SRC`](src.md)      |Source        |Monadic function|
|[`⎕STACK`](stack.md) |Report Stack             |Constant|
|[`⎕STATE`](state.md) |Return State of an object|Monadic function|
|[`⎕STOP`](query-stop.md)   |Query Stop vector|Monadic function|
|[`⎕STOP`](set-stop.md)   |Set Stop vector   |Dyadic function|
|[`⎕SVC`](query-access-control.md)|Query access Control       |Monadic function|
|[`⎕SVC`](set-access-control.md)|Set access Control         |Dyadic function|
|[`⎕SVO`](query-degree-of-coupling.md)|Query degree of coupling   |Monadic function|
|[`⎕SVO`](shared-variable-offer.md)|Shared Variable Offer      |Dyadic function|
|[`⎕SVQ`](svq.md)|Shared Variable Query      |Monadic function|
|[`⎕SVR`](svr.md)|Retract offer              |Monadic function|
|[`⎕SVS`](svs.md)|Query Shared Variable State|Monadic function|
|[`⎕TALLOC`](talloc.md) |Allocate Token Range         |Abivalent function|
|[`⎕TALLOC`](talloc.md)|Allocate Token Range|Ambivalent function|
|[`⎕TC`](tc.md)   |Terminal Control           |Constant|
|[`⎕TCNUMS`](tcnums.md) |Thread Child Numbers         |Monadic function|
|[`⎕TGET`](tget.md)  |Get Tokens          |Ambivalent function|
|[`⎕THIS`](this.md)     |Self-reference|Reference|
|[`⎕TID`](tid.md)   |Current Thread Identity      |Constant|
|[`⎕TKILL`](tkill.md) |Kill Threads        |Ambivalent function|
|[`⎕TNAME`](tname.md) |Current Thread Name          |Variable|
|[`⎕TNUMS`](tnums.md) |Thread Numbers               |Constant|
|[`⎕TPOOL`](tpool.md) |Token Pool          |Monadic function|
|[`⎕TPUT`](tput.md)  |Put Tokens          |Ambivalent function|
|[`⎕TRACE`](query-trace.md)  |Query Trace vector|Monadic function|
|[`⎕TRACE`](set-trace.md)  |Set Trace vector  |Dyadic function|
|[`⎕TRAP`](trap.md)     |Event Trap                                      |Variable|
|[`⎕TREQ`](treq.md)  |Token Requests      |Monadic function|
|[`⎕TS`](ts.md)      |Timestamp                                          |Constant|
|[`⎕TSYNC`](tsync.md) |Wait for Threads to Terminate|Monadic function|
|[`⎕UCS`](ucs.md)  |Unicode Convert                                      |Ambivalent function|
|[`⎕USING`](using.md)|Microsoft .NET Search Path                              |Variable|
|[`⎕VFI`](vfi.md)  |Verify and Fix numeric                               |Ambivalent function|
|[`⎕VGET`](vget.md)     |Value Get    |Ambivalent function|
|[`⎕VR`](vr.md)     |Vector Representation   |Monadic function|
|[`⎕VSET`](vset.md)     |Value Set    |Ambivalent function|
|[`⎕WA`](wa.md)    |Workspace Available      |Constant|
|[`⎕WC`](wc.md)    |Create GUI object          |Ambivalent function|
|[`⎕WG`](wg.md)    |Get GUI object properties  |Ambivalent function|
|[`⎕WN`](wn.md)    |Query GUI object Names     |Ambivalent function|
|[`⎕WS`](ws.md)    |Set GUI object properties  |Ambivalent function|
|[`⎕WSID`](wsid.md)  |Workspace Identification|Variable|
|[`⎕WX`](wx.md)    |Expose GUI property names  |Variable|
|[`⎕XML`](xml.md)  |XML Convert                                          |Ambivalent function|
|[`⎕XSI`](xsi.md)   |Extended State Indicator |Constant|
|[`⎕XT`](query-external-variable.md)   |Query External variable  |Monadic function|
|[`⎕XT`](set-external-variable.md)   |Associate External variable|Dyadic function|
