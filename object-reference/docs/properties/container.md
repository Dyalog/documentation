# <span>Container</span> <span>Property</span>



**Applies To:** [ActiveXControl](../objects/activexcontrol.md)

**Description**


The Container property is a read-only property whose value is the `⎕OR` of an ActiveXContainer object that represents the *ActiveX Site* object of the application that is hosting the [ActiveXControl](../objects/activexcontrol.md).


The value of Container may be converted to a namespace using `⎕NS` or `⎕WC`.


The resulting object may then be used to obtain the values of ambient properties, or to access methods exposed by the host application via OLE interfaces. See [OLEQueryInterface](../methodorevents/olequeryinterface.md).



