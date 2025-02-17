<h1 class="heading"><span class="name">I-Beam</span> <span class="command">R←{X}(A⌶)Y</span></h1>

I-Beam is a monadic operator that provides a range of system related services.

!!! warning
    Although documentation is provided for I-Beam functions, any service provided using I-Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I-Beams in applications should therefore be carefully isolated in cover-functions that can be adjusted if necessary. See also: [RIDE and Experimental Features-related I-Beams](../the-i-beam-operator/supplementary-i-beam-functions.md).

`A` is an integer that specifies the type of operation to be performed  as shown in the table below. `Y` is an array that supplies further information about what is to be done.

`X` may or may not be required depending on `A`.

`R` is the result of the derived function.

When attempting to use  I-Beam with an unsupported operation value, `A`, one of three different error messages will be reported:

- Invalid I-Beam function selection
- I-Beam function xxx has been withdrawn
- I-Beam function xxx is not supported by this interpreter

This allows the user to distinguish between operation values that have never been used, those that have been used in earlier versions but are no longer included in the current version, and those
that are valid in other editions or on other platforms other than the current interpreter.


The column labelled *O/S* indicates if a function applies only on Windows (W), only on Windows .NET Framework, (WF), only under IBM AIX (AIX), or only on non-Windows (X) platforms.

