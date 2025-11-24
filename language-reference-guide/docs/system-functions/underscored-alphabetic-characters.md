---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕ 
</div>






<h1 class="heading"><span class="name">Underscored Alphabetic Characters</span> <span class="command">R←⎕Ⓐ</span></h1>



`⎕Ⓐ` is a deprecated feature. Dyalog **strongly** recommends that you move away from the use of `⎕Ⓐ` and of the underscored alphabet itself, as these symbols now constitute the sole remaining non-standard use of characters in Dyalog applications.


In Versions of Dyalog APL prior to Version 11.0, `⎕Ⓐ` was a simple character vector, composed of the letters of the alphabet with underscores. If the Dyalog Alt font was in use, these symbols displayed as additional National Language characters.

## Version 10.1 and Earlier
```apl
      ⎕Ⓐ
ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ
```


For compatibility with previous versions of Dyalog APL, functions that contain references to `⎕Ⓐ` will continue to return characters with the same *index* in `⎕AV` as before. However, the display of `⎕Ⓐ` is now `⎕Á`, and the old underscored symbols appear as they did in previous Versions when the Dyalog Alt font was in use.

## Current Version
```apl
      ⎕Á
ÁÂÃÇÈÊËÌÍÎÏÐÒÓÔÕÙÚÛÝþãìðòõ
```



