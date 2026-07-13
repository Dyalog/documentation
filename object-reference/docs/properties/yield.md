# <span>Yield</span> <span>Property</span>

**Applies To:** [Root](../objects/root.md)

**Description**

This property determines how frequently Dyalog checks the windows message queue. The message queue contains the underlying Windows messages for User interface events, such as mouse clicks, timers, and so on. Dyalog needs to check for the existence of these messages in order to pass them on to any GUI windows that may exist. In addition the windows message queue is used to handle interrupts and to implement the session window.

The value of Yield is an integer expressed in 1/1000's of a second. Its default value is 200. Yield defines the period of time allowed to elapse between the execution of successive lines of APL code before APL yields to Windows by requesting a message from the Windows queue. If Yield is set to zero APL does not explicitly yield.

Note that the value of this property only controls the yield frequency when APL is executing user-defined code. APL may also yield implicitly during [`⎕DQ`](../../../language-reference-guide/system-functions/dq), [`⎕NQ`](../../../language-reference-guide/system-functions/nq), [`⎕WC`](../../../language-reference-guide/system-functions/wc), `⎕SR`, [`⎕WS`](../../../language-reference-guide/system-functions/ws) and [`⎕WG`](../../../language-reference-guide/system-functions/wg) and in communicating with Auxiliary processors. Note that setting Yield to 0 (or to a very high value) during the execution of code that does not implicitly yield will effectively de-activate all other applications (including Program manager) and disable APL interrupts (Ctrl+Break). It should therefore be used with extreme caution.
