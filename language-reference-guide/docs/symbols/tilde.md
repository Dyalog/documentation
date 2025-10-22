---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Tilde</span> <span class="command">~</span></h1>

Monadic Tilde means
[NOT](../primitive-functions/not.md)
```apl
      ~ 0 1 0 1
1 0 1 0
```

Dyadic Tilde means
[Without](../primitive-functions/without.md)
```apl
      3 1 4 1 5 ~ 5 1
3 4

      'aa' 'bb' 'cc' 'bb'  ~ 'bb' 'xx'
┌──┬──┐
│aa│cc│
└──┴──┘
```
[Language Elements](../glyphs.md)


