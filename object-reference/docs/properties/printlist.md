<h1 class="heading"><span class="name">PrintList</span> <span class="right">Property</span></h1>



**Applies To:** [Root](../objects/root.md)

**Description**


This property provides a list of the printers that are installed on your computer system, that is, those listed when you select "printers" from the MS-Windows Control Panel. It is a "read-only" property of the [Root](../objects/root.md) object `'.'`.


PrintList is a vector of character vectors. Each item in PrintList contains the name of an installed printer followed by a comma (,) and then the name of the device to which it is attached. The first item in PrintList is the default system printer.

<h2 class="example">Example</h2>
```apl
      ⍴'.'⎕WG'PrintList'
6
      ]Display ⊃'.'⎕WG'PrintList'
┌→─────────────────────┐
│KODAK ESP-3 AiO,USB001│
└──────────────────────┘
      ↑'.'⎕WG'PrintList'
KODAK ESP-3 AiO,USB001
Send To OneNote 2007,Send To Microsoft OneNote Port:
Microsoft XPS Document Writer,XPSPort:
Microsoft Office Document Image Writer,Microsoft Document Imaging Writer Port:
Fax,SHRFAX:                                               
Auto Canon MP600 Printer on DIMENSION5150,\\DIMENSION5150\Canon               

```



