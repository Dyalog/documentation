---
search:
  exclude: true
---

# :While Statement

```
 
       |
       :While bexp
       |
       .-------.
       |       |
       |       andor
       |       |
       |<------'
       |
       code
       |
       .---------------.
       |               |
       :End[While]     :Until bexp
       |               |
       |               .-------.
       |               |       |
       |               |       andor
       |               |       |
       |               |<------'
       |               |
       |<--------------'
       |
```
