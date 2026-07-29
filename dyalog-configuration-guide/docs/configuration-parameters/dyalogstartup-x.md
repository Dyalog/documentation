# DyalogStartup_X

During Session initialisation, code is loaded from the directories given by [`DyalogStartupSE`](dyalogstartupse.md) into a corresponding namespace tree in `⎕SE`, and is then optionally executed. This parameter controls that execution.

Valid values are:

- `0` : the `Run` function (if it exists) in each top-level namespace loaded during Session start-up is executed, in alphabetical order of namespace
- `1` : the `Run` function is not executed

Other values are reserved for future extension.

Default is `0`.

Related parameters: [DyalogStartupSE](dyalogstartupse.md).
