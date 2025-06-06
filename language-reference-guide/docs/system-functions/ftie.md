<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FTIE FTIE
</div>






<h1 class="heading"><span class="name">Exclusive File Tie</span> <span class="command">{R}←X ⎕FTIE Y</span></h1>


## Access code 2


`Y` must be 0 or a simple 1 or 2 element integer vector containing an available file tie number to be associated with the file for further file operations, and an optional passnumber.  If the passnumber is omitted it is assumed to be zero.  The tie number must not already be associated with a share tied or exclusively tied file.


`X` must be a simple character scalar or vector which specifies the name of the file to be exclusively tied.  The file must be named in accordance with the operating system's conventions, and may be a relative or absolute pathname. If no file extension is supplied, the set of extensions specified by the  **CFEXT** parameter are tried one after another until the file is found or the set of extensions is exhausted. See [ CFEXT](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters).


The file must exist and  the user must have write access to it.  It may not already be tied by another user.



## Automatic Tie Number Allocation


A tie number of 0 as argument to a create, share tie or exclusive tie operation, allocates the first (closest to zero) available tie number, and returns it as an explicit result. This allows you to simplify code. For example:


from:
```apl
      tie←1+⌈/0,⎕FNUMS ⍝ With next available number,
      file ⎕FTIE tie   ⍝ ... tie file.
```


to:
```apl
      tie←file ⎕FTIE 0 ⍝ Tie with first available number.
```



The shy result of `⎕FTIE` is the tie number of the file.

<h2 class="example">Examples</h2>
```apl
      'SALES' ⎕FTIE 1
 
      '../budget/COSTS' ⎕FTIE  2
 
      '../budget/expenses' ⎕FTIE 0
3
```
# Variant Options
## Mode Variant

Variant option ‘Mode’ specifies the intended use of the tie and can affect how and when errors are signalled.

-|---
R| File must only be be read. Any attempt to write to the file will fail.
U| Use is unspecified (default). It will be tied even if the file read-only, but if it is read-only any *subsequent* attempt to write to the file will fail. 
W|File must be writable. If it is read-only for any reason the tie will fail.

### Notes

* 'Mode' 'W' will not cause the tie to fail purely because the file's access matrix would prevent any or all subsequent writes.
* Files may not be writable for reasons other than the host filesystem not permitting it. For example, small-span (32-bit) component files are not writable.
. If the file is not writable because the host filesystem does not permit it, ⎕FTIE (not ⎕FSTIE) will likely fail regardless of the Mode because it cannot be exclusively locked.
* Successfully tying a file with Mode ‘W’ does not guarantee that subsequent writes will succeed. The file permissions on the host filesystem might be changed in the meantime, or the filesystem may be full, for example.