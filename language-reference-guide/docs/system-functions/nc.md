---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NC NC
</div>

# <span>Name Classification</span> `R←⎕NC Y`{{key}}

`Y` must be a simple  character scalar, vector, matrix, or vector of vectors that specifies a list of names. `R` is a simple numeric vector containing one element per name in `Y`. Each element of `R` is the name class of the active referent to the object named in `Y`.

If `Y` is **simple**, a name class may be:

|Name Class|Description                       |
|----------|----------------------------------|
|`¯1`      |invalid name                      |
|`0`       |undefined name                    |
|`1`       |Label                             |
|`2`       |Variable                          |
|`3`       |Function                          |
|`4`       |Operator                          |
|`8`       |Event                             |
|`9`       |Object (GUI, namespace, COM, .NET)|

If `Y` is **nested** a more precise analysis of name class is obtained whereby different types  are identified by a decimal extension. For example, defined functions have name class 3.1, dfns have name class 3.2, and so forth. The complete set of name classification is as follows:

|&nbsp;|Array (2)      |Function (3)        |Operator (4)        |Namespace (9)                           |
|------|---------------|--------------------|--------------------|----------------------------------------|
|n.1   |Variable       |Traditional         |Traditional         |Created by `⎕NS` , `)NS` or `:Namespace`|
|n.2   |Field          |dfn                 |dop                 |Instance                                |
|n.3   |Property       |Derived or Primitive|Derived or Primitive|&nbsp;                                  |
|n.4   |&nbsp;         |&nbsp;              |&nbsp;              |Class                                   |
|n.5   |&nbsp;         |&nbsp;              |&nbsp;              |Interface                               |
|n.6   |External Shared|External            |&nbsp;              |External Class                          |
|n.7   |&nbsp;         |&nbsp;              |&nbsp;              |External Interface                      |

In addition, values in `R` are negative to identify names of methods, properties and events that are inherited through the *class hierarchy* of the current class or instance.

## Variable (Name-Class 2.1)

Conventional APL arrays have name-class 2.1.
```apl
      NUM←88
      CHAR←'Hello World'
 
      ⎕NC ↑'NUM' 'CHAR'
2 2
 
      ⎕NC 'NUM' 'CHAR'
2.1 2.1
 
      'MYSPACE'⎕NS ''
      MYSPACE.VAR←10
      MYSPACE.⎕NC'VAR'
2
      MYSPACE.⎕NC⊂'VAR'
2.1
```

## Field (Name-Class 2.2)

Fields defined by APL Classes have name-class 2.2.
```apl
:Class nctest
    :Field Public pubFld
    :Field pvtFld
 
    ∇ r←NameClass x 
      :Access Public 
      r←⎕NC x 
    ∇ 
...
:EndClass ⍝ nctest       
 
      ncinst←⎕NEW nctest
```

The name-class of a Field, whether Public or Private, viewed from a Method that is executing within the Instance Space, is 2.2.
```apl
      ncinst.NameClass'pubFld' 'pvtFld'
2.2 2.2
```

Note that an internal Method sees both Public and Private Fields in the Class Instance. However, when viewed from *outside* the instance, only public fields are visible
```apl
      ⎕NC 'ncinst.pubFld' 'ncinst.pvtFld'
¯2.2 0
```

In this case, the name-class is negative to indicate that the name has been exposed by the class hierarchy, rather than existing in the associated namespace which APL has created to contain the instance. The same result is returned if `⎕NC` is executed inside this space:
```apl
      ncinst.⎕NC'pubFld' 'pvtFld'
¯2.2 0
```

Note that the names of Fields are reported as being *unused* if the argument to `⎕NC` is simple.
```apl
      ncinst.⎕NC 2 6⍴'pubFldpvtFld'
0 0
```

## Property (Name-Class 2.3)

Properties defined by APL Classes have name-class 2.3.
```apl
:Class nctest
    :Field pvtFld←99
    
    :Property pubProp
    :Access Public
        ∇ r←get
          r←pvtFld
        ∇
    :EndProperty
    
    :Property pvtProp
        ∇ r←get
          r←pvtFld
        ∇
    :EndProperty
    
    ∇ r←NameClass x
      :Access Public
      r←⎕NC x
    ∇
...
:EndClass ⍝ nctest       
 
      ncinst←⎕NEW nctest
```

