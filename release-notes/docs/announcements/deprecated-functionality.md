# Deprecated Functionality

Over time, certain functionality (such as language elements, development environment features, or supplied samples or tools) can become obsolete or cease to be useful. There are many reasons why this might happen. For example:

* a superior alternative has been introduced.<br />For example, `⎕UCS` has superseded `⎕TC` (which generates only the newline, backspace, and tabstop characters).
* the feature was originally implemented as an I-beam but has since been superseded by a formal addition to Dyalog APL.<br />For example, `⎕JSON` replaced `7159⌶`.
* the feature is associated with hardware or technology that is itself becoming obsolete.<br />For example, 32-bit processes and address spaces limited to 4GB in size.

In these circumstances, the feature is classified as _deprecated_. This means that it is unlikely to be developed or extended further, and its use in new development work is discouraged. Some deprecated features remain for backwards compatibility reasons, but some are later removed in a pre-announced Dyalog version.

## Deprecated Functionality Scheduled for Removal

If removing a deprecated feature is considered to be sufficiently significant, Dyalog Ltd will enable the ability to identify where this feature exists in a given codebase.

Deprecated functionality can be identified either when it is encountered in code that is executed or by scanning a directory for deprecated file types.

### Identifying Deprecated Functionality in Executed Code

Dyalog can be configured to log use of a deprecated feature when it is encountered. Logging must be configured and enabled/disabled in each APL process – information about logging is not retained.  

To enable logging of deprecated features:

1. Specify the name of the file into which the JSON5 log messages will be written (using [`109⌶`](../../../language-reference-guide/primitive-operators/i-beam/log-file-for-deprecations/) with a right argument of `0`). By default, the file is created in the current working directory; if you do not have write permission for the current working directory, you will also need to include a path. If a filename is not set, then all logging information will be silently discarded.
2. Specify which deprecated features should be logged (using [`13⌶`](../../../language-reference-guide/primitive-operators/i-beam/log-use-of-deprecated-features/) with a right argument of the names identifying the deprecated features of interest).

For Dyalog v20.0, the following names are valid:

* `J0C0` – component files that have both journalling (J) and checksum (C) properties set to `0`
* `S32` – small-span component files
* `⎕XT` – external variables

In addition, there are two reserved names than can be used:  

* `All` – enables logging for all valid names
* `None` – disable all logging

Each time `13⌶` is called, the new list of features replaces the existing list. 

<p class="example">Example</p>

```apl
⍝ Specify the name of the log file
      'C:/Users/fiona/deprecated_log.txt'(109⌶)0
	  
⍝ Select the features to log
      13⌶ 'J0C0' 'S32'  
```

After logging has been enabled, every subsequent use of the specified deprecated features is logged. Each line in the log file contains a complete JSON5 object, which includes a description of the deprecated feature and the SI Stack at the point it was called. The log file can be examined using any text editor or from within a Dyalog Session. For example:

```apl
      log_entries←0⎕JSON⍠'Dialect' 'JSON5'¨⊃⎕NGET 'C:/Users/fiona/deprecated_log.txt' 1
	  '⋄'⎕ED'log_entries'
```
If an error occurs when writing to the log file, further logging is suspended. The log file status can be queried at any time by calling `109⌶` with a right argument of `1`; the result is a numeric status code (`0` indicates no error) and a character vector describing the error that was encountered (empty if no error). For example:

```apl
      (109⌶)1
┌─┬┐
│0││
└─┴┘
```
or:
```apl
      (109⌶)1
┌─┬──────────────────────────────────────────┐
│3│The system cannot find the path specified.│
└─┴──────────────────────────────────────────┘
```

### Identifying Files Pertaining to Deprecated Functionality

A directory can be scanned for deprecated functionality using [`3535⌶`](../../../language-reference-guide/primitive-operators/i-beam/scan-for-deprecated-files/) with a right argument of the directory to be scanned. If the left argument is set to `1`, sub-directories will also be scanned. The names of any files that pertain to deprecated functionality are returned, with labels specifying the reason for identification.

For Dyalog v20.0, the following labels can be returned: 

| Label | Meaning |
|-------|---------|
| `J0C0`  | File is a component file with both the Journalling (J) and Checksum (C) properties set to `0`
| `OLDWS` | File is a workspace saved by Dyalog v12.0 or earlier
| `S32`   | File is a small span component file
| `⎕XT`   | File is an external variable file
| `?`     | File could not be read and its content is unknown

<p class="example">Example</p>

```apl
      1(3535⌶)'.'
 ./J0C0.dcf             J0C0
 ./ws2000.dws           OLDWS
 ./subdir/S32J0C0.dcf   J0C0  S32
```