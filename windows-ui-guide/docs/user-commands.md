<h1 class="heading"><span class="name">User Commands</span></h1>

Dyalog includes a mechanism to define *User Commands*.

User commands are developer tools, written in APL, which can be executed without having to explicitly copy code into your workspace and/or save it in every workspace in which you want to use it.

A User Command is a name prefixed by a closing square bracket, which may be niladic or take an argument. A User Command executes APL code that is typically stored somewhere outside the current active workspace.

By default, the existing SPICE command processor is hooked up to the user command mechanism, and a number of new SPICE commands have been added. For example:
```apl
      ]Display 'hello' (⍪'world')
┌→────────────┐
│ ┌→────┐ ┌→┐ │
│ │hello│ ↓w│ │
│ └─────┘ │o│ │
│         │r│ │
│         │l│ │
│         │d│ │
│         │w│ │
│         └─┘ │
└∊────────────┘
```

The implementation of User Commands is very simple: If a line of input begins with a closing square bracket (`]`), and there exists a function by the name `⎕SE.UCMD`, then the interpreter will call that function, passing the input line (without the bracket) as the right argument.

To add a user command, drop a new Spice command file in the folder SALT\Spice.
