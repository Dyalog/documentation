# <span>ExecuteJavaScript</span> <span>Method 839</span>

**Applies To:** [HTMLRenderer](../objects/htmlrenderer.md)

**Description**

This method is used to execute JavaScript in an [HTMLRenderer](../objects/htmlrenderer.md) object.

The argument to ExecuteJavaScript is a single item as follows:

|-----|----|-------------------------------------------|
|`[1]`|Code|character vector containing JavaScript code|

The shy result of ExecuteJavaScript is currently 1; this may change.

<h2 class="example">Example</h2>
```apl
      hr.ExecuteJavaScript 'alert("Hello")'
```
