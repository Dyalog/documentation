<h1 class="heading"><span class="name">Deprecated Features</span></h1>

Over time, certain features supplied by Dyalog - be they part of the language, functionality within the development environments, or the supplied samples or Tools - may become obsolete or simply not as useful as they once were. There are many reasons why this may happen; some examples are:

* A superior alternative has been introduced - as an example, `⎕TC` (terminal control) allows the generation of certain Unicode characters, but `⎕UCS` was later added which provides this functionality too - and more.
* It was originally experimental and has now been formally integragted into the product - such as the I-Beam function which was obsoleted by `⎕JSON` which replaced it.
* It is associated with hardware or technology which is itself becoming obsolete - such as 32-bit processes and address spaces limited to 4GB in size.

When this happens the feature becomes **deprecated**, meaning it may not be developed or extended further and its use in new developments may be discouraged, and in some cases Dyalog may even announce plans to formally remove them at a specified point in the future - for announcements about any features to which this currently applies, see the [Release Notes](xxxLINKxxx).

## Identifying uses of deprecated features

If the planned removal features is announced is important to be able to identify *if* and *where* they are still being used within applications so that appropriate preparations can be made. To do this, Dyalog can be configured to log their use in a file.

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

If the result of [`109⌶`](../../../language-reference-guide/the-i-beam-operator/log-file-for-deprecations)does not have a 0 in the first element, an error occurred and the second element will include a description of what it was.

Entries written to the logfile will be lines of complete JSON5 text. They can be simply examined using `]open` or by loading the file into an editor, or they may be read and reformatted using `⎕NGET` and `⎕JSON`, for example:

```apl
      (⎕JSON⍠('Dialect' 'JSON5')('Compact' 0))⍣2¨⊃⎕NGET 'logfile.txt' 1
```

The log entries will include a description of the deprecated feature being used and the SIstack at the time.