<h1 class="heading"><span class="name">Configuring the Editor</span></h1>

The editor in non-GUI versions of Dyalog APL can be considered to have 5 separate functional columns.  Below is the contents of the editor window, which shows the namespace ns, which has two traditional-style functions and one dfn.  The statement `5 ⎕STOP 'ns.fn1'` has been run too:
```

[0]         :Namespace ns
[1]  [0]   ├    ∇ r←fn1 a
[2]  [1]   ├      :If a=1
[3]  [2]   │          r←1
[4]  [3]   │      :Else
[5]  [4]   ├          :If today≡'Friday'
[6]  [5]  ○│              r←2
[7]  [6]   ├          :EndIf
[8]  [7]   ├      :EndIf
[9]  [8]   ├    ∇
[10]
[11] [0]        dfn←{⍺+⍵}
[12]
[13] [0]   ├    ∇ r←a fn2 w
[14] [1]   │      r←a+w
[15] [2]   ├    ∇
[16]        :EndNamespace
```

This is formed of 5 separate columns:
```

┌────┬───┬───┬──┬────────────────────────────┐
│C1  │C2 │C3 │C4│C5                          │
├────┼───┼───┼──┼────────────────────────────┤
│[0] │   │   │  │:Namespace ns               │
│[1] │[0]│   │├ │    ∇ r←fn1 a               │
│[2] │[1]│   │├ │      :If a=1               │
│[3] │[2]│   ││ │          r←1               │
│[4] │[3]│   ││ │      :Else                 │
│[5] │[4]│   │├ │          :If today≡'Friday'│
│[6] │[5]│  ○││ │              r←2           │
│[7] │[6]│   │├ │          :EndIf            │
│[8] │[7]│   │├ │      :EndIf                │
│[9] │[8]│   │├ │    ∇                       │
│[10]│   │   │  │                            │
│[11]│[0]│   │  │    dfn←{⍺+⍵}               │
│[12]│   │   │  │                            │
│[13]│[0]│   │├ │    ∇ r←a fn2 w             │
│[14]│[1]│   ││ │      r←a+w                 │
│[15]│[2]│   │├ │    ∇                       │
│[16]│   │   │  │:EndNamespace               │
└────┴───┴───┴──┴────────────────────────────┘
```

|Functional Column|Value (see below)|Purpose                                                              |
|-----------------|-----------------|---------------------------------------------------------------------|
|C1               |4                |Line numbers for entire object                                       |
|C2               |64               |Line numbers for functions etc. within scripted namespaces           |
|C3               |2                |Trace/Stop points                                                    |
|C4               |8                |Control Structure Outlining                                          |
|C5               |16               |Text (or content)This value is ignored; this column is always present|

It is possible to control at startup time which of these columns are visible. By default, for all types of object, only the text column is visible; this can be overridden on a per-object basis by setting one or more of the EDITOR_COLUMNS_ variables listed in Table E5. The value of these variables is the sum of the values for each of the columns which are desired.

<h2 class="example">Examples</h2>

EDITOR_COLUMNS_NAMESPACE=94 shows all columns (the first example in this section)

Various values for EDITOR_COLUMNS_FUNCTION

|Value|Editor window appearance|
|-----|------------------------|
|0    |<pre> fn1 a<br /> :If a=1 <br/>     b←2<br /> :EndIf</pre>|
|22   |<pre>[0]   fn1 a<br />[1]   :If a=1 <br />[2] ○     b←2<br />[3]   :EndIf</pre>|
|26   |<pre>   fn1 a<br /> ├ :If a=1 <br />○│     b←2<br /> ├ :EndIf</pre>|
|30   |<pre>[0]    fn1 a<br />[1]  ├ :If a=1<br />[2] ○│     b←2<br />[3]  ├ :EndIf<br></pre>|

