# Including Script Files in Scripts

A Class or Namespace script in the workspace or in a script file may specify that other  script files are to be loaded prior to the fixing of the script itself. To do so, it must begin with one or more `:Require` statements, with the following syntax:
```apl
:Require file://[path]/file
```

If no `path` is specified, the path is taken to be relative to the current script file or, if in a workspace script, the current working directory. Note that a leading `'./'` or `'.\'` in `path` is not  allowed, to avoid any potential confusion with "current directory".

`:Require` is a directive to the Editor (more specifically, to the internal mechanism that fixes a script as an object in the workspace) and can appear in any script containing APL code, but **must** precede all code in the script. `:Require` is thus not valid within a function, class, namespace or any other definition.

The prefix `file://`  allows for the possibility of a future extension of `https://` and `ftp://`.

In version {{ version_majmin }} `⍝!:require` is a synonym for `:Require`.  This allows the user to create scripts which can be used in multiple versions of Dyalog; in 14.1 and earlier SALT parses `⍝!:require` statements and loads the appropriate files, in {{ version_majmin }} it is the interpreter loads the file named in `⍝!:require` statements.   Dyalog intends to remove support for the `⍝!:require` statement from the interpreter in a future version. Note that unlike `:Require`, `⍝!:require` can appear within code.
