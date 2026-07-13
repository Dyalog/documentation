# SALT Tab

SALT is the Simple APL Library Toolkit, a simple source code management system for Classes and script-based Namespaces. SPICE uses SALT to manage development tools which "plug in" to the Dyalog session

![configuration dialog salt tab](../../img/configuration-dialog-salt-tab.png)

Table: Configuration dialog: SALT

|Label|Parameter|Description|
|---|---|---|
|Enable Salt|AddSALT|Specifies whether or not SALT is enabled|
|Compare command line:|CompareCMD|The command line for a 3 <sup>rd</sup> party file comparison tool to be used to compare two versions of a file. See note.|
|Editor command line:|Editor|Name of the program to be used to edit script files (default "Notepad").|
|Source folders:|SourceFolder|Sets the SALT working directory; a list of folders to be searched for source code. Include "." on a separate line to include source files from the current working directory|
