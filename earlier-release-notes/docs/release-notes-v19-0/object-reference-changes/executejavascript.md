<h1 class="heading"><span class="name">ExecuteJavaScript</span> <span class="command">Method 839</span></h1>

|-----------|--------------------------------------------------------------|
|Applies To:|[HTMLRenderer](https://help.dyalog.com/19.0/index.htm#GUI/Objects/HTMLRenderer.htm)|

**Description**

This method is used to execute JavaScript in an [HTMLRenderer](https://help.dyalog.com/19.0/index.htm#GUI/Objects/HTMLRenderer.htm) object.

The argument to ExecuteJavaScript is a single item as follows:

|-----|----|-------------------------------------------|
|`[1]`|Code|character vector containing JavaScript code|

The shy result of ExecuteJavaScript is currently 1; this may change.

<h2 class="example">Example</h2>
```apl
      hr.ExecuteJavaScript 'alert("Hello")'
```
