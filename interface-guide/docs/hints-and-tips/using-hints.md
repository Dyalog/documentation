# Using Hints

All of the GUI objects supported by Dyalog APL that have a visible presence on the screen have a Hint property and a HintObj property. Quite simply, when the user moves the mouse pointer over the object the contents of its Hint property are displayed in the object referenced by its HintObj property. When the user moves the mouse pointer away from the object, its Hint disappears. If an object has a Hint, but its HintObj property is empty, the system uses the HintObj defined for its parent, or for its parent's parent, and so forth up the tree. If there is no HintObj defined, the Hint is simply not displayed. This mechanism has two useful attributes:

1. it allows you to easily define a single region for help messages for all of the controls in a Form, but still provides the flexibility for using different message locations for different controls if appropriate.
2. to enable or disable the display of hints all you typically have to do is to set or clear the HintObj property on the parent Form

The object named by HintObj may be any object with either a Caption property or a Text property. Thus you can use the Caption on a Label, Form, or Button or the text in an Edit object. If you use a StatusField object which has both Caption *and* Text properties, the Text property is employed. If you set HintObj to the name of an object which possesses neither of these properties, the hints will simply not be displayed. The following example illustrates the use of a StatusField for displaying hints.

## Example: Using a StatusField for Hints

This example illustrates the use of a StatusField object to display hints. .
```apl

    'Test'⎕WC 'Form' 'Using Hints'('HintObj' 'Test.SB.H')
 
    'Test.MB' ⎕WC 'MenuBar'
    'Test.MB.F' ⎕WC 'Menu' '&File'
    HINT ← 'Creates a new empty document'
    'Test.MB.F.New' ⎕WC 'MenuItem' '&New' ('Hint' HINT)
 
    'Test.SB' ⎕WC 'StatusBar'
    'Test.SB.H' ⎕WC 'StatusField' ('Size' ⍬ 98)
```

![](../img/hints-statusbar.png)

Using a StatusBar to display Hints

## Example: Using an Edit Object for Hints

You can display a much larger amount of information using a multi-line Edit object as shown in this example.
```apl
     'Test'⎕WC 'Form' 'Using Hints' ('HintObj' 'Test.ED')
      'Test.MB' ⎕WC 'MenuBar'
      'Test.MB.F' ⎕WC 'Menu' '&File'
      HINT ← 100⍴'Creates a new empty document '
      'Test.MB.F.New' ⎕WC 'MenuItem' '&New' ('Hint' HINT)
```
```apl
      'Test.ED' ⎕WC 'Edit' ('Style' 'Multi')
```

![](../img/hints-edit.png)

Displaying Hints in an Edit object
