<h1 class="heading"><span class="name">Trace_Level_Warn</span></h1>

This parameter specifies the maximum number of Trace windows that will be displayed when an error occurs and **Trace_on_error** is set to 1.  If there are a large number of functions in the state indicator, the display of their Trace windows may take several seconds. This parameter allows you to restrict the potential delay to a reasonable value and its default is 16. If the number of Trace windows would exceed this number, the system instead displays a warning message box. This parameter is ignored if you invoke the Tracer explicitly. This parameter applies only in Classic Dyalog mode.

See also [Warn if trace stack bigger than](../configuring-the-ide/configuration-dialog/configuration-dialog-trace-edit-tab.md).
