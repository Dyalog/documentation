# Defining Namespaces

At least one namespace must be specified in an APL Source file. Namespaces are specified in an APL Source file using the `:Namespace` and `:EndNamespace` statements. Although you can use `⎕NS` and `⎕CS` within functions inside an APL Source file, you should not use these system functions outside function bodies; such use is not prevented, but the results will be unpredictable.

`:Namespace Name` introduces a new namespace  relative to the current namespace called `Name`.

`:EndNamespace` terminates the definition of the current namespace. Subsequent statements and function bodies are processed in the context of the original space.

All functions specified between the `:Namespace` and `:EndNamespace` statements are fixed within that namespace. Similarly, all assignments define variables inside that namespace.
