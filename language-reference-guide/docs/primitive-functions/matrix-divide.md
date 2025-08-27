<div style="display: none;">
  ⌹
</div>






<h1 class="heading"><span class="name">Matrix Divide</span> <span class="command">R←X⌹Y</span></h1>



`Y` must be a simple numeric array of rank 2 or less.  `X` must be a simple numeric array of rank 2 or less.  `Y` must be non-singular.  A scalar argument is treated as a matrix with one-element.  If `Y` is a vector, it is treated as a single column matrix.  If `X` is a vector, it is treated as a single column matrix.  The number of rows in `X` and `Y` must be the same.  `Y` must have at least the same number of rows as columns.


`R` is the result of matrix division of `X` by `Y`.  That is, the matrix product `Y+.×R` is `X`.


`R` is determined such that `(X-Y+.×R)*2` is minimised.


The shape of `R` is `(1↓⍴Y),1↓⍴X`.


<h2 class="example">Examples</h2>
```apl

      ⎕PP←5
 
      B
3 1 4
1 5 9
2 6 5
 
      35 89 79 ⌹ B
2.1444 8.2111 5.0889
 
      A
35 36
89 88
79 75
 
      A ⌹ B
2.1444 2.1889
8.2111 7.1222
5.0889 5.5778
```


If there are more rows than columns in the right argument, the least squares solution results.  In the following example, the constants a and b which provide the best fit for the set of equations represented by P = a + bQ are determined:
```apl

      Q
1 1
1 2
1 3
1 4
1 5
1 6
 
      P
12.03 8.78 6.01 3.75 ¯0.31 ¯2.79
 
      P⌹Q
14.941 ¯2.9609
```

## Example: linear regression on complex numbers
```apl
      x←j⌿¯50+?2 13 4⍴100
      y←(x+.×3 4 5 6) + j⌿0.0001×¯50+?2 13⍴100
      ⍴x
13 4
      ⍴y
13
      y ⌹ x
3J0.000011066 4J¯0.000018499 5J0.000005745 6J0.000050328
      ⍝ that is, y⌹x recovered the coefficients 3 4 5 6
```


## Additional Information
```apl

      x⌹y ←→ (⌹(⍉y)+.×y)+.×(⍉y)+.×x

```


(Use `+⍉` instead of `⍉` for complex `y`.)


This equivalence, familiar to mathematicians and statisticians, explains

- the conformability requirements for `⌹`
- how to compute the result for tall matrices from the better known square matrix case



