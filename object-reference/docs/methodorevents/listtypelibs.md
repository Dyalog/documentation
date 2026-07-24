# <span>ListTypeLibs</span> <span>Method 520</span>

**Description**

The ListTypeLibs method reports the names and CLSIDs of all the loaded Type Libraries.

The ListTypeLibs method is niladic.

The result is a nested vector with one element per loaded Type Library.

Each element is a vector of 2-element characater vectors. The first is the name of the Type Library; the second is its class identifier or CLSID.

<h2 class="example">Example</h2>
```apl
      'EX'⎕WC'OLEClient' 'Excel.Application'
      ⍴ListTypeLibs
3
      ↑⊃ListTypeLibs
Microsoft Excel 9.0 Object Library    
{00020813-0000-0000-C000-000000000046}

      ↑⊃¨ListTypeLibs
Microsoft Excel 9.0 Object Library                       
Microsoft Visual Basic for Applications Extensibility 5.3
Microsoft Office 9.0 Object Library                      
```

**Application**

Objects: [Root](../objects/root.md)
