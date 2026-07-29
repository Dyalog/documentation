# <span>OLEQueryInterface</span> <span>Method 543</span>

**Description**

This method is used to obtain the methods and properties associated with a particular *interface* that is provided by a COM object. An interface is simply a pointer to a table of methods (not properties) that are exported by an object.

Note that methods and properties exported using the standard IDispatch interface are established automatically when the object is created. OLEQueryInterface is required only to support alternative or additional interfaces that the object may implement.

The argument to OLEQueryInterface is a single item as follows:

|-----|--------------|----------------|
|`[1]`|Interface name|character vector|

The result is a namespace.

It is normal, although not strictly required, that the new namespace be a child of the one for which the method is run.

Note that if the object does not support a type library, the new namespace will be empty and you will have to establish functions corresponding to the methods exported by the interface using [SetMethodInfo](./setmethodinfo.md).

**Application**

Objects: [ActiveXContainer](../objects/activexcontainer.md), [OLEClient](../objects/oleclient.md)
