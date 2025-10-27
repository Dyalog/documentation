<div style="display: none;">
  ← gets
</div>

<h1 class="heading"><span class="name">Assignment</span> <span class="command">X←Y</span></h1>

Assignment  allocates the result of the expression `Y` to the *name* or *names* in `X`.

If `Y` is an array expression, `X` must contain one or more names which are variables, system variables, or are undefined. Following assignment, the name(s) in `X` become variable(s) with value(s) taken from the result of the expression `Y`.


If `X` contains a single name, the variable assumes the value of `Y`. If `X` contains multiple names then `Y` can be a single-item array of any rank (including a scalar) or  a vector. If `Y` is a single-item array, the scalar value `⊃Y` is assigned to all names in `X`. Otherwise, each element of `Y` is assigned to the corresponding name in `X`.  Although not mandatory, Dyalog recommends that the names in `X` are enclosed in parentheses to reduce potential ambiguity in assignment statements.

The assignment arrow (or specification arrow) is often read as 'Is' or 'Gets'.

## Examples of single assignment
```apl

      A←2.3
      A
2.3

      A←⍳3
      A
1 2 3
```

## Examples of multiple assignment using parentheses
```apl

      (A B)←2
      A
2
      B
2

      (P ⎕IO Q)←'TEXT' 1 (1 2 3)
      P
TEXT
      ⎕IO
1
      Q
1 2 3
```

## Example of multiple assignment without parentheses
```apl

      year month day←2017 05 24
      day
24
      month
5
      year
2017			
			
```
Implementation note: erroneous expressions such as `var 3←5` will result in `5` being assigned to `var`, even though a `SYNTAX ERROR` will be generated. In the case of `(var 3)←5` no assignment will be made.

Pass-through assignments are permitted. The value of `Y` is carried through each assignment:
```apl

      I←J←K←0
      I,J,K
0 0 0
			

```

## Function Assignment

If `Y` is a function expression, `X` must be a single name which is either undefined, or is the name of an existing function or defined operator. `X` may not be the name of a system function, or a primitive symbol.

<h2 class="example">Examples</h2>
```apl

      PLUS←+
      PLUS
+

      SUM←+/
      SUM
+/

      MEAN←{(+/⍵)÷⍴⍵}

```

## Namespace Reference Assignment

If an expression evaluates to a namespace reference, or *ref*, you may assign it to a name. A name assigned to a simple scalar *ref*, has name class 9, whereas one assigned to an *array* containing *refs* has name class 2.
```apl

      'f1'⎕WC'Form'
      'ns1' ⎕NS ''

      N←ns1
      ⎕NC'N'           ⍝ name class of a scalar ref
9
      F←f1
      ⎕NC'F'           ⍝ name class of a scalar ref
9
      refs←N F         ⍝ vector of refs.
      ⎕NC'refs'        ⍝ nameclass of vector.
2
      F2←2⊃refs
      ⎕NC 'F2'
9
		
```

## Re-Assignment

A name that already exists may be assigned a new value if the assignment will not alter its name class, or will change it from 2 to 9 or vice versa. The table of permitted re-assignments is as follows:


|&nbsp;  |Ref   |Variable|Function|Operator|
|--------|------|--------|--------|--------|
|Ref     |Yes   |Yes     |&nbsp;  |&nbsp;  |
|Variable|Yes   |Yes     |&nbsp;  |&nbsp;  |
|Function|&nbsp;|&nbsp;  |Yes     |Yes     |
|Operator|&nbsp;|&nbsp;  |Yes     |Yes     |
