# Distributed Functions

Namespace ref array expansion syntax applies to functions too.
```apl
      JOHN.PLOT←{↑⍵⍴¨'⎕'}
      JOHN.PLOT ⍳10
⎕
⎕⎕
⎕⎕⎕
⎕⎕⎕⎕
⎕⎕⎕⎕⎕
⎕⎕⎕⎕⎕⎕
⎕⎕⎕⎕⎕⎕⎕
⎕⎕⎕⎕⎕⎕⎕⎕
⎕⎕⎕⎕⎕⎕⎕⎕⎕
⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕
 
      PAUL.PLOT←{(⍵,¨1)⍴¨'⎕'}
      PAUL.PLOT ⍳10
 ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
    ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
       ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
          ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
             ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
                ⎕  ⎕  ⎕  ⎕  ⎕
                   ⎕  ⎕  ⎕  ⎕
                      ⎕  ⎕  ⎕
                         ⎕  ⎕
                            ⎕
 
      EMP.PLOT⊂⍳10  ⍝ (temporary vector of functions)
 ⎕            ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
 ⎕⎕              ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
 ⎕⎕⎕                ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
 ⎕⎕⎕⎕                  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
 ⎕⎕⎕⎕⎕                    ⎕  ⎕  ⎕  ⎕  ⎕  ⎕
 ⎕⎕⎕⎕⎕⎕                      ⎕  ⎕  ⎕  ⎕  ⎕
 ⎕⎕⎕⎕⎕⎕⎕                        ⎕  ⎕  ⎕  ⎕
 ⎕⎕⎕⎕⎕⎕⎕⎕                          ⎕  ⎕  ⎕
 ⎕⎕⎕⎕⎕⎕⎕⎕⎕                            ⎕  ⎕
 ⎕⎕⎕⎕⎕⎕⎕⎕⎕⎕                              ⎕

```

```apl
      (x y).⎕NL 2 3               ⍝ x:vars, y:fns
 varx  funy
 
      (x y).⎕NL⊂2 3               ⍝ x&y: vars&fns
 funx  funy
 varx  vary
 
      (x y).(⎕NL¨)⊂2 3           ⍝ x&y: separate vars&fns
  varx  funx    vary  funy
 
      'v'(x y).⎕NL 2 3            ⍝ x:v-vars, y:v-fns
  varx
 
      'vf'(x y).⎕NL 2 3           ⍝ x:v-vars, y:f-fns
  varx  funy
                                  ⍝ x:v-vars&fns,
      'vf'(x y).⎕NL⊂2 3           ⍝ y:f-vars&fns
  varx  funy
 
      x.⎕NL 2 3                   ⍝ depth 0 ref
funx
varx
 
      (x y).⎕NL⊂2 3               ⍝ depth 1 refs
 funx  funy
 varx  vary
 
      ((u v)(x y)).⎕NL⊂⊂2 3       ⍝ depth 2 refs
  funu  funv    funx  funy
  varu  varv    varx  vary
 
      (1 2)3 4(w(x y)z).+1 2(3 4) ⍝ arg distribution.
 2 3  5 5  7 8
```
