<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FREAD FREAD
</div>






<h1 class="heading"><span class="name">File Read Components</span> <span class="command">R←⎕FREAD Y</span></h1>


## Access code 1


`Y` is a  2 or 3 item  vector containing the file tie number, the component number(s), and an optional passnumber.  If the passnumber is omitted it is assumed to be zero. All elements of `Y` must be integers.


The second item in `Y` may be scalar which specifies a single component number or a vector of component numbers. If it is a scalar, the result is the value of the array that is stored in the specified component on the tied file. If it is a vector, the result is a vector of such arrays.




Note that any invocation of  `⎕FREAD` is an atomic operation.  Thus if `compnos` is a vector, the statement:
```apl
      ⎕FREAD tie compnos passno
```


will return the same result as:
```apl
      {⎕FREAD tie ⍵ passno}¨compnos
```



However, the first statement will, in the case of a share-tied file,  prevent any potential intervening file access from another user (without the need for a  `⎕FHOLD`). It will also perform slightly faster, especially when reading from a share-tied file.

<h2 class="example">Examples</h2>
```apl
      ⍴SALES←⎕FREAD 1 241
3 2 12
 
GetFile←{⎕IO←0                ⍝ Extract contents.
    tie←⍵ ⎕FSTIE 0            ⍝ new tie number.
    fm to←2↑⎕FSIZE tie        ⍝ first and next component.
    cnos←fm+⍳to-fm            ⍝ vector of component nos.
    cvec←⎕FREAD tie cnos      ⍝ vector of components.
    cvec⊣⎕FUNTIE tie        ⍝ ... untie and return.
}
```


