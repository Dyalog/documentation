# Defining Classes

A Class is defined by a script that may be entered and changed using the editor. A class script may also be constructed from a vector of character vectors, and fixed using `⎕FIX`.

A class script begins with a [`:Class` statement](../../defined-functions-and-operators/traditional-functions-and-operators/control-structures/class.md) and ends with a `:EndClass` statement.

For example, using the editor:
```apl
      )CLEAR
clear ws
      )ED ○Animal
```

[an edit window opens containing the following skeleton Class script ...]
```apl
:Class Animal
:EndClass
```

[the user edits and fixes the Class script]
```apl
      )CLASSES
Animal
      ⎕NC⊂'Animal'
9.4
```
