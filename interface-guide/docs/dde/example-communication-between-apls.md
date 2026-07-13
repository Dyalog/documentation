# Example: Communication Between APLs

The following instructions will allow you to explore how the DDE interface can be used to communicate between two Dyalog APL/W workspaces.

Start two separate APL sessions and arrange their windows one above the other so that they do not overlap.

Select the top window and type:
```apl
      )WSID SERVER
      A←?5 5⍴100 ⋄ A
      'DDE:' ⎕SVO 'A EXTNAME'
1
```

The result of `⎕SVO` is 1, indicating that no client has yet joined in the conversation.

Select the lower window and type:
```apl
      )WSID CLIENT
      'DDE:DYALOG|SERVER' ⎕SVO 'B EXTNAME'
      B
```

The result of `⎕SVO` is 2 indicating that the connection with the SERVER workspace has been successfully made. Now type `B`. It will have the same value as `A` in the upper window.

Select the top window (SERVER) again and type:
```apl
      A←⌹A
      ⎕SVS 'A'
1 0 1 0
```

Note that the result of `⎕SVS` indicates that the SERVER has set `A`, but the CLIENT has not yet referenced the value.

Select the lower window (CLIENT) and type:
```apl
      ⎕SVS 'B'
0 1 0 1
      B
...
      ⎕SVS 'B'
0 0 1 1
```

Note how, after referencing the shared variable, its state has changed.

Still in the CLIENT workspace, write the following function called `FOO`:
```apl
     ∇ FOO
[1]   ⍝ This function gets called on event 50 (DDE)
[2]    →(0 0 1 1≡⎕SVS'B')/0 ⍝ Exit if no change
[3]    B
     ∇    
```

Then, to attach `FOO` as a callback and to "wait"...
```apl
      '.' ⎕WS 'Event' 50 'FOO'
⎕DQ '.'
```

Now switch to the upper window (SERVER) and type:
```apl
      A←⌹A
```

Type this expression repeatedly, or experiment with others. Note how changing `A` generates a DDE event (event number 50) on the system object `'.'` in CLIENT, which in turn fires the callback.

To interrupt `⎕DQ` in the CLIENT, type Ctrl+Break or select "Interrupt" from the *Action* menu in the Session Window.
