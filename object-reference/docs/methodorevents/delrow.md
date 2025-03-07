<h1 class="heading"><span class="name">DelRow</span> <span class="right">Method 154</span></h1>



**Applies To:** [Grid](../objects/grid.md)

**Description**


This method is used to delete a specified row from a [Grid](../objects/grid.md) object.


The argument to DelRow is a 1 or 2-element array as follows:


|-----|----------|-------------------------------------|
|`[1]`|Row number|number of the row (integer) to delete|
|`[2]`|Undo flag |0 or 1 (optional; default 0)         |


If the *Undo flag* is 1, the column may subsequently be restored by invoking the [Undo](./undo.md) method. If the *Undo flag* is omitted or is 0, the operation may not be undone.



