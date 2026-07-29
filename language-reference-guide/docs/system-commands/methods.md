

# <span>List Methods</span> `)METHODS`

The `)METHODS` system command lists the Methods that apply to the object associated with the current space.

For example:
```apl
      ⎕CS 'F' ⎕WC 'Form'
      )METHODS
Animate ChooseFont   Detach  GetFocus    GetTextSize Wait
```

`)METHODS` produces no output when executed in a pure (non-GUI) namespace, for example:
```apl
      ⎕CS 'X' ⎕NS ''
      )METHODS
```
