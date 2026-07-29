# Closing the Application Window

Then we need something to allow our user to terminate our application. He will expect the application to terminate when he closes the window. We will implement this by having a callback function called `QUIT` which will simply call `⎕OFF`, that is:
```apl
     ∇ QUIT
[1]   ⎕OFF
     ∇
```

We can associate this with the Close event on the Form `TEMP`. This event will be generated when the user closes the window from its System Menu
```apl
      TEMP.onClose←'QUIT'
```

Although here we have used assignment to set the Event property, we could just as easily have defined it when we created the Form by adding `('Event' 'Close' 'QUIT')` to the right argument of `⎕WC`.
