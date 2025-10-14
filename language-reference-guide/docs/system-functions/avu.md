<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AVU AVU
</div>






<h1 class="heading"><span class="name">Atomic Vector - Unicode</span> <span class="command">⎕AVU</span></h1>



`⎕AVU` specifies the contents of the atomic vector, `⎕AV`, and is used to translate data between Unicode and non-Unicode character formats when required, for example when:

- Unicode Edition loads or copies a Classic Edition workspace or a workspace saved by a Version prior to Version 12.0.
- Unicode Edition reads character data from a non-Unicode component file, or receives data type 82 from a TCP socket.
- Unicode Edition writes data to a non-Unicode component file
- Unicode Edition reads or writes data from or to a Native File using conversion code 82.
- Classic Edition loads or copies a Unicode Edition workspace
- Classic Edition reads character data from a Unicode component file, or receives data type 80, 160, or 320 from a TCP socket.
- Classic Edition writes data to a Unicode component file.


`⎕AVU` is an integer vector with 256 elements, containing the Unicode code points which define the characters in `⎕AV`. `⎕AVU` has Namespace scope.

## Note


In Versions of Dyalog prior to Version 12.0 and in the Classic Edition, a character is stored internally as an index into the atomic vector, `⎕AV`. When a character is displayed or printed, the index in `⎕AV` is translated to a number in the range 0-255 which represents the index of the character in an Extended ASCII font. This mapping is done by the Output Translate Table which is user-configurable. Note that although ASCII fonts typically all contain the same symbols in the range 0-127, there are a number of different Extended ASCII font layouts, including proprietary APL fonts, which provide different symbols in positions 128-255. The actual symbol that appears on the screen or on the printed page is therefore a function of the Output Translate Table and the font in use. Classic Edition provides two different fonts (and thus two different `⎕AV` layouts) for use with the Development Environment, named *Dyalog Std* (with APL underscores) and *Dyalog Alt* (without APL underscores).



The default value of `⎕AVU` corresponds to the use of the **Dyalog Alt** Output Translate Table and font in the Classic Edition or in earlier versions of Dyalog APL.
```apl
      2 13⍴⎕AVU[97+⍳26]
193 194 195 199 200 202 203 204 205 206 207 208 210
211 212 213 217 218 219 221 254 227 236 240 242 245
      ⎕UCS 2 13⍴⎕AVU[97+⍳26]
ÁÂÃÇÈÊËÌÍÎÏÐÒ
ÓÔÕÙÚÛÝþãìðòõ
```



`⎕AVU` can be localised, in order to make it straightforward to write access functions which receive or read data from systems with varying atomic vectors. If you have been using Dyalog Alt for most things but have some older code which uses underscores, you can bring this code together in the same workspace and have it all look "as it should" by using the Alt and Std definitions for `⎕AVU` as you copy each part of the code into the same Unicode Edition workspace.
```apl
      )COPY avu.dws Std.⎕AVU
C:\Program Files\Dyalog\Dyalog APL 12.0 Unicode\ws\avu saved Thu Dec 06 11:24:32 2007
 
      2 13⍴⎕AVU[97+⍳26]
9398 9399 9400 9401 9402 9403 9404 9405 9406 9407 9408 9409 9410
9411 9412 9413 9414 9415 9416 9417 9418 9419 9420 9421 9422 9423
       ⎕UCS 2 13⍴⎕AVU[97+⍳26]
ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂ
ⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ
```

!!! Hint "Hints and Recommendations"
    The majority of Unicode fonts display APL's underscored alphabet as a circled alphabet instead. Unicode does not contain the underscored letters as distinct glyphs; Dyalog APL maps these characters to the Unicode positions for the circled alphabet, and provides APL fonts (such as APL385 Unicode) that display them as underscores. To avoid confusion, Dyalog Ltd recommends that you remove underscored characters from your APL application at your earliest convenience.

## Rules for Conversion on Import


When the Unicode Edition imports APL objects from a non-Unicode source, function comments and character data of type 82 are converted to Unicode. When the Classic Edition imports APL objects from a Unicode source, this translation is performed in reverse.


If the objects are imported from a Version 12.0 (or later) workspace (that is, from a workspace that contains its own value of `⎕AVU`) the value of `#.⎕AVU` (the value of `⎕AVU` in the root) in the *source* workspace is used. Otherwise, such as when APL objects are imported from a pre-Version 12 workspace, from a component file, or from a TCP socket, the local value of `⎕AVU` in the *target* workspace is used.


## Rules for Conversion on Export


When the Unicode Edition exports APL objects to a non-Unicode destination, such as a non-Unicode Component File or non-Unicode TCPSocket Object, function comments (in `⎕OR`s) and character data of type 82 are converted to `⎕AV` indices using the local value of `⎕AVU`.


When the Classic Edition exports APL objects to a Unicode destination, such as a Unicode Component File or Unicode TCPSocket Object, function comments (in `⎕OR`s) and character data of type 82 are converted to Unicode using the local value of `⎕AVU`.


In all cases, if a character to be translated is not defined in `⎕AVU`, a `TRANSLATION ERROR` (event number 92) will be signalled.




