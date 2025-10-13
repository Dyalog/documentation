
<!-- Hidden search keywords -->
<div style="display: none;">
  4001⌶
</div>






<h1 class="heading"><span class="name">Change User</span> <span class="command">R←4001⌶Y</span></h1>



`Y` is a character vector that specifies a valid UNIX user name. The function changes the *userid (uid)* and *groupid (gid)* of the process to values that correspond to the specified user name.


Note that it is only possible to change the user name if the *effective uid* is 0 (that is, the process has root privileges).


If the operation is successful, `R` is the user name specified in `Y`. Note that the value of `⎕AN` will not be affected, but the value of `⊃⎕AI` will be.


If the operation fails, the function generates a `FILE ERROR 1 Not Owner` error.



If the argument to `4001⌶` is other than a non-empty simple character vector, the function generates a `DOMAIN ERROR`.


If the argument is not the name of a valid user the function generates a `FILE ERROR 3 No such process`.


If the argument is the same name as the current effective user, then the function returns that name, but has no effect.


If the argument is a valid name other than the name of the effective user id of the current process, and that effective user id is not root the function generates a `FILE ERROR 1 Not owner`.


