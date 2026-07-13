# Fonts

In keeping with the manner in which fonts are managed by Microsoft Windows and other GUI environments, Dyalog APL treats fonts as objects which you create (load) using `⎕WC` and erase (unload) using `⎕EX` or localisation.

A Font **object** is created and assigned a name using `⎕WC`. This name is then referenced by other objects via their FontObj **properties**. For example to use an Arial bold italic font of height 32 pixels in two Labels:
```apl
     'A32' ⎕WC 'Font' 'ARIAL' 32 0 1 0 700
 
     'F.L1' ⎕WC 'Label' 'Hello' (20 10) ('FontObj' 'A32')
     'F.L2' ⎕WC 'Label' 'World' (20 10) ('FontObj' 'A32')
```

If a font is referenced by more than one Form, you should create the Font as a top-level object, as in the above example. However, if the font is referenced by a single Form, you may make the Font object a child of that Form. The font will then automatically be unloaded when you erase the Form with which it is associated.

**Compatibility Note:**

In the first release of Dyalog APL/W (Version 6.2), fonts were referenced **directly** by the FontObj property. The above example would have been achieved by:
```apl
      'F.L1' ⎕WC 'Label' 'Hello' (10 10)
                 ('FontObj' 'ARIAL' 32 0 1 0 700)
 
      'F.L2' ⎕WC 'Label' 'World' (20 10)
                 ('FontObj' 'ARIAL' 32 0 1 0 700)
```

Although this original mechanism continues to be supported, it is recommended that you use the method based on Font **objects** which supersedes it.
