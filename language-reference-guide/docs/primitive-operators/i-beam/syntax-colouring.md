
<!-- Hidden search keywords -->
<div style="display: none;">
  200⌶
</div>






<h1 class="heading"><span class="name">Syntax Colouring</span> <span class="command">R←200⌶Y</span></h1>



This function obtains syntax colouring information for a function.


`Y` is a vector of character vectors containing the `⎕NR` representation of a function or operator.


`R` is a vector of integer vectors with the same shape and structure of `Y` in which each number identifies the syntax colour element associated with the corresponding character in `Y`.

```apl
      ∇foo∇
     ∇ foo;local
[1]    global
[2]    local←⍴⍴'hello'
     ∇
      ⎕NR 'foo'
  foo;local   global   local←⍴⍴'hello' 
 
     {(↑⍵),↑200⌶⍵}⎕NR 'foo'
 foo;local       3 21 21 21 19 34 34 34 34 34 0 0 0 0 0 0
 global          3  7  7  7  7  7  7  0  0  0 0 0 0 0 0 0
 local←⍴⍴'hello' 3 34 34 34 34 34 19 23 23  4 4 4 4 4 4 4

```



In this example:


|---|-------------------------------------------------|
|21 |is the syntax identifier for "character constant"|
|19 |is the syntax identifier for "primitive"         |
|3  |is the syntax identifier for "white space"       |
|34 |is the syntax identifier for "local name"        |
|7  |is the syntax identifier for "global name"       |
|23 |is the syntax identifier for "idiom"             |



The list of syntax colour elements supported by the current interpreter is given by `201⌶`. It is important to note that the values may change within a release, and are very likely to change across releases .. you should always call `201⌶` rather than relying the results from a different interpreter. See [Syntax Colour Tokens](syntax-colour-tokens.md).


