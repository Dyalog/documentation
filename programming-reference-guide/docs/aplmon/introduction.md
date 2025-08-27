<h1 class="heading"><span class="name">Introduction</span></h1>

APLMON is a built-in Dyalog feature that, when enabled, monitors the execution of APL primitives and functions and writes the results to a CSV file. When not enabled (the default), it has no impact on execution.

When running an APL application with APLMON enabled, Dyalog logs the use of every primitive operation; how many times it was called, how much time was spent running it and details  about the arguments it was processing. This makes it possible to identify the primitive operations on which the application spends the most time. Dyalog Ltd can use this data to help determine which optimisations to prioritise and where to concentrate performance work. For additional information on this topic, please contact [support@dyalog.com](mailto:support@dyalog.com).

APLMON does not return any application-side information. APL programmers should use `⎕PROFILE` or the `cmpx` function from the `dfns` workspace to determine which parts of the application can be optimized programmatically. However, APLMON can be useful for APL programmers who want to verify that their application uses primitives as expected or that it does not perform unnecessary computations such as disclosing simple scalars.
