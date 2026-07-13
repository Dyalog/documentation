# Loading an ActiveX Control

An ActiveX or OLE Control is in fact a type of Dynamic Link Library (DLL) which must be loaded before it can be used. This is done by creating an OCXClass object using `⎕WC` or `⎕NEW`.

For  example, if you have an OLE Control named "Microsoft Office Chart 9.0 ", you can load it with the following statements (which are split here only to prevent text wrap)

```apl
      NAME←' Microsoft Office Chart 9.0 '
      MOC←⎕NEW 'OCXClass' (⊂'ClassName' NAME)
```

or, using `⎕WC`

```apl
      'MOC' ⎕WC 'OCXClass' NAME
```

The right argument is a character string containing the name or class identifier of the ActiveX Control. The left argument is an arbitrary name of your own choosing by which you will subsequently refer to the Control class.

## Using an OLE Control

Having created an OCXClass object, you may *use* an OLE Control by creating an *instance* of it from its class. The instance must be created as the child of a Form. For example:

```apl
      'F' ⎕WC 'Form'
      'F.MM' ⎕WC 'MOC' ⍝ Instance of MOC
```

Although you can obtain general information about an OLE Control from both the class (represented by the OCXClass object) and any instance, you may only query and manipulate a control through an instance.
