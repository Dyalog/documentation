<h1 class="heading"><span class="name">Deprecated Features</span></h1>

Over time, certain features supplied by Dyalog - for example, part of Dyalog APL (the language), functionality within the development environments or one of the supplied samples or Tools - may become obsolete or simply not as useful as it once was. There are many reasons why this may happen, including, but not limited to:

* A superior alternative has been introduced - for example, `⎕TC` (terminal control) allows the generation of certain Unicode characters but this and more is possible using the later-introduced `⎕UCS`.
* The feature was originally experimental and has now been formally integrated - for example, `⎕JSON` now provides the functionality which was originally provided as an I-Beam function.
* The feature is associated with hardware or technology which is itself becoming obsolete - such as 32-bit processes limited to 4GB of memory.

When this happens, and a feature remains only for compatibility with previous versions, it becomes **deprecated** - meaning it is unlikely to be developed or extended further and its use in new developments is discouraged. This may or may not be formally stated - for example, the documentation for `⎕TC` explicitly says that it should not be used, whereas non-journaled non-checksummed (J0 C0) component files (which are less-well protected from data corruption than other formats) have largely disappeared because `⎕FCREATE` and `⎕FCOPY` have simply stopped creating them.

Deprecated features may remain in support for many releases and there may be no plans to ever remove that support. In some instances, however, deprecated features may reach the stage where there is no need or no ability to keep them, and at that point Dyalog may announce a plan to formally remove them at some specified point in the future. For announcements of any features which are deprecated and are currently planned to be removed in future, see the [Release Notes](xxxLINKxxx).

## Identifying uses of deprecated features

Applications which still use deprecated features will cease to work correctly when that feature is removed. It is therefore important to be able to identify *if* and *where* such features are used once plans for their removal are announced, so that appropriate preparations can be made. To facilitate this, Dyalog can log the use of language features, tools and samples which are deprecated and will be removed in future. I-Beam functions exist to control this logging capability.

!!! note
    Once logging is enabled it will remain so until disabled again or the interpreter exits. Logging does not automatically restart when an interpreter is restarted, nor is the log configuration stored in a saved workspace and resored on load.

To enable logging, first use [`109⌶`](../../../language-reference-guide/the-i-beam-operator/log-file-for-deprecations) to specify the file to which log messages should be written, for example:

```apl
      'logfile.txt'(109⌶)0
```

If this file already exists, new log messages will be appended to it.

Next, select which features should be logged using [`13⌶`](../../../language-reference-guide/the-i-beam-operator/deprecated-features). The names by which the features are identified are specified in the [Release Notes](LINK), but the name 'All' may be used to enable logging of all such features, viz:

```apl
      13⌶'All'
```

At this point, an application can be run and tested as normal.

Then, if desired, stop logging:

```apl
      13⌶'None'
```

and check that no errors occurred when writing to the logfile:

```apl
      (109⌶)1
┌─┬┐
│0││
└─┴┘
```

If the result of `109⌶` does not have a 0 in the first element, an error occurred and the second element will include a description of what it was.

Entries written to the logfile will be lines of complete JSON5 text. They can be simply examined using `]open` or by loading the file into an editor, or they may be read and reformatted using `⎕NGET` and `⎕JSON`, for example:

```apl
      (⎕JSON⍠('Dialect' 'JSON5')('Compact' 0))⍣2¨⊃⎕NGET 'logfile.txt' 1
```

The contents of the log entries will include a description of the deprecated feature being used and the SIstack at the time.