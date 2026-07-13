---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NPARTS NPARTS
</div>






# <span>File Name Parts</span> `R←{X} ⎕NPARTS Y`{{key}}



Splits a file or directory name into its constituent parts.


`Y` is a character vector or scalar containing a single name, or a vector of character vectors containing zero or more names. Names must conform to the file-naming rules of the host Operating System.


The file(s) need not exist; indeed this system function makes no attempt to identify or locate it/them.



The optional left-argument `X` specifies whether or not the name or names specified by `Y` are *normalised* before being processed. The default value 0 means no normalisation; 1 means normalise as follows:

- Pathnames are made absolute.
- On Windows, all "\" directory separators are changed to "/".
- The resultant name is simplified by removing extraneous directory separators etc. On Windows, this includes resolving occurrences of "." and ".."  within the name. On non-Windows platforms single "." are removed. Note that ".." and symbolic links interact differently on Windows to other platforms; on other platforms they cannot be removed without reference to the file system itself and are left in place. 


If `Y` is a scalar or vector, the result `R` is a 3-element vector of character vectors as follows:


|-----|-----------|
|`[1]`|*path*     |
|`[2]`|*base name*|
|`[3]`|*extension*|


The *path* identifies the directory in which the file exists.


The *base name* is the name of the file stripped of its path and extension, if any.


The *extension* is the file extension including the leading ".".


If `Y` is a vector of character vectors, `R` is a vector of 3-element character vectors and is the same length as `Y`.

<h2 class="example">Examples</h2>
```apl
      ⎕CMD 'CD'⍝ Current working directory
c:\Users\Pete
			
      1 ⎕NPARTS 'α'
┌→─────────────────────────┐
│ ┌→─────────────┐ ┌→┐ ┌⊖┐ │
│ │c:/Users/Pete/│ │α│ │ │ │
│ └──────────────┘ └─┘ └─┘ │
└∊─────────────────────────┘
      1 ⎕NPARTS '\Users\Pete\Documents\dyalog.zip'
┌→───────────────────────────────────────────┐
│ ┌→───────────────────────┐ ┌→─────┐ ┌→───┐ │
│ │C:/Users/Pete/Documents/│ │dyalog│ │.zip│ │
│ └────────────────────────┘ └──────┘ └────┘ │
└∊───────────────────────────────────────────┘

      ⊃'.'⎕WG'APLVersion'
AIX-64
      1 ⎕NPARTS'/home/andys/./..'
┌────────────┬──┬┐
│/home/andys/│..││
└────────────┴──┴┘

      1 ⎕NPARTS '.' '..'
┌────────────────┬───────┐
│┌───┬─────────┬┐│┌───┬┬┐│
││i:/│Documents││││i:/││││
│└───┴─────────┴┘│└───┴┴┘│
└────────────────┴───────┘		

```



Note that `⊃1 ⎕NPARTS ''` returns the current working directory.
```apl
      ⊃1 ⎕NPARTS ''
┌→─────────────┐
│c:/Users/Pete/│
└──────────────┘

```



