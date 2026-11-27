# Ride_Spawned

!!! Info "Information"
    This configuration parameter is only relevant when using Ride.

Whether `⎕SR` and `)SH` are disabled. It is used to prevent user interfaces that a Ride session does not support (and which would otherwise make the session unresponsive) from being executed.

Valid values are:

- `0` : `⎕SR` and `)SH` behave normally
- non-zero : `⎕SR` and `)SH` are disabled and instead generate a `DOMAIN ERROR`

<!-- REVIEW(default): default value not present in the migrated source; confirm. -->

For more information, see the [Ride User Guide](https://dyalog.github.io/ride).
