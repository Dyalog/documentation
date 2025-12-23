## Before Initiating the Collection of Data

To improve the accuracy of the data and minimise the impact of timer overhead (see [Timer Overhead]()):

* Switch off as much hardware as possible, including peripherals and network connections.
* Switch off as many other tasks and processes as possible, including anti-virus software, firewalls, internet services and background tasks.
* Raise the priority on the Dyalog APL task to higher than normal.
!!! windows "Dyalog on Microsoft Windows"
    On Microsoft Windows, avoid giving it the highest priority.

Data collected by the `⎕PROFILE` system function is cumulative whenever the `⎕PROFILE` system function is in an active state (but does not persist between Sessions); to discard any previously-collected data, enter `⎕PROFILE 'clear'.