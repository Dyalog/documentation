<div style="display: none;">
  |
</div>

<h1 class="heading"><span class="name">Magnitude</span> <span class="command">R←|Y</span></h1>

`Y` may be any numeric array. `R` is numeric composed of the absolute (unsigned) values of `Y`.

Note that the magnitude of a complex number <math xmlns="http://www.w3.org/1998/Math/MathML">
<mi>z</mi>
<mo>=</mo>
<mi>a</mi>
<mo>+</mo>
<mi>b</mi>
<mi>i</mi>
</math> (where <math xmlns="http://www.w3.org/1998/Math/MathML">
<mi>a</mi>
</math> and <math xmlns="http://www.w3.org/1998/Math/MathML">
<mi>b</mi>
</math> are real numbers, and <math xmlns="http://www.w3.org/1998/Math/MathML">
<mi>i</mi>
</math> is the imaginary unit) is defined to be:

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mrow>
    <mo>|</mo>
    <mi>z</mi>
    <mo>|</mo>
  </mrow>
  <mo>=</mo>
  <msqrt>
    <mrow>
      <msup>
        <mi>a</mi>
        <mn>2</mn>
      </msup>
      <mo>+</mo>
      <msup>
        <mi>b</mi>
        <mn>2</mn>
      </msup>
    </mrow>
  </msqrt>
</math>

<h2 class="example">Examples</h2>
```apl
      |2 ¯3.4 0 ¯2.7
2 3.4 0 2.7
 
      |3j4
5
```

`⎕IO` is an implicit argument of magnitude.



