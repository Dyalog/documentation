# Additional Interfaces

Most COM objects and their sub-objects provide information about their methods and properties through the IDispatch interface which is the normal interface used for OLE Automation. When you create an instance of an OLEClient object or an OCXClass object, Dyalog APL uses this interface to gain the information it requires.

If an object does not provide an IDispatch interface, or if an object provides additional functionality through other interfaces, it is possible to access the object's functionality using the OLEQueryInterface method.

In addition, if an object exposes sub-objects using an interface other than IDispatch, you may access these sub-objects using the OLEQueryInterface method..

See OLEQueryInterface for further details.
