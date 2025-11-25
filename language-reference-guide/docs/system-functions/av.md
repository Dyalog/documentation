---
search:
  boost: 2
---
<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕AV AV
</div>






<h1 class="heading"><span class="name">Atomic Vector</span> <span class="command">R←⎕AV</span></h1>



`⎕AV` is a deprecated feature and is replaced by `⎕UCS`.


This is a simple character vector of all 256 characters in the Classic Dyalog APL character.


In the Classic Edition the contents of `⎕AV` are defined by the Output Translate Table.


In the Unicode Edition, the contents of `⎕AV` are defined by the system variable `⎕AVU`.

<h2 class="example">Examples</h2>
```apl
      ⎕AV[48+⍳10]
0123456789
 
      5 52⍴12↓⎕AV
%'⍺⍵_abcdefghijklmnopqrstuvwxyz¯.⍬0123456789⊢¥$£¢
∆ABCDEFGHIJKLMNOPQRSTUVWXYZý·⍙ÁÂÃÇÈÊËÌÍÎÏÐÒÓÔÕÙÚÛ
Ýþãìðòõ{€}⊣⌷¨ÀÄÅÆ⍨ÉÑÖØÜßàáâäåæçèéêëíîïñ[/⌿\⍀<≤=≥>≠∨∧
-+÷×?∊⍴~↑↓⍳○*⌈⌊∇∘(⊂⊃∩∪⊥⊤|;,⍱⍲⍒⍋⍉⌽⊖⍟⌹!⍕⍎⍫⍪≡≢óôöø"#&´
┘┐┌└┼─├┤┴┬│@ùúû^ü`∣¶:⍷¿¡⋄←→⍝)] §⎕⍞⍣%'⍺⍵_abcdefghijk

```



