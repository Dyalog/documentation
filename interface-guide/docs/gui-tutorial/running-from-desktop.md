# Running from Desktop

Now that we have a final working application, it would be nice to add it as a shortcut, so that the user can run it from the Start Menu or from the Desktop, like any other application.

First we need to define `⎕LX` so that the application starts automatically.
```apl
      ⎕LX ← '⎕DQ''.'''
```

or, to avoid so many confusing quotes...
```apl
      ⎕LX ← ⍞
⎕DQ '.'
```

Next, it would be a good idea to clear the edit fields and ensure that the scrollbar is in its default position:
```apl
      'TEMP.F' ⎕WS 'Text' ''
      'TEMP.C' ⎕WS 'Text' ''
      'TEMP.S' ⎕WS 'Thumb' 1
```

Then we must `)SAVE` the workspace in a suitable directory to which we have write-access ...
```apl
      )SAVE c:\MyWS\TEMP
c:\MyWS\TEMP.dws saved Wed Jun  1 14:53:48 2016

```

... and exit APL
```apl
      )OFF
```

The next step is to add the application to the Desktop. This is done in the normal way, that is:

Right-click on the Desktop and choose "New" followed by "Shortcut".

Browse to the Dyalog program and add the name of the workspace to the command line.

![](../img/temperature-converter-12.png)

Select "Next" and give the application a name, then select "Finish".

![](../img/temperature-converter-13.png)

The resulting icon is shown below. Note that although by default you will get a standard Dyalog APL icon, you could of course select another one from elsewhere on your system.

![](../img/temperature-converter-14.png)

Clicking on this icon will start your application. Notice that the APL Session Window will NOT appear at any stage unless there is an error in your code. All the user will see is your "Temperature Converter" dialog box.
