---
search:
  boost: 2
---

# <span>Terminal Control</span> `(⎕ML)`

`⎕TC` is a deprecated feature and is replaced by `⎕UCS` (see below).

`⎕TC` is a simple three element vector.  If `⎕ML<3` this is ordered as follows:

|--------|---------|
|`⎕TC[1]`|Backspace|
|`⎕TC[2]`|Linefeed |
|`⎕TC[3]`|Newline  |

`⎕TC≡⎕AV[1+⍳3]` for `⎕ML<3`.

If `⎕ML≥3`the order of the elements of `⎕TC` is instead compatible with IBM's APL2:

|--------|---------|
|`⎕TC[1]`|Backspace|
|`⎕TC[2]`|Newline  |
|`⎕TC[3]`|Linefeed |

Elements of `⎕TC` beyond 3 are not defined but are reserved.

With the introduction of `⎕UCS` in Dyalog v12.0, the use of `⎕TC` is discouraged and it is strongly recommended that you generate control characters using `⎕UCS` instead. This recommendation holds true even if you continue to use the Classic Edition.

|Control Character|Old                           |New      |
|-----------------|------------------------------|---------|
|Backspace        |`⎕TC[1]`                      |`⎕UCS 8` |
|Linefeed         |`⎕TC[2] (⎕ML<3)`<br>`⎕TC[3] (⎕ML≥3)`|`⎕UCS 10`|
|Newline          |`⎕TC[3] (⎕ML<3)`<br>`⎕TC[2] (⎕ML≥3)`|`⎕UCS 13`|

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ML ML
</div>