The name-class of a Property, whether Public or Private, *viewed from a Method that is executing within the Instance Space*, is 2.3.
```apl
      ncinst.NameClass'pubProp' 'pvtProp'
2.3 2.3
 
```

Note that an internal Method sees both Public and Private Properties in the Class Instance. However, when viewed from *outside* the instance, only Public Properties are visible
```apl
      ⎕NC 'ncinst.pubProp' 'ncinst.pvtProp'
¯2.3 0
```

In this case, the name-class is negative to indicate that the name has been exposed by the class hierarchy, rather than existing in the associated namespace which APL has created to contain the instance. The same result is returned if `⎕NC` is executed inside this space:
```apl
      ncinst.⎕NC 'pubProp' 'pvtProp'
¯2.3 0
```

Note that the names of Properties are reported as being *unused* if the argument to `⎕NC` is simple.
```apl
      ncinst.⎕NC 2 6⍴'pubProppvtProp'
0 0
```

## External Property (Name-Class 2.6)

Properties exposed by external objects (.NET and COM and the APL GUI) have name-class `¯2.6`.
```apl
      ⎕USING←'System'
      dt←⎕NEW DateTime (2006 1 1)
      dt.⎕NC 'Day' 'Month' 'Year'
¯2.6 ¯2.6 ¯2.6
 
      'ex' ⎕WC 'OLEClient' 'Excel.Application'
      ex.⎕NC 'Caption' 'Version' 'Visible'
¯2.6 ¯2.6 ¯2.6
 
     'f'⎕WC'Form'
      f.⎕NC'Caption' 'Size'
¯2.6 ¯2.6
```

Note that the names of such Properties are reported as being *unused* if the argument to `⎕NC` is simple.
```apl
      f.⎕NC 2 7⍴'CaptionSize   '
0 0
```

## Defined Function (Name-Class 3.1)

Traditional APL defined functions have name-class 3.1.
```apl
     ∇ R←AVG X
[1]    R←(+/X)÷⍴X
     ∇
      AVG ⍳100
50.5
 
      ⎕NC'AVG'
3
      ⎕NC⊂'AVG'
3.1
 
      'MYSPACE'⎕NS 'AVG'
       MYSPACE.AVG ⍳100
50.5
 
      MYSPACE.⎕NC'AVG'
3
      ⎕NC⊂'MYSPACE.AVG'
3.1
```

Note that a function that is simply cloned from a defined function by assignment retains its name-class.
```apl
      MEAN←AVG
      ⎕NC'AVG' 'MEAN'
3.1 3.1
```

Whereas, the name of a function that amalgamates a defined function with any other functions has the name-class of a Derived Function, that is, 3.3.
```apl
      VMEAN←AVG∘,
      ⎕NC'AVG' 'VMEAN'
3.1 3.3
```

## Dfn (Name-Class 3.2)

Dfns have name-class 3.2
```apl
      Avg←{(+/⍵)÷⍴⍵}
 
      ⎕NC'Avg'
3
      ⎕NC⊂'Avg'
3.2
```

## Derived Function (Name-Class 3.3)

Names that reference a primitive or derived function have a name-class of 3.3.
```apl
      PLUS←+
      SUM←+/
      CUM←PLUS\
      ⎕NC'PLUS' 'SUM' 'CUM'
3.3 3.3 3.3
      ⎕NC 3 4⍴'PLUSSUM CUM '
3 3 3
```

Note the difference between the name-class of a name referring to a defined function (3.1) and that of a name referring to a defined function bound with an operator to form a derived function (3.3). Trains, being derived functions, also have  nameclass 3.3.
```apl
     ∇ R←AVG X
[1]    R←(+/X)÷⍴X
     ∇
 
      MEAN←AVG
      VMEAN←AVG∘,

      negrec←-,÷ 

      ⎕NC'AVG' 'MEAN' 'VMEAN' 'negrec'
3.1 3.1 3.3 3.3
 
```

## External Function (Name-Class 3.6)

