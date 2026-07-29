# Global & Local Names

The following names, if present, are local to the defined operation:

1. the result,
2. the argument(s) and operand(s),
3. additional names in the header line following the model, each name preceded by a semi-colon character,
4. labels,
5. the argument list of the system function `⎕SHADOW` when executed,
6. a name assigned within a dfn.

All names in a defined operation must be valid APL names. The same name may be repeated in the header line, including the operation name (whence the name is localised). Normally, the operation name is not a local name.

The same name may not be given to both arguments or operands of a dyadic operation. The name of a label may be the same as a name in the header line. More than one label may have the same name. When the operation is executed, local names in the header line after the model are initially undefined; labels are assigned the values of line numbers on which they occur, taken in order from the last line to the first; the result (if any) is initially undefined.

In the case of a defined function, the left argument (if any) takes the value of the array to the left of the function when called; and the right argument (if any) takes the value of the array to the right of the function when called. In the case of a defined operator, the left operand takes the value of the function or array to the left of the operator when called; and the right operand (if any) takes the value of the function or array to the right of the operator when called.

During execution, a local name temporarily excludes from use an object of the same name with an active definition. This is known as LOCALISATION or SHADOWING. A value or meaning given to a local name will persist only for the duration of execution of the defined operation (including any time whilst the operation is halted). A name which is not local to the operation is said to be GLOBAL. A global name could itself be local to a pendent operation. A global name can be made local to a defined operation during execution by use of the system function `⎕SHADOW`. An object is said to be VISIBLE if there is a definition associated with its name in the active environment.

<h2 class="example">Examples</h2>
```apl
      A←1
 
     ∇ F
[1]    A←10
[2]  ∇
 
      F ⍝ <A> NOT LOCALISED IN <F>, GLOBAL VALUE REPLACED
      A
10
      A←1
      )ERASE F
 
     ∇ F;A
[1]    A←10
[2]  ∇
 
      F  ⍝ <A> LOCALISED IN <F>, GLOBAL VALUE RETAINED
      A
1
```

Any statement line in the body of a defined operation may begin with a LABEL. A label is followed by a colon (`:`).  A label is a constant whose value is the number of the line in the operation defined by system function `⎕FX` or on closing definition mode.

The value of a label is available on entering an operation when executed, and it may be used but not altered in any expression.

<h2 class="example">Example</h2>
```apl
      ⎕VR'PLUS'
    ∇ R←{A} PLUS B
[1]   →DYADIC ⍴⍨2=⎕NC'A' ⋄ R←B ⋄ →END
[2]  DYADIC: R←A+B
[3]  END:
    ∇
 
      1 ⎕STOP'PLUS'
 
      2 PLUS 2
 
PLUS[1]
      DYADIC
2
 
      END
3
```
