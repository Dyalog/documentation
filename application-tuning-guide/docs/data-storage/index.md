<h1 class="heading"><span class="name">Data Storage</span></h1>

The `]Profile` user command can direct output to a file instead of displaying it in the Session. To do this, the `-outfile` modifier must be included; its modifier value must be the name of file in which to write the report data. By default, data is stored in an XML format, but this can be changed with the `-format` modifier:

* To save data in [XML format](xml-format.md), include `-format=xml` in the call to the `]Profile` user command (see Section ).  This is the default, so does not have to be explicitly stated.

* To save data in [CSV format]( ./csv-format.md), include `-format=csv` in the call to the `]Profile` user command.

* To save data in [text format]( ./text-format.md), include `-format=txt` in the call to the `]Profile` user command.