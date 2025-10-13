<h1 class="heading"><span class="name">AplCoreName</span></h1>

This parameter specifies the directory and name of the file in which *aplcore* should be saved. The optional wild-card character (`*`) is replaced by a number when the file is written. If there is more than one `*` in **AplCoreName**, the string is used as is; no substitution is made. For more details, including how to prevent aplcore files from being generated, see [MaxAplCores](maxaplcores.md).

Note that APL terminates with an exit code of 3 when an aplcore file is generated.

See also [aplcore Parameters](../../../language-reference-guide/primitive-operators/i-beam/aplcore-parameters).
