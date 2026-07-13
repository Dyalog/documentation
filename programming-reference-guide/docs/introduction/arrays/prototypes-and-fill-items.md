# Prototypes and Fill Items

Every array has an associated *prototype* which is derived from the array's first item.

If the first item is a number, the prototype is 0. Otherwise, if the first item is a character, the prototype is `' '`(space). Otherwise, if the first item is a (ref to) an instance of a Class, the prototype is a ref to that Class.

Otherwise (in the nested case, when the first item is other than a simple scalar), the prototype is defined recursively as the prototype of each of the array's first item.

## Examples { .example }

|Array                   |Prototype      |
|------------------------|---------------|
|`1 2 3.4`               |`0`            |
|`2 3 5⍴'hello'`         |`' '`          |
|`99 'b' 66`             |`0`            |
|`(1 2)(3 4 5)`          |`0 0`          |
|`((1 2)3)(4 5 6)`       |`(0 0)0`       |
|`'hello' 'world'`       |`'     '`      |
|`⎕NEW MyClass`          |`MyClass`      |
|`(88(⎕NEW MyClass)'X')7`|`0 MyClass ' '`|

## Fill Items

Fill items for an overtake operation, are derived from the argument's prototype. For each `0` or `' '` in the prototype, there is a corresponding `0` or `' '` in the fill item and for each class reference in the prototype, there is a ref to a (newly constructed and distinct) instance of that class that is initialised by the niladic (default) constructor for that class, if defined.

<h3 class="example">Examples</h3>

```apl
      4↑1 2
1 2 0 0
      4↑'ab'
ab  
      4↑(1 2)(3 4 5)
 1 2  3 4 5  0 0  0 0 
      2↑⎕NEW MyClass
 #.[Instance of MyClass]  #.[Instance of MyClass]
```

In the last example, two distinct instances are constructed (the first by `⎕NEW` and the second by the overtake).

Fill items are used in a number of operations including:

- First (`⊃` or `↑`) of an empty array
- Fill-elements for overtake
- For use with the Each operator on an empty array
