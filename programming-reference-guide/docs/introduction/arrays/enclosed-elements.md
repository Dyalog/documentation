# Enclosed Elements

An array may be enclosed to form a scalar element through any of the following means:

- by the enclose function (`⊂`)
- by inclusion in vector notation
- as the result of certain functions when applied to arrays

<h2 class="example">Examples</h2>

```apl
      (⊂1 2 3),⊂'ABC'
1 2 3  ABC
			 
	(1 2 3) 'ABC'
1 2 3  ABC
			 
      ⍳2 3
1 1  1 2  1 3
2 1  2 2  2 3
```
