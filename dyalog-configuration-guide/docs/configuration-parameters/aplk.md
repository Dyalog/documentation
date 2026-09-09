# APLK

!!! Info "Information"
    This configuration parameter is only relevant when using the Classic edition of Dyalog.

The name of the Input Translate Table, which defines the keyboard layout. The keyboard list in the Configuration dialog shows every `.DIN` file in the directory given by [`APLKeys`](aplkeys.md); any of the supplied tables can be chosen, and you can add your own. The `FILE.DIN` table is intended for input from file and should not normally be chosen as a keyboard table.

Valid values are the name of a `.DIN` input translate table.

On a terminal, the default is the value of the `TERM` environment variable, or `default` if `TERM` is not set. When input and output are redirected to a file, the default is `utf8` for a `#!` script and `redirected` otherwise. On Microsoft Windows, `.din` is appended, and `TERM` is itself `win` by default, so the default there is `WIN.DIN`.

Related parameters: [APLKeys](aplkeys.md).

See also the [Input tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-input-tab-classic-edition-only) of the Windows Configuration Dialog.
