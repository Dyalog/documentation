<h1 class="heading"><span class="name">Announcements</span></h1>

## Supported Versions

The supported versions of Dyalog are now versions 19.0, 18.2, 18.0, and 17.1. Version 17.0 and earlier versions are no longer supported.

## Dyalog on macOS

Dyalog v19.0 is natively available for both Intel and ARM-based Macs. Dyalog v19.0 is expected to be the last version that will be available for Intel-based Macs.

## Performance Issue with Namespaces

We have identified a namespace performance issue which is especially noticeable with JSON Import. We have a fix planned for the next release of Dyalog. In the meantime, there is an easy workaround.

For further information, see [Performance Warning](https://help.dyalog.com/19.0/index.htm#Language/System%20Functions/json.htm)

## Hash and Lookup Tables

In the next major version of Dyalog the performance of the set functions will be improved. The new code will involve increasing the amount of workspace allocated to the internal tables used by these functions. These tables are described using  the terms *hash table* and *lookup table*. The latter refers to internal tables that do not require hashing.

For more information, see [Search Functions and Hash Tables](https://help.dyalog.com/19.0/index.htm#Language/Defined%20Functions%20and%20Operators/Search%20Functions%20and%20Hash.htm#SearchFunctionsAndHashTables) and [Hash Array](https://help.dyalog.com/19.0/index.htm#Language/I%20Beam%20Functions/Hash%20Array.htm#Hash_Array).

The proposed size increase may potentially cause `WS FULL` errors or may change the frequency of workspace compactions.

To allow the user to evaluate the effect of this future change on their applications, two new I-beam functions have been provided. These functions increase the space allocated to the internal tables for the sole purpose of testing these potential effects. The new I-beams may affect performance either directly or by triggering a change of algorithm, but should not be used for that sole purpose since performance degradation in some cases cannot be excluded. See [Hash Table Size](../language-reference-changes/hash-table-size.md) and [Lookup Table Size](../language-reference-changes/lookup-table-size.md).

When the next major release is published, it is anticipated that few, if any, users will notice negative effects from changing the internal table sizes. Rather, they will benefit from the improved performance that will result.

## PCRE2 Upgrade

Dyalog  uses the PCRE 8.x library to support regular expression searches in `⎕R`, `⎕S` and in the IDE. PCRE 8 is widely used, but future development and maintenance of PCRE will be based upon the newer PCRE2 (PCRE 10.x) library. Dyalog intends to switch to  the new library  in a forthcoming release.

## Chromium Embedded Framework (CEF)

Version 19.0 is supplied with CEF version 121 on all supported platforms.

## Forthcoming Removal of 819⌶

The system function `⎕C` was introduced in Dyalog v18.0, at which point we announced that `819⌶` was deprecated. `819⌶` is still present in Dyalog v19.0, but it will be removed from the next version.

There is a temporary new configuration parameter: **DYALOG_IBEAM819**.

If **DYALOG_IBEAM819** is set to 0, use of `819⌶` will  signal an error and the DMX.Message will state that it has been withdrawn; in other words, the behaviour is what you would get with the next release. This is to help users prepare for its removal now if they want to.

`819⌶` will only operate if either **DYALOG_IBEAM819** is not set, or **DYALOG_IBEAM819** is set to 1.

## Forthcoming Removal of Array Editor

Dyalog v19.0 is expected to be the last version that will include David Liebtag's Array Editor.

## Forthcoming Removal of Syncfusion from Microsoft Windows installation images

Dyalog v19.0 is expected to be the last version that will include the Syncfusion library of WPF controls; Dyalog Ltd will cease to offer support for the Syncfusion controls from the end of September 2024.

The Syncfusion licence provided with Dyalog v19.0 will continue to be valid for use with Dyalog v19.0 beyond this date, but later versions of Dyalog will not include a Syncfusion licence.

## Removal of RConnect (R Interface)

RConnect (the R interface) and the  R Interface Guide, are no longer included with Dyalog. Instead, Dyalog Ltd recommends  RSconnect - R connection for Dyalog APL with Rserve, which can be obtained from [ https://github.com/kimmolinna/rsconnect](https://github.com/kimmolinna/rsconnect).
