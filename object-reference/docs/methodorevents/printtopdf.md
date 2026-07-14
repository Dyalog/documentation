# <span>PrintToPDF</span> <span>Method 845</span>

**Applies To:** [HTMLRenderer](../objects/htmlrenderer.md)

**Description**

This method writes the content displayed in an [HTMLRenderer](../objects/htmlrenderer.md) object to a specified file in Portable Document Format (pdf).

The argument to PrintToPDF is a simple character scalar or vector containing a file name. Note that the method does not add any extension to the file name that is supplied.

The method returns a Boolean result which indicated whether or not the operation succeeded. If the file name contains a directory path, the path must already exist. The user must have permission to write the file.
