# Lexical Name Scope

When an inner (nested) dfn refers to a name, the interpreter searches for it by looking outwards through enclosing dfns, rather than searching back along the state indicator. This regime, which is more appropriate for nested functions, is said to employ **lexical scope** instead of APL's usual **dynamic scope**.  This distinction becomes apparent only if a call is made to a function defined at an outer level. For the more usual inward calls, the two systems are indistinguishable.

For example, in the following function, variable `type` is defined both within `which` itself and within the inner function `fn1`. When `fn1` calls outward to `fn2` and `fn2` refers to `type`, it finds the outer one (with value `'lexical'`) rather than the one defined in `fn1`:
```apl
      which←{
 
          type←'lexical' 
    
          fn1←{        
              type←'dynamic'
              fn2 ⍵
          }
    
          fn2←{    
              type ⍵ 
          }
    
          fn1 ⍵
      }
                     
      which'scope'
 lexical  scope
```
