<h1 class="heading"><span class="name">DyalogStartup_X</span></h1>

During Session initialisation, code is loaded from the directories specified by the **DyalogStartupSE** parameter into a corresponding namespace tree in the Session namespace `⎕SE`. Optionally, the code is then executed.

If **DyalogStartup_X** is 0 (the default if not defined), the `Run` function (if it exists) in each  *top-level* namespace loaded during Session start-up is executed. The  namespaces are processed in alphabetical order.

If  **DyalogStartup_X** is 1, the `Run` function is not executed.

Other values are reserved for future extension.

See also: [DyalogStartupSE](dyalogstartupse.md).
