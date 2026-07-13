# <span>PropList</span> <span>Property</span>

[**Applies To**](../propertyapplies/proplist.md)

**Description**

This is a "read-only" property that supplies a list of all other properties which are applicable to the object in question. The list is returned as a vector of character vectors in the order in which the corresponding properties are expected by [`⎕WC`](../../../language-reference-guide/system-functions/wc) and [`⎕WS`](../../../language-reference-guide/system-functions/ws).

<h2 class="example">Example</h2>
```apl
      'F'    ⎕WC 'Form'
      'F.MB' ⎕WC 'MenuBar'
      'F.MB' ⎕WG 'PropList'
 Type  Visible  FontObj  Data  EdgeStyle  MDIMenu  PropList
```
