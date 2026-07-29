# <span>CEFVersion</span> <span>Property</span>

**Description**

CEFVersion is a read-only property that reports the version of the [Chromium Embedded Framework (CEF)](https://en.wikipedia.org/wiki/Chromium_Embedded_Framework) that is being used. This information is primarily used for debugging and support.

It is a 10-element vector containing the following:

|Index |Description                                                                             ||
|------|----------------------------------------------------------------------------------|------|
|`[1]` |Formatted CEF release number. This is the primary identifier for a version of CEF.      ||
|`[2]` |CEF major version.                                                                      ||
|`[3]` |Commit number.                                                                          ||
|`[4]` |Chromium version number.                                                                ||
|`[5]` |Chromium version number.                                                          |&nbsp;|
|`[6]` |Chromium version number.                                                          |&nbsp;|
|`[7]` |Chromium version number.                                                          |&nbsp;|
|`[8]` |GIT Hashes                                                                        |&nbsp;|
|`[9]` |GIT Hashes                                                                        |&nbsp;|
|`[10]`|GIT Hashes                                                                        |&nbsp;|

**Application**

Objects: [HTMLRenderer](../objects/htmlrenderer.md)
