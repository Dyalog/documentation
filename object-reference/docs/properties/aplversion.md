# <span>APLVersion</span> <span>Property</span>

**Description**

This is a read-only property that provides information about the Version of Dyalog APL that you are using. It is
a 4-element vector of character vectors as described in the table below. In future releases these values may change, be removed, or new ones added.

|Index|Description              |Possible Values  |
|-----|-------------------------|-----------------|
|`[1]`|Target Environment       |Windows<br/>Windows-64<br/>Windows Mobile<br/>Linux<br/>Linux-64<br/>AIX<br/>AIX-64<br/>Mac-64<br/>Solaris<br/>Solaris-64|
|`[2]`|Version Number           |&nbsp;|
|`[3]`|Version Type             |`W` Windows<br/>`S` Server (terminal) version<br/>`M` Motif |
|`[4]`|Program Type             |Development<br/>Runtime<br/>DLL<br/>DLLRT|

<h2 class="example">Example</h2>
```apl
      '.'⎕WG'APLVersion'
┌──────────┬────────────┬─┬───────────┐
│Windows-64│18.0.38434.0│W│Development│
└──────────┴────────────┴─┴───────────┘

```

**Application**

Objects: [Root](../objects/root.md)
