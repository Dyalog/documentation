---
search:
  boost: 2
---

# <span>Atomic Vector</span> `R←⎕AV`{{key}}

This is a system constant, a simple character vector of the 256 characters that the Classic Edition can represent. The Classic Edition stores each character as its position in `⎕AV`.

!!! Legacy "Legacy"
    `⎕AV` is retained for backwards compatibility purposes. Dyalog Ltd recommends using [`⎕UCS`](ucs.md) to convert between characters and integers instead.

In the Unicode Edition, `⎕AV` is `⎕UCS ⎕AVU`, where [`⎕AVU`](avu.md) is the value in the current namespace. Assigning `⎕AVU` therefore changes `⎕AV`. In the Classic Edition, the output translate table defines the content of `⎕AV`.

<h2 class="example">Examples</h2>

```apl
      ⎕AV[48+⍳10]
0123456789
      ⎕AV≡⎕UCS ⎕AVU
1
```

Characters that are not in `⎕AV` cannot be represented in the Classic Edition:

```apl
      ⎕AV⍳'⍺α'
15 257
      ⎕UCS'⍺α'
9082 945
      ∧/'Grüße ⍺⍵'∊⎕AV
1
      ∧/'Γειά σου'∊⎕AV
0
```

<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AV AV
</div>
