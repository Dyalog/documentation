
<!-- Hidden search keywords -->
<div style="display: none;">
  201⌶
</div>






<h1 class="heading"><span class="name">Syntax Colour Tokens</span> <span class="command">R←201⌶Y</span></h1>



This function provides a description of the syntax colour tokens reported by `200⌶`. See [Syntax Colouring](syntax-colouring.md).


`Y` is `⍬` (zilde).


`R` is a 4-column matrix that describes the syntax colouring tokens as follows:


|-------|--------------------|
|`R[;1]`|Token type          |
|`R[;2]`|Token Value         |
|`R[;3]`|Internal description|
|`R[;4]`|Colour index        |



The 4th column is intended for the benefit of non-Windows users using the tty interface and indicates the video/foreground/background colour index. These indices appear in the output translate tables found in `$DYALOG/apltrans`, and are used to define the colours used in the tty interface.

<h2 class="example">Example</h2>
```apl
      ⍴201⌶⍬
207 4
     3 4↑201⌶⍬
┌────────────┬─┬────────────┬───┐
│Global token│0│MINI_NULL   │129│
├────────────┼─┼────────────┼───┤
│Global token│1│MINI_COMMENT│137│
├────────────┼─┼────────────┼───┤
│Global token│2│MINI_UCC    │129│
└────────────┴─┴────────────┴───┘

```


