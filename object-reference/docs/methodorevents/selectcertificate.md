# <span>SelectCertificate</span> <span>Event 848</span>

**Description**

This event is triggered when [HTMLRenderer](../objects/htmlrenderer.md) requests a resource from a server that requires a certificate.

The event message reported as the result of `⎕DQ`, or supplied as the right argument to your callback function, is a 7-element vector as follows:

|-----|------------|----------------------------|
|`[1]`|Object      |ref or character vector     |
|`[2]`|Event       |`'SelectCertificate'` or 848|
|`[3]`|Index       |Integer (see below)         |
|`[4]`|Addr        |Host address                |
|`[5]`|Port        |Host port                   |
|`[6]`|&nbsp;      |`'is proxy'`                |
|`[7]`|Certificates|See below                   |

**Certificates** is a vector of namespaces, each of which represents an available certificate and contains the following variables:

|Name          |Description                                    |
|--------------|-----------------------------------------------|
|`DER`         |Distinguished Encoding Rules. Character Vector.|
|`Subject`     |Namespace (see below)                          |
|`Issuer`      |Namespace (see below)                          |
|`SerialNumber`|Integer                                        |

The **Subject** and **Issuer** namespaces contain the following variables:

|Name         |Description     |
|-------------|----------------|
|`CommonName` |Character vector|
|`CountryName`|Character vector|
|`DisplayName`|Character vector|

The application should respond to this event by selecting a certficate from the list of available certificates reported by the 7th element of the event message. This is done by having a callback function that sets the 3rd element of the event message (Index) to the 0-origin index in Certificates and returns the event message as its result.

<h2 class="example">Example</h2>
```apl

     ∇ arg←cb arg
[1]   ⍝ SelectCertificate callback function
[2]    arg[3]←0 ⍝ Select the first certificate
     ∇
```

**Application**

Objects: [HTMLRenderer](../objects/htmlrenderer.md)
