<h1 class="heading"><span class="name">Miscellaneous</span></h1>

## Running from scripts

Dyalog APL can be run with input being directed from a script file, and output being redirected as well.

The script file needs to be built in such a way that it contains valid input according to the input translate table that is defined in the APLK variable.

The classic edition of Dyalog APL expects that the input script by default uses Ctrl-O and Ctrl-N to swap between APL and ASCII characters, and Ctrl-H is used to create overstrikes. Be aware that when editing such an input file, cut and paste of ^H, ^N or ^O may well result in the two character sequences being copied, rather than the single character Ctrl-H, Ctrl-N and Ctrl-O.

The Unicode edition by default expects that the input file has Unicode characters in it; a Unicode-aware editor is therefore required. Note however that applications such as Notepad will add BOMs (Byte Order Markers) to the Unicode text; these must be removed as the Dyalog APL input translate table does not have BOMs defined in it.

The example below shows the same set of APL expressions as they would appear in a script file for classic and Unicode editions: it is rather easier to read the Unicode edition's input !

### Classic example
```apl
^O(2^NLnqK.K K^OGetBuildID^NK^O),(^NK.KLwgK^OAPLVersion^NK^O)
^Ovar^N[1+1 J^HC^O Check input from file: Classic
)SI
^N"si
^Nloff
```

### Unicode example
```apl
(+2⎕NQ'.'  'GetBuildID'),('.'⎕WG'APLVersion')
var←1÷1 ⍝ Check input from file: Unicode
)SI
)SI
⎕OFF
```
