# <span>GetBuildID</span> <span>Method 992</span>

This method is used to obtain the Build ID of a Dyalog executable or the checksum of a file.

The argument to GetBuildID is `⍬` or a
single item as follows:

|-----|---------|----------------|
|`[1]`|File name|character vector|

The ([shy](../../../programming-reference-guide/introduction/results#shy-results)) result is an 8-element character vector of hexadecimal digits that
represents the Build ID.

If the argument is `⍬`, the build id is
that of the current version of Dyalog that is running the expression.

Although this method is designed to uniquely identify different versions of Dyalog by the checksum, it can be used to obtain a checksum
for *any* arbitrary file.

<h2 class="example">Examples</h2>
```apl
      GetBuildID ⍬
38091b76
      GetBuildID 'E:\DYALOG81\DYALOG.EXE'
cbf0d376
      GetBuildID 'myfile'
4a29334d
```

If the file does not exist, the result is 00000000.

## Application

Objects: [Root](../objects/root.md)
