---
search:
  exclude: true
---

# <span>UpperCase</span> <span>Property</span>

**Description**

This property specifies whether or not property names returned by [`⎕WG`](../../../language-reference-guide/system-functions/wg) and event names supplied by [`⎕DQ`](../../../language-reference-guide/system-functions/dq) and [`⎕NQ`](../../../language-reference-guide/system-functions/nq) are converted to uppercase or not. It is a Boolean property where 1 means convert to upper case and 0 means not. The default is 0. For example :
```apl
      '.' ⎕WG 'Type'

Root

      '.' ⎕WS 'UpperCase' 1
      '.' ⎕WG 'Type'
ROOT
```

In Dyalog v6, property names were always reported in upper case. This was changed in Version 7. The UpperCase property is provided to enable applications developed prior to Dyalog v7 to function with minimal alteration.

**Application**

Objects: [Root](../objects/root.md)
