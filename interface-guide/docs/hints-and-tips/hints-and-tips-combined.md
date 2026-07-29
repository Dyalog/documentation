# Hints and Tips Combined

There is no reason why you cannot provide Hints *and* Tips. The next example shows how an object, in this case a Combo, can have both defined.

<h2 class="example">Example</h2>
```apl
      'Test'⎕WC 'Form' 'Using Hints and Tips'
 
      'Test.SB' ⎕WC 'StatusBar'
      'Test.SB.H' ⎕WC 'StatusField' ('Size' ⍬ 98)
      'Test' ⎕WS 'HintObj' 'Test.SB.H'
 
      'Test.Tip' ⎕WC 'TipField'
      'Test' ⎕WS 'TipObj' 'Test.Tip'
 
      'Test.C' ⎕WC 'Combo' WINES
      'Test.C' ⎕WS 'Hint' 'Select your wine from this
                           list'
      'Test.C' ⎕WS 'Tip' 'Wine Cellar'
```

![](../img/hints-and-tips-combined.png)

Hints and Tips Combined
