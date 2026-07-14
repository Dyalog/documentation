# <span>RealSize</span> <span>Property</span>

**Applies To:** [Metafile](../objects/metafile.md)

**Description**

There are several distinct types of Windows metafiles. A *placeable* metafile is one that carries with it its *suggested size*. Certain programs (such as Word for Windows) only support placeable metafiles.

The RealSize property specifies the suggested size of a Metafile in units of 0.01mm. Thus to make a placeable Metafile with a suggested size of 20 x 10 cm, you would set RealSize to (20000 10000).

The RealSize property is not used or required by Dyalog and is provided only to enable you to make and save a new metafile that is placeable. If you create a Metafile object from a file, the value of RealSize will be obtained from the value recorded in the file (if it is placeable). Otherwise, RealSize will be (0 0). If so, you must set RealSize to make it placeable. Each element of RealSize must be an integer in the range 0-144745.
