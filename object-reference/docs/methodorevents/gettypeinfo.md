# <span>GetTypeInfo</span> <span>Method 553</span>

**Applies To:** [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md)

**Description**

This method is used to obtain information about a type list supported by a COM object.

The argument to GetTypeInfo is a single item as follows:

|-----|-----------------|-----------------|
|`[1]`|Type List name(s)|see below        |
|`[2]`|Value            |(usually) numeric|
|`[3]`|Description      |character vector |

*Type List name(s)* is a simple character vector or a vector of character vectors specifying one or more names of type lists supported by the object.

The result is a nested vector with one element per [Type List](../properties/typelist.md). Each element of this vector is itself a 3-element vector of character vectors made up as follows:

|-----|----------------|-----------------|
|`[1]`|Name of Constant|character vector |
|`[2]`|Value           |(usually) numeric|
|`[3]`|Description     |character vector |
