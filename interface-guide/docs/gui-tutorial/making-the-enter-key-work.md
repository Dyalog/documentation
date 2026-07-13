# Making the Enter Key Work

Ok, so the basic application works. Let's look at what we can do to improve it.

The first thing we can do is to let the user press the Enter key to make the system re-calculate, rather than having to click on a button. There are a number of alternatives, but we will do it using the Default property of Buttons.

In any Form, you can allocate a single Button to be the Default Button. In simple terms, pressing Enter anywhere in the Form has the same effect as clicking the Default Button. Let's do this for the "F->C" Button :
```apl
      TEMP.F2C.Default←1
```

Now type a number into the Fahrenheit field and then press the Enter key. As you will see, this fires the Default Button labelled "F->C". The only problem with this is that the user cannot run the calculation the other way round using the Enter key. We need some mechanism to switch which Button is the Default one depending upon which field the user typed in.

This is easily achieved by making use of the GotFocus event. This is generated when the user puts the cursor into the edit field prior to typing. So all we need do is attach a callback to set the Default Button whenever a GotFocus event occurs in either edit field. We could use two separate callbacks or we could make use of the fact that you can make APL supply data of your choice to a callback when it is fired. This is supplied as its left argument.

The first of the next two statements attaches the callback function `'SET_DEF'` to the GotFocus event in the Fahrenheit edit field. It also specifies that when APL runs the callback, it should supply the character vector `'TEMP.F2C'` to `SET_DEF` as its left argument. `'TEMP.F2C'` is of course the name of the Button which we want to make the Default one. The second statement is identical, except that it instructs APL to supply the name of the Centigrade to Fahrenheit Button `'TEMP.C2F'`
```apl
      TEMP.F.onGotFocus ← 'SET_DEF' 'TEMP.F2C'
      TEMP.C.onGotFocus ← 'SET_DEF' 'TEMP.C2F'
```

Where the callback `'SET_DEF'` is defined as...
```apl
     ∇ BTN SET_DEF MSG
[1]    BTN ⎕WS'Default' 1
     ∇
```

Now let's test the application again. Try typing numbers in both fields and pressing enter each time.
