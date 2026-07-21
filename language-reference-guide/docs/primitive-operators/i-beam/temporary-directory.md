---
search:
  boost: 2
---

<!-- Hidden search keywords -->
<div style="display: none;">
  739⌶
</div>

# <span>Temporary Directory</span> `R←739⌶Y`{{key}}

Returns the name of a system temporary directory suitable for user files, as a character vector. The name reported does not include a trailing directory separator

`Y` is 0.

The result `R` is a character vector.

## Example (Windows)
```apl
      739⌶0
C:/Users/Pete/AppData/Local/Temp

```

## Example (non-Windows)
```apl
      739⌶0
/tmp
		
```

!!! Info "Information"
    `739⌶` is deprecated, and is scheduled for removal in a future release. For information on how to identify code that calls `739⌶` see the [Release Notes](https://docs.dyalog.com/21.0/release-notes/announcements/deprecated-functionality/#identifying-deprecated-functionality-in-executed-code). 
    
    The functionality provided by `739⌶0` is now provided by `⎕SYSTEM.Directories.Temp` – this returns an equivalent result, but uses the operating system's preferred directory separator.  

