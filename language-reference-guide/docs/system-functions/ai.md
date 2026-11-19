---
search:
  boost: 2
---

# <span>Account Information</span> `R←⎕AI`{{key}}

This is a system constant: a 4-item integer vector that identifies the user and reports how much time the session has used. [`⎕SYSTEM`](system.md) gives more information of this kind, such as the user's name and the identifier of the interpreter's process.

<h2 class="example">Example</h2>

```apl
      ⎕AI
1000 312 20079 19765
```

## Result

`R` is a 4-item integer vector:

|Item |Content|
|-----|-------|
|`1⊃R`|The [user number](#user-number)|
|`2⊃R`|Compute time: the processor time that the session has used|
|`3⊃R`|Connect time: the time since the session started|
|`4⊃R`|Keying time: the time that the session has spent waiting for input from the keyboard|

The times are in milliseconds. They are for the whole session, so clearing the workspace or loading another one does not reset them. Future releases might add items to `R`.

Keying time includes waiting at the session prompt, and waiting for input to [`⎕`](evaluated-input-output.md) or [`⍞`](character-input-output.md). Input that is not typed, such as input piped to the interpreter, does not count.

<h3 class="example">Example</h3>

The difference between two values of `⎕AI` gives the times in between. A [delay](dl.md) counts as connect time but not as compute time, while a calculation counts as both:

```apl
      t←⎕AI ⋄ ⎕DL 2 ⋄ ⎕AI-t
0 2 2005 0
      t←⎕AI ⋄ x←{+/⍳⍵}¨10/1e7 ⋄ ⎕AI-t
0 226 226 0
```

## User Number

The user number identifies the user to the [access control](../../programming-reference-guide/component-files/component-files.md#user-number) of component files.

Under Microsoft Windows, the user number is the value of the [**aplnid**](../../windows-installation-and-configuration-guide/configuration-parameters/aplnid.md) configuration parameter, or `0` if that is not set.

Under Unix, the user number is the [real user identifier](https://en.wikipedia.org/wiki/User_identifier#Real_user_ID) (UID) of the interpreter's process, which `⎕SYSTEM.Host.UserId` gives as a character vector.

A user number of `0`, which is the root user's under Unix, bypasses the access matrix, leaving only the operating system's file permissions.

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AI AI
</div>
