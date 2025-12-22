## Initiating the Collection of Data

Data collection is initiated by entering:
```apl
⎕PROFILE'start'
```

This puts ⎕PROFILE into an active state.

⎕PROFILE supports profiling using either CPU or elapsed time. CPU
time is usually of more interest in profiling application performance
and, by default, ⎕PROFILE will register CPU usage data using the
best available counter.
