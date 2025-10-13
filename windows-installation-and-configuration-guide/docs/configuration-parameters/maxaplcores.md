<h1 class="heading"><span class="name">MaxAplCores</span></h1>

This parameter is used in conjunction with the **AplCoreName** parameter to control the maximum number of*aplcore* files that are saved. It applies when the string specified by **AplCoreName** ends with an asterisk (*). If so, when saving an *aplcore* file, Dyalog performs the following steps:

1. Identifies the highest number ending of those files that match the directory/name pattern specified by **AplCoreName** . If none, assume 0.
2. Increments that number, then saves the *aplcore* in a new file ending with the new number.
3. If necessary, deletes lower-numbered files to retain only the maximum number of files specified by **MaxAplCores** .

See also: [AplCoreName](aplcorename.md).

See also [aplcore Parameters](../../../language-reference-guide/primitive-operators/i-beam/aplcore-parameters).
