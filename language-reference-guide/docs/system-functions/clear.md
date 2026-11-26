---
search:
  boost: 2
---

# <span>Clear Workspace</span> `⎕CLEAR`{{key}}

This is a system constant. Evaluating it replaces the active workspace with a clear workspace, whose name is `CLEAR WS`.

<h2 class="example">Example</h2>

```apl
      x←42
      ⎕CLEAR
      x
VALUE ERROR: Undefined name: x
      x
      ∧
      ⎕WSID
CLEAR WS
```

## What Is Kept

`⎕CLEAR` keeps the session namespace `⎕SE` and its contents, and the [system variables](system-functions-by-category.md#system-variables) that relate to the session, `⎕PATH` and `⎕PW`. All the other system variables have their default values in the clear workspace.

A .NET object in `⎕SE` is kept, but it is disconnected from .NET, so calling one of its methods signals `VALUE ERROR`.

<h3 class="example">Example</h3>

```apl
      ⎕PW←60 ⋄ ⎕IO←0
      ⎕SE.Note←'kept'
      ⎕CLEAR
      ⎕PW ⎕IO
60 1
      ⎕SE.Note
kept
```

## Execution

`⎕CLEAR` ends all execution. Nothing after it runs, whether on the same line or in the functions that called the one in which it is evaluated.

<h3 class="example">Example</h3>

```apl
      ∇ Tidy
[1]    ⎕←'before'
[2]    ⎕CLEAR
[3]    ⎕←'after'
      ∇
      Tidy ⋄ ⎕←'next'
before
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕CLEAR CLEAR
</div>
