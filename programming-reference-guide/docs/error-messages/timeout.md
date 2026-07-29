

# <span>TIMEOUT</span> `1006`

This report is given when the time limit specified by the system variable `⎕RTL` is exceeded while awaiting input through character input (`⍞`) or `⎕SR`.

It is also reported by `⎕FHOLD` if it times out.

It is usual for this error to be trapped.

<h2 class="example">Example</h2>
```apl
      ⎕RTL←5 ⋄ ⍞←'RESPOND WITHIN 5 SECONDS: ' ⋄ R←⍞
RESPOND WITHIN 5 SECONDS:
TIMEOUT
      ⎕RTL←5 ⋄ ⍞←'RESPOND WITHIN 5 SECONDS: ' ⋄ R←⍞
                                                  ^
```
