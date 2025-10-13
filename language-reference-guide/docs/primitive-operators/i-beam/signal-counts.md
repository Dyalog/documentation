
<!-- Hidden search keywords -->
<div style="display: none;">
  4007⌶
</div>

<h1 class="heading"><span class="name">Signal Counts</span> <span class="command">R←4007⌶Y</span></h1>

!!! note
    **UNIX, Linux and macOS only.**

`Y` must be a simple empty vector but is ignored.

The result `R` is an integer vector of signal counts. The length of the vector is system dependent. On AIX 32-bit it is 63 on AIX 64-bit it is 256 but code should not rely on the length.

Each element is a count of the number of signals that have been generated since the last call to this function, or since the start of the process. `R[1]` is the number of occurrences of signal 1 (SIGHUP), `R[2]` the number of occurrences of signal 2, and so forth.

Each time the function is called it zeros the counts; it is therefore inadvisable to call it in more than one APL thread.

Currently, only SIGHUP, SIGINT, SIGQUIT, SIGTERM and SIGWINCH are counted and all other corresponding elements of `R` are 0.



