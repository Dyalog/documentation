<h1 class="heading"><span class="name">The Session Colour Scheme</span></h1>

Within the Development Environment, different colours are used to identify different types of information. These colours are normally defined by registry entries and may be changed using the Colour Configuration dialog box as described later in this chapter.

In the Classic Edition, colours may alternatively be defined in the Output Translate Table (normally WIN.DOT). This table recognises up to 256 foreground and 256 background colours which are referenced by colour indices 0-255. These colour indices are mapped to physical colours in terms of their Red, Green and Blue intensities (also 0-255). Foreground and background colours are specified independently as Cnnn or Bnnn. For example, the following entry in the Output Translate Table defines colour 250 to be red on magenta.
```
   C250: 255 0 0   + Red foreground
   B250: 255 0 255 + Magenta background
```

The first table below shows the colours used for different session components. The second table shows how different colours are used to identify different types of data in edit windows.

Table: Default Colour Scheme - Session {: #default-colour-scheme-session }

|Colour|Used for                   |Default            |
|------|---------------------------|-------------------|
|249   |Input and marked lines     |Red on White       |
|250   |Session log                |Black on White     |
|252   |Tracer : Suspended Function|Yellow on Black    |
|253   |Tracer : Pendent Function  |Yellow on Dark Grey|
|245   |Tracer : Current Line      |White on Red       |

Table: Default Colour Scheme Edit windows {: #default-colour-scheme-edit-windows }

|Colour|Array Type                 |Editable|Default         |
|------|---------------------------|--------|----------------|
|236   |Simple character matrix    |Yes     |Green on Black  |
|239   |Simple numeric             |No      |White on Dk Grey|
|241   |Simple mixed               |No      |Cyan on Dk Grey |
|242   |Character vector of vectors|Yes     |Cyan on Black   |
|243   |Nested array               |No      |Cyan on Dk Grey |
|245   |`⎕OR` object               |No      |White on Red    |
|248   |Function or Operator       |No      |White on Dk Cyan|
|254   |Function or Operator       |Yes     |White on Blue   |

## Syntax Colouring in the Session

As an adjunct to the overall Session Colour Scheme, you may choose to apply a *syntax colouring scheme* to the current Session Input line(s). You may also extend syntax colouring to previously entered input lines, although this only applies to input lines in the current session; syntax colouring information is not remembered in the Session Log.

Syntax colouring may be used to highlight the context of names and other elements when the line was entered. For example, you can identify global names and local names by allocating them different colours.

See [Colour Selection Dialog](../../windows-installation-and-configuration-guide/configuring-the-ide/colour-selection-dialog) for further details.
