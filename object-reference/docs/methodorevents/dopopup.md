# <span>DoPopup</span> <span>Event 846</span>

**Description**

This event is triggered when the [HTMLRenderer](../objects/htmlrenderer.md) client attempts to open a new window. This could be fired by an HTML `<a>` tag with the target attribute set to open a URL in a new window or by a JavaScript `window.open()` call. Note that this does not apply to JavaScript Popup Boxes.

By default the HTMLRenderer ignores a request for a new window, but if  the DoPoup event, is enabled, it provides the information needed to process the request in the workspace.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq), or supplied as the right argument to your callback function, is a 5-element vector as follows:

|-----|----------|---------------------------------------|
|`[1]`|Object    |ref or character vector                |
|`[2]`|Event     |`'DoPopup'` or 846                     |
|`[3]`|URL       |the requested url                      |
|`[4]`|Attributes|requested window attributes (see below)|
|`[5]`|Framename |character vector framename             |

**Attributes** is a 7-element nested vector that specifies the requested attributes for the new window. The HTMLRenderer  currently provides no mechanism to use this information.

|-----|---------------------------------------------|
|`[1]`|2-element vector of top, left positions – positions not specified are ⍬                                                     |
|`[2]`|2-element vector of height, width – sizes not specified are ⍬                                                               |
|`[3]`|Integer "WindowDisposition". See https://magpcss.org/ceforum/apidocs3/projects/(default)/cef_window_open_disposition_t.html.|
|`[4]`|Boolean menubar (default=1)                                                                                                 |
|`[5]`|Boolean scrollbar (default=1                                                                                                |
|`[6]`|Boolean statusbar (default=1)                                                                                               |
|`[7]`|Boolean location/toolbar (default=1)                                                                                        |

To respond to the request for a new window, the callback function should open the requested URL as appropriate, for example, in a newly created [HTMLRenderer](../objects/htmlrenderer.md) object.

<h2 class="example">Example</h2>
```apl
      'h'⎕WC  'HTMLRenderer'
      'h'⎕WS  ('Event' 'DoPopUp' 'DoPopUpCB')
```
```apl
      html← '<a href="https://www.dyalog.com"'
      html,← target="_blank">Dyalog Website</a>'

      h.HTML←html
```
```apl
     ∇ DoPopUpCB msg;props;posn
[1]    props←⊂'URL'(3⊃msg)
[2]    (posn size)←2↑4⊃msg
[3]    props,←('Posn'posn)('Size'size)
[4]    'popup'⎕WC'HTMLRenderer'props
     ∇

```

<h2 class="example">Extended Example</h2>
```apl
     ∇ {r}←DoPopupDemo args;html;h;c;s;e;p;d
[1]    →EndHTML
[2]   StartHTML:
[3]   ⍝<html>
[4]   ⍝  <head><title>DoPopupDemo</title></head>
[5]   ⍝<body>
[6]   ⍝  {}
[7]   ⍝  <button type="button" onclick="window.open('callback','_blank','width=400,height=200')">Click me!</button>
[8]   ⍝</body>
[9]   ⍝</html>
[10]  EndHTML:
[11]   html←∊'⍝'(⍳⍨↓⊢)¨(1+StartHTML)↓EndHTML↑⎕NR⊃⎕SI
[12]   :If 0∊⍴args
[13]       renderers←⍬
[14]       html←'{}'⎕R'This is the original window'⊢html
[15]       s←'Size'(⍬ ⍬)
[16]       p←'Posn'(⍬ ⍬)
[17]       d←'Data' 0
[18]       →Create
[19]   :Else
[20]       :Select 2⊃args
[21]       :Case 'DoPopup'
[22]           d←'Data'(1+⌈/renderers.Data)
[23]           html←'{}'⎕R('This is window ',⍕2⊃d)⊢html
[24]           s←'Size'(2⊃4⊃args)
[25]           p←'Posn'(100+(⊃args).Posn)
[26]           →Create
[27]       :Case 'Close'
[28]           renderers~←⊃args
[29]       :EndSelect
[30]   :EndIf
[31]   →0
[32]  Create:
[33]   h←'HTML'html
[34]   c←'Coord' 'Pixel'
[35]   e←'Event'('onAll' 'DoPopupDemo')
[36]   renderers,←⎕NEW'HTMLRenderer'(h c s p e d)
     ∇

```

The example function show above will display a new window when the button labelled Click me! is pressed. To start, type:
```apl
      DoPopupDemo ''
```

**Application**

Objects: [HTMLRenderer](../objects/htmlrenderer.md)