Methods exposed by the Dyalog APL GUI and COM and .NET objects have name-class `¯3.6`. Methods exposed by External Functions created using `⎕NA` and `⎕SH` all have name-class `3.6`.
```apl
      'F'⎕WC'Form'
 
      F.⎕NC'GetTextSize' 'GetFocus'
¯3.6 ¯3.6
 
      'EX'⎕WC'OLEClient' 'Excel.Application'
      EX.⎕NC 'Wait' 'Save' 'Quit'
¯3.6 ¯3.6 ¯3.6
 
      ⎕USING←'System'
      dt←⎕NEW DateTime (2006 1 1)
      dt.⎕NC 'AddDays' 'AddHours'
¯3.6 ¯3.6
 

```
```apl
      'beep'⎕NA'user32|MessageBeep i'
 
      ⎕NC'beep'
3
      ⎕NC⊂'beep'
3.6
      'xutils'⎕SH''
      )FNS
avx     box     dbr     getenv  hex     ltom    ltov    mtol    ss      vtol
      ⎕NC'hex' 'ss'
3.6 3.6 
```

Note that the names of such Methods are reported as being *unused* if the argument to `⎕NC` is simple.
```apl
      'F'⎕WC'Form'
      F.⎕NC↑'GetTextSize' 'GetFocus'
0 0
```

## Operator (Name-Class 4.1)

Traditional Defined Operators have name-class 4.1.
```apl
      ∇FILTER∇
     ∇ VEC←(P FILTER)VEC  ⍝ Select from VEC those elts ..
[1]    VEC←(P¨VEC)/VEC    ⍝ for which BOOL fn P is true.
     ∇
 
      ⎕NC'FILTER'
4
      ⎕NC⊂'FILTER'
4.1
```

## Dop (Name-Class 4.2)

Dops have name-class 4.2.
```apl
     pred←{⎕IO ⎕ML←1 3   ⍝ Partitioned reduction.
     ⊃⍺⍺/¨(⍺/⍳⍴⍺)⊂⍵
     }
 
      2 3 3 2 +pred ⍳10
3 12 21 19
 
      ⎕NC'pred'
4
      ⎕NC⊂'pred'
4.2
```

## Derived Operator (Name-Class 4.3)

Derived operators include:

- A name referring to a monadic operator.
- A dyadic operator curried with its right-operand. 

<h2 class="example">Example</h2>
```apl
       each←¨
       each
¨
       ⎕NC ⊂'each'
4.3 
```
```apl
       inv←⍣¯1
       inv
⍣ ¯1
       ⎕NC ⊂'inv'
4.3
       c2f←(32∘+)∘(×∘1.8) ⍝ Centigrade to Fahrenheit
       f2c 0 100
32 212
       f2c inv 32 212     ⍝ Fahrenheit to Centigrade
0 100

```

## External Event (Name-Class 8.6)

Events exposed by Dyalog APL GUI objects, COM and .NET objects have name-class `¯8.6`.
```apl
      f←⎕NEW'Form'('Caption' 'Dyalog GUI Form')
      f.⎕NC'Close' 'Configure' 'MouseDown'
¯8.6 ¯8.6 ¯8.6
 
      xl←⎕NEW'OLEClient'(⊂'ClassName' 'Excel.Application')
      xl.⎕NL -8
 NewWorkbook  SheetActivate  SheetBeforeDoubleClick ...
 
      xl.⎕NC 'SheetActivate' 'SheetCalculate'
¯8.6 ¯8.6
 
    ⎕USING←'System.Windows.Forms,system.windows.forms.dll'
    ⎕NC,⊂'Form'
9.6
    Form.⎕NL -8
 Activated  BackgroundImageChanged  BackColorChanged ...
```

## Namespace (Name-Class 9.1)

Plain namespaces created using `⎕`NS, or fixed from a `:Namespace` script, have name-class 9.1.
```apl
      'MYSPACE' ⎕NS ''
      ⎕NC'MYSPACE'
9
      ⎕NC⊂'MYSPACE'
9.1
```

Note however that a namespace created by cloning, where the right argument to `⎕NS` is a `⎕OR` of a namespace, retains the name-class of the original space.
```apl
      'CopyMYSPACE'⎕NS ⎕OR 'MYSPACE'
      'CopyF'⎕NS ⎕OR 'F'⎕WC'Form'
 
      ⎕NC'MYSPACE' 'F'
9.1 9.2
      ⎕NC'CopyMYSPACE' 'CopyF'
9.1 9.2
```

