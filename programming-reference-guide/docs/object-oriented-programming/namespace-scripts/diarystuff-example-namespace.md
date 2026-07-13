---
search:
  exclude: true
---

# DiaryStuff Example Namespace

```apl
:Namespace DiaryStuff
:Using System
    
    :Class DiaryEntry
        :Field Public When
        :Field Public What
        ∇ Make(ymdhm wot)
          :Access Public
          :Implements Constructor
          When What←(⎕NEW DateTime(6↑5↑ymdhm))wot
          ⎕DF⍕When What
        ∇
        ∇ Make0
          :Access Public
          :Implements Constructor
          When What←⎕NULL''
        ∇
    :EndClass ⍝ DiaryEntry
```

```apl
    :Class Diary
        :Field Private entries←0⍴⎕NEW DiaryEntry
        ∇ R←Add(ymdhm wot)
          :Access Public
          R←⎕NEW DiaryEntry(ymdhm wot)
          entries,←R
        ∇
        ∇ R←DoingOn ymd;X
          :Access Public
          X←,(↑entries.When.(Year Month Day))^.=3 1⍴3↑ymd
          R←X/entries
        ∇
        ∇ R←Remove ymdhm;X
          :Access Public
          :If R←∨/X←entries.When=⎕NEW DateTime(6↑5↑ymdhm)
              entries←(~X)/entries
          :EndIf
        ∇
        :Property Numbered Default Entry
            ∇ R←Shape
              R←⍴entries
            ∇
            ∇ R←Get arg
              R←arg.Indexers⊃entries
            ∇
            ∇ Set arg
              entries[arg.Indexers]←arg.NewValue
            ∇
        :EndProperty
    :EndClass ⍝ Diary
    
:EndNamespace
```
