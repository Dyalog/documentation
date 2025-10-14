
<!-- Hidden search keywords -->
<div style="display: none;">
  3012⌶
</div>

<h1 class="heading"><span class="name">Enable Compression of Large Components</span> <span class="command">{R}←3012⌶Y</span></h1>

Specifies whether large components (>2GB) may be compressed.

`Y` is an integer defined as follows:

| Value | Description |
|-------|---------------|
| 0     | Large components will not be compressed. |
| 1     | Large components will be compressed if Z property is 1 (see [File Properties](../../system-functions/fprops.md)), but versions of Dyalog prior to v19.0 will not be able to read them.|

The shy result `R` is the previous value of this setting.
