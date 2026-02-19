<h1 class="heading"><span class="name">Introduction</span></h1>

Application design includes assumptions about usage patterns and data
volumes. Over time, these can evolve to the detriment of the application's
performance. The most effective way to counter drops in performance caused
by changes external to the application is to identify the hot spots
(places in the application where a high proportion of CPU or Elapsed
Time is consumed); these hot spots can then be tuned to improve the
application's performance.

The `⎕PROFILE` system function and the `]Profile` user command
facilitate the hot spot identification process; the `⎕PROFILE` system
function gathers statistics from an application and the `]Profile`
user command summarises, filters and reports on this data, simplifying
the process of drilling down on the (frequently large amounts of) data
returned by `⎕PROFILE`.

!!! Legacy "Legacy "
	The `⎕MONITOR` system function, which was in use prior to
	the introduction of the `⎕PROFILE` system function, has been
	deprecated and Dyalog Ltd recommends rewriting tools to use the
	`⎕PROFILE` system function instead; `⎕PROFILE` provides high
	precision timing, calling tree analysis, and superior dfn and
	recursive code handling.

For more information on the `⎕PROFILE` system function, see the [Language Reference Guide](../../language-reference-guide).
For more information on the `]Profile` user command, see [Appendix A](appendix-a-syntax-of-profile-user-command.md).

