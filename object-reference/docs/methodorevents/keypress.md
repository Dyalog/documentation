# <span>KeyPress</span> <span>Event 22</span>

[**Applies To**](../methodoreventapplies/keypress.md)

**Description**

If enabled, this event is generated when the user presses and releases a key
on the keyboard. It is reported for whichever object has the keyboard focus at
the time.

The event message reported as the result of [`⎕DQ`](../../../language-reference-guide/system-functions/dq),
or supplied as the right argument to your callback function, is a 6-element
vector as follows :

|-----|--------------|--------------------------|
|`[1]`|Object        |ref or character vector   |
|`[2]`|Event         |`'KeyPress'` or 22        |
|`[3]`|Input Code    |character scalar or vector|
|`[4]`|Character code|integer scalar            |
|`[5]`|Key Number    |integer scalar            |
|`[6]`|Shift state   |integer scalar            |

If the keystroke resolves to a character, the Input Code is a character
scalar.

If the keystroke resolves to a command recognised by Dyalog APL, such as UC
(Up Cursor) or ER (Enter) the Input Code contains the corresponding 2-element
character vector.

In the Classic Edition, the resolution of the keystroke to a character (in `⎕AV`)
or to a command, is performed using the Input Translate Table.

In the Unicode Edition, the resolution is performed by the Operating System.
However, if the keystroke resolves to a navigation or control key (such as
Cursor Up or Enter), the same 2-character "command" is reported. Note
however that commands that are purely internal to Dyalog APL (such as Trace,
commonly Ctrl+Enter) are not reported as such and the Input Code will be empty.

In the Unicode Edition, the Character Code is the Unicode code point of the
character that the user entered. In the Classic Edition, it is a number in the
range 0-255 which specifies the ASCII character that would normally be generated
by the keystroke, and is independent of the Input Translate Table. If there is
no corresponding ASCII character, the ASCII code reported is 0.

The key number is the physical key number reported by Windows when the key is
pressed.

The Shift State indicates which (if any) of the Shift, Ctrl and Alt keys are
down at the same time as the key is pressed. It is the sum of the following
numbers :

|---|----------------|
|1  |Shift key down  |
|2  |Control key down|
|4  |Alt key down    |

Thus a Shift State of 3 indicates that the user has pressed the key in
conjunction with both the Shift and Ctrl keys. A Shift State of 0 indicates that
the user pressed the key on its own.

<h2 class="example">Example</h2>
```apl
     ∇ Key;Form1
[1]    'Form1'⎕WC'Form'('Event' 'KeyPress' 'Keycb')
[2]    ⎕DQ'Form1'
     ∇

     ∇ Keycb msg
[1]    DISPLAY msg
     ∇
```

On running function Key, the following output will be displayed as a result
of the user pressing the following 5 keys in succession:

1. "a"
2. Shift+"a"
3. Cursor Up
4. β ("b" using a Greek keyboard)
5. `⍳` (Ctrl+"i" using a UK APL
    keyboard)

## Unicode Edition
```apl

┌→─────────────────────────────┐
│ ┌→────┐ ┌→───────┐           │
│ │Form1│ │KeyPress│ a 97 65 0 │
│ └─────┘ └────────┘ -         │
└∊─────────────────────────────┘
┌→─────────────────────────────┐
│ ┌→────┐ ┌→───────┐           │
│ │Form1│ │KeyPress│ A 65 65 1 │
│ └─────┘ └────────┘ -         │
└∊─────────────────────────────┘

```
```apl

┌→───────────────────────────────┐
│ ┌→────┐ ┌→───────┐ ┌→─┐        │
│ │Form1│ │KeyPress│ │UC│ 0 38 0 │
│ └─────┘ └────────┘ └──┘        │
└∊───────────────────────────────┘
┌→───────────────────────────────┐
│ ┌→────┐ ┌→───────┐             │
│ │Form1│ │KeyPress│ β 9075 90 1 │
│ └─────┘ └────────┘ -           │
└∊───────────────────────────────┘
┌→───────────────────────────────┐
│ ┌→────┐ ┌→───────┐             │
│ │Form1│ │KeyPress│ ⍳ 9075 73 2 │
│ └─────┘ └────────┘ -           │
└∊───────────────────────────────┘

```

## Classic Edition
```apl

┌→─────────────────────────────┐
│ ┌→────┐ ┌→───────┐           │
│ │Form1│ │KeyPress│ a 97 65 0 │
│ └─────┘ └────────┘ -         │
└∊─────────────────────────────┘
┌→─────────────────────────────┐
│ ┌→────┐ ┌→───────┐           │
│ │Form1│ │KeyPress│ A 65 65 1 │
│ └─────┘ └────────┘ -         │
└∊─────────────────────────────┘
┌→───────────────────────────────┐
│ ┌→────┐ ┌→───────┐ ┌→─┐        │
│ │Form1│ │KeyPress│ │UC│ 0 38 0 │
│ └─────┘ └────────┘ └──┘        │
└∊───────────────────────────────┘
┌→────────────────────────────────┐
│ ┌→────┐ ┌→───────┐ ┌⊖┐          │
│ │Form1│ │KeyPress│ │ │ 223 66 0 │
│ └─────┘ └────────┘ └─┘          │
└∊────────────────────────────────┘
┌→────────────────────────────┐
│ ┌→────┐ ┌→───────┐          │
│ │Form1│ │KeyPress│ ⍳ 9 73 2 │
│ └─────┘ └────────┘ -        │
└∊────────────────────────────┘

```
