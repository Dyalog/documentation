# <span>URL</span> <span>Property</span>

**Description**

The URL property is a character vector that  specifies the url of a resource to be requested by the [HTMLRenderer](../objects/htmlrenderer.md). Its default value is an empty character vector.

Specifying URL is an alternative way to setting the [HTML](html.md) property in order to display content in the [HTMLRenderer](../objects/htmlrenderer.md).

When you set the URL property, the [HTMLRenderer](../objects/htmlrenderer.md) will request the corresponding resource (from either the internet or the workspace via an [HTTPRequest](../methodorevents/httprequest.md) event) and the display will change according to the response. The [HTML](html.md) property is ignored and remains unchanged.

When you set the [HTML](html.md) property, the content of the [HTMLRenderer](../objects/htmlrenderer.md) will change accordingly. The current value of the URL property is ignored and remains unchanged.

If you set BOTH URL and [HTML](html.md) in the same statement, the value of URL takes precedence and the assignment to [HTML](html.md) is ignored (it remains unchanged).

**Application**

Objects: [HTMLRenderer](../objects/htmlrenderer.md)
