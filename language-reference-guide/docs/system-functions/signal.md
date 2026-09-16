---
search:
  exclude: true
---

# <span>Signal Event</span> `⎕SIGNAL`

`⎕SIGNAL` generates an event under program control, or clears the information left behind by the most recent event.

The first element of the right argument chooses which action `⎕SIGNAL` performs (an empty right argument does nothing).

## [Reset Event Constants](signal-reset.md)

`0` resets the system constants describing the most recent event, without generating one:

```apl
      ⎕←⎕SIGNAL 0
0
```

## [Signal Default Event](signal-default.md)

An event number generates that event with its standard event message, which an optional left argument can replace:

```apl
      ⎕SIGNAL 200
ERROR 200
      ⎕SIGNAL 200
      ∧

      'Hello'⎕SIGNAL 200
Hello
      'Hello'⎕SIGNAL 200
             ∧
```

## [Signal Extended Event](signal-extended.md)

A set of name/value pairs generates an event with chosen values for the members of [`⎕DMX`](dmx.md):

```apl
      ⎕SIGNAL⊂('EN' 200)('Message' 'My error')
ERROR 200: My error
      ⎕SIGNAL⊂('EN' 200)('Message' 'My error')
      ∧
```
