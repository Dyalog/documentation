---
search:
  boost: 2
---
# Introduction

Dyalog includes a collection of built-in facilities that provide various services related to both the APL and the external environment. They have distinguished case-insensitive names beginning with the `⎕` symbol, and are implicitly available in a clear workspace. Collectively, these  facilities are referred to as **System Functions** but they are variously implemented as constants, variables, functions, operators, and namespaces.

!!! Hint "Hints and Recommendations"
    Dyalog can extend any of these facilities by, for example, adding extra elements, rows, or columns to a result, so code should take this possibility into account.

|Name                   |Description                |Form|
|-----------------------|---------------------------|----|
|[`⎕`](evaluated-input-output.md)      |Evaluated Input/Output|Variable|
|[`⍞`](character-input-output.md)      |Character Input/Output|Variable|
|[`⎕A`](a.md)   |Alphabetic uppercase characters|Variable|
|[`⎕Ⓐ` or `⎕Á`](underscored-alphabetic-characters.md) |Underscored Alphabetic Characters|Constant|
|[`⎕AI`](ai.md)      |Account Information        |Constant|
|[`⎕AN`](an.md)      |Account Name               |Constant|
|[`⎕ARBIN`](arbin.md) |Arbitrary Input       |Dyadic function|
|[`⎕ARBOUT`](arbout.md)|Arbitrary Output      |Dyadic function|
|[`⎕AT`](at-monadic.md)|Object Attributes       |Monadic function   |
|[`⎕AT`](at-dyadic.md)|Object Attributes for APL2|Dyadic function    |
|[`⎕ATX`](atx.md)   |Extended Attributes     |Dyadic function|
|[`⎕AV`](av.md)   |Atomic Vector              |Constant|
|[`⎕AVU`](avu.md)  |Atomic Vector - Unicode         |Variable|
|[`⎕BASE`](base.md)     |Base Class   |Reference|
|[`⎕C`](c-monadic.md)|Case Fold                                              |Monadic function   |
|[`⎕C`](c-dyadic.md)|Case Map                                               |Dyadic function    |
|[`⎕CLASS`](class-monadic.md)|Class Hierarchy|Monadic function|
|[`⎕CLASS`](class-dyadic.md)|Get Class/Interface Implementation|Dyadic function |
|[`⎕CLEAR`](clear.md)|Clear workspace (WS)       |Constant|
|[`⎕CMD`](execute-windows-command.md)  |Execute the Windows Command Processor or another program|Monadic function|
|[`⎕CMD`](start-windows-auxiliary-processor.md)  |Start a Windows Auxiliary Processor|Dyadic function|
|[`⎕CR`](cr.md)     |Canonical Representation|Monadic function|
|[`⎕CS`](cs.md)       |Change Space   |Monadic function|
|[`⎕CSV`](csv-monadic.md)|Import CSV                                           |Monadic function   |
|[`⎕CSV`](csv-dyadic.md)|Export CSV                                           |Dyadic function    |
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
|[`⎕ED`](ed-monadic.md)|Edit Objects            |Monadic function   |
|[`⎕ED`](ed-dyadic.md)|Edit Objects with Type  |Dyadic function    |
|[`⎕EM`](em.md)       |Event Messages                                  |Monadic function|
|[`⎕EN`](en.md)       |Event Number          |Constant|
|[`⎕EX`](ex.md)     |Expunge objects         |Monadic function|
|[`⎕EX`](ex.md)     |Expunge objects         |Monadic function|
|[`⎕EXCEPTION`](exception.md)|Reports the most recent Microsoft .NET Exception|Reference|
|[`⎕EXPORT`](export-monadic.md)|Query Export Type    |Monadic function   |
|[`⎕EXPORT`](export-dyadic.md)|Set Export Type      |Dyadic function    |
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
|[`⎕FIX`](fix-monadic.md)|Define Namespace|Monadic function   |
|[`⎕FIX`](fix-dyadic.md)|Define Objects|Dyadic function    |
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
|[`⎕FRESIZE`](fresize-monadic.md)|Compact Component File     |Monadic function   |
|[`⎕FRESIZE`](fresize-dyadic.md)|Resize Component File      |Dyadic function    |
|[`⎕FSIZE`](fsize.md)   |File Size                  |Monadic function|
|[`⎕FSTAC`](fstac.md)   |Set File Access matrix     |Dyadic function|
|[`⎕FSTIE`](fstie.md)   |Share-Tie a File           |Dyadic function|
|[`⎕FTIE`](ftie.md)    |Tie a File exclusively     |Dyadic function|
|[`⎕FUNTIE`](funtie.md)  |Untie Files                |Monadic function|
|[`⎕FX`](fx.md)     |Fix definition          |Monadic function|
|[`⎕INSTANCES`](instances.md)|Instances|Monadic function|
|[`⎕IO`](io.md) |Index Origin                 |Variable|
|[`⎕JSON`](json-monadic.md)|Auto-convert JSON                                   |Monadic function   |
|[`⎕JSON`](json-dyadic.md)|Convert JSON                                        |Dyadic function    |
|[`⎕KL`](kl.md)   |Key Labels                       |Monadic function|
|[`⎕LC`](lc.md)    |Line Count               |Constant|
|[`⎕LOAD`](load.md)  |Load a saved WS            |Function|
|[`⎕LOCK`](lock-monadic.md)|Lock Function         |Monadic function   |
|[`⎕LOCK`](lock-dyadic.md)|Custom Lock Function  |Dyadic function    |
|[`⎕LX`](lx.md)    |Latent Expression        |Variable|
|[`⎕MAP`](map-monadic.md)|Map Array File                                          |Monadic function   |
|[`⎕MAP`](map-dyadic.md)|Map Raw Data File                                       |Dyadic function    |
|[`⎕MKDIR`](mkdir-monadic.md)|Create Directory                                             |Monadic function   |
|[`⎕MKDIR`](mkdir-dyadic.md)|Custom Create Directory                                      |Dyadic function    |
|[`⎕ML`](ml.md) |Migration Level              |Variable|
|[`⎕MONITOR`](query-monitor.md)|Monitor query|Monadic function|
|[`⎕MONITOR`](set-monitor.md)|Monitor set    |Dyadic function|
|[`⎕NA`](na-monadic.md)|Associate External Function with Own Name               |Monadic function   |
|[`⎕NA`](na-dyadic.md)|Associate External Function with Custom Name            |Dyadic function    |
|[`⎕NAPPEND`](nappend.md) |Append to File                                               |Dyadic function|
|[`⎕NC`](nc.md)    |Name Classification      |Monadic function|
|[`⎕NCOPY`](ncopy.md)   |Copy files and directories                                   |Dyadic function|
|[`⎕NCREATE`](ncreate.md) |Create a File                                                |Dyadic function|
|[`⎕NDELETE`](ndelete-monadic.md)|Delete Native File                                           |Monadic function   |
|[`⎕NDELETE`](ndelete-dyadic.md)|Custom Delete Native File                                    |Dyadic function    |
|[`⎕NERASE`](nerase.md)  |Erase a File                                                 |Dyadic function|
|[`⎕NEW`](new.md)      |New Instance  |Monadic function|
|[`⎕NEXISTS`](nexists.md) |Discover whether or not a file or directory exists           |Monadic function|
|[`⎕NGET`](nget-monadic.md)|Get Text File Content                                        |Monadic function   |
|[`⎕NGET`](nget-dyadic.md)|Decode Text File Content                                     |Dyadic function    |
|[`⎕NINFO`](ninfo-monadic.md)|Native File Name                                                   |Monadic function   |
|[`⎕NINFO`](ninfo-dyadic.md)|Native File Information                                            |Dyadic function    |
|[`⎕NL`](nl-monadic.md)|List Object Names        |Monadic function|
|[`⎕NL`](nl-dyadic.md)|List Object Names with Filter|Dyadic function |
|[`⎕NLOCK`](nlock.md)   |Lock a region of a file                                      |Dyadic function|
|[`⎕NMOVE`](nmove.md)   |Move files and directories                                   |Dyadic function|
|[`⎕NNAMES`](nnames.md)  |Names of tied Files                                          |Constant|
|[`⎕NNUMS`](nnums.md)   |Tie Numbers of tied Files                                    |Constant|
|[`⎕NPARTS`](nparts-monadic.md)|File Name Parts                                              |Monadic function   |
|[`⎕NPARTS`](nparts-dyadic.md)|Normalised File Name Parts                                   |Dyadic function    |
|[`⎕NPUT`](nput.md)    |Write Text File                                              |Dyadic function|
|[`⎕NQ`](nq-monadic.md)|Enqueue Event              |Monadic function   |
|[`⎕NQ`](nq-dyadic.md)|Custom Enqueue Event       |Dyadic function    |
|[`⎕NR`](nr.md)     |Nested Representation   |Monadic function|
|[`⎕NREAD`](nread.md)   |Read from File                                               |Monadic function|
|[`⎕NRENAME`](nrename.md) |Rename a File                                                |Dyadic function|
|[`⎕NREPLACE`](nreplace.md)|Replace data on File                                         |Dyadic function|
|[`⎕NRESIZE`](nresize.md) |File Resize                                                  |Dyadic function|
|[`⎕NS`](ns-monadic.md)|Create/Clone Namespace|Monadic function   |
|[`⎕NS`](ns-dyadic.md)|Create/Clone Custom Namespaces|Dyadic function    |
|[`⎕NSI`](nsi.md)   |Namespace Indicator      |Constant|
|[`⎕NSIZE`](nsize.md)   |File Size                                                    |Monadic function|
|[`⎕NTIE`](ntie.md)    |Tie a File exclusively                                       |Dyadic function|
|[`⎕NULL`](null.md)|Null Item                       |Variable|
|[`⎕NUNTIE`](nuntie.md)  |Untie Files                                                  |Monadic function|
|[`⎕NXLATE`](nxlate-monadic.md)|Query Native File Translation Vector|Monadic function   |
|[`⎕NXLATE`](nxlate-dyadic.md)|Set Native File Translation Vector|Dyadic function    |
|[`⎕OFF`](off.md)    |End the session            |Constant|
|[`⎕OPT`](or.md)     |Variant            |Dyadic operator|
|[`⎕OR`](or.md)     |Object Representation   |Monadic function|
|[`⎕PATH`](path.md)  |Search Path            |Variable|
|[`⎕PFKEY`](pfkey-monadic.md)|Query Programmable Function Key|Monadic function   |
|[`⎕PFKEY`](pfkey-dyadic.md)|Program Function Key          |Dyadic function    |
|[`⎕PP`](pp.md) |Print Precision              |Variable|
|[`⎕PROFILE`](profile-monadic.md)|Profile Code       |Monadic function   |
|[`⎕PROFILE`](profile-dyadic.md)|Filter Profile Data|Dyadic function    |
|[`⎕R`](r.md)    |Replace                                                 |Dyadic operator|
|[`⎕REFS`](refs.md)   |Local References      |Monadic function|
|[`⎕RL`](rl.md) |Random Link                  |Variable|
|[`⎕RSI`](rsi.md)   |Space Indicator          |Constant|
|[`⎕RTL`](rtl.md)   |Response Time Limit   |Variable|
|[`⎕S`](s.md)    |Search                                                  |Dyadic operator|
|[`⎕SAVE`](save.md)  |Save the active WS         |Function|
|[`⎕SD`](sd.md)   |Screen Dimensions                |Constant|
|[`⎕SE`](se.md)   |Session Namespace                |Reference|
|[`⎕SH`](execute-unix-command.md)   |Execute a UNIX command or another program|Monadic function|
|[`⎕SH`](start-unix-auxiliary-processor.md)   |Start a UNIX Auxiliary Processor|Dyadic function|
|[`⎕SHADOW`](shadow.md)|Shadow names             |Monadic function|
|[`⎕SHADOW`](shadow.md)|Shadow names         |Monadic function|
|[`⎕SHELL`](shell.md)|Execute a shell command or another program              |Monadic function|
|[`⎕SI`](si.md)    |State Indicator          |Constant|
|[`⎕SIGNAL`](signal-monadic.md)|Signal Default/Custom Event                     |Monadic function   |
|[`⎕SIGNAL`](signal-dyadic.md)|Signal Event with Custom Name                   |Dyadic function    |
|[`⎕SIZE`](size.md)  |Size of objects        |Monadic function|
|[`⎕SM`](sm.md)   |Screen Map                       |Variable|
|[`⎕SR`](sr-monadic.md)|Screen Read                      |Monadic function   |
|[`⎕SR`](sr-dyadic.md)|Custom Screen Read               |Dyadic function    |
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
|[`⎕SYSTEM`](system.md)|System Information|Reference|
|[`⎕TALLOC`](talloc-monadic.md)|Allocate New Token Range|Monadic function   |
|[`⎕TALLOC`](talloc-dyadic.md)|Allocate Existing Token Range|Dyadic function    |
|[`⎕TC`](tc.md)   |Terminal Control           |Constant|
|[`⎕TCNUMS`](tcnums.md) |Thread Child Numbers         |Monadic function|
|[`⎕TGET`](tget-monadic.md)|Get Tokens          |Monadic function   |
|[`⎕TGET`](tget-dyadic.md)|Get Tokens with Timeout|Dyadic function    |
|[`⎕THIS`](this.md)     |Self-reference|Reference|
|[`⎕TID`](tid.md)   |Current Thread Identity      |Constant|
|[`⎕TKILL`](tkill-monadic.md)|Kill Threads        |Monadic function   |
|[`⎕TKILL`](tkill-dyadic.md)|Kill Threads and Descendants|Dyadic function    |
|[`⎕TNAME`](tname.md) |Current Thread Name          |Variable|
|[`⎕TNUMS`](tnums.md) |Thread Numbers               |Constant|
|[`⎕TPOOL`](tpool.md) |Token Pool          |Monadic function|
|[`⎕TPUT`](tput-monadic.md)|Put Tokens          |Monadic function   |
|[`⎕TPUT`](tput-dyadic.md)|Put Tokens with Values|Dyadic function    |
|[`⎕TRACE`](query-trace.md)  |Query Trace vector|Monadic function|
|[`⎕TRACE`](set-trace.md)  |Set Trace vector  |Dyadic function|
|[`⎕TRAP`](trap.md)     |Event Trap                                      |Variable|
|[`⎕TREQ`](treq.md)  |Token Requests      |Monadic function|
|[`⎕TS`](ts.md)      |Timestamp                                          |Constant|
|[`⎕TSYNC`](tsync.md) |Wait for Threads to Terminate|Monadic function|
|[`⎕UCS`](ucs-monadic.md)|Convert Unicode Code Point                           |Monadic function   |
|[`⎕UCS`](ucs-dyadic.md)|Convert Unicode Representation                       |Dyadic function    |
|[`⎕USING`](using.md)|Microsoft .NET Search Path                              |Variable|
|[`⎕VFI`](vfi-monadic.md)|Parse Numbers                                        |Monadic function   |
|[`⎕VFI`](vfi-dyadic.md)|Parse Numbers with Separators                        |Dyadic function    |
|[`⎕VGET`](vget-monadic.md)|Get Value from Current Namespace|Monadic function   |
|[`⎕VGET`](vget-dyadic.md)|Get Value from Namespace|Dyadic function    |
|[`⎕VR`](vr.md)     |Vector Representation   |Monadic function|
|[`⎕VSET`](vset-monadic.md)|Set Value in Current Namespace|Monadic function   |
|[`⎕VSET`](vset-dyadic.md)|Set Value in Namespace|Dyadic function    |
|[`⎕WA`](wa.md)    |Workspace Available      |Constant|
|[`⎕WC`](wc-monadic.md)|Convert Namespace to GUI Object|Monadic function   |
|[`⎕WC`](wc-dyadic.md)|Create GUI Object          |Dyadic function    |
|[`⎕WG`](wg-monadic.md)|Get Properties of Current GUI Object|Monadic function   |
|[`⎕WG`](wg-dyadic.md)|Get Properties of GUI Object|Dyadic function    |
|[`⎕WN`](wn-monadic.md)|Get GUI Child Names in Current Object|Monadic function   |
|[`⎕WN`](wn-dyadic.md)|Get GUI Child Names in Parent Object|Dyadic function    |
|[`⎕WS`](ws-monadic.md)|Set Properties of Current GUI Object|Monadic function   |
|[`⎕WS`](ws-dyadic.md)|Set Properties of GUI Object|Dyadic function    |
|[`⎕WSID`](wsid.md)  |Workspace Identification|Variable|
|[`⎕WX`](wx.md)    |Expose GUI property names  |Variable|
|[`⎕XML`](xml-monadic.md)|Convert XML                                          |Monadic function   |
|[`⎕XML`](xml-dyadic.md)|Custom Convert XML                                   |Dyadic function    |
|[`⎕XSI`](xsi.md)   |Extended State Indicator |Constant|
|[`⎕XT`](query-external-variable.md)   |Query External variable  |Monadic function|
|[`⎕XT`](set-external-variable.md)   |Associate External variable|Dyadic function|
