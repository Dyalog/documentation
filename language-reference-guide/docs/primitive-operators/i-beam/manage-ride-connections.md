
<!-- Hidden search keywords -->
<div style="display: none;">
  3502⌶
</div>

<h1 class="heading"><span class="name">Manage Ride Connections</span> <span class="command">R←3502⌶Y</span></h1>

`3502⌶` gives control over Ride connections to the interpreter. More details about Ride can be found in the [Ride User Guide](https://dyalog.github.io/ride).

`Y` may be either `0` or `1` or a simple character vector.

`R` has the value `0` if the call to `3502⌶` was successful; if unsuccessful the value may be either a positive or negative integer.

If `Y` is `0`, then any active Ride connections are disconnected, and no future connections may be made.

If `Y` is `1`, then the interpreter attempts to enable Ride, using the value of the initialisation string to determine the connection details.  If the current initialisation string is ill-defined, `R` will be 64. If the Conga DLL/shared libraries are not available,  `R` will be 32. In previous versions of Dyalog there were separate Ride and Conga DLLs/shared libraries; these have been merged into one set in 16.0.

If `Y` is a character vector and Ride is currently disabled, then the current initialisation string is unconditionally replaced by the contents of `Y`. If Ride is currently enabled, the initialisation string is not replaced, and `R` will have the value `¯2`.

The initialisation string has the same syntax as the value of the **RIDE_INIT** configuration parameter which is described in the [Ride User Guide](https://dyalog.github.io/ride).

The configuration parameter **RIDE_INIT** can still be used to establish the initial value of the Ride initialisation string.

The runtime interpreter has Ride disabled by default, whether or not **RIDE_INIT** is set; the only method of enabling Ride in a runtime interpreter is to  call `3502⌶1`.

If **RIDE_INIT** is set when a development interpreter is called, Ride will be enabled provided that the Ride DLL/shared library is available and the **RIDE_INIT** variable is properly formed. If the connection is of type SERVE the port must not be in use.  If any of these conditions are not met, then the interpreter fails with a non-zero exit code.  If **RIDE_INIT** is not set then the development interpreter will start, but with Ride disabled.

It is therefore possible to override the **RIDE_INIT** variable in the development interpreter with code similar to:
```apl

      r←3502⌶0             ⍝ Stop Ride
      r←3502⌶'SERVE::4511' ⍝ Update init string
      r←3502⌶1             ⍝ Start Ride
                          
```

and similarly for altering the Ride settings in an active APL session.

!!! note
    In 14.1 and earlier `3502⌶⍬` was used to enable Ride; this value is still valid, albeit deprecated: code should call `3502⌶1` instead.

Enabling Ride to access applications that use the run-time interpreter means that the APL code of those applications can be accessed. The I-beam mechanism described above means that the APL code itself must grant the right for a Ride client to connect to the run‑time interpreter. Although Dyalog Ltd might change the details of this mechanism, the APL code will **always** need to grant connection rights. In particular, no mechanism that is only dependent on configuration parameters will be implemented.



