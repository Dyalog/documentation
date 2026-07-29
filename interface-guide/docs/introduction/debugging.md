# Debugging

Four features are built into the system to assist in developing and debugging GUI applications.

Firstly, if you execute `⎕WC` and/or `⎕WS` statements from the Session or by tracing a function, they have an **immediate** effect on the screen. Thus you can see immediately the visual result of an expression, and go back and edit it if it isn't quite what you want.

Secondly, if you use `⎕WC` with an existing name, the original object is destroyed and then re-created. This allows you to repeatedly edit and execute a single statement until it gives the effect you desire.

Thirdly, if you TRACE a `⎕DQ` statement, any callback functions that are invoked will be traced as they occur. This is invaluable in debugging. However, callbacks invoked by certain "raw" events, for example MouseMove, can be awkward to trace as the act of moving the mouse pointer to the Trace window interferes with the operation in the object concerned.

Finally, `⎕NQ` can be used to artificially generate events and sequences of events in a controlled manner. This can be useful for developing repeatable test data for your application.
