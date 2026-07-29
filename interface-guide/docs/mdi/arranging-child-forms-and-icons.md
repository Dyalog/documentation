# Arranging Child Forms and Icons

Another common feature of MDI applications is that the user can ask for the SubForms to be displayed in a particular way, or that any SubForm icons are arranged in an orderly fashion. This is implemented in Dyalog APL/W by your application invoking an method using `⎕NQ`. The MDIClient recognises three different methods, namely MDICascade (110), MDITile (111) and MDIArrange (112).

The MDICascade method causes the child forms to be arranged in an overlapping manner. The MDITile method causes them to be tiled, either horizontally or vertically. Finally, the MDIArrange method arranges any child form icons in an orderly fashion. The most convenient way to provide these actions is to attach a Callback function to appropriate MenuItems. The callback function is called with different left arguments according to the MenuItem selected. The following code snippet illustrates this technique.

The following lines define callbacks for each of the MenuItem objects in the Menu `F1.MB.WM`. Each one uses the callback function `MDI_ARRANGE`, but with a left argument corresponding to the message that must be sent to the MDIClient to cause the desired action. For example, clicking the MenuItem named `F1.MB.WM.Vert` runs `MDI_ARRANGE` with a left argument of (`111 1`)
```apl
'F1.MB.WM.CASCADE' ⎕WS 'Event' 30 'MDI_ARRANGE' 110
'F1.MB.WM.HORZ'    ⎕WS 'Event' 30 'MDI_ARRANGE' (111 0)
'F1.MB.WM.VERT'    ⎕WS 'Event' 30 'MDI_ARRANGE' (111 1)
'F1.MB.WM.ARRANGE' ⎕WS 'Event' 30 'MDI_ARRANGE' 112
```

The `MDI_ARRANGE` function uses its left argument to construct a message for the MDIClient object, in this case `F1.MDI`, and returns it as a result. This causes the desired action.
```apl
     ∇ MSG←M MDI_ARRANGE MSG
[1]    MSG←(⊂'F1.MDI'),M
     ∇
```

An alternative approach which does not require a callback function is to use `⎕NQ`
```apl
'F1.MB.WM.CASCADE' ⎕WS 'Event' 30 '⍎⎕NQ ''F1.MDI 110'''
'F1.MB.WM.HORZ'    ⎕WS 'Event' 30 '⍎⎕NQ ''F1.MDI 111 0'''
'F1.MB.WM.VERT'    ⎕WS 'Event' 30 '⍎⎕NQ ''F1.MDI 111 1'''
'F1.MB.WM.ARRANGE' ⎕WS 'Event' 30 '⍎⎕NQ ''F1.MDI 112'''
```
