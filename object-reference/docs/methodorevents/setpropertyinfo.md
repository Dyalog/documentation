# <span>SetPropertyInfo</span> <span>Method 554</span>



**Applies To:** [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md)

**Description**


This method is used to redefine a property that is exported by a COM object. SetPropertyInfo is used to override the information provided by the object's Type Library.




The argument to SetPropertyInfo is a  2 or 3-element array as follows:


|-----|-----------------|---------------------------------------------------------------|
|`[1]`|Property name    |character vector                                               |
|`[2]`|Property info    |nested vector                                                  |
|`[3]`|Property function|integer                                                        |
|`[4]`|DISPID           |integer. See [DISPID (Dispatch ID)](../miscellaneous/dispid.md)|




For example, the Visible property exported by *Excel.Application* has the data type VT_BOOL and may be declared as follows:
```apl
      'EX' ⎕WC 'OLEClient' 'Excel.Application'
      EX.SetPropertyInfo 'Visible' 'VT_BOOL'
```



*Property function* may be required if the property value is retrieved or set via a function. This typically applies if the property takes parameters and will result in the property being fixed as a function rather than as a variable. Such properties may have a PropertyGet function, a PropertyPut function and/or a PropertyPutByReference function. If so, it is necessary to say to which of these three functions the details apply. The value of *Property function* is an integer 2 (PropertyGet), 4 (PropertyPut), or 8 (PropertyPutByReference).



For example, the following statement declares the PropertyGet function for the Item property of the Fields collection of the OLE object DAO.DBEngine. This property takes an index (into the collection) and returns an object.
```apl
      Fields.SetPropertyInfo 'Item'('VT_DISPATCH' 'VT_I4')2
```



