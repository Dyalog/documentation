# APLKeys

!!! Info "Information"
    This configuration parameter is only relevant when using the Classic edition of Dyalog.

A search path for the Input Translate Table, useful when configuring a run-time application. Directory paths use the operating system's conventions and are separated by `;` (Windows) or `:` (UNIX and macOS).

Valid values are a list of directory paths.

Default is the `aplkeys` sub-directory of the Dyalog installation directory (given by [`Dyalog`](dyalog.md)).

On UNIX and macOS, if this parameter is unset the search path defaults to the directory given by [`Dyalog`](dyalog.md); if that is also unset, it defaults to `/usr/dyalog`.
<!-- REVIEW(default): reconcile the Microsoft Windows default (aplkeys sub-directory) with the UNIX and macOS default (the Dyalog directory, else /usr/dyalog). -->

Related parameters: [APLK](aplk.md), [Dyalog](dyalog.md).

See also the [Input tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-input-tab-classic-edition-only) of the Windows Configuration Dialog.