|A      |Derived Function                                                                                           |O/S   |
|-------|-----------------------------------------------------------------------------------------------------------|------|
|`8`    |[Inverted Table Index-of](../the-i-beam-operator/inverted-table-index-of.md)                               |&nbsp;|
|`85`   |[Execute Expression](../the-i-beam-operator/execute-expression.md)                                         |&nbsp;|
|`127`  |[Overwrite Free Pockets](../the-i-beam-operator/overwrite-free-pockets.md)                                 |&nbsp;|
|`180`  |[Canonical Representation](../the-i-beam-operator/canonical-representation.md)                             |&nbsp;|
|`181`  |[Unsqueezed Type](../the-i-beam-operator/unsqueezed-type.md)                                               |&nbsp;|
|`200`  |[Syntax Colouring](../the-i-beam-operator/syntax-colouring.md)                                             |&nbsp;|
|`201`  |[Syntax Colour Tokens](../the-i-beam-operator/syntax-colour-tokens.md)                                     |&nbsp;|
|`219`  |[Compress/Decompress Vector of Short Integers](../the-i-beam-operator/compress-vector-of-short-integers.md)|&nbsp;|
|`220`  |[Serialise/Deserialise Array](../the-i-beam-operator/serialise-array.md)                                   |&nbsp;|
|`400`  |[Compiler Control](../the-i-beam-operator/compiler-control.md)                                             |&nbsp;|
|`600`  |[Trap Control](../the-i-beam-operator/trap-control.md)                                                     |&nbsp;|
|`739`  |[Temporary Directory](../the-i-beam-operator/temporary-directory.md)                                       |&nbsp;|
|`819`  |[Case Convert](../the-i-beam-operator/case-convert.md)                                                     |&nbsp;|
|`900`  |[Called Monadically](../the-i-beam-operator/called-monadically.md)                                         |&nbsp;|
|`950`  |[Loaded Libraries](../the-i-beam-operator/loaded-libraries.md)                                             |&nbsp;|
|`1010` |[Set Shell Script Debug Options](../the-i-beam-operator/set-shell-script-debug-options.md)                 |&nbsp;|
|`1111` |[Number of Threads](../the-i-beam-operator/number-of-threads.md)                                           |&nbsp;|
|`1112` |[Parallel Execution Threshold](../the-i-beam-operator/parallel-execution-threshold.md)                     |&nbsp;|
|`1159` |[Update Function Time and User Stamp](../the-i-beam-operator/update-function-timestamp.md)                 |&nbsp;|
|`1200` |[Format Date-time](../the-i-beam-operator/format-datetime.md)                                              |&nbsp;|
|`1302` |[Set aplcore Parameters](../the-i-beam-operator/set-aplcore-parameters.md)                                 |&nbsp;|
|`1500` |[Hash Array](../the-i-beam-operator/hash-array.md)                                                         |&nbsp;|
|`2000` |[Memory Manager Statistics](../the-i-beam-operator/memory-manager-statistics.md)                           |&nbsp;|
|`2002` |[Specify Workspace Available](../the-i-beam-operator/specify-workspace-available.md)                       |&nbsp;|
|`2007` |[Disable Global Triggers](../the-i-beam-operator/disable-global-triggers.md)                               |&nbsp;|
|`2010` |[Update DataTable](../the-i-beam-operator/update-datatable.md)                                             |WF    |
|`2011` |[Read DataTable](../the-i-beam-operator/read-datatable.md)                                                 |WF    |
|`2014` |[Remove Data Binding](../the-i-beam-operator/remove-data-binding.md)                                       |WF    |
|`2015` |[Create Data Binding Source](../the-i-beam-operator/create-data-binding-source.md)                         |WF    |
|`2016` |[Create .NET Delegate](../the-i-beam-operator/create-net-delegate.md)                                      |WF    |
|`2017` |[Identify .NET Type](../the-i-beam-operator/identify-net-type.md)                                          |WF    |
|`2022` |[Flush Session Caption](../the-i-beam-operator/flush-session-caption.md)                                   |W     |
|`2023` |[Close all Windows](../the-i-beam-operator/close-all-windows.md)                                           |&nbsp;|
|`2035` |[Set Dyalog Pixel Type](../the-i-beam-operator/set-dyalog-pixel-type.md)                                   |W     |
|`2041` |[Override COM Default Value](../the-i-beam-operator/override-com-default-value.md)                         |W     |
|`2100` |[Export to Memory](../the-i-beam-operator/export-to-memory.md)                                             |W     |
|`2101` |[Close .NET AppDomain](../the-i-beam-operator/close-net-appdomain.md)                                      |WF    |
|`2250` |[Verify .NET Interface](../the-i-beam-operator/verify-net-interface.md)                                    |&nbsp;|
|`2400` |[Set Workspace Save Options](../the-i-beam-operator/set-workspace-save-options.md)                         |&nbsp;|
|`2401` |[Expose Root Properties](../the-i-beam-operator/expose-root-properties.md)                                 |&nbsp;|
|`2501` |[Discard thread on exit](../the-i-beam-operator/discard-thread-on-exit.md)                                 |W     |
|`2502` |[Discard parked threads](../the-i-beam-operator/discard-parked-threads.md)                                 |W     |
|`2503` |[Mark Thread as Uninterruptible](../the-i-beam-operator/mark-thread-as-uninterruptible.md)                 |&nbsp;|
|`2520` |[Use Separate Thread For .NET](../the-i-beam-operator/use-separate-thread-for-net.md)                      |WF    |
|`2704` |[Continue Autosave](../the-i-beam-operator/continue-autosave.md)                                           |&nbsp;|
|`3002` |[Disable Component Checksum Validation](../the-i-beam-operator/disable-component-checksum-validation.md)   |&nbsp;|
|`3012` |[Enable Compression of Large Components](../the-i-beam-operator/enable-compression-of-large-components.md) |&nbsp;|
|`3500` |[Send Text to RIDE-embedded Browser](../the-i-beam-operator/send-text-to-ride-embedded-browser.md)         |&nbsp;|
|`3501` |[Connected to the RIDE](../the-i-beam-operator/connected-to-the-ride.md)                                   |&nbsp;|
|`3502` |[Manage RIDE Connections](../the-i-beam-operator/manage-ride-connections.md)                               |&nbsp;|
|`4000` |[Fork New Task](../the-i-beam-operator/fork-new-task.md)                                                   |AIX   |
|`4001` |[Change User](../the-i-beam-operator/change-user.md)                                                       |X     |
|`4002` |[Reap Forked Tasks](../the-i-beam-operator/reap-forked-tasks.md)                                           |AIX   |
|`4007` |[Signal Counts](../the-i-beam-operator/signal-counts.md)                                                   |X     |
|`5171` |[Discard Source Information](../the-i-beam-operator/discard-source-information.md)                         |&nbsp;|
|`5172` |[Discard Source Code](../the-i-beam-operator/discard-source-code.md)                                       |&nbsp;|
|`5176` |[List Loaded Files](../the-i-beam-operator/list-loaded-files.md)                                           |&nbsp;|
|`5177` |[List Loaded File Objects](../the-i-beam-operator/list-loaded-file-objects.md)                             |&nbsp;|
|`5178` |[Remove Loaded File Object Info](../the-i-beam-operator/remove-loaded-file-object-info.md)                 |&nbsp;|
|`5179` |[Loaded File Object Info](../the-i-beam-operator/loaded-file-object-info.md)                               |&nbsp;|
|`7162` |[JSON Translate Name](../the-i-beam-operator/json-translate-name.md)                                       |&nbsp;|
|`8373` |[Shell Process Control](../the-i-beam-operator/shell-process-control.md)
|`8415` |[Singular Value Decomposition](../the-i-beam-operator/singular-value-decomposition.md)                     |&nbsp;|
|`9468` |[Hash Table Size](../the-i-beam-operator/hash-table-size.md)                                               |&nbsp;|
|`9469` |[Lookup Table Size](../the-i-beam-operator/lookup-table-size.md)                                           |&nbsp;|
|`16808`|[Sample Probability Distribution](../the-i-beam-operator/sample-probability-distribution.md)               |&nbsp;|
|`50100`|[Line Count](../the-i-beam-operator/line-count.md)                                                         |&nbsp;|
