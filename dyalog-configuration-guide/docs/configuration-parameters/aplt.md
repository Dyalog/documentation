# APLT

!!! Info "Information"
    This configuration parameter is only relevant when using the Classic edition of Dyalog.

The name of the Output Translate Table. There is rarely a need to alter it.

Valid values are the name of an output translate table.

On a terminal, the default is the value of the `TERM` environment variable, or `default` if `TERM` is not set. When input and output are redirected to a file, the default is `utf8` for a `#!` script and `redirected` otherwise. On Microsoft Windows, `.dot` is appended, and `TERM` is itself `win` by default, so the default there is `WIN.DOT`.

Related parameters: [APLTrans](apltrans.md).

See also the [Output tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-output-tab-classic-edition-only) of the Windows Configuration Dialog.
