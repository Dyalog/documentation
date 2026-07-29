

# <span>Display Held Tokens</span> `)HOLDS`

System command `)HOLDS` displays a list of tokens which have been acquired or requested by the `:Hold` control structure.

Each line of the display is of the form:
```apl
token:  acq  req  req ...
```

Where `acq` is the number of *the* thread that has acquired the token, and `req` is the number of *a* thread which is requesting it. For a token to appear in the display, a thread (and only one thread) must have acquired it, whereas any number of threads can be requesting it.

<h2 class="example">Example</h2>

Thread `300`’s attempt to acquire token `'blue'` results in a deadlock:
```apl
300:DEADLOCK
Sema4[1] :Hold 'blue'
        ^
 
      )HOLDS
blue:   100
green:  200     100
red:    300     200     100
 
```

- `Blue` has been acquired by thread `100`.
- `Green` has been acquired by `200` and requested by `100`.
- `Red` has been acquired by `300` and requested by `200` and `100`.

The following cycle of dependencies has caused the deadlock:
```
Thread 300 attempts to acquire blue,      300 → blue
which is owned by 100,                     ↑      ↓
which is waiting for red,                 red ←  100
which is owned by 300.
```
