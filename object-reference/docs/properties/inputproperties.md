# <span>InputProperties</span> <span>Property</span>

When an ActiveX Control or .NET Class is used as a child of the [Grid](../objects/grid.md), InputProperties is used to specify how the value in each [Grid](../objects/grid.md) cell corresponds to the value of one or more properties of the child object.

For example, suppose there is a third-party ActiveX Control that displays a playing card. The control has two properties named Suit and Value that specify the suit (1=clubs, 2=diamonds, 3=hearts, 4=spades) and card value (1="Ace", 2="2", …11="Jack",…) respectively. To display these cards in a [Grid](../objects/grid.md), the InputProperties property may be set to `('Suit' 'Value')` and each element of the [Values](values.md) property must be a 2-element integer vector specifying the suit and value of the corresponding card.
```apl
     'CARDS'⎕WC'OCXClass' '...'
     'F'⎕WC'Form'
     'F.G'⎕WC'Grid'
     'F.G.card'⎕WC'CARDS'
     F.G.Input←'F.G.card'
     F.G.InputProperties←'Suit' 'Value'
     F.G.Values←⍳4 13
```

If InputProperties is not specified, the *default* property of the ActiveX Control or .NET Class is used.