The Name-Class of .NET namespaces (visible through `⎕USING`) is also 9.1
```apl
      ⎕USING←''
      ⎕NC 'System' 'System.IO'
9.1 9.1
```

## Instance (Name-Class 9.2)

Instances of Classes created using `⎕NEW`, and GUI objects created using `⎕WC` all have name-class 9.2.
```apl
      MyInst←⎕NEW MyClass
      ⎕NC'MyInst'
9
      ⎕NC⊂'MyInst'
9.2
      UrInst←⎕NEW ⎕FIX ':Class'  ':EndClass'
      ⎕NC 'MyInst' 'UrInst'
9.2 9.2
 
      'F'⎕WC 'Form'
      'F.B' ⎕WC 'Button'
      ⎕NC 2 3⍴'F  F.B'
9 9
      ⎕NC'F' 'F.B'
9.2 9.2

```
```apl
      F.⎕NC'B'
9
      F.⎕NC⊂,'B'
9.2
```

Instances of COM Objects whether created using `⎕WC` or `⎕NEW` also have name-class 9.2.
```apl
      xl←⎕NEW'OLEClient'(⊂'ClassName' 'Excel.Application')
      'XL'⎕WC'OLEClient' 'Excel.Application'
      ⎕NC'xl' 'XL'
9.2 9.2
```

The same is true of Instances of .NET Classes (Types) whether created using `⎕NEW` or `.New`.
```apl
      ⎕USING←'System'
      dt←⎕NEW DateTime (3↑⎕TS)
      DT←DateTime.New 3↑⎕TS
      ⎕NC 'dt' 'DT'
9.2 9.2
```

Note that if you remove the GUI component of a GUI object, using the Detach method, it reverts to a plain namespace.
```apl
      F.Detach
      ⎕NC⊂,'F'
9.1
```

Correspondingly, if you attach a GUI component to a plain namespace using the monadic form of `⎕WC`, it morphs into a GUI object
```apl
      F.⎕WC 'PropertySheet'
      ⎕NC⊂,'F'
9.2
```

## Class (Name-Class 9.4)

Classes created using the editor or `⎕FIX` have name-class 9.4.
```apl
      )ED ○MyClass
 
:Class MyClass
    ∇ r←NameClass x
      :Access Public Shared
      r←⎕NC x
    ∇
:EndClass ⍝ MyClass
 
      ⎕NC 'MyClass'
9
      ⎕NC⊂'MyClass'
9.4

```
```apl
      ⎕FIX ':Class UrClass'  ':EndClass'
      ⎕NC 'MyClass' 'UrClass'
9.4 9.4
```

Note that the name of the Class is visible to a Public Method in that Class, or an Instance of that Class.
```apl
      MyClass.NameClass'MyClass'
9
      MyClass.NameClass⊂'MyClass'
9.4
```

## Interface (Name-Class 9.5)

Interfaces, defined by `:Interface ... :EndInterface` clauses, have name-class 9.5.
```apl
:Interface IGolfClub
:Property Club
    ∇ r←get
    ∇
    ∇ set
    ∇
:EndProperty
 
∇ Shank←Swing Params
∇
 
:EndInterface ⍝ IGolfClub
 
      ⎕NC 'IGolfClub'
9
      ⎕NC ⊂'IGolfClub'
9.5
```

## External Class (Name-Class 9.6)

External Classes (Types) exposed by .NET have name-class 9.6.
```apl
      ⎕USING←'System' 'System.IO'
 
      ⎕NC 'DateTime' 'File' 'DirectoryInfo'
9.6 9.6 9.6
```

Note that referencing a .NET class (type) with `⎕NC`, fixes the name of that class in the workspace and obviates the need for APL to repeat the task of searching for and loading the class when the name is next used.

## External Interface (Name-Class 9.7)

External Interfaces exposed by .NET have name-class 9.7.

```apl
      ⎕USING←'System.Web.UI,system.web.dll' 
 
      ⎕NC 'IPostBackDataHandler' 'IPostBackEventHandler' 
9.7 9.7
```

Note that referencing a .NET Interface with `⎕NC`, fixes the name of that Interface in the workspace and obviates the need for APL to repeat the task of searching for and loading the Interface when the name is next used.
