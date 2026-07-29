# Legal Names

APL objects may be given names. A name may be any sequence of characters, starting with a non-numeric character, selected from the following:

| --- |
| `ABCDEFGHIJKLMNOPQRSTUVWXYZ_` |
| `abcdefghijklmnopqrstuvwxyz` |
| `ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝß` |
| `àáâãäåæçèéêëìíîïðñòóôõöøùúûüþ` |
| `0123456789` |
| `∆⍙` |
| `ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ` |

Note that using a standard Unicode font (rather than APL385 Unicode used in the table above), the last row above would appear as the circled alphabet, Ⓐ to Ⓩ.

**Examples**

| Legal | Illegal |
| --- | --- |
| `THIS∆IS∆A∆NAME` | `BAD NAME` |
| `X1233` | `3+21` |
| `SALES` | `S!H|PRICE` |
| `pjb_1` | `1_pjb` |
