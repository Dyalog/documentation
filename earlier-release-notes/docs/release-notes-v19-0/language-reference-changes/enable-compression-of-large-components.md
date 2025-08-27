<h1 class="heading"><span class="name">Enable Compression of Large Components</span> <span class="command">{R}←3012⌶Y</span></h1>

Specifies whether large components (>2GB) may be compressed.

`Y` is an integer defined as follows:

|Value|Description|
|---|---|
|0|Large components will not be compressed|
|1|Large components will be compressed if Z property is 1 (see [File Properties](https://help.dyalog.com/19.0/index.htm#Language/System%20Functions/fprops.htm#FileProperties) ) , but versions of Dyalog prior to 19.0 will not be able to read them.|

The shy result `R` is the previous value of this setting.
