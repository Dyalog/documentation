---
search:
  exclude: true
---

# GolfCourse Class

```apl

    :Class GolfCourse
        :Field Public Code←¯1
        :Field Public Name←''
        
        ∇ ctor args
          :Implements Constructor
          :Access Public Instance
          Code Name←args
          ⎕DF Name,'(',(⍕Code),')'
        ∇
    
    :EndClass
    
```
