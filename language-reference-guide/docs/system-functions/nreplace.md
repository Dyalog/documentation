---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕NREPLACE NREPLACE
</div>

<h1 class="heading"><span class="name">Native File Replace</span> <span class="command">{R}←X ⎕NREPLACE Y</span></h1>

`⎕NREPLACE` is used to write data to a native file, replacing data which is already there.

`X` must be a simple homogeneous APL array containing the data to be written.

`Y` is a 2- or 3-element integer vector whose elements are as follows:

|-----|----------|
|`[1]`|negative tie number,|
|`[2]`|start byte, counting from 0, at which the data is to be written; the value `¯1` causes the data to be written from the current position in the file (initially, 0).|
|`[3]`|conversion code (optional).|

See [Native File Read](nread.md) for a list of valid conversion codes.

The shy result is the location of the internal file pointer which will be pointing to the end of the newly written data. Used, for example, in:
```apl

      ⍝ Replace sequentially from indx.
      {⍺ ⎕NREPLACE tie ⍵}/vec,indx 
```

Note that `8 ⎕NINFO ⊃Y`  can be used to report the current position of the file pointer.

## Unicode Edition

Unless you specify the data type in `Y[3]`, a character array will by default be written using type 80.

If the data will not fit into the specified character width (bytes) `⎕NREPLACE` will fail with a `DOMAIN ERROR`.

As a consequence of these two rules, you must specify the data type (either 160 or 320) in order to write Unicode characters whose code-point is in the range 256-65535 and >65535 respectively.

<h2 class="example">Example</h2>
```apl

      n←'test'⎕NTIE 0 ⍝ See "Example"

      ⎕NREAD n 80 3 0
abc
      ⎕NREAD n 160 7
ταβέρνα

      ⎕←'εστιατόριο'⎕NREPLACE n 3
DOMAIN ERROR
      ⎕←'εστιατόριο'⎕NREPLACE n 3
     ∧

      ⎕←'εστιατόριο'⎕NREPLACE n 3 160
23
      ⎕NREAD n 80 3 0
abc
      ⎕NREAD n 160 10
εστιατόριο
```

For compatibility with old files, you may specify that the data be converted to type 82 on output. The conversion (to `⎕AV` indices) will be determined by the local value of `⎕AVU`.
