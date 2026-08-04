---
search:
  boost: 2
---

# <span>List Object Names</span> `R←⎕NL Y`{{key}}

`Y` must be a simple numeric scalar or vector containing one or more of the values for name-class.  See also [Name Classification](nc.md).

`R` is a list of the names of active objects whose name-class is included in `Y` in standard sorted order.

If *any* element of `Y` is negative, positive values in `Y` are treated as if they were negative, and R is a vector of character vectors. Otherwise, `R` is simple character matrix.

Furthermore, if `⎕NL` is being evaluated inside the namespace associated with a Class or an Instance of a Class, and any element of `Y` is negative, `R` includes the Public names exposed by the Base Class (if any) and all other Classes in the Class hierarchy.

Standard sorted order is in Unicode point order for Unicode editions, and in the collation order of `⎕AV` for Classic editions.

If an element of `Y` is an integer, the names of all of the corresponding sub-name-classes are included in `R`. For example, if `Y` contains the value 2, the names of all variables (name-class 2.1), fields (2.2), properties (2.3) and external or shared variables (2.6) are obtained. Otherwise, only the names of members of the corresponding sub-name-class are obtained.

<h2 class="example">Examples</h2>
```apl

      ⎕NL 2 3
A
FAST
FIND
FOO
V

      ⎕NL ¯9
 Animal  Bird  BirdBehaviour  Coin  Cylinder  DomesticParrot  Eeyore  FishBehaviour  Nickel  Parrot  Penguin  Polly  Robin 
      ⎕NL ¯9.3 ⍝ Instances
 Eeyore  Nickel  Polly  Robin 
      ⎕NL ¯9.4 ⍝ Classes
 Animal  Bird  Coin  Cylinder  DomesticParrot  Parrot  Penguin
      ⎕NL ¯9.5 ⍝ Interfaces
 BirdBehaviour  FishBehaviour
```

`⎕NL` can also be used to explore Dyalog GUI Objects, .NET types and COM objects.

### Dyalog GUI Objects

`⎕NL` may be used to obtain lists of the Methods, Properties and Events provided by Dyalog APL GUI Objects.

### .NET Classes (Types)

`⎕NL` can be used to explore .NET types.

When a reference is made to an undefined name, and `⎕USING` is set, APL attempts to load the Type from the appropriate .NET Assemblies. If successful, the name is entered into the symbol table with name-class 9.6.
```apl

      ⎕USING←'System'
      DateTime
(System.DateTime)
      ⎕NL -9
 DateTime
      ⎕NC,⊂'DateTime'
9.6
```

The names of the Properties and Methods of a .NET Type may then be obtained using `⎕NL`.

In fact it is not necessary to make a separate reference first, because the expression `Type.⎕NL` (where `Type` is a .NET Type) is itself a reference to Type. So, (with `⎕USING` still set to `'System'`):
```apl

      ⎕NL -9
 Array  DateTime
```

Another use for `⎕NL` is to examine .NET *enumerations*. For example:
```apl

      ⎕USING←'System.Windows.Forms,system.windows.forms.dll'

      FormBorderStyle.FixedDialog.value__
3

      FormBorderStyle.({⍵,[1.5]⍎¨⍵,¨⊂'.value__'}⎕NL -2)
 Fixed3D            2
 FixedDialog        3
 FixedSingle        1
 FixedToolWindow    5
 None               0
 Sizable            4
 SizableToolWindow  6
```

### COM Objects

Once a reference to a COM object has been obtained, `⎕NL` may be used to obtain lists of its Methods, Properties and Events.
```apl

      xl←⎕NEW'OLEClient'(⊂'ClassName' 'Excel.Application')

      ⎕NL -9
 xl
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NL NL
</div>
