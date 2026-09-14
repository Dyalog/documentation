---
search:
  exclude: true
---

# :Trap Statement

```
 
       |
       :Trap <ecode>
       |
       code
       |
       |<------------------------------------.
       |                                     |
       .-------.-------.                     |
       |       |       |                     |
       |       :Else   :Case[List] <ecode>   |
       |       |       |                     |
       |       |       |                     |
       |       |       |                     |
       |       code    code                  |
       |       |       |                     |
       |<------'       `---------------------'
       |
       :End[Trap]
       |
```

Where `ecode` is a scalar or vector of `⎕TRAP` event codes.

Within the `:Trap` control structure, `:Case` is used for a single event code and `:CaseList` for a vector of event codes.
