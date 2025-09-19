<h1 class="heading"><span class="name">Semaphore Example</span></h1>

A *semaphore* to control a number of resources can be implemented by keeping that number of tokens in the pool. Each thread will take a token while processing, and return it to the pool when it has finished.

For example, if we want to restrict the number of threads that can have sockets open at any one time.
```apl
    sock←99                  ⍝ socket-token
                               any +ive number will do).
    ⎕TPUT 5/sock             ⍝ add 5 socket-tokens to pool.
 
    ∇ sock_open ...
[1]   :If sock=⎕TGET sock    ⍝ grab a socket token
[.]       ...                ⍝ do stuff.
[.]       ⎕TPUT sock         ⍝ release socket token
[.]   :Else
[.]       error'sockets off' ⍝ sockets switched off by
                               retract (see below).
[.]   :EndIf
    ∇
 
    0 ⎕TPUT ⎕TREQ ⎕TNUMS     ⍝ retract socket "service"
                               with 0 value.
```
