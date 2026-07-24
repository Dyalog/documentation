# <span>InterceptedURLs</span> <span>Property</span>

**Description**

The InterceptedURLs property is a 2-column matrix that specifies whether the [HTMLRenderer](../objects/htmlrenderer.md) will attempt to satisfy a request for a resource from the workspace or, via the CEF, from the internet. If directed to the workspace, the request will trigger an [HTTPRequest](../methodorevents/httprequest.md) event if the protocol is `http`, or a [WebSocketUpgrade](../methodorevents/websocketupgrade.md) event if the protocol is `ws`.

The first column is a wild-carded character scalar or vector containing a pattern to match. The second column is numeric indicating whether or not the [HTMLRenderer](../objects/htmlrenderer.md) should trigger an event as shown in the table below. InterceptedURLs may contain any number of rows.

|Value|Meaning                                                                                                                                             |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------|
|0    |Ignore request; pass to  CEF for fulfilment                                                                                                         |
|1    |Trigger an [HTTPRequest](../methodorevents/httprequest.md) or [WebSocketUpgrade](../methodorevents/websocketupgrade.md) (automatic) in the workspace|
|2    |Trigger an [HTTPRequest](../methodorevents/httprequest.md) or [WebSocketUpgrade](../methodorevents/websocketupgrade.md) (manual) in the workspace   |

If the requested url is a relative rather than an absolute URL, it is prepended by the string `http://dyalog_root/`. So, for example, if the [HTML](html.md) property contains :
```apl
<link rel="stylesheet" href="style.css">
<script src="app.js"></script>
```

the HTMLRenderer will request `http://dyalog_root/style.css` and `http://dyalog_root/app.js` respectively.

When the value of InterceptedURLs is its default ( `(0 2⍴'')` it is treated as if it were set to `((1 2⍴'*://dyalog_root/*' 1)`. So by default, requests for a relative URL will fire an event in the workspace while absolute URL will be directed by the CEF to the internet.

Note that if code in the page creates a web socket intended for internal use, with anything other than `dyalog_root` as the URL, the URL must match a pattern in InterceptedURLs with 1 in the second column. The following example does not require a matching pattern in InterceptedURLs.
```apl
 // Create a new WebSocket.
  window.socket = new WebSocket('ws://dyalog_root/');
```

<h2 class="example">Examples</h2>

The following will trigger an  event for all requested URLs.
```apl
      InterceptedURLs ← 1 2⍴'*' 1
```

The following will attempt to retrieve from the net URLs containing `'.dyalog.com'` and trigger an [HTTPRequest](../methodorevents/httprequest.md) event for all other requested URLs.
```apl
      InterceptedURLs ← 2 2⍴'*.dyalog.com*' 0 '*' 1
```

**Application**

Objects: [HTMLRenderer](../objects/htmlrenderer.md)
