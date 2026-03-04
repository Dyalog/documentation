# Directory and File Manipulation

The .NET namespace System.IO (in the  System.IO.FileSystem assembly) provides some useful facilities for manipulating files. For example, you can create a DirectoryInfo object associated with a particular directory on your computer, call its GetFiles method to obtain a list of files, and then get their Name and CreationTime properties:
```apl
      ⎕USING←,⊂'System.IO, System.IO.FileSystem'
      dir←'C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode'
      d←⎕NEW DirectoryInfo (⊂dir)
```

where `d` is an instance of the Directory class, corresponding to the directory **[DYALOG]**.

**[DYALOG]** refers to the directory in which Dyalog is installed; this example assumes **[DYALOG]** to be **C:/Program Files/Dyalog/Dyalog APL-64 19.0 Unicode**.

The GetFiles method returns a list of files (more precisely, FileInfo objects) that represent each of the files in the directory. Its optional argument specifies a filter. For example:
```apl
      d.GetFiles ⊂'*.exe'
C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyaedit.exe C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyalog.exe C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyalogc.exe C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyalogc64_unicode.exe  C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyalogrt.exe  C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\dyascript.exe
```

The Name property returns the name of the file associated with the File object:
```apl
      (d.GetFiles ⊂'*.exe').Name
dyaedit.exe  dyalog.exe  dyalogc.exe  dyalogc64_unicode.exe  dyalogrt.exe  dyascript.exe
```

and the CreationTime property returns its creation time, which is a DateTime object:
```apl
     (d.GetFiles ⊂'*.exe').CreationTime
 08/02/2024 20:51:24  08/02/2024 20:50:06  08/02/2024 ...
```

Calling the GetFiles overload that does not take any arguments (from Dyalog by supplying an argument of `⍬`) returns a complete list of files:
```apl
      files←d.GetFiles ⍬
      files
C:\Program Files\Dyalog\Dyalog APL-64 19.0 Unicode\aplunicd.ini...
```

Taking advantage of namespace reference array expansion, an expression to display file names and their creation times is:
```apl
      files,[1.5]files.CreationTime
C:\...\...Unicode\aplunicd.ini               08/02/2024 20:12:02
C:\...\...Unicode\bridge190-64_unicode.dll   08/02/2024 20:47:36
...
```
