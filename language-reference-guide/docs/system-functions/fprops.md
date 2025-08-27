<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FPROPS FPROPS
</div>

<h1 class="heading"><span class="name">File Properties</span> <span class="command">R←X ⎕FPROPS Y</span></h1>

## Access Code 1 (to read) or 8192 (to change properties)

`⎕FPROPS` reports and sets the properties of a component file.

`Y` must be a simple integer scalar or  1 or 2-element vector containing the file tie number followed by an optional passnumber. If the passnumber is omitted, it is assumed to be 0.

`X` must be a simple character scalar or vector containing one or more valid Identifiers listed in the table below, or a 2-element nested vector which specifies an Identifier and a (new) value for that property. To set new values for more than one property, `X` must be is a vector of 2-element vectors, each of which contains an Identifier and a (new) value for that property.

If the left argument is a simple character array, the result `R` contains the current values for the properties identified by `X`. If the left argument is nested, the result `R` contains the previous values for the properties identified by `X`.


|Identifier|Property|Description / Legal Values|
|---|---|---|
|`S`|File Size (read only)|32 = Small-span Component Files (<4GB)<br>64 = Large-span Component Files|
|`E`|Endian-ness (read only)|0 = Little-endian<br>1 = Big-endian|
|`U`|Unicode|0 = Characters will be written as type 82 arrays<br>1 = Characters will be written as Unicode arrays|
|`J`|Journaling|0 = Disable Journaling<br>1 = Enable *APL crash proof* Journaling<br>2 = Enable *System crash proof* Journaling; repair needed on recovery<br>3 = Enable full *System crash proof* Journaling|
|`C`|Checksum|0 = Disable checksum<br>1 = Enable checksum|
|`Z`|Compression|0 = Disable compression<br>1 = Enable compression|




The default properties for a newly created file are as follows:

- S = 64
- U = 1 (in Unicode Edition) or 0 (in Classic Edition)
- J = 1
- C = 1
- Z = 0
- E depends upon the computer architecture.



Note that the defaults for C and J can be overridden by calling `⎕FCREATE` via the Variant operator `⍠`. For further information, see [File Properties](fcreate.md).

# Journaling Levels


**Level 1** journaling (APL crash-proof) automatically protects a component file from damage in the event of abnormal termination of the APL process. The file state will be implicitly committed between updates and an incomplete update will automatically be rolled forward or back when the file is re-tied. In the event of an operating system crash the file may be more seriously damaged. If checksum was also enabled it may be repaired using `⎕FCHK` but some components may be restored to a previous state or not restored at all.


**Level 2** journaling (system crash-proof – repair needed on recovery) extends level 1 by ensuring that a component file is fully repairable using `⎕FCHK` with no component loss in the event of an operating system failure. If an update was in progress when the system crashed the affected component will be rolled back to the previous state. Tying and modifying such a file without first running `⎕FCHK` may however render it un-repairable.


**Level 3** journaling (system crash-proof) extends level 2 by protecting a component file from damage in the event of abnormal termination of the APL process and also the operating system. Rollback of an incomplete update will be automatic and no explicit repair will be needed.


Enabling journaling on a component file will reduce performance of file updates; higher journaling levels have a greater impact.


Journaling levels 2 and 3 cannot be set unless the checksum option is also enabled.


The default level of journaling may be changed using the **APL_FCREATE_PROPS_J** parameter (see *Dyalog for Microsoft Windows Installation and Configuration Guide: Configuration Parameters* for more information).


## Checksum Option


The checksum option is enabled by default. This  enables a damaged file to be repaired using `⎕FCHK`. It will however  reduce the performance of file updates slightly and result in larger component files. The default may be changed using the **APL_FCREATE_PROPS_C** parameter (See User Guide).


Enabling the checksum option on an existing non-empty component file will result in all previously written components without a checksum  being check-summed and converted. This operation which will take place when `⎕FPROPS` is changed, may not therefore be instantaneous.



Journaling and checksum settings may be changed at any time a file is exclusively tied.

<h2 class="example">Example</h2>
```apl

      tn←'myfile64' ⎕FCREATE 0
      'SEUJ' ⎕FPROPS tn
64 0 1 0

```



The following expression disables Unicode and switches Journaling on. The function returns the previous settings:
```apl

      ('U' 0)('J' 1) ⎕FPROPS tn
1 0
```




Note that to set the value of just a single property, the following two statements are equivalent:
```apl

      'J' 1 ⎕FPROPS tn
      (,⊂'J' 1) ⎕FPROPS tn
```



Properties may be read by a task with `⎕FREAD` permission (access code 1), and set by a task with `⎕FSTAC` access (8192). To set the value of the Journaling property, the file must be exclusively tied.

## Recommendation


It is recommended that all component files are protected by  a minimum of Level 1 Journalling and have Checksum enabled.


Unprotected files  should only be used:

- for temporary work files where speed is paramount and integrity a secondary issue
- or where compatibility with Versions of Dyalog prior to Version 12.0 is required



This recommendation is given for the following reasons:

- Unprotected files are easily damaged by abnormal termination of the interpreter
- They cannot be repaired using `⎕FCHK`
- They do not support `⎕FHIST`
- They are not well supported by the Dyalog File Server (DFS)
- They do not support compression of components
- Additional features added in future may not be supported


## Compression Option


Components are compressed using the *LZ4* compressor which delivers a medium level of compression, but is considered to be very fast compared to other algorithms.


Compression is intended to deliver a performance gain reading and writing large components on fast computers with slow (for example, network) file access. Conversely, on a slow computer with fast file access compression may actually reduce read/write performance. For this reason it is optional at the component level.


The default for the `'Z'` property is 0 which means no compression; 1 means compression. When written, components are compressed or not according to the current value of the `'Z'` property. Changing this property does not change any components already in the file.


A component file may therefore contain a mixture of normal and compressed components. Note that only the data in file components are compressed, the file access matrix and other header information is not compressed.


When read, compressed components are decompressed regardless of the value of the `'Z'` property.


An exclusive tie is not needed to change the file property.


Compression is not supported for files in which both Journalling and Checksum are disabled.

!!! Info "Information"
    Component files that have both journalling and checksum properties set to `0` have been deprecated; from Dyalog v21.0, component files with this combination of properties will be read-only. Dyalog Ltd recommends using `⎕FPROPS` to convert any such files to have different properties. For information on how to identify component files that have both journalling and checksum properties set to `0` in your existing codebase, see the [Release Notes](../../../release-notes/announcements/deprecated-functionality/). Be aware that converting from non-checksummed components to checksummed components can take a significant amount of time.
