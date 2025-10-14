
<!-- Hidden search keywords -->
<div style="display: none;">
  2023⌶
</div>

<h1 class="heading"><span class="name">Close All Windows</span> <span class="command">R←2023⌶Y</span></h1>

Under Windows the option, *Windows -> Close All Windows* allows the user to close all open Editor and Tracer Windows, but does not reset the *state indicator*.

This I-beam mimics this behaviour, thus allowing the user to write code which can close all windows before attempting to save the workspace; with the exception of calling `0 ⎕SAVE` it is not possible to save a workspace if any editor or tracer windows are open.

Under non-Windows operating systems this is the only mechanism for closing all such windows. This I-beam is effective in Ride too.

<h2 class="example">Example</h2>
```apl
      2023⌶0    
```
