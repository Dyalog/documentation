# APLTn

!!! Info "Information"
    This configuration parameter is only relevant when using the Classic edition of Dyalog on the UNIX and macOS operating systems.

An output translate table that overrides [`APLT`](aplt.md), if set. The name ends with a digit (for example `APLT0`), so that more than one can be defined. It takes precedence over the table implied by the terminal type.

Valid values are the name of an output translate table.
<!-- REVIEW(default): default value not present in the migrated source; confirm the naming convention. -->

Related parameters: [APLT](aplt.md), [APLTrans](apltrans.md).
