# APLTrans

!!! Info "Information"
    This configuration parameter is only relevant when using the Classic edition of Dyalog.

A search path for the Output Translate Table, useful when configuring a run-time application. Directory paths use the operating system's conventions and are separated by `;` (Windows) or `:` (UNIX and macOS).

Valid values are a list of directory paths.

Default is the `apltrans` sub-directory of the Dyalog installation directory (given by [`Dyalog`](dyalog.md)).

On UNIX and macOS, if this parameter is unset the search path defaults to the directory given by [`Dyalog`](dyalog.md); if that is also unset, it defaults to `/usr/dyalog`.
<!-- REVIEW(default): reconcile the Microsoft Windows default (apltrans sub-directory) with the UNIX and macOS default (the Dyalog directory, else /usr/dyalog). -->

Related parameters: [APLT](aplt.md), [Dyalog](dyalog.md).

See also the [Output tab](../../../windows-installation-and-configuration-guide/configuring-the-ide/configuration-dialog/configuration-dialog-output-tab-classic-edition-only) of the Windows Configuration Dialog.
