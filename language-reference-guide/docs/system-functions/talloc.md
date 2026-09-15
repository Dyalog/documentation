---
search:
  exclude: true
---

# <span>Token Allocation</span> `⎕TALLOC`

A *token range* reserves a set of token types for one purpose, so that unrelated parts of an application can use [`⎕TPUT`](tput.md) and [`⎕TGET`](tget.md) without choosing the same types by accident. The first element of the right argument chooses which action `⎕TALLOC` performs on such ranges.

## [Allocate Token Range](talloc-allocate.md)

`⎕TALLOC 1` reserves a range and returns the number identifying it, optionally recording a description:

```apl
      ⎕←trg←⎕TALLOC 1 'cats'
1
```

## [De-allocate Token Range](talloc-deallocate.md)

`⎕TALLOC ¯1` releases the range identified by the left argument, making it free for re-allocation:

```apl
      ⎕←trg ⎕TALLOC ¯1
1
```

## [Query Allocated Token Ranges](talloc-ranges.md)

`⎕TALLOC 0` reports the ranges currently allocated and their descriptions, or the description of the one range identified by the left argument:

```apl
      ⎕TALLOC 0
┌────────┐
│┌─┬────┐│
││1│cats││
│└─┴────┘│
└────────┘
```

## [Query Pooled Tokens in Range](talloc-pool.md)

`⎕TALLOC 2` reports the tokens in the token pool that fall within the range identified by the left argument:

```apl
      trg ⎕TALLOC 2
1.5
```
