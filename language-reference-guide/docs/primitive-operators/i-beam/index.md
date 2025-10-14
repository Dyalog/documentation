<div style="display: none;">
  ⌶
</div>

<h1 class="heading"><span class="name">I-Beam</span> <span class="command">R←{X}(A⌶)Y</span></h1>

I-Beam is a monadic operator that provides a range of system-related services.

!!! Warning "Warning"
    Any service provided using an I-beam should be considered as experimental and subject to change – without notice – from one release to the next. Any use of I&#8209;beams in applications should, therefore, be carefully isolated in cover-functions that can be adjusted if necessary.

`A` is an integer that specifies the type of operation to be performed – see the table below.

`X` (optionally, depends on `A`) and `Y` are arrays that supply further information about what is to be done and to what.

`R` is the result.

When attempting to use the I-beam operator with an unsupported operation value `A`, one of three different error messages will be reported:

- Invalid I-Beam function selection
- I-Beam function A has been withdrawn
- I-Beam function A is not supported by this interpreter

This allows the user to distinguish between operation values that have never been used, those that have been used in earlier versions but are no longer included in the current version, and those that are valid in other editions or on other platforms.

Key to restrictions in the following table:

- AIX: AIX only
- LiW: Linux/Windows only
- WF: Microsoft .NET Framework only
- WIN: Microsoft Windows only
- X: AIX/Linux/macOS only
- 64U: 64-bit Unicode only


|`A`      |Derived Function                                                                      |Restrictions |
|-------|--------------------------------------------------------------------------------------|------|
|`8`    |[Inverted Table Index-of](./inverted-table-index-of.md)                               |&nbsp;|
|`13`   |[Log Use of Deprecated Features](./log-use-of-deprecated-features.md)                 |&nbsp;|
|`43`   |[Monadic Operator Generator](./monadic-operator-generator.md)                         |&nbsp;|
|`85`   |[Execute Expression](./execute-expression.md)                                         |&nbsp;|
|`109`  |[Log File for Deprecations](./log-file-for-deprecations.md)                           |&nbsp;|
|`120`  |[Generate UUID](./generate-uuid.md)                                                   |&nbsp;|
|`127`  |[Overwrite Free Pockets](./overwrite-free-pockets.md)                                 |&nbsp;|
|`180`  |[Canonical Representation](./canonical-representation.md)                             |&nbsp;|
|`181`  |[Unsqueezed Type](./unsqueezed-type.md)                                               |&nbsp;|
|`200`  |[Syntax Colouring](./syntax-colouring.md)                                             |&nbsp;|
|`201`  |[Syntax Colour Tokens](./syntax-colour-tokens.md)                                     |&nbsp;|
|`219`  |[Compress/Decompress Vector of Short Integers](./compress-decompress-vector-of-short-integers.md)|&nbsp;|
|`220`  |[Serialise/Deserialise Array](./serialise-deserialise-array.md)                                   |&nbsp;|
|`400`  |[Compiler Control](./compiler-control.md)                                             |&nbsp;|
|`600`  |[Disable Traps](./disable-traps.md)                                                     |&nbsp;|
|`739`  |[Temporary Directory](./temporary-directory.md)                                       |&nbsp;|
|`900`  |[Called Monadically?](./called-monadically.md)                                         |&nbsp;|
|`950`  |[List Loaded Libraries](./list-loaded-libraries.md)                                   |&nbsp;|
|`1010` |[Set Shell Script Debug Options](./set-shell-script-debug-options.md)                 |&nbsp;|
|`1111` |[Number of Threads](./number-of-threads.md)                                           |&nbsp;|
|`1112` |[Parallel Execution Threshold](./parallel-execution-threshold.md)                     |&nbsp;|
|`1159` |[Update Function Time and User Stamp](./update-function-time-and-user-stamp.md)       |&nbsp;|
|`1200` |[Format Date-time](./format-datetime.md)                                              |&nbsp;|
|`1302` |[aplcore Parameters](./aplcore-parameters.md)                                         |&nbsp;|
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
|`2022` |[Flush Session Caption](./flush-session-caption.md)                                   |WIN     |
|`2023` |[Close all Windows](./close-all-windows.md)                                           |&nbsp;|
|`2035` |[Set Dyalog Pixel Type](./set-dyalog-pixel-type.md)                                   |WIN     |
|`2041` |[Override COM Default Value](./override-com-default-value.md)                         |WIN     |
|`2100` |[Export to Memory](./export-to-memory.md)                                             |WIN     |
|`2101` |[Close .NET AppDomain](./close-net-appdomain.md)                                      |WF    |
|`2250` |[Verify .NET Interface](./verify-net-interface.md)                                    |&nbsp;|
|`2400` |[Set Workspace Save Options](./set-workspace-save-options.md)                         |&nbsp;|
|`2401` |[Expose Root Properties](./expose-root-properties.md)                                 |&nbsp;|
|`2501` |[Discard Thread on Exit](./discard-thread-on-exit.md)                                 |WIN     |
|`2502` |[Discard Parked Threads](./discard-parked-threads.md)                                 |WIN     |
|`2503` |[Mark Thread as Uninterruptible](./mark-thread-as-uninterruptible.md)                 |&nbsp;|
|`2520` |[Use Separate Thread For .NET](./use-separate-thread-for-net.md)                      |WF    |
|`2704` |[Continue Autosave](./continue-autosave.md)                                           |&nbsp;|
|`3002` |[Disable Component Checksum Validation](./disable-component-checksum-validation.md)   |&nbsp;|
|`3012` |[Enable Compression of Large Components](./enable-compression-of-large-components.md) |&nbsp;|
|`3500` |[Send Text to Ride-embedded Browser](./send-text-to-ride-embedded-browser.md)         |&nbsp;|
|`3501` |[Connected to Ride?](./connected-to-ride.md)                                          |&nbsp;|
|`3502` |[Manage Ride Connections](./manage-ride-connections.md)                               |&nbsp;|
|`3535` |[Scan For Deprecated Files](./scan-for-deprecated-files.md)                           |&nbsp;|
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
|`8659` |[List Shared Code Files/Attached Names](./list-shared-code-files-attached-names.md)   |64U   |
|`8666` |[Attach/Assimilate/Detach Shared Code Files](./attach-assimilate-detach-shared-code-files.md)    |64U   |
|`8667` |[Save Shared Code Files](./save-shared-code-files.md)                                 |64U   |
|`16808`|[Sample Probability Distribution](./sample-probability-distribution.md)               |LiW|
|`50100`|[Line Count](./line-count.md)                                                         |&nbsp;|