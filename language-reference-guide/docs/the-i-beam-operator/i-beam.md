<h1 class="heading"><span class="name">I-Beam</span> <span class="command">R←{X}(A⌶)Y</span></h1>

I-Beam is a monadic operator that provides a range of system related services.

!!! warning 
    Although documentation is provided for I-Beam functions, any service provided using I-Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I-Beams in applications should therefore be carefully isolated in cover-functions that can be adjusted if necessary. See also: [Ride and Experimental Features-related I-Beams](./supplementary-i-beam-functions.md).

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


|A      |Derived Function                                                                      |O/S   |
|-------|--------------------------------------------------------------------------------------|------|
|`8`    |[Inverted Table Index-of](./inverted-table-index-of.md)                               |&nbsp;|
|`43`   |[Monadic Operator Generator](./monadic-operator-generator.md)                         |&nbsp;|
|`85`   |[Execute Expression](./execute-expression.md)                                         |&nbsp;|
|`127`  |[Overwrite Free Pockets](./overwrite-free-pockets.md)                                 |&nbsp;|
|`180`  |[Canonical Representation](./canonical-representation.md)                             |&nbsp;|
|`181`  |[Unsqueezed Type](./unsqueezed-type.md)                                               |&nbsp;|
|`200`  |[Syntax Colouring](./syntax-colouring.md)                                             |&nbsp;|
|`201`  |[Syntax Colour Tokens](./syntax-colour-tokens.md)                                     |&nbsp;|
|`219`  |[Compress/Decompress Vector of Short Integers](./compress-vector-of-short-integers.md)|&nbsp;|
|`220`  |[Serialise/Deserialise Array](./serialise-array.md)                                   |&nbsp;|
|`400`  |[Compiler Control](./compiler-control.md)                                             |&nbsp;|
|`600`  |[Trap Control](./trap-control.md)                                                     |&nbsp;|
|`739`  |[Temporary Directory](./temporary-directory.md)                                       |&nbsp;|
|`819`  |[Case Convert](./case-convert.md)                                                     |&nbsp;|
|`900`  |[Called Monadically](./called-monadically.md)                                         |&nbsp;|
|`950`  |[Loaded Libraries](./loaded-libraries.md)                                             |&nbsp;|
|`1010` |[Set Shell Script Debug Options](./set-shell-script-debug-options.md)                 |&nbsp;|
|`1111` |[Number of Threads](./number-of-threads.md)                                           |&nbsp;|
|`1112` |[Parallel Execution Threshold](./parallel-execution-threshold.md)                     |&nbsp;|
|`1159` |[Update Function Time and User Stamp](./update-function-timestamp.md)                 |&nbsp;|
|`1200` |[Format Date-time](./format-datetime.md)                                              |&nbsp;|
|`1302` |[Set aplcore Parameters](./set-aplcore-parameters.md)                                 |&nbsp;|
|`1500` |[Hash Array](./hash-array.md)                                                         |&nbsp;|
|`2000` |[Memory Manager Statistics](./memory-manager-statistics.md)                           |&nbsp;|
|`2002` |[Specify Workspace Available](./specify-workspace-available.md)                       |&nbsp;|
|`2007` |[Disable Global Triggers](./disable-global-triggers.md)                               |&nbsp;|
|`2010` |[Update DataTable](./update-datatable.md)                                             |WF    |
|`2011` |[Read DataTable](./read-datatable.md)                                                 |WF    |
|`2014` |[Remove Data Binding](./remove-data-binding.md)                                       |WF    |
|`2015` |[Create Data Binding Source](./create-data-binding-source.md)                         |WF    |
|`2016` |[Create .NET Delegate](./create-net-delegate.md)                                      |WF    |
|`2017` |[Identify .NET Type](./identify-net-type.md)                                          |WF    |
|`2022` |[Flush Session Caption](./flush-session-caption.md)                                   |W     |
|`2023` |[Close all Windows](./close-all-windows.md)                                           |&nbsp;|
|`2035` |[Set Dyalog Pixel Type](./set-dyalog-pixel-type.md)                                   |W     |
|`2041` |[Override COM Default Value](./override-com-default-value.md)                         |W     |
|`2100` |[Export to Memory](./export-to-memory.md)                                             |W     |
|`2101` |[Close .NET AppDomain](./close-net-appdomain.md)                                      |WF    |
|`2250` |[Verify .NET Interface](./verify-net-interface.md)                                    |&nbsp;|
|`2400` |[Set Workspace Save Options](./set-workspace-save-options.md)                         |&nbsp;|
|`2401` |[Expose Root Properties](./expose-root-properties.md)                                 |&nbsp;|
|`2501` |[Discard thread on exit](./discard-thread-on-exit.md)                                 |W     |
|`2502` |[Discard parked threads](./discard-parked-threads.md)                                 |W     |
|`2503` |[Mark Thread as Uninterruptible](./mark-thread-as-uninterruptible.md)                 |&nbsp;|
|`2520` |[Use Separate Thread For .NET](./use-separate-thread-for-net.md)                      |WF    |
|`2704` |[Continue Autosave](./continue-autosave.md)                                           |&nbsp;|
|`3002` |[Disable Component Checksum Validation](./disable-component-checksum-validation.md)   |&nbsp;|
|`3012` |[Enable Compression of Large Components](./enable-compression-of-large-components.md) |&nbsp;|
|`3500` |[Send Text to Ride-embedded Browser](./send-text-to-ride-embedded-browser.md)         |&nbsp;|
|`3501` |[Connected to Ride](./connected-to-the-ride.md)                                       |&nbsp;|
|`3502` |[Manage Ride Connections](./manage-ride-connections.md)                               |&nbsp;|
|`4000` |[Fork New Task](./fork-new-task.md)                                                   |AIX   |
|`4001` |[Change User](./change-user.md)                                                       |X     |
|`4002` |[Reap Forked Tasks](./reap-forked-tasks.md)                                           |AIX   |
|`4007` |[Signal Counts](./signal-counts.md)                                                   |X     |
|`5171` |[Discard Source Information](./discard-source-information.md)                         |&nbsp;|
|`5172` |[Discard Source Code](./discard-source-code.md)                                       |&nbsp;|
|`5176` |[List Loaded Files](./list-loaded-files.md)                                           |&nbsp;|
|`5177` |[List Loaded File Objects](./list-loaded-file-objects.md)                             |&nbsp;|
|`5178` |[Remove Loaded File Object Info](./remove-loaded-file-object-info.md)                 |&nbsp;|
|`5179` |[Loaded File Object Info](./loaded-file-object-info.md)                               |&nbsp;|
|`5581` |[Unicode Normalisation](./unicode-normalisation.md)                                   |&nbsp;|
|`7162` |[JSON Translate Name](./json-translate-name.md)                                       |&nbsp;|
|`8373` |[Shell Process Control](./shell-process-control.md)                                   |&nbsp;|
|`8415` |[Singular Value Decomposition](./singular-value-decomposition.md)                     |&nbsp;|
|`9468` |[Hash Table Size](./hash-table-size.md)                                               |&nbsp;|
|`9469` |[Lookup Table Size](./lookup-table-size.md)                                           |&nbsp;|
|`16808`|[Sample Probability Distribution](./sample-probability-distribution.md)               |&nbsp;|
|`50100`|[Line Count](./line-count.md)                                                         |&nbsp;|



